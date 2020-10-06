from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Main(models.Model):
    created_at = models.DateField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    news_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=0)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()
    page_visit = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'AddNews'

    def get_absolute_url(self):
        return reverse('generic-details', kwargs={'pk': self.pk})




class Blog(models.Model):
    created_at = models.DateField()
    status = models.BooleanField(default=0)
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='blog')
    description = RichTextField()

    class Meta:
        # verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('generic-details', kwargs={'pk':self.pk})


