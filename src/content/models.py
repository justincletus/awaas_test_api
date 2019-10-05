from django.db import models


# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)


    def get_absolute_url(self):
        return f"/content/{self.id}/update"

    def __str__(self):
        return self.title
