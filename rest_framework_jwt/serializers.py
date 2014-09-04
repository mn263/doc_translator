from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from translately.models import Document

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class TokenSerializer(serializers.Serializer):
    """
    Serializer class used to validate a username and password.

    Returns a JSON Web Token that can be used to authenticate later calls.
    """
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = User.objects.get(username=username)
            if password == user.password:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)
                return {
                    'authorization': 'verified'
                }
            else:
                msg = 'Unable to login with provided credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "username" and "password"'
            raise serializers.ValidationError(msg)


class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        if username and password:
            users = User.objects.all()
            for user in users:
                if user.username == username:
                    msg = 'Unable to create account with provided credentials (check that you have a valid email).'
                    print msg
                    raise serializers.ValidationError(msg)

            User.objects.create_user(username, email, password)
            user = User.objects.get(username=username)
            user.password = password
            user.save()
            if not user.is_active:
                msg = 'User account is disabled.'
                print msg
                raise serializers.ValidationError(msg)
            return {
                'user': 'created'
            }
        else:
            msg = 'Must include "username", "email" and "password"'
            print msg
            raise serializers.ValidationError(msg)


class DeleteUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = User.objects.get(username=username)
            if password == user.password:
                user = User.objects.get(username=username)
                documents = Document.objects.filter(account=user.id)
                user.delete()
                documents.delete()
                return {
                    'account': 'deleted'
                }
            else:
                msg = 'Unable to delete account.'
                print msg
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include valid "username" and "password"'
            print msg
            raise serializers.ValidationError(msg)


class ChangeUsernameSerializer(serializers.Serializer):
    username = serializers.CharField()
    new_username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        new_username = attrs.get('new_username')
        password = attrs.get('password')
        if username and new_username and password:
            user = User.objects.get(username=username)
            if password == user.password:
                payload = jwt_payload_handler(user)
                user = User.objects.get(username=username)
                user.username = new_username
                user.save()
                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                msg = 'Unable to update username, invalid credentials provided.'
                print msg
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include valid "username", "new_username" and "password"'
            print msg
            raise serializers.ValidationError(msg)


class ChangeEmailSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        password = attrs.get('password')
        if username and email and password:
            user = User.objects.get(username=username)
            if password == user.password:
                payload = jwt_payload_handler(user)
                user = User.objects.get(username=username)
                user.email = email
                user.save()
                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                msg = 'Unable to update email.'
                print msg
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include valid "username", "email" (the new one), and "password".'
            print msg
            raise serializers.ValidationError(msg)


class ChangePasswordSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        new_password = attrs.get('new_password')
        if username and password and new_password:
            user = User.objects.get(username=username)
            if password == user.password:
                payload = jwt_payload_handler(user)
                user = User.objects.get(username=username)
                user.password = new_password
                user.save()
                return {
                    'token': jwt_encode_handler(payload)
                }
            else:
                msg = 'Unable to update password. Invalid credentials provided.'
                print msg
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "username", "password", and "new_password".'
            print msg
            raise serializers.ValidationError(msg)

##################### DOCUMENTS SERIALIZERS NOW ##########################################


class AddDocumentSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    language = serializers.CharField()
    title = serializers.CharField()
    text = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        language = attrs.get('language')
        title = attrs.get('title')
        text = attrs.get('text')
        if username and password and language and title and text:
            user = User.objects.get(username=username)
            if password == user.password:
                # get highest document id and add one, to get our next new id
                docs = Document.objects.all()
                highest_id = 1
                for doc in docs:
                    if doc.id >= highest_id:
                        highest_id = doc.id + 1
                # now we can make a document of that person
                document = Document(highest_id, user.id, language, title, text)
                document.save()
                return {
                    'document': 'added'
                }
        else:
            msg = 'Must include "username", "password", "language", "title", and "text"'
            print msg
            raise serializers.ValidationError(msg)


class RemoveDocumentSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    document_id = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        document_id = attrs.get('document_id')
        if username and password:
            # first check that the user is valid
            user = User.objects.get(username=username)
            if password == user.password:
                # now get the document and delete it
                document = Document.objects.get(id=document_id)
                if document.account_id == user.id:
                    document.delete()
                    return {
                        'document': 'deleted'
                    }
                else:
                    msg = 'Failed: document is not associated with given account/user.'
                    print msg
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Unable to delete document.'
                print msg
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include valid "username", "password", and "document_id"'
            print msg
            raise serializers.ValidationError(msg)