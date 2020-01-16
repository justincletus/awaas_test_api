from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save


# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50, help_text="Enter the course name")
    course_sn = models.CharField(max_length=50, default=None, blank=True, null=True, help_text="course short name")
    slug = models.SlugField(unique=False, blank=True, null=True)
    detail = models.TextField(blank=True, null=True, default='some course detail')
    course_year = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6')
    )

    course_year = models.CharField(
        max_length=10,
        choices=course_year,
        blank=True,
        default='1',
        help_text='Select Course year.'
    )
    course_choice = (
        ('FT', 'FullTime'),
        ('PT', 'PartTime'),
        ('CT', 'Correspondence')
    )

    course_type = models.CharField(
        max_length=10,
        choices=course_choice,
        blank=True,
        default='FullTime',
        help_text='Select Course type.'
    )
    category = models.ForeignKey('category.Category', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    college_id = models.ForeignKey('colleges.College', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.course_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.course_name)
        super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('course-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.course_name

def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.course_name)
    exists = Course.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=Course)
