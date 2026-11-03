from django.shortcuts import render,get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions
from rest_framework import serializers
from rest_framework.generics import UpdateAPIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from evaluation.models import Submission,Answer
from evaluation.serializers import SubmissionSerializer,AnswerSerializer
from evaluation.permissions import IsStudentUser

from exams.models import Assessment

from problem.models import Question

class SubmissionStartView(APIView):

    authentication_classes = [JWTAuthentication]

    permission_classes = [permissions.IsAuthenticated,IsStudentUser]

    def post(self,request,pk=None):

        assessment_id = pk

        assessment_obj = get_object_or_404(Assessment,id=assessment_id)

        instance = Submission.objects.create(student=request.user,assessment=assessment_obj)

        serializer = SubmissionSerializer(instance)

        return Response(serializer.data)


class SubmissionRetrieveView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    def get(self,request,pk=None):

        instance = get_object_or_404(Submission,id=pk)

        serializer = SubmissionSerializer(instance)

        return Response(data=serializer.data)


class AnswerCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsStudentUser]

    def post(self,request,pk=None):

        submission_id = pk

        submission_obj = get_object_or_404(Submission,id=pk)

        form_data = request.data

        # validation start

        assessment_obj = submission_obj.assessment

        assessment_questions = Question.objects.filter(assessment=assessment_obj).values_list("id",flat=True)

        question = form_data.get("question")

        if question not in assessment_questions: raise serializers.ValidationError("invalid question,Question noy exist in assessment")

        # validation ends

        serializer = AnswerSerializer(data=form_data)

        if serializer.is_valid():

            serializer.save(submission=submission_obj)

            return Response(data=serializer.data)

        else: return Response(data=serializer.errors)


class AnswerUpdateView(UpdateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAdminUser]

    # serializer_class = AnswerSerializer

    # queryset = Answer.objects.all()

    def patch(self,request,pk=None):

        answer_id = pk

        answer_obj = get_object_or_404(Answer,id=answer_id)

        form_data = request.data

        serializer = AnswerSerializer(data=form_data,instance=answer_obj,partial=True)

        serializer.fields["marks_awarded"].read_only = False
        serializer.fields["feedback"].read_only = False
 

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

            # Answer.objects.filter(id=answer_id).update(** form_data)

            # return Response({"message":"answer evaluated...."})

        else:return Response(data=serializer.errors)