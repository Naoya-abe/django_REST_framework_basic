from rest_framework import serializers

"""
シリアライザー
    ・複雑な入力値をモデルに合わせてバリデーションしてレコードに伝える(入力：シリアライズ)
    ・Model(レコード)を適切な形式にフォーマットする(出力：デシリアライズ)
"""

class HelloSerializers(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)