from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.

class University(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter the university name: "
    )
    slug = models.SlugField(unique=True, default="university")
    address = models.TextField(null=True, blank=True)
    country_id = models.ForeignKey('country.Country', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    state_id = models.ForeignKey('country.State', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    college_id = models.ForeignKey('colleges.College', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    university_type = models.ForeignKey('university.UniversityType', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('university-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

class UniversityType(models.Model):
    name = models.CharField(
        max_length=100,
        help_text="Enter the university type eg: private, state, deemed, central."
    )

    def __str__(self):
        return self.name

def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = University.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=University)
