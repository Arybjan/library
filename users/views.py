from rest_framework import viewsets
from users import models, serializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer


class RoleViewSet(viewsets.ModelViewSet):
    queryset = models.Roles.objects.all()
    serializer_class = serializer.RoleSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializer.CountrySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = models.Cities.objects.all()
    serializer_class = serializer.CitySerializer


class GenderViewSet(viewsets.ModelViewSet):
    queryset = models.Genders.objects.all()
    serializer_class = serializer.GenderSerializer


class OccupationViewSet(viewsets.ModelViewSet):
    queryset = models.Occupations.objects.all()
    serializer_class = serializer.OccupationSerializer
