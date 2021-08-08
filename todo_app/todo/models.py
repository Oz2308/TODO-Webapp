from django.db import models

class ToDoItem(models.Model):
    item = models.CharField(max_length=200)
    date_posted = models.DateTimeField(auto_now_add=True)
    

