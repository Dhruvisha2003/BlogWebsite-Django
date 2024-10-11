from django.db import models

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
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class slide(models.Model):
    image = models.ImageField()
    name = models.ForeignKey(category,on_delete=models.CASCADE,default=1)

class Myprofile(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=10000)

    def __str__(self):
        return self.name


