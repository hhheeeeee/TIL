from django.db import models
from django.conf import settings


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 조회수는 상세 페이지에서만 조회 가능하다고 가정
    views = models.IntegerField(default=0)
    # author 추가
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    # like_users 추가
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_board'
    )

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # author 추가
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)