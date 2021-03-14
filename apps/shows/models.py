from __future__ import unicode_literals
from django.db import models
from datetime import *

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Show title must have at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Show network must have at least 3 characters"
        if len(postData['description']) < 1:
            pass
        elif len(postData['description']) > 1 and len(postData['description']) < 10:
            errors['description'] = "If present, show description must have at least 10 characters"
        if datetime.strptime(postData['release_date'], "%Y-%m-%d") > datetime.now():
            errors['release_date'] = "Show release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.TextField()
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = ShowManager()

