from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null= False, blank= False)
    data_created = models.DateField(auto_now_add=True, null = False, blank = False)
    deadline = models.DateField(null = False, blank=False)
    finished_data = models.DateField(null=True)
