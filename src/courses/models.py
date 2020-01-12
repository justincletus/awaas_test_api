from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=50, help_text="Enter the course name")
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
    college_id = models.ForeignKey('colleges.College', null=True, blank=True, default=None, on_delete=models.SET_NULL)

    def get_absolute_url(self):
        return reverse('course-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.course_name
