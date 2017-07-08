import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from Mozio import settings
from Mozio.models import Provider, Polygons


@require_http_methods(["GET", "POST"])
def hello(request):
    # Test API
    provider = Provider(name='CP', email='cp@cp.com')
    provider.phoneNumber = '+919501289879'
    provider.language = 'en'
    provider.currency = 'INR'
    if settings.DEBUG:
        provider.save()

    d = dict()
    d['type'] = "Polygon"
    d['coordinates'] = [
        [
            [
                -73.93068465493032,
                40.66362047727534
            ],
            [
                -73.928540683823,
                40.66168068611841
            ],
            [
                -73.9282824922159,
                40.661447066502724
            ],
            [
                -73.92646424218866,
                40.65981436177378
            ],
            [
                -73.92725505325629,
                40.659337563577296
            ],
            [
                -73.92819257852784,
                40.66017717353752
            ],
            [
                -73.92834017576637,
                40.660060036443674
            ],
            [
                -73.92817215363176,
                40.65847734532552
            ],
            [
                -73.92799465183667,
                40.65680210148187
            ],
            [
                -73.92896419407968,
                40.65674261382688
            ],
            [
                -73.92989802426044,
                40.65668443579569
            ],
            [
                -73.93090354932272,
                40.65661035598414
            ],
            [
                -73.93190743894836,
                40.65653765254296
            ],
            [
                -73.9328465729284,
                40.65647848205148
            ],
            [
                -73.93381012074782,
                40.656422992674976
            ],
            [
                -73.93478437377932,
                40.65636039558984
            ],
            [
                -73.93571813261279,
                40.65630329672934
            ],
            [
                -73.9361792775009,
                40.65627397206927
            ],
            [
                -73.93668469506125,
                40.65624182330086
            ],
            [
                -73.93712063808269,
                40.65621590359206
            ],
            [
                -73.93765923512817,
                40.65618387639598
            ],
            [
                -73.93859348998163,
                40.65612237929743
            ],
            [
                -73.93955925311144,
                40.65606275324776
            ],
            [
                -73.94053214686076,
                40.65600153896512
            ],
            [
                -73.9414626092295,
                40.65594424853205
            ],
            [
                -73.94240147928579,
                40.65588481159506
            ],
            [
                -73.94335488899262,
                40.65582833538432
            ],
            [
                -73.94431012333266,
                40.65576866576864
            ],
            [
                -73.94487284338389,
                40.655734762103876
            ],
            [
                -73.94507909388307,
                40.6557220470435
            ],
            [
                -73.94715896257101,
                40.65559378727068
            ],
            [
                -73.95006664927287,
                40.65542299720057
            ],
            [
                -73.94993008791383,
                40.65415032686895
            ],
            [
                -73.9497687497526,
                40.65264232265615
            ],
            [
                -73.94966851174581,
                40.651697519580836
            ],
            [
                -73.94957113083304,
                40.65080789987119
            ],
            [
                -73.95137845862438,
                40.650715745338196
            ],
            [
                -73.9524690130785,
                40.65066945528932
            ],
            [
                -73.95295083898296,
                40.65065556059234
            ],
            [
                -73.95480071964025,
                40.6505693028637
            ],
            [
                -73.95582518373742,
                40.650529808078566
            ],
            [
                -73.95870789822969,
                40.65038727378257
            ],
            [
                -73.95892527261269,
                40.65121155009773
            ],
            [
                -73.95915001039316,
                40.65214455720857
            ],
            [
                -73.95932926470222,
                40.652928178711704
            ],
            [
                -73.95945183797798,
                40.653575387815685
            ],
            [
                -73.9596966586303,
                40.654839215228776
            ],
            [
                -73.9598610304714,
                40.65563478893648
            ],
            [
                -73.96069809379553,
                40.655340924680544
            ],
            [
                -73.96156461422332,
                40.6550041171529
            ],
            [
                -73.96188086439827,
                40.654881191549634
            ],
            [
                -73.96245536567206,
                40.65828697752453
            ],
            [
                -73.96281298376562,
                40.660509393313
            ],
            [
                -73.96307724112154,
                40.66213019404663
            ],
            [
                -73.9630696443646,
                40.66220900936865
            ],
            [
                -73.96305428998836,
                40.662287166950705
            ],
            [
                -73.96303126482813,
                40.66236422464174
            ],
            [
                -73.96300069911543,
                40.662439746511495
            ],
            [
                -73.96296276579896,
                40.66251330505162
            ],
            [
                -73.96291767947459,
                40.66258448441146
            ],
            [
                -73.96286569518065,
                40.66265288191772
            ],
            [
                -73.96280710698109,
                40.66271811063324
            ],
            [
                -73.96245015697434,
                40.66318260548278
            ],
            [
                -73.96213146329632,
                40.663208162617515
            ],
            [
                -73.96095595387627,
                40.663285054834
            ],
            [
                -73.96061544798397,
                40.663302750168135
            ],
            [
                -73.96033682872293,
                40.66410869834836
            ],
            [
                -73.95934422428242,
                40.66417564714975
            ],
            [
                -73.95787061929286,
                40.664273358006405
            ],
            [
                -73.95729172603521,
                40.664302632819414
            ],
            [
                -73.95720935391155,
                40.66351739728013
            ],
            [
                -73.95384851077017,
                40.66372780885375
            ],
            [
                -73.95097410077457,
                40.66390486786387
            ],
            [
                -73.94940638959486,
                40.6640053077823
            ],
            [
                -73.94816604109278,
                40.664081821978485
            ],
            [
                -73.94546293588499,
                40.664226104136254
            ],
            [
                -73.94489227687053,
                40.66417414358648
            ],
            [
                -73.94408198675568,
                40.664128572936846
            ],
            [
                -73.94269628894098,
                40.664055129235244
            ],
            [
                -73.9428289224684,
                40.66284748566927
            ],
            [
                -73.94002976952827,
                40.66302074259743
            ],
            [
                -73.93726377502635,
                40.66319183379344
            ],
            [
                -73.93455236748132,
                40.66336228628636
            ],
            [
                -73.93437459333317,
                40.66337281114163
            ],
            [
                -73.93237940108233,
                40.66349778930994
            ],
            [
                -73.93160743269029,
                40.663556723297994
            ],
            [
                -73.93068465493032,
                40.66362047727534
            ]
        ]
    ]

    polygon = Polygons()
    polygon.name = "Bellandur"
    polygon.price = 34
    polygon.geometry = d
    polygon.providerId = provider
    if settings.DEBUG:
        polygon.save()

    return JsonResponse(json.loads(provider.to_json()), safe=False)


@require_http_methods(["GET", "POST"])
def addProvider(request):
    params = request.GET

    provider = Provider()
    provider.name = params['name'] if 'name' in params else ''
    provider.email = params['email'] if 'email' in params else ''
    provider.phoneNumber = params['phoneNumber'] if 'phoneNumber' in params else ''
    provider.language = params['language'] if 'language' in params else ''
    provider.currency = params['currency'] if 'currency' in params else ''
    provider.save()

    js = json.loads(provider.to_json())
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def deleteProvider(request):
    params = request.GET

    pId = params['id']
    provider = fetchProviderWithId(pId)
    provider.delete()

    js = {}
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def updateProvider(request):
    params = request.GET

    pId = params['id']
    provider = fetchProviderWithId(pId)[0]
    provider.name = params['name'] if 'name' in params else provider['name']
    provider.email = params['email'] if 'email' in params else provider['email']
    provider.phoneNumber = params['phoneNumber'] if 'phoneNumber' in params else provider['phoneNumber']
    provider.language = params['language'] if 'language' in params else provider['language']
    provider.currency = params['currency'] if 'currency' in params else provider['currency']
    provider.save()

    js = json.loads(provider.to_json())
    return JsonResponse(js)


@require_http_methods(["GET", "POST"])
def getProvider(request):
    params = request.GET

    provider = fetchProviderWithId(params['id'])[0]

    js = json.loads(provider.to_json())
    return JsonResponse(js)


def fetchProviderWithId(pId):
    return Provider.objects(id=pId)
