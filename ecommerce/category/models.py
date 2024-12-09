from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=50, unique=True)
    description=models.TextField(max_length=255,blank=True)
    image=models.ImageField(upload_to='images/categories',blank=True)
    
    class Meta:
        verbose_name='Category'
        verbose_name_plural="Categoies"

    def getUrl(self):
        return reverse('products_by_category',args=[self.slug])
        
    
    def __str__(self):
        return self.categoryName