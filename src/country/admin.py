from django.contrib import admin
from .models import Country
from .models import State
from .models import City
from .models import Urban

# Register your models here.

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Urban)
