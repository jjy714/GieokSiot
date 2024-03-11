from django.db import models

# Create your models here.


class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class People(models.Model):
    names = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    
    def __str__(self):
        return self.names
    
class Item(models.Model):
    people = models.ForeignKey(People, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    complete = models.BooleanField()
    
    def __str__(self) -> str:
        return self.text