from django.db import models

# from projects.models import Question
# from projects.models import Category

# Create your models here.


class Technology(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    question_id = models.ForeignKey(
        'surveys.Question', on_delete=models.CASCADE)
    category_id = models.ForeignKey(
        'projects.Category', on_delete=models.CASCADE)
