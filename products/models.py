import uuid

from django.db import models
from django.utils.text import slugify

from category.models import Category

# Create your models here.

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False)
    title = models.CharField(max_length=225)
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.FloatField()
    # discount_percentage = models.FloatField(blank=True, null=True, default=0)
    # discount_price = models.FloatField(blank=True, null=True)
    # discounted_price = models.FloatField(blank=True, null=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    instock = models.BooleanField(default=True)
    offer_badge = models.BooleanField(default=False)
    popular_items = models.BooleanField(default=False)
    new_arrivals = models.BooleanField(default=False)
    width_field = models.IntegerField(default=400)
    height_field = models.IntegerField(default=400)
    image = models.ImageField(upload_to='images/',
                              null=True,
                              blank=True,
                              width_field='width_field',
                              height_field='height_field',)
    image_url = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.slug} | {self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

