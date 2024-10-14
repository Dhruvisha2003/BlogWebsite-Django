from typing import Any
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class category(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)

    def __str__(self): 
         return self.name

class blog(models.Model):
    image = models.ImageField()
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=250)
    desc = RichTextField()

    def __str__(self):
        return self.title


class slide(models.Model):
    image = models.ImageField()
    name = models.ForeignKey(category,on_delete=models.CASCADE,default=1) 

class Myprofile(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)
    desc = RichTextField()

    def __str__(self):
        return self.name

class cmt(models.Model):
    blog_id = models.ForeignKey(blog,on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    sub = models.CharField(max_length=100)
    msg = models.CharField(max_length=500)

    def __str__(self):
        return self.name