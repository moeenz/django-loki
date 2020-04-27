from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return f'Post: {self.title}'
