from django.db import  models
from django.urls import reverse

class TypeProduct(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('core:product_list_by_category',
                       args=[self.slug])