from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        # many=False가 기본값, 근데 단일데이터 아니라 다중데이커일 때는 many=True해줘야댐
        serializer = ArticleListSerializer(articles, many=True)
        # serializer 자체는 객체라서 .data로 해서 보내줘야댐
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): # 참고 :form 에서 쓴거랑 다른거임! 이름만 똑같은거임!
            serializer.save() # 얘도 이름만 똑같은거
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE','PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    
    if request.method == 'GET':
        # many=False가 기본값, 근데 단일데이터 아니라 다중데이터일 때는 many=True해줘야댐
        serializer = ArticleSerializer(article)
        # serializer 자체는 객체라서 .data로 해서 보내줘야댐
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
                # 성공임 당신의 요청으로 인해서 컨텐츠가 없어졌다
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # 수정성공은 보통 200, 그래서 생략가능
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


