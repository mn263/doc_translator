from django.contrib.auth.models import User
from django.db import models


# acc.documents.objects.all()
class Document(models.Model):
  account = models.ForeignKey(User, related_name='documents')
  language = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  text = models.TextField()

  def __unicode__(self):
    return '%s' % self.title