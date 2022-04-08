from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Core(models.Model):
    title = models.CharField(max_length=200)
    excerpet=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField(max_length=100, unique=True)
    updated=models.DateTimeField(auto_now=True)
    published=models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="pics/",default="pics/default.jpg")
    
    def get_absolute_url(self):
        return reverse('core:single',args=[self.slug])

    class Meta:
        ordering=['-published']

    def __str__(self):
        return self.title
