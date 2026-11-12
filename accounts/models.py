from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):   #AbstractUser contains username password password_encryption .. (inherited)

    phone = models.CharField(max_length=12,unique=True)

    ROLE_CHOICES = (
        ("student","student"),
        ("admin","admin")
    )

    role = models.CharField(max_length=200,choices=ROLE_CHOICES,default="student")

class StudentProfile(models.Model):

    skills = models.CharField(max_length=200,null=True)

    qualification = models.CharField(max_length=200,null=True)

    passout_year = models.CharField(max_length=20,null=True)

    github_url = models.URLField(null=True)

    linked_url = models.URLField(null=True)

    student = models.OneToOneField(User,on_delete=models.CASCADE)


# SIGNAL CREATION
# On creating student user , student profile created automatically using signal

from django.db.models.signals import post_save

def create_student_profile(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        StudentProfile.objects.create(student=instance)

post_save.connect(create_student_profile,sender=User)


from django.core.mail import send_mail

def send_invitation_mail(sender,instance,created,*args,**kwargs):

    if created and instance.role == "student":

        send_mail(
                    "Student Profile Creation Confirmation",
                    "Your profile created successfully in codepilot",
                    "ADMIN_EMAIL",
                    ["STUDENT_EMAIL"],
                )

post_save.connect(send_invitation_mail,sender=User)