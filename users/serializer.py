from rest_framework import serializers
from users import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = "__all__"


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Roles
        fields = "__all__"


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Occupations
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cities
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = "__all__"


class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genders
        fields = "__all__"
