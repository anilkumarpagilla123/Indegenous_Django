from django.db import models

# Create your models here.
class Simple(models.Model):
    
    Title= models.CharField(max_length=25)
    Discription= models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Discription
    