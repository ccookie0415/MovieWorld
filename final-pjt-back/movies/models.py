from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    title = models.CharField(max_length=50)
    poster_URL = models.URLField(max_length=200)
    video_key = models.TextField(blank=True)
    release_date = models.DateField()
    overview = models.TextField()
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre, related_name='movie_genre')
    popularity = models.FloatField()
    # 안씀
    season = models.IntegerField(default=0)
    weather = models.IntegerField(default=0)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    title = models.CharField(max_length=50)
    content = models.TextField()
    img = models.ImageField(upload_to='%Y/%m/%d/', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
