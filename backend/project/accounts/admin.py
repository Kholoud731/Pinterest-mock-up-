from django.contrib import admin
from .models import User,  Message


admin.site.register(User)
# admin.site.register(Following)
admin.site.register(Message)