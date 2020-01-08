from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class College(models.Model):
    college_name = models.CharField(
        max_length=100,
        help_text="Enter the college name: "
    )
    slug = models.SlugField(unique=True, default="college")
    university_id = models.ForeignKey(
        'university.University',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def get_absolute_url(self):
        return reverse('college-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.college_name

def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.college_name)
    exists = College.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=College)
