from django.db import models


class Account(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class Document(models.Model):
    account = models.ForeignKey(Account, related_name='documents')
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=100000)

    def __unicode__(self):
        return '%s: %s' % (self.title, self.text)

