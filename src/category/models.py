from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Enter course category eg arts, science etc")
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_abosulte_url(self):
        return reverse('category-detail-view', args=[str(self.id)])


def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.name)
    exists = Category.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
        instance.slug = slug

pre_save.connect(pre_save_receiver, sender=Category)
