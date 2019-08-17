from django.db import models
from django.urls import reverse

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

# Create your models here.
class Product(models.Model):
    title        = models.CharField(max_length=120)
    slug         = models.SlugField(max_length=200, null=True, blank=True)
    description  = models.TextField(blank=True, null=True)
    price        = models.DecimalField(decimal_places=2, max_digits=1000)
    summary      = models.TextField(default='Some more summary')
    featured     = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})

    class Meta:
        ordering = ('-published_at', )

    def __str__(self):
        return self.title
    
    def pre_save_receiver(self, sender, instance, *args, **kwargs):
        if not instance.slug:
            instance.slug = unique_slug_generator(instance)
        
        pre_save_connect(pre_save_receiver, sender = Product)
