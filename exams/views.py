from django.shortcuts import render,get_object_or_404

from rest_framework import authentication,permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,DestroyAPIView,UpdateAPIView

from exams.models import Assessment
from exams.serializers import AssessmentSerializer

from datetime import timedelta,datetime

class AssessmentListView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Assessment.objects.all()

        serializer = AssessmentSerializer(qs,many=True)

        return Response(data=serializer.data)

class AssessmentCreateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [permissions.IsAdminUser]

    def post(self,request):

        form_data = request.data

        serializer = AssessmentSerializer(data=form_data)

        if serializer.is_valid():

            # cleaned_data = serializer.validated_data

            # examdate = cleaned_data.get("exam_date")

            # starttime = cleaned_data.get("start_time")

            # duration = cleaned_data.get("duration")

            # enddatetime = datetime.combine(examdate,starttime) + timedelta(hours = duration)

            # cleaned_data["end_time"] = enddatetime.time()

            # instance = Assessment.objects.create(created_by=request.user,** cleaned_data)

            # serial_inst = AssessmentSerializer(instance)

            serializer.save(created_by= request.user)

            return Response(data= serializer.data)

        else: return Response(data=serializer.errors)

class AssessmentRetrieveUpdateDelete(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]
    
    permission_classes = [permissions.IsAdminUser]

    serializer_class = AssessmentSerializer

    queryset = Assessment.objects.all()

    # def get(self,request,pk=None):

    #     instance = get_object_or_404(Assessment,id=pk)

    #     self.check_object_permissions(request,instance)

    #     serializer = AssessmentSerializer(instance)

    #     return Response(data=serializer.data)

    # def put(self, request, pk=None):

    #     instance = get_object_or_404(Assessment, id=pk)

    #     self.check_object_permissions(request,instance)

    #     form_data = request.data

    #     serializer = AssessmentSerializer(data=form_data, instance=instance)

    #     if serializer.is_valid():


    #         cleaned_data = serializer.validated_data

    #         examdate = cleaned_data.get("exam_date")
    #         starttime = cleaned_data.get("start_time")
    #         duration = cleaned_data.get("duration")

    #         enddatetime = datetime.combine(examdate, starttime) + timedelta(hours=duration)

    #         instance = serializer.save(end_time=enddatetime.time())

    #         serial_inst = AssessmentSerializer(instance)

    #         serializer.save(created_by=request.user)

    #         return Response(data=serializer.data)

    #     else:
    #         return Response(data=serializer.errors)

    
    # def delete(self,request,pk=None):

    #     instance = get_object_or_404(Assessment, id=pk)
        
    #     self.check_object_permissions(request,instance)

    #     instance.delete()

    #     return Response({"message":"Assessment deleted successfully.."})
