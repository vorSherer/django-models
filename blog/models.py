from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    body = models.TextField(max_length= 200)

    def __str__(self):
        return self.title
