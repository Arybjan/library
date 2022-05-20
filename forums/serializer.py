from rest_framework import serializers
from forums import models


class ForumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumPost
        fields = "__all__"


class ForumTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ForumTopic
        fields = "__all__"


class ForumPostReply(serializers.ModelSerializer):
    class Meta:
        model = models.ForumPostReply
        fields = "__all__"


class MarathonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marathons
        fields = "__all__"


class MarathonsBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MarathonBooks
        fields = "__all__"


class MarathonUser(serializers.ModelSerializer):
    class Meta:
        model = models.MarathonUsers
        fields = "__all__"
