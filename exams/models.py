from django.db import models

from accounts.models import User

class Assessment(models.Model):

    LANGUAGE_CHOICES = (
                ('python', 'Python'),
                ('java', 'Java'),
                ('c', 'C'),
                ('cpp', 'C++'),
                ('javascript', 'JavaScript')
                ) 
    STATUS_CHOICES = ( 
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('completed', 'Completed')
     )

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=200)

    language = models.CharField(max_length=20,choices=LANGUAGE_CHOICES)

    exam_date = models.DateField()

    duration = models.PositiveIntegerField()

    start_time = models.TimeField()

    end_time = models.TimeField(null=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default="draft")

    def __str__(self):
        return f"{self.title} : {self.exam_date}"
    