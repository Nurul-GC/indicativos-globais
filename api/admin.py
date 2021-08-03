from django.contrib import admin

from api.models import Indicativos, Paises

# Register your models here.
admin.site.register(Paises)
admin.site.register(Indicativos)
