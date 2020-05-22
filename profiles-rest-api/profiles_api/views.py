# APIViewクラスを継承してクラスベースビューを作成
from rest_framework.views import APIView

# restframeworkでは、値を返す際にResponseを用いる
from rest_framework.response import Response

# HTTPステータスコード(200, 400, etc)
from rest_framework import status

# Viewsetsを継承してクラスベースビューを作成
from rest_framework import viewsets

# Tokenを用いて認証を行う
from rest_framework.authentication import TokenAuthneticatoin

# Serializerをimport
from profiles_api import serializers

# modelをimport
from profiles_api import models

# permissionをimport
from profiles_api import permissioins


class HelloAPIView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to atraditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        # If validation process succeded is_valid set validated_data
        # dictionary which is used for creation or updating data in DB.
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': "PUT"})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': "PATCH"})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializers

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses action (list,create,retrieve,update,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_mothod': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()

    # Token認証を行うことを定義
    authentication_classes=(TokenAuthneticatoin,)
    # 認証方法を定義
    permission_classes=(permissioins.UpdateOwnProfile,)


    """
    ModelViewSetsを使用することで、自動的に以下のメソッドを実装してくれる。
    list(), retrieve(), create(), update(), partial_update(), destroy()
    したがって最低限設定するのは、serializer_classとquerysetだけで良い
    """