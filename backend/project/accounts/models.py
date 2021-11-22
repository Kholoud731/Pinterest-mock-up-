from django.db import models
from django.contrib.auth.models import AbstractUser
from pins.models import Topic
# Create your models here.


class User(AbstractUser):
    # user ide created by itself
    # username exits in AbstractUser with the validation 
    # password in AbstractBaseUser
    # first_name AbstractUser
    # last_name AbstractUser
    # email AbstractUser
    # is_staff to validate the permissions AbstractUser
    # is_active default ture  AbstractUser
    # date_joined once create the account 

    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    dateOfBirth = models.DateField(null=True, blank=True)
    business = models.BooleanField(default=True)
    gender = models.CharField(max_length=6,choices=[('Male','Male'),('Female','Female')])
    avatar = models.ImageField(verbose_name='Avatar',
    upload_to='photo/%y/%m/%d', 
    null=True, blank=True) # we need to add a default photo 
    interest = models.ManyToManyField(Topic)
    followers = models.ManyToManyField('self', related_name='following',blank=True)
 
class Message(models.Model):
    sender = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='sender', verbose_name='sender', null=True)
    receiver = models.ForeignKey('User', on_delete=models.SET_NULL, related_name='receiver', verbose_name='receiver', null=True)
    time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(max_length=200)
    class Meta:
        unique_together = ('sender', 'receiver', 'time')

    def __str__(self):
        return self.receiver.username

