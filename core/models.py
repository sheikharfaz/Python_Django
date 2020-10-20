from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django import urls
from django.utils.timezone import datetime

# Create your models here.
class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    description = models.TextField(null=True)
    post_image = models.ImageField(upload_to='images/', max_length=2083)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='core')
    slug = models.SlugField(max_length=100, unique=True)
    updated_date = models.DateTimeField(auto_now=True)
    Published = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('core:single', args=[self.slug])

    class Meta:
        ordering = ['-Published']

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        if self.post_image:
            return self.post_image.url
        return '#'

# Create your models here.
class Project(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True, verbose_name='Name')
    Age = models.IntegerField(null=True, blank=True, verbose_name='Age')
    Gender = models.CharField(max_length=10, null=True, blank=True, verbose_name='Gender')
    Leaving_From = models.ForeignKey("LeavingFromPlaces", null=True, blank=True, on_delete=models.CASCADE, related_name="Leaving_From")
    Going_To = models.ForeignKey("LeavingFromPlaces", null=True, blank=True, on_delete=models.CASCADE, related_name="Going_To")
    Date_Of_Journey = models.DateField(default=datetime.now)
    Date_of_return = models.DateField(default=datetime.now)
    Additional_feature = models.ForeignKey("MasterSpares", null=True, blank=True, on_delete=models.CASCADE)
    services = models.ManyToManyField("Facility", null=True, blank=True)
    Type_of_vehicle = models.CharField(max_length=100, null=True, blank=True, verbose_name='Type of vehicle')

    def __str__(self):
        return '{} - {}'.format(self.Name)

    def get_absolute_url(self):
        return urls.reverse('core:project-detail', kwargs={'pk': self.id})

class MasterSpares(models.Model):
    name = models.CharField(max_length=255, verbose_name='Spare Name', null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

class LeavingFromPlaces(models.Model):
    name = models.CharField(max_length=255, verbose_name='Places', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)

# class ServiceList(models.Model):
#     name = models.CharField(max_length=255, verbose_name='services', null=True, blank=True)
#
#     def __str__(self):
#         return '{}'.format(self.name)

class Facility(models.Model):
    facilities = models.CharField(max_length=255, verbose_name='Facilities', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.facilities)

