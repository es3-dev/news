from django.contrib import admin
from .models import autor, seccion, noticias_main, noticias_aside, noticias_second

# Register your models here.
admin.site.register(autor)
admin.site.register(seccion)
admin.site.register(noticias_main)
admin.site.register(noticias_aside)
admin.site.register(noticias_second)