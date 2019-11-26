from rest_framework import serializers
from polls.models import Choice, Question



class ChoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        exclude = ['question']
        

class QuestionsSerializer(serializers.ModelSerializer):
    choices = ChoicesSerializer(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ("question_text", "pub_date", "choices", "id", "url","total_votes")
