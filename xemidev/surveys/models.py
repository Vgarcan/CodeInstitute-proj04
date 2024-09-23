from django.db import models
# from projects.models import Category

# Create your models here.


class Question(models.Model):
    category_id = models.ForeignKey(
        'projects.Category', on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
