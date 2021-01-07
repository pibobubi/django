from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(default='', max_length=255)
    slug = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Posts(models.Model):
    title = models.CharField(default='', max_length=255)
    slug = models.CharField(default='', max_length=100)
    description = models.TextField(default='')
    content = models.TextField(default='')
    pictrue = models.ImageField(upload_to='post_pictures')
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
