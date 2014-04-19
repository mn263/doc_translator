from django.contrib.auth.models import User
from translately.models import Document
from translately.serializers import DocumentSerializer, UserSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class UserDetail(APIView):

  def get_user_for_id(self, username, password):
    try:
        print "try user"
        return User.objects.get(username=username, password=password)
    except User.DoesNotExist:
      raise Http404

  def get(self, request, username, password, format=None):
    user = self.get_user_for_id(username, password)
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)


class DocumentDetail(APIView):

  def get_documents_for_account(self, username, password):
    try:
        user = User.objects.get(username=username, password=password)
        return Document.objects.filter(account=user.id)
    except Document.DoesNotExist:
      raise Http404

  def get(self, request, username, password, format=None):
    documents = self.get_documents_for_account(username, password)
    serialized_document = DocumentSerializer(documents, many=True)
    return Response(serialized_document.data)
