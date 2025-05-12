from django.db import models

# Create your models here.
class author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class section(models.Model):
    id_section = models.AutoField(primary_key=True)
    name_section = models.CharField(max_length=60)

    def __str__(self):
        return self.name_section

class new(models.Model):
    id_news = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    short_description = models.CharField(max_length=124)
    description = models.TextField()
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='noticias/') 
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    section = models.ForeignKey(section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
