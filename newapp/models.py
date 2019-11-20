from django.db import models

# Create your models here.

# creating new trble


class Blog(models.Model):
    # can use null = true or blank also in CharField
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title
