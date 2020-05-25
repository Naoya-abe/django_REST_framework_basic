from rest_framework import serializers

from profiles_api import models

"""
シリアライザー
    ・複雑な入力値をモデルに合わせてバリデーションしてレコードに伝える(入力：シリアライズ)
    ・Model(レコード)を適切な形式にフォーマットする(出力：デシリアライズ)
"""


class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serialize a user profile object"""

    class Meta:
        # Serializersに紐付けるmodelを定義
        model = models.UserProfile
        # 管理したい項目を定義（タプル形式）
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                # セキュリティの関係上パスワードは書き込むだけ。
                'write_only': True,
                # パスワード入力の際に「・・・」となるようにstyleを指定
                'style': {'input_type': 'password'}
            }
        }

    # ModelSerializerにデフォルトでcreate(),update()が実装されているが
    # passwordがハッシュ化されないので、それぞれオーバーライドする
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta():
        model = models.ProfilesFeedItem
        fields = ('id', 'user_profile', 'created_on', 'status_text')
        extra_kwargs = {'user_profile': {'read_only': True}}
