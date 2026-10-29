from rest_framework import serializers

from evaluation.models import Submission,Answer

from problem.models import Question

class SubmissionSerializer(serializers.ModelSerializer):

    assessment = serializers.StringRelatedField(read_only = True)
    
    student = serializers.StringRelatedField(read_only = True)

    answers = serializers.SerializerMethodField()

    class Meta:

        model = Submission

        fields = "__all__"

        read_only_fields = [fields]

    def get_answers(self,obj):

        answer_obj = Answer.objects.filter(submission=obj)

        serializer = AnswerSerializer(answer_obj,many=True)

        return serializer.data

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Answer

        fields = "__all__"

        read_only_fields = ["id","submission","marks_awarded","feedback","evaluated_at"]


