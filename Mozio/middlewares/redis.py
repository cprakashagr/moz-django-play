import json

import redis
from django.http import JsonResponse


# from Mozio.urls import providerRegEx, polygonsRegEx, userEndPointRegEx


class RedisMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

        poolLatLong = redis.ConnectionPool(host="localhost", port=6379, db=0)
        self.redisLatLong = redis.Redis(connection_pool=poolLatLong)

        poolPolygons = redis.ConnectionPool(host="localhost", port=6379, db=1)
        self.redisPolygons = redis.Redis(connection_pool=poolPolygons)

        poolProviders = redis.ConnectionPool(host="localhost", port=6379, db=2)
        self.redisProviders = redis.Redis(connection_pool=poolProviders)

    def __call__(self, request):

        # Check for the existence in the Redis
        # return from here if available

        if 'api/userEndPoint' in request.path:
            if request.method == 'GET':
                redisLtLnKey = request.GET['lnlt']
                val = self.redisLatLong.get(redisLtLnKey)
                if val is not None:
                    poly = json.loads(val.decode('ascii'))
                    return JsonResponse(poly, safe=False)

        response = self.get_response(request)
        # Add to Redis and return the response

        if 'api/userEndPoint' in request.path:
            if request.method == 'GET':
                redisLtLnKey = request.GET['lnlt']
                results = json.loads(response.content.decode('ascii'))

                for result in results:
                    providerId = result['providerId']['id']
                    polygonId = result['id']

                    fromRedisProvider = self.redisProviders.lrange(providerId, 0, -1)
                    if fromRedisProvider is not None:
                        providerList = list()
                        providerList.extend(fromRedisProvider)
                        providerList.append(redisLtLnKey.encode)
                        self.redisProviders.lpush(providerId, *providerList)
                    else:
                        self.redisProviders.lpush(providerId, *[redisLtLnKey])

                    fromRedisPolygons = self.redisPolygons.lrange(polygonId, 0, -1)
                    if fromRedisPolygons is not None:
                        polygonList = list()
                        polygonList.extend(fromRedisPolygons)
                        polygonList.append(redisLtLnKey.encode())
                        self.redisPolygons.lpush(polygonId, *polygonList)
                        pass
                    else:
                        self.redisPolygons.lpush(polygonId, *[redisLtLnKey])

                self.redisLatLong.set(redisLtLnKey, response.content)

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        if request.method == 'DELETE' or request.method == 'PUT' or request.method == 'PATCH':
            if 'api/polygons' in request.path:
                polygonId = view_kwargs['id']
                self.clearRedis(self.redisPolygons, polygonId)
            elif 'api/providers' in request.path:
                providerId = view_kwargs['id']
                self.clearRedis(self.redisProviders, providerId)

    def clearRedis(self, redisRef, pId):
        ltLnKeys = redisRef.lrange(pId, 0, -1)
        if ltLnKeys is not None:
            ltLnList = list()
            ltLnList.extend(ltLnKeys)
            for ltln in ltLnList:
                self.redisLatLong.delete(ltln.decode('ascii'))
        redisRef.delete(pId)
        pass
