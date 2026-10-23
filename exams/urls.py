from django.urls import path

from exams.views import AssessmentCreateListView,AssessmentRetrieveUpdateDelete

urlpatterns = [
    path('assessments/',AssessmentCreateListView.as_view()),
    path('assessments/<int:pk>/',AssessmentRetrieveUpdateDelete.as_view()),
]