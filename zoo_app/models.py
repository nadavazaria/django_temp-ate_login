from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    sug_haya = models.CharField(max_length=20)
    desc =  models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ha{self.sug_haya}" 