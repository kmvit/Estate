from django.db import models
from tinymce import models as tinymce_models



class Category(models.Model):
    name = models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=False)
    parent_category = models.ForeignKey('self', null=True, blank=True)

    def __unicode__(self):
        return self.name



class Estate(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=256, unique=True)
    code = models.IntegerField(default=0, unique=False)
    adres = models.CharField(max_length=256, null=True )
    body = tinymce_models.HTMLField()
    phone = models.CharField(max_length=128, unique=True)
    room = models.IntegerField (blank=True)
    square = models.IntegerField(blank=True)
    price = models.IntegerField(max_length=64, default=0)
    picture1 = models.ImageField(blank=True )
    picture2 = models.ImageField(blank=True )
    picture3 = models.ImageField(blank=True )
    slug = models.SlugField(unique=False)

    def __unicode__(self):
        return self.name

    
class Headermenu(models.Model):
    name = models.CharField(max_length=256, unique=True)
    url = models.CharField(max_length=256, unique=True)

class Page(models.Model):
    title =  models.CharField(max_length=256, unique=True)
    slug = models.SlugField(unique=False)
    body = tinymce_models.HTMLField()
    keyword = models.CharField(max_length=256, unique=True, null=True)
    description = models.CharField(max_length=256, unique=True, null=True)
