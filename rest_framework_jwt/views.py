from rest_framework.views import APIView
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework.response import Response

from rest_framework_jwt.serializers import TokenSerializer, DeleteUserSerializer, \
    CreateUserSerializer, ChangeEmailSerializer, ChangePasswordSerializer, ChangeUsernameSerializer, \
    AddDocumentSerializer, RemoveDocumentSerializer


class ObtainJSONWebToken(APIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = TokenSerializer

    def get(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'authorization': 'verified'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

obtain_jwt_auth = ObtainJSONWebToken.as_view()


class ObtainJSONWebUser(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CreateUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.DATA)
        print serializer
        if serializer.is_valid():
            return Response({'user': 'created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

create_jwt_user = ObtainJSONWebUser.as_view()


class JSONWebDeleteUser(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = DeleteUserSerializer

    def delete(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'account': 'deleted'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

delete_jwt_user = JSONWebDeleteUser.as_view()


class JSONWebChangeUsername(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ChangeUsernameSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            print serializer
            return Response({'username', 'updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

change_jwt_username = JSONWebChangeUsername.as_view()


class JSONWebChangeEmail(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ChangeEmailSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'email', 'updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

change_jwt_email = JSONWebChangeEmail.as_view()


class JSONWebChangePassword(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = ChangePasswordSerializer

    def put(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'password', 'updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

change_jwt_password = JSONWebChangePassword.as_view()


##################### DOCUMENTS NOW ##########################################

class JSONWebAddDocument(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AddDocumentSerializer

    def post(self, request):
        print "Request: %s" % request
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'document', 'added'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

add_jwt_document = JSONWebAddDocument.as_view()


class JSONWebRemoveDocument(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = RemoveDocumentSerializer

    def delete(self, request):
        serializer = self.serializer_class(data=request.DATA)
        if serializer.is_valid():
            return Response({'document', 'deleted'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

remove_jwt_document = JSONWebRemoveDocument.as_view()