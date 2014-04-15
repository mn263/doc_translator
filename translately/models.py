from django.db import models
from time import time


class Account(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    # documents = models.ManyToManyField(Document)

    def __unicode__(self):
      return '%s' % self.user_name


class Document(models.Model):
    account = models.ForeignKey(Account, related_name='documents')
    title = models.CharField(max_length=100)
    # text = models.CharField(max_length=100000)
    text = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

