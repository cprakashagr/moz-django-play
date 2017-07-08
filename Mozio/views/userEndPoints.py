import json
import redis

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from Mozio.models import Polygons
from Mozio.views import providers

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)


@require_http_methods(["GET", "POST"])
def searchPolygon(request, latitude, longitude):
    # params = request.GET

    key = latitude.join(longitude)
    redisLookup = r.get(key)
    if redisLookup is not None:
        poly = json.loads(r.get(key).decode('ascii'))
        return JsonResponse(poly)

    longitude = float(longitude)
    latitude = float(latitude)

    # point = {'type': 'Point', 'coordinates': [longitude, latitude]}

    allPoly = Polygons.objects(geometry__geo_intersects=[longitude, latitude])

    polygons = dict()
    polygons['items'] = []
    for poly in allPoly:
        p = json.loads(poly.to_json())
        providerId = p['providerId']['$oid']
        provider = providers.fetchProviderWithId(providerId)[0]
        p['providerName'] = provider.name
        polygons['items'].append(p)

    r.set(key, json.dumps(polygons))
    return JsonResponse(polygons)
