from django.contrib.auth.models import User
from translately.models import Document
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Document
      fields = ('id', 'account', 'language', 'title', 'text')













# class AccountSerializer(serializers.Serializer):
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     user_name = serializers.CharField(required=True, max_length=200)
#     password = serializers.CharField(widget=widgets.Textarea, max_length=200)
#
#     def restore_object(self, attrs, instance=None):
#         """
#         Create or update a new snippet instance, given a dictionary
#         of deserialized field values.
#
#         Note that if we don't define this method, then deserializing
#         data will simply return a dictionary of items.
#         """
#         if instance:
#             # Update existing instance
#             instance.user_name = attrs.get('user_name', instance.user_name)
#             instance.password = attrs.get('password', instance.password)
#             return instance
#
#         # Create new instance
#         return Accounts(**attrs)
#
# class DocumentSerializer(serializers.Serializer):
#     pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
#     account = serializers.ForeignKey()
#     file_name = serializers.CharField(required=True, max_length=200)
#     code = serializers.CharField(widget=widgets.Textarea,
#                                  max_length=100000)
#     linenos = serializers.BooleanField(required=False)
#
#     def restore_object(self, attrs, instance=None):
#         if instance:
#             # Update existing instance
#             instance.title = attrs.get('title', instance.title)
#             instance.code = attrs.get('code', instance.code)
#             instance.linenos = attrs.get('linenos', instance.linenos)
#             instance.language = attrs.get('language', instance.language)
#             instance.style = attrs.get('style', instance.style)
#             return instance
#
#         # Create new instance
#         return Snippet(**attrs)