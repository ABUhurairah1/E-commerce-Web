from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50,default='',blank=True,null=True)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    host = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=200,default='',blank=True,null=True)
    description = models.TextField(default='',blank=True,null=True)
    image = models.ImageField(upload_to='Product-images/',default='',blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    published = models.DateTimeField(default='',blank=True,null=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title

