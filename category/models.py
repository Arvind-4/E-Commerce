from django.db import models

from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=225)
    text = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        return super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.category} | {self.slug}'