from django.db import models
from project import settings
# from accounts.models import User

# Create your models here.

class Pin(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500,null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True)
    website = models.CharField(max_length=500,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='Creator')
    # will be removed
    board = models.ManyToManyField('Board',blank=True)
    # react will be renamed
    topic = models.ManyToManyField('Topic', blank=True)
    #react will be renamed
    react = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+", blank=True)
    # seen by from history

    def __str__(self):
        return self.title


class Board(models.Model):
    name = models.CharField(max_length=50)
    visiblity = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    creator_id = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='Creator')

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500,null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.name



class Save(models.Model):
    pin_id = models.ForeignKey('Pin' ,on_delete=models.PROTECT,verbose_name='Pin saved')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='User')
    time_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('pin_id', 'user_id')

    def __str__(self):
        return self.user_id.username


class History(models.Model):
    pin_id = models.ForeignKey('Pin' ,on_delete=models.PROTECT,verbose_name='Watched Pin')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='User')
    time_seen = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('pin_id', 'user_id', 'time_seen')

    def __str__(self):
        return self.user_id


class Comment(models.Model):
    pin_id = models.ForeignKey('Pin' ,on_delete=models.PROTECT,verbose_name='Pin')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='User')
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    react = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+")


    def __str__(self):
        return self.user_id.username 

class Reply(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.PROTECT, verbose_name='User')
    comment_id = models.ForeignKey('Comment' ,on_delete=models.PROTECT, verbose_name='Comment')
    time_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    react = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="+")


    def __str__(self):
        return self.user_id.username                 
