from django.conf import settings
from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductsSerializer, DepositOptionsSerializer, NestedSerialzer
import requests
from django.db.models import Max

API_KEY = settings.API_KEY

# Create your views here.
@api_view(['GET'])
def save_deposit_products(request):
    url = f"http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1"
    
    response = requests.get(url).json()
    result = response['result']['baseList']
    
    for prod in result:
        save_product = {
            'fin_prdt_cd' : prod["fin_prdt_cd"],
            'kor_co_nm' : prod["kor_co_nm"],
            'fin_prdt_nm' : prod["fin_prdt_nm"],
            'join_deny' : prod["join_deny"],
            'etc_note' : prod["etc_note"],
            'join_member' : prod["join_member"],
            'join_way' : prod["join_way"],
            'spcl_cnd' : prod["spcl_cnd"],
        }
        serializer = DepositProductsSerializer(data=save_product)
        if serializer.is_valid(): 
            serializer.save()

    optionlist = response['result']["optionList"]
    for opt in optionlist:
        
        # try:
        #     product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
        # except:
        #     product = None

        save_option = {
        'fin_prdt_cd' : opt["fin_prdt_cd"],
        'intr_rate_type_nm' : opt["intr_rate_type_nm"],
        'intr_rate' : opt["intr_rate"],
        'intr_rate2' : opt["intr_rate2"],
        'save_trm' : opt["save_trm"],
        }
        serializer = DepositOptionsSerializer(data=save_option)
        if serializer.is_valid(): 
            product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
            serializer.save(product=product)
    
    return Response({'message' : 'okay'})


@api_view(['GET', 'POST'])
def deposit_products(request):
    # 전체 정기 예금 상품 목록 반환
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        # serializer 자체는 객체라서 .data로 해서 보내줘야댐
        return Response(serializer.data)
    
    # 상품 데이터 저장
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(): # 참고 :form 에서 쓴거랑 다른거임! 이름만 똑같은거임!
            serializer.save() # 얘도 이름만 똑같은거
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    if request.method == 'GET':
        optionlist = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
        serializer = DepositOptionsSerializer(optionlist, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    # 'intr_rate2' 필드에서 가장 큰 값을 가지는 레코드들을 가져옴
    max_intr_rate2 = DepositOptions.objects.all().aggregate(max_intr_rate2=Max('intr_rate2'))['max_intr_rate2']

    if max_intr_rate2 is not None:
        # 'intr_rate2' 필드가 가장 큰 값을 가지는 레코드들을 가져옴
        # top_products = DepositOptions.objects.filter(intr_rate2=max_intr_rate2)
        top_product = DepositOptions.objects.filter(intr_rate2=max_intr_rate2).first()
        serializer = NestedSerialzer(top_product)
        return Response(serializer.data)


        
    #     if top_products.exists():
    #         response_data = []
    #         for top_product in top_products:
    #             # 각 최고 금리 상품의 상세 정보 및 옵션을 함께 직렬화
    #             product_serializer = DepositProductsSerializer(top_product.product)
    #             options_serializer = DepositOptionsSerializer(top_product)

    #             product_data = {
    #                 'product': product_serializer.data,
    #                 'options': options_serializer.data
    #             }
    #             response_data.append(product_data)

    #         return Response(response_data)
    #     else:
    #         # 해당하는 상품이 없는 경우 처리
    #         return Response({"message": "No product found."}, status=status.HTTP_404_NOT_FOUND)
    # else:
    #     # 데이터베이스에 레코드가 없는 경우 처리
    #     return Response({"message": "No records found."}, status=status.HTTP_404_NOT_FOUND)
