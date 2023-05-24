from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Review

# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followers')
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    self_introduction = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='profile/%Y/%m/%d/', default='profilepic.png')
    # 
    feel=models.IntegerField(default=1)
    ytb = models.CharField(max_length=100, default='https://www.youtube.com/embed/zaLJfJ8ESm0')
    # 
    action = models.IntegerField(default=0)
    adventure = models.IntegerField(default=0)
    animation = models.IntegerField(default=0)
    comedy = models.IntegerField(default=0)
    crime = models.IntegerField(default=0)
    documentary = models.IntegerField(default=0)
    drama = models.IntegerField(default=0)
    family = models.IntegerField(default=0)
    fantasy = models.IntegerField(default=0)
    history = models.IntegerField(default=0)
    horror = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    mystery = models.IntegerField(default=0)
    romance = models.IntegerField(default=0)
    science = models.IntegerField(default=0)
    tv = models.IntegerField(default=0)
    thriller = models.IntegerField(default=0)
    war = models.IntegerField(default=0)
    western = models.IntegerField(default=0)

class Guestbook(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE) # 방명록 주인
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)