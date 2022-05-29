from io import BytesIO


from django.core.files import File
from django.db import models

class Building(models.Model):
    address = models.CharField(max_length = 200)
    zipcode = models.IntegerField()
    city = models.CharField(max_length = 100)
    def __str__(self):
        return self.address+self.city

class Tenant(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    building = models.ForeignKey(Building, related_name = 'tenantsRN', on_delete = models.CASCADE)
    def __str__(self):
        return self.fname+self.lname+" tenant"

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    lon = models.DecimalField(max_digits=6, decimal_places=2)
    lat = models.DecimalField(max_digits=6, decimal_places=2)
    place = models.CharField(max_length=255)
    depth = models.DecimalField(max_digits=6, decimal_places=2)
    square = models.DecimalField(max_digits=6, decimal_places=2)
    typez = models.CharField(max_length=255)
    descriptions = models.TextField(max_length=255)
    thumbnail = models.ImageField()
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'
def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    slug = models.SlugField()
    date = models.CharField(max_length=255)
    stat1 = models.DecimalField(max_digits=6, decimal_places=2)
    stat2 = models.DecimalField(max_digits=6, decimal_places=2)
    stat3 = models.DecimalField(max_digits=6, decimal_places=2)
    stat4 = models.DecimalField(max_digits=6, decimal_places=2)
    stat5 = models.DecimalField(max_digits=6, decimal_places=2)
    stat6 = models.DecimalField(max_digits=6, decimal_places=2)
    stat7 = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.date
    
    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
    

