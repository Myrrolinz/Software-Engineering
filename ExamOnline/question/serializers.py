from rest_framework import serializers

from question.models import Choice, Fill, Judge, Subjective


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class FillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fill
        fields = '__all__'


class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = '__all__'


class SubjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjective
        fields = '__all__'
