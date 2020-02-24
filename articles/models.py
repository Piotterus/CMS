from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    # add in thunbnail later
    # add in author later

    def snippet(self):
        return self.body[:50] + '...'

    def __str__(self):
        return self.title

# Create your models here.
