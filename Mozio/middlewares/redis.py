import json

import redis
from django.http import JsonResponse

# from Mozio.urls import providerRegEx, polygonsRegEx, userEndPointRegEx
from mongoengine.queryset.visitor import Q

from Mozio.models import Polygons


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

        if request.method == 'POST':
            if 'api/polygons' in request.path:
                allLtLnKeys = self.redisLatLong.keys()
                allLtLnKeys = self.normalizeKeys(allLtLnKeys)

                # TODO: Fix me
                x = Polygons.objects(Q(id=response.data['id']) & Q(geometry__geo_intersects=[allLtLnKeys]))
                self.redisLatLong.flushall()

        if 'api/userEndPoint' in request.path:
            if request.method == 'GET':
                redisLtLnKey = request.GET['lnlt']
                results = json.loads(response.content.decode('ascii'))

                for result in results:
                    providerId = result['providerId']['id']
                    polygonId = result['id']

                    self.redisProviders.lpush(providerId, *[redisLtLnKey])
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
        for ltln in ltLnKeys:
            self.redisLatLong.delete(ltln.decode('ascii'))
        redisRef.delete(pId)
        pass

    def normalizeKeys(self, allLtLnKeys):
        retList = list()
        for lnLtKey in allLtLnKeys:
            lnLtKey = lnLtKey.decode('ascii').split(',')
            retList.append(lnLtKey)
        return retList
