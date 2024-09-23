from django.db import models

# from users.models import User

# from techs.models import Technology

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category_name


class Project(models.Model):
    customer_id = models.ForeignKey('users.User', on_delete=models.RESTRICT)
    category_id = models.ForeignKey(
        'projects.Category', on_delete=models.RESTRICT)
    project_name = models.CharField(max_length=150, blank=True)
    description = models.TextField(max_length=150, blank=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=4)
    start_date = models.DateField(blank=True, null=True)
    submition_date = models.DateField(blank=True, null=True)
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.project_name


class SelectedTech(models.Model):
    project_id = models.ForeignKey(
        'projects.Project', on_delete=models.CASCADE)
    technology_id = models.ManyToManyField(
        'techs.Technology')

    def __str__(self):
        return f'{self.project_id} - {self.technology_id}'
