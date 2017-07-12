from rest_framework_mongoengine.viewsets import ModelViewSet

from rest_framework_mongoengine import serializers as mongoserializers

from Mozio.models import Provider, Polygons


class ProviderSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class PolygonsSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Polygons
        fields = '__all__'


class ProviderFiilteredSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'id']


class PolygonsFilteredSerailizer(mongoserializers.DocumentSerializer):

    providerId = ProviderFiilteredSerializer()

    class Meta:
        model = Polygons
        depth = 1
        fields = ["name", "price", "providerId", 'id']


class ProviderViewSet(ModelViewSet):
    lookup_field = 'id'
    serializer_class = ProviderSerializer

    def get_queryset(self):
        return Provider.objects.all()


class PolygonsViewSet(ModelViewSet):
    lookup_field = 'id'
    serializer_class = PolygonsSerializer

    def get_queryset(self):
        return Polygons.objects.all()


class UserEndPointViewSet(ModelViewSet):

    serializer_class = PolygonsFilteredSerailizer

    def get_queryset(self):
        longitude, latitude = self.request.GET['lnlt'].split(',')
        longitude = float(longitude)
        latitude = float(latitude)

        return Polygons.objects(geometry__geo_intersects=[longitude, latitude])
