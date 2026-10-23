from rest_framework import serializers

from exams.models import Assessment

from datetime import datetime

class AssessmentSerializer(serializers.ModelSerializer):

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