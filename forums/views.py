from rest_framework import viewsets
from forums import models, serializer


class ForumPostViewSet(viewsets.ModelViewSet):
    queryset = models.ForumPost.objects.all()
    serializer_class = serializer.ForumPostSerializer


class ForumTopicViewSet(viewsets.ModelViewSet):
    queryset = models.ForumTopic.objects.all()
    serializer_class = serializer.ForumTopicSerializer


class ForumPostReply(viewsets.ModelViewSet):
    queryset = models.ForumPostReply.objects.all()
    serializer_class = serializer.ForumPostReplySerializer


class MarathonsViewSet(viewsets.ModelViewSet):
    queryset = models.Marathons.objects.all()
    serializer_class = serializer.MarathonSerializer


class MarathonBooksViewSet(viewsets.ModelViewSet):
    queryset = models.MarathonBooks.objects.all()
    serializer_class = serializer.MarathonsBookSerializer


class MarathonUserViewSet(viewsets.ModelViewSet):
    queryset = models.MarathonUsers.objects.all()
    serializer_class = serializer.MarathonUser
