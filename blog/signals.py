from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.cache import cache

@receiver(user_logged_in, sender = User)
def login_success(sender, request, user, **kwargs):
    # print("---------")
    # print("logged-in Signal.. Run Intro")
    # ip = request.META.get('REMOTE_ADDR')  # This gives the ip Address of the client..
    # print("Client IP: ", ip)
    # request.session['ip'] = ip  # By this we can store ip in session ... 
    ct = cache.get('count', 0, version = user.pk)
    newcount = ct + 1
    print("Login Count ", newcount)
    cache.set('count', newcount, 60*60*24, version = user.pk)