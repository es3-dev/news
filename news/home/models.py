from django.db import models

# Create your models here.
class autor(models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class seccion(models.Model):
    id_seccion = models.AutoField(primary_key=True)
    nombre_seccion = models.CharField(max_length=60)

    def __str__(self):
        return self.nombre_seccion

class noticias_main(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/') 
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    seccion = models.ForeignKey(seccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class noticias_aside(models.Model):
    id_aside = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField()
    ciudad = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='noticias/') 
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    seccion = models.ForeignKey(seccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class noticias_second(models.Model):
    id_noticia_second = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='noticias/')
    autor = models.ForeignKey(autor, on_delete=models.CASCADE)
    seccion = models.ForeignKey(seccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo