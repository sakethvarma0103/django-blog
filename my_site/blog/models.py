from typing import Iterable, Optional
from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.

class Author(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email_add=models.EmailField()

    def __str__(self):
        return f"{self.fname} {self.lname}"
    
class Tag(models.Model):
    caption=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=200)
    image_name=models.CharField(max_length=100)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    author=models.ForeignKey(Author,null=True ,on_delete=models.CASCADE)
    content=models.TextField(MinLengthValidator(10))
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"