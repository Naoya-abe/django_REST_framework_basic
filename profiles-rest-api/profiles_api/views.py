# APIViewクラスを継承してクラスベースビューを作成
from rest_framework.views import APIView

# restframeworkでは、値を返す際にResponseを用いる
from rest_framework.response import Response

# HTTPステータスコード(200, 400, etc)
from rest_framework import status

# シリアライザーをimport
from profiles_api import serializers

class HelloAPIView(APIView):
    """Test API View"""

    serializer_class=serializers.HelloSerializers

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to atraditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serializer=self.serializer_class(data=request.data)

        # If validation process succeded is_valid set validated_data
        # dictionary which is used for creation or updating data in DB.
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request, pk=None):
        """Handle updating an object"""
        return Response({'method': "PUT"})

    def patch(self,request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': "PATCH"})

    def delete(self,request,pk=None):
        """Delete an object"""
        return Response({'method': "DELETE"})

