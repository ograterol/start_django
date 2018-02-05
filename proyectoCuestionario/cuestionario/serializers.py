# -*- coding: utf-8 -*-

# Django
from rest_framework import serializers

# local Django
from .models import Answer, Questionary


class QuestionarySerializer(serializers.ModelSerializer):
    """
    Determine how to serialize the fields
    and which fields to show
    """
    user = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Questionary
        fields = '__all__'

    def error_string(self, obj):
        """
        Check that Questionary's attributes are correct
        """
        if obj.isdigit():
            raise serializers.ValidationError(
                "The input can't be only numbers")

    def validate(self, attrs):
        """
        Check that Questionary's attributes are correct
        """

        self.error_string(attrs['name'])

        self.error_string(attrs['questionA'])
        self.error_string(attrs['questionB'])
        self.error_string(attrs['questionC'])
        self.error_string(attrs['questionD'])

        self.error_string(attrs['optionA1'])
        self.error_string(attrs['optionA2'])
        self.error_string(attrs['optionA3'])
        self.error_string(attrs['optionB1'])
        self.error_string(attrs['optionB2'])
        self.error_string(attrs['optionB3'])
        self.error_string(attrs['optionC1'])
        self.error_string(attrs['optionC2'])
        self.error_string(attrs['optionC3'])
        self.error_string(attrs['optionD1'])
        self.error_string(attrs['optionD2'])
        self.error_string(attrs['optionD3'])

        self.error_string(attrs['respuesta_A'])
        self.error_string(attrs['respuesta_B'])
        self.error_string(attrs['respuesta_C'])

        return attrs


class QuestionsSerializer(serializers.ModelSerializer):
    """
    Determine how to serialize the fields
    and which fields to show
    """
    user = serializers.ReadOnlyField(source='user.id')

    questionA_options = serializers.SerializerMethodField()
    questionB_options = serializers.SerializerMethodField()
    questionC_options = serializers.SerializerMethodField()
    questionD_options = serializers.SerializerMethodField()

    class Meta:
        model = Questionary
        fields = (
            'name',
            'questionA',
            'questionB',
            'questionC',
            'questionD',
            'questionA_options',
            'questionB_options',
            'questionC_options',
            'questionD_options',
            'user'
        )

    def get_question_options(self, obj, question):
        options = obj.get_options(question)
        return options

    def get_questionA_options(self, obj):
        return self.get_question_options(obj, 'A')

    def get_questionB_options(self, obj):
        return self.get_question_options(obj, 'B')

    def get_questionC_options(self, obj):
        return self.get_question_options(obj, 'C')

    def get_questionD_options(self, obj):
        return self.get_question_options(obj, 'D')


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'
