# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Django
from django.contrib.auth.mixins import (
    LoginRequiredMixin
)
from rest_framework import generics, status
from rest_framework.response import Response


# local Django
from base.mixin import UserPerfilRestMixin

from .models import Answer, Questionary
from .serializers import (
    AnswersSerializer,
    QuestionsSerializer,
    QuestionarySerializer
)


class QuestionaryListFilter(LoginRequiredMixin, generics.ListAPIView):
    """
    Represent a collection of Questionary model filter by user
    """
    serializer_class = QuestionarySerializer

    def get_queryset(self):
        return Questionary.objects.filter(user=self.request.user)


class QuestionaryList(LoginRequiredMixin, generics.ListAPIView):
    """
    Represent a collection of Questionary model
    """
    serializer_class = QuestionarySerializer

    def get_queryset(self):
        return Questionary.objects.filter(is_public=True)


class QuestionaryCreate(LoginRequiredMixin, generics.CreateAPIView):
    """
    Create a new instance of Questionary model
    """
    serializer_class = QuestionarySerializer

    def get_queryset(self):
        return Questionary.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class QuestionaryUpdate(
    LoginRequiredMixin,
    UserPerfilRestMixin,
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Show or Update or delete one instance of Questionary model
    """
    queryset = Questionary.objects.all()
    serializer_class = QuestionarySerializer

    def put(self, request, *args, **kwargs):
        serializer = QuestionarySerializer(data=request.data)
        if serializer.is_valid():
            return self.update(request, *args, **kwargs)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionsCopy(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    """
    Create a new answer from a questionary
    """
    serializer_class = QuestionsSerializer

    def get_queryset(self):
        return Questionary.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class AnswerList(LoginRequiredMixin, generics.ListAPIView):
    """
    Represent a collection of Answer model
    """
    serializer_class = AnswersSerializer

    def get_queryset(self):
        return Answer.objects.all()


class AnswerUpdate(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    """
    Show or Update one instance of Answer model
    """
    serializer_class = AnswersSerializer

    def get_queryset(self):
        return Answer.objects.all()

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
