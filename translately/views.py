from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from translately.serializers import UserSerializer, GroupSerializer, AccountSerializer


def index(request):
  # latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
  template = loader.get_template('translately/static/index.html')
  context = RequestContext(request, {})
  return HttpResponse(template.render(context))


def detail(request, account_id):
  return HttpResponse("You're looking at poll %s." % account_id)


def results(request, account_id):
  return HttpResponse("You're looking at the results of poll %s." % account_id)


def vote(request, account_id):
  return HttpResponse("You're voting on poll %s." % account_id)


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all()
  serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
  queryset = Group.objects.all()
  serializer_class = GroupSerializer


class AccountViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = AccountSerializer

#
# class DocumentViewSet(viewsets.ModelViewSet):
#   """
#   API endpoint that allows groups to be viewed or edited.
#   """
#   queryset = Group.objects.all()
#   serializer_class = DocumentSerializer