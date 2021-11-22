from django.contrib import admin
from .models import Pin,Topic, Board, Save, History, Comment, Reply


# Register your models here.
admin.site.register(Pin)
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Save)
admin.site.register(History)
admin.site.register(Comment)
admin.site.register(Reply)
