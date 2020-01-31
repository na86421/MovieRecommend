
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

from .forms import CustomUserCreationForm

#print(Signuser._meta.selected)

class User_(UserAdmin):
    model = User
    form = CustomUserCreationForm
    list_display=['username', 'email', 'selected1', 'selected2','selected3','selected4','selected5','photo', 'user_comment']
    
    
    
class test(admin.ModelAdmin):
    list_per_page=5
    
    

    
admin.site.register(Users)

admin.site.register(User, User_)

#admin.site.register(Signuser)

# Register your models here.