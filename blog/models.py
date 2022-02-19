from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()

class Comment(models.Model):
    class Meta:
        db_table = "comment"

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=256)