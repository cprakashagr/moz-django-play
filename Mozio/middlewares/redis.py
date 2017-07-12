import json
import re
import redis
from django.http import HttpResponse, JsonResponse


# from Mozio.urls import providerRegEx, polygonsRegEx, userEndPointRegEx


class RedisMiddleWare(object):

    def __init__(self, get_response):
        self.get_response = get_response

        poolLatLong = redis.ConnectionPool(host="localhost", port=6379, db=0)
        self.redisLatLong = redis.Redis(connection_pool=poolLatLong)

        poolPolygons = redis.ConnectionPool(host="localhost", port=6379, db=1)
        self.redisPolygons = redis.Redis(connection_pool=poolPolygons)

    def __call__(self, request):

        # Check for the existence in the Redis
        # return from here if available

        if 'api/userEndPoint' in request.path:
            print("Matched !")
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
                self.redisLatLong.set(redisLtLnKey, response.content.decode('ascii'))


        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        if 'api/polygons' in request.path:
            print("Matched !")

        if 'api/providers' in request.path:
            print("Matched !")
