from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    year= models.IntegerField()
    finish_date = models.DateField(null=True)
    
    class Meta:
        db_table = 'books'
        