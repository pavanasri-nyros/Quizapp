from rest_framework import serializers
from .models import Quiz


class QuizSerializers(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id','question','option1','option2','option3','option4','correct_answer')