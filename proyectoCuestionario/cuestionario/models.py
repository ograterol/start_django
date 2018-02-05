# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from users.models import User


class Questionary(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField(max_length=50)
    questionA = models.TextField()
    optionA1 = models.CharField(max_length=50)
    option_pointA1 = models.IntegerField()
    optionA2 = models.CharField(max_length=50)
    option_pointA2 = models.IntegerField()
    optionA3 = models.CharField(max_length=50)
    option_pointA3 = models.IntegerField()
    questionB = models.TextField()
    optionB1 = models.CharField(max_length=50)
    option_pointB1 = models.IntegerField()
    optionB2 = models.CharField(max_length=50)
    option_pointB2 = models.IntegerField()
    optionB3 = models.CharField(max_length=50)
    option_pointB3 = models.IntegerField()
    questionC = models.TextField()
    optionC1 = models.CharField(max_length=50)
    option_pointC1 = models.IntegerField()
    optionC2 = models.CharField(max_length=50)
    option_pointC2 = models.IntegerField()
    optionC3 = models.CharField(max_length=50)
    option_pointC3 = models.IntegerField()
    questionD = models.TextField()
    optionD1 = models.CharField(max_length=50)
    option_pointD1 = models.IntegerField()
    optionD2 = models.CharField(max_length=50)
    option_pointD2 = models.IntegerField()
    optionD3 = models.CharField(max_length=50)
    option_pointD3 = models.IntegerField()
    user = models.ForeignKey(
        User, related_name="questionaries", on_delete=models.CASCADE
    )
    respuesta_A = models.TextField(default="")
    respuesta_B = models.TextField(default="")
    respuesta_C = models.TextField(default="")
    is_public = models.BooleanField(default=True)

    def get_options(self, question, num_options=3):
        options = list()

        for index in range(0, num_options):
            option_name = 'option%s%s' % (question, index + 1)
            option = getattr(self, option_name, False)

            options.append((option, option))

        return options


class Answer(models.Model):
    option_A = models.IntegerField()
    option_B = models.IntegerField()
    option_C = models.IntegerField()
    option_D = models.IntegerField()
    questionary = models.ForeignKey(
        Questionary, related_name="questionary", on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User, related_name="answers", on_delete=models.CASCADE,
        blank=True, null=True
    )
