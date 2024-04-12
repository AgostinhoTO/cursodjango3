from django.db import models


class Categorias(models.TextChoices):
    TECH = 'TC', 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
        max_length=2,
        choices=Categorias.choices,
        default=Categorias.GR,
    )
    deleted = models.BooleanField(default=True)

    def full_name(self):
        return self.title + self.sub_title
    
    def get_categoty_label(self):
        return self.get_categories_display()

