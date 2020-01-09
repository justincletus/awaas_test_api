from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Country(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter the country name: ",
        unique=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class State(models.Model):
    state_name = models.CharField(
        max_length=100,
        help_text="Enter the state name",
        unique=True
    )
    slug = models.SlugField()
    country_id = models.ForeignKey('Country', null=True, blank=True, default=None, on_delete=models.SET_NULL)


    def __str__(self):
        return self.state_name


class City(models.Model):
    city_name = models.CharField(
        max_length=100,
        help_text="Enter the state name",
        unique=True
    )
    state_id = models.ForeignKey('State', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.city_name

class Urban(models.Model):
    urban_name = models.CharField(
        max_length=100,
        help_text="Enter the state name"
    )
    state_id = models.ForeignKey('State', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __str__(self):
        return self.urban_name


def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Country.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=Country)

def pre_save_state_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.state_name)
    exists = State.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_state_receiver, sender=State)
