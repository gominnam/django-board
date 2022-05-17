from django.db import models
# from django.contrib.auth import get_user_model


class PostCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'PostCategory(id={self.id},name={self.name})'


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, blank=True, null=True)
