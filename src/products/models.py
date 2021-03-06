from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
)

def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)
# Create your models here.
class Product(models.Model):
    title         = models.CharField(max_length=120)
    slug          = models.SlugField(unique=True)
    description   = models.TextField(blank=True, null=True)    
    price         = models.DecimalField(decimal_places=2, max_digits=3)
    summary       = models.TextField(default='Some more summary')
    featured      = models.BooleanField(default=True)
    published_at  = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    product_image = models.ImageField(upload_to=upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field  = models.IntegerField(default=0)
    width_field   = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ('-published_at', )

    def __str__(self):
        return self.title
    
def pre_save_receiver(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    exists = Product.objects.filter(slug=slug).exists()
    if exists:
        slug = "%s-%s" %(slug, instance.id)
    instance.slug = slug
    # if not instance.slug:
    #     instance.slug = unique_slug_generator(instance)
    
pre_save.connect(pre_save_receiver, sender=Product)
