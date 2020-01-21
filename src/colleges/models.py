from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class College(models.Model):
    college_name = models.CharField(
        max_length=100,
        help_text="Enter the college name: ",
        null=False
    )
    slug = models.SlugField(unique=False, default="college", max_length=100)
    address = models.TextField(blank=True, null=True)
    gra = (
        ('UG', 'Under Graduate'),
        ('PG', 'Post Graduate'),
        ('Ph.D', 'Doctrate'),
        ('Diploma', 'Diploma'),
        ('Technical', 'Technical')
    )
    graduate = models.CharField(
        max_length=20,
        choices=gra,
        blank=True,
        default='Under Graduate'
    )

    university_id = models.ForeignKey(
        'university.University',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    course_id = models.ForeignKey(
        'courses.Course',
        default=None,
        related_name='name',
         null=True,
         blank=True,
         on_delete=models.SET_NULL
    )

    def get_absolute_url(self):
        return reverse('college-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.college_name


class CollegeAdmin(admin.ModelAdmin):
    search_fields = ('college_name', )
    list_filter = [
        'university_id'
    ]

def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.college_name)
    exists = College.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=College)
