
from django.contrib.auth.backends import ModelBackend

from accounts.models import User

class EmailBackend(ModelBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try: 

            user_obj = User.objects.get(email=username)

            if user_obj.check_password(password):

                return user_obj

            else: return None

        except:

            return None

                
class PhoneBackend(ModelBackend):

    def authenticate(self, request, username = None, password = None, **kwargs):

        try: 
            user_obj = User.objects.get(phone=username)

            if user_obj.check_password(password):

                return user_obj

            else: return None

        except: return None