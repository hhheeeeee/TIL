from django.db import models

# Create your models here.
class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True) # 금융 상품 코드
    kor_co_nm = models.TextField(default='None') # 금융회사명
    fin_prdt_nm = models.TextField(default='None') # 금융상품명
    etc_note = models.TextField(default='None') # 금융 상품 설명
    join_deny = models.IntegerField(default="-1") # 가입제한(1. 제한없음, 2. 서민전용, 3. 일부제한)
    join_member = models.TextField(default='None') # 가입대상
    join_way = models.TextField(default='None') # 가입 방법
    spcl_cnd = models.TextField(default='None') # 우대 조건


class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE, null=True) # 외래키 참조
    fin_prdt_cd = models.TextField(default="None") # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100,default="None") # 저축금리 유형명
    intr_rate = models.FloatField(default="-1") # 저축 금리
    intr_rate2 = models.FloatField(default="-1") # 최고우대금리
    save_trm = models.IntegerField(default="-1") # 저축기간(단위 : 개월)
