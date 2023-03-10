from django.db import models

# Create your models here.

class Computer(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Shirt(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Jhumka(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Kangan(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Laptop(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Mobile(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Neklesh(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class T_Shirt(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"
    
class Women_Cloth(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    image = models.ImageField(upload_to='Images')
    
    def __str__(self):
        return f"{self.name} : {self.price}$"