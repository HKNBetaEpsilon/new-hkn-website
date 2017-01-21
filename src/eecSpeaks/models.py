from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField("Title", max_length=120)
    text = models.TextField("Blog text")
    author = models.CharField("Author", max_length=120)
    publicationDate = models.DateTimeField("Publication Date", null=True)

    def __unicode__(self):
        return self.title