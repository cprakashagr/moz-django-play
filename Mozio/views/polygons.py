import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_http_methods

from Mozio.models import Polygons
from Mozio.views import providers


@require_http_methods(["GET", "POST"])
def addPolygons(request):
    params = request.GET

    polygon = Polygons()
    name = params['name'] if 'name' in params else ''
    price = params['price'] if 'price' in params else ''
    if 'userId' not in params:
        return HttpResponse('False')
    else:
        user = providers.fetchProviderWithId(params['userId'])
        if len(user) > 0:
            polygon.providerId = user[0]
        else:
            return HttpResponse('False')
    if 'geometry' not in params:
        return HttpResponse('False')
    else:
        geo = getGeometryFromUserInput(params['geometry'])
        if type(geo) is bool:
            return HttpResponse('False')

    polygon.name = name
    polygon.price = price
    polygon.geometry = geo
    polygon.save()

    js = json.loads(polygon.to_json())
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def deletePolygons(request):
    params = request.GET

    pId = params['id']
    polygon = fetchPolygonWithId(pId)
    if len(polygon) > 0:
        polygon = polygon[0]
    else:
        return HttpResponse('False')
    polygon.delete()

    js = {}
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def updatePolygons(request):
    params = request.GET

    pId = params['id']
    polygon = fetchPolygonWithId(pId)
    if len(polygon) > 0:
        polygon = polygon[0]
    else:
        return HttpResponse('False')
    polygon.name = params['name'] if 'name' in params else polygon['name']
    polygon.price = params['price'] if 'price' in params else polygon['price']
    geo = getGeometryFromUserInput(params['geometry']) if 'geometry' in params else polygon['geometry']

    if type(geo) is bool:
        return HttpResponse('False')
    else:
        polygon.geometry = geo

    js = json.loads(polygon.to_json())
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def getPolygons(request):
    params = request.GET

    polygon = fetchPolygonWithId(params['id'])
    if len(polygon) > 0:
        polygon = polygon[0]
    else:
        return HttpResponse('False')

    js = json.loads(polygon.to_json())
    return JsonResponse(js)


def getGeometryFromUserInput(geometry):

    try:
        d = dict()
        d['type'] = "Polygon"
        allC = []
        allCords = geometry.split(',')
        for cords in allCords:
            current = cords.strip().split(':')
            point = [float(current[0]), float(current[1])]
            allC.append(point)
        d['coordinates'] = [allC]
        return d
    except Exception:
        return False


def fetchPolygonWithId(pId):
    return Polygons.objects(id=pId)
