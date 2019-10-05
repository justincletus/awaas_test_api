from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return f"/contact/{self.id}/update"

    def __str__(self):
        return self.name



