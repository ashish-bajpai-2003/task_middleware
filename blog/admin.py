from django.contrib import admin
from .models import Post
from .models import Userinfo
# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title' , 'desc']

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display = ['id','clientname' , 'clientip' , 'clientcount', 'clienttime', 'clienturl' , 'clientview' , 'hit_count']
    