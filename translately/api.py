__author__ = 'matt'

from translately.models import Account, Document
from translately.serializers import AccountSerializer
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response


class AccountList(APIView):

  def get(pk, format=None):
    accounts = Account.objects.all()
    serialized_account = AccountSerializer(accounts, many=True)
    return Response(serialized_account.data)


class AccountDetail(APIView):

  def get_object(self, pk):
    try:
      return Account.objects.get(pk=pk)
    except Account.DoesNotExist:
      raise Http404

  def get(self, request, pk, format=None):
    account = self.get_object(pk)
    serialized_account = AccountSerializer(account)
    return Response(serialized_account.data)





