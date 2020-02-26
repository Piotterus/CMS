from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    intro = models.TextField(max_length = 250, default=None)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    # add in author later

    def snippet(self):
        return self.intro + '</br>read more...'

    def __str__(self):
        return self.title

# Create your models here.
