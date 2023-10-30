# pjt 07

## 느낀 점 및 배운 점 

1. 라이브를 통해 views.py의 함수에서 데이터를 받아오고 그 데이터를 DB에 저장할 때 serializer의 is_valid() 옵션을 통하여 유효성 검사를 한 뒤에 저장하는 방법을 배웠다. 
    - 원래는 아래와 같이 그냥 인스턴스를 하나 생성한 후에 값을 집어 넣고 저장하려고 했으나 이러한 방식은 유효성 검사를 하기에 매우 어려웠다. 
    ```python
    product = DepositProducts()
    ```
    - 받은 값을 딕셔너리 형태로 만든 후에 serializer를 통해 변환하고 serializer.is_valid()를 통과했을 경우에만 serialzer.save()를 하여 더 쉽게 문제를 풀 수 있었다.

2. 추후 option 목록을 출력하기 위해서 요구사항 A에서 optionlist의 값들도 DB에 저장해야 했는데 이 과정이 제일 어려웠다. 
    - 비어 있거나 없는 데이터를 처리하는 방법으로 models.py에서 적절한 default값을 넣어줌으로써 빈 데이터를 처리했다.
    - optionlist에서 만약 옵션과 연결되는 상품이 없을 경우 에러가 발생했다
    ```python
    try:
    product = DepositProducts.objects.get(fin_prdt_cd=opt["fin_prdt_cd"])
    except:
        product = None
    ```
    - 처음에는 try except 구문을 이용하려고 했는데 그런 경우 optionlist DB에 product_id가 모두 NULL 값으로 들어가는 문제가 발생하였다.  
    ```python
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
    ```
    - 다음과 같이 일단 product값을 제외한 값을 먼저 유효성 검사 한 뒤에 만약 유효하다면 product의 db에서 fin_prdt_cd가 동일한 항목을 가져오는 왔다. 그 이후 save를 할 때 product에 값을 넣어줌으로서 문제를 해결할 수 있었다.
  

  3. views.py에서 top_rate를 만들 때 최고 금리가 제일 높은 항목이 여러개일 경우를 고려하여 여러항목을 한번에 출력할 수 있도록 하고 싶었다. 따라서 빈 리스트를 만든 후, 해당하는 모든 data를 product에서 따로, option 따로 구하고 한데 묶은 후 리스트에 추가하는 방식으로 만들었다. 문제가 없이 작동했으나 NestedSerializer를 사용해보라는 강사님의 조언에 따라 수정하였다.
- 수정 전
```python
    @api_view(['GET'])
        def top_rate(request):
            # 'intr_rate2' 필드에서 가장 큰 값을 가지는 레코드들을 가져옴
            max_intr_rate2 = DepositOptions.objects.all().aggregate(max_intr_rate2=Max('intr_rate2'))['max_intr_rate2']

            if max_intr_rate2 is not None:
                # 'intr_rate2' 필드가 가장 큰 값을 가지는 레코드들을 가져옴
                top_products = DepositOptions.objects.filter(intr_rate2=max_intr_rate2).first()
                if top_products.exists():
                    response_data = []
                    for top_product in top_products:
                        # 각 최고 금리 상품의 상세 정보 및 옵션을 함께 직렬화
                        product_serializer = DepositProductsSerializer(top_product.product)
                        options_serializer = DepositOptionsSerializer(top_product)

                        product_data = {
                            'product': product_serializer.data,
                            'options': options_serializer.data
                        }
                        response_data.append(product_data)

                    return Response(response_data)
                else:
                    # 해당하는 상품이 없는 경우 처리
                    return Response({"message": "No product found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                # 데이터베이스에 레코드가 없는 경우 처리
                return Response({"message": "No records found."}, status=status.HTTP_404_NOT_FOUND)
```


- 수정 후

1. serializers.py 
```python
class NestedSerialzer(ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
```
2. views.py
```python
@api_view(['GET'])
def top_rate(request):
    # 'intr_rate2' 필드에서 가장 큰 값을 가지는 레코드들을 가져옴
    max_intr_rate2 = DepositOptions.objects.all().aggregate(max_intr_rate2=Max('intr_rate2'))['max_intr_rate2']

    if max_intr_rate2 is not None:
        # 'intr_rate2' 필드가 가장 큰 값을 가지는 레코드 - 하나만 가져옴
        top_product = DepositOptions.objects.filter(intr_rate2=max_intr_rate2).first()
        serializer = NestedSerialzer(top_product)
        return Response(serializer.data)

```
이 방식은 코드가 좀 더 간결해지지만 최고 금리에 해당하는 경우 하나만을 골라온다.