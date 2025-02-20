# class TraceIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         print("Middleware called")
#         ip = request.META.get('REMOTE_ADDR')
#         print(f"IP: {ip}")  
#         response = self.get_response(request)
#         return response
    

# class LogUserMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         if request.user.is_authenticated:
#             print(f"Logged in user: {request.user.clientname}") 
#         else:
#             print("Anonyms User")
#         response = self.get_response(request)
#         return response

from django.utils.timezone import now
from django.contrib.auth.models import User
from .models import Userinfo
from django.urls import resolve


url_tracking_data = {}
class TrackUserLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_ip = request.META.get('REMOTE_ADDR') 
        url_path = request.path
        view_name = resolve(url_path).func.__name__ if resolve(url_path) else "unknownview"
        if not hasattr(request,'url_tracking_data'):
            request.url_tracking_data = {}
        # url_tracking_data[url_path] = view_name
        if url_path not in request.url_tracking_data:
            request.url_tracking_data[url_path] = {'view_name' : view_name, 'hit_count' : 1}
        else:
            request.url_tracking_data[url_path]['hit_count'] += 1 
        if request.user.is_authenticated:
                user = request.user
                login_record,created = Userinfo.objects.get_or_create(user=user)
                if created:
                    login_record.clientcount = 1
                else:
                    login_record.clientcount += 1
                login_record.clientip = user_ip
                login_record.clientname = user.get_username()
                login_record.clienttime = now()
                login_record.clienturl = url_path
                login_record.clientview = view_name
                login_record.url_tracking_data = request.url_tracking_data
                login_record.save()
       

        else:
            
            login_record, created = Userinfo.objects.get_or_create(user=None, clientip = user_ip, clientname = "Anonymous")
            if created:
                login_record.clientcount = 1
            else:
                login_record.clientcount += 1
            
            
            login_record.clienttime = now()
            login_record.clienturl = url_path
            login_record.clientview = view_name
            login_record.url_tracking_data = request.url_tracking_data
            login_record.save()
        response = self.get_response(request)
        return response


            

    

    