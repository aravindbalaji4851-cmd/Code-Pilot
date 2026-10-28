from rest_framework import serializers

from exams.models import Assessment

from problem.models import Question
from problem.serializers import QuestionSerializer

from datetime import datetime

from django.db.models import Sum

class AssessmentSerializer(serializers.ModelSerializer):

    # greetings = serializers.SerializerMethodField(read_only=True)  # to add field that isnt in model

    question_count = serializers.SerializerMethodField(read_only=True) # to add field that isnt in model

    total_marks = serializers.SerializerMethodField(read_only=True)

    questions = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Assessment

        fields = "__all__"

        read_only_fields = ["id","end_time","created_by"]

    def validate(self,validated_data):

        exam_date = validated_data.get("exam_date")

        start_time = validated_data.get("start_time")

        exam_date_time = datetime.combine(exam_date,start_time)

        if datetime.now() >= exam_date_time:

            raise serializers.ValidationError("Invalid date and time")
        
        return validated_data

    # def get_greetings(self,obj):

    #     return "good mrng"

    def get_question_count(self,obj):

        return Question.objects.filter(assessment=obj).count()

    def get_total_marks(self,obj):

        return Question.objects.filter(assessment=obj).values("score").aggregate(total=Sum("score")).get("total")

    def get_questions(self,obj):

        instances = Question.objects.filter(assessment=obj)

        serializer = QuestionSerializer(instances,many=True)

        return serializer.data