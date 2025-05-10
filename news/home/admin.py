from django.contrib import admin
from .models import autor, seccion, noticia

# Register your models here.
admin.site.register(autor)
admin.site.register(seccion)
admin.site.register(noticia)