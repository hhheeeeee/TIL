from rest_framework import serializers
from .models import Article

# 모델 폼 만드는 과정과 유사
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title','content')

# 주의사항 : 이름이 꼭 serializers.py 아니어도 되고 위치도 아무데나 둬도 되긴 함
# 근데 관용적으로..
# 규칙! 은 아님

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
