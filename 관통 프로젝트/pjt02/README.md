# 어려웠던 부분과 느낀 점
1. 리스트 안에 여러 딕셔너리 요소가 있는 경우


      * 리스트 안에 딕셔너리가 여러개 있을 때 그 딕셔너리 특정 키 값을 가진 요소를 뽑아오는 것이 어려웠다.
   ```python
   try:
           for item in response:
               track_id = item['id']
           for item in response1:
               artist_id =item['id'] 
       except:
           return
   ```
     * 이런 방식으로 뽑아올 수는 있었으나 코드가 너무 길어지고 가독성이 떨어지는 아쉬움이 있었다. 
     * 검색을 해보니

   ```python
   track_id = next((item['id'] for item in response), None)
   artist_id = next((item['id'] for item in response1), None)
   ```
     * 위와 같은 방식으로 코드 길이를 줄일 수 있다는 사실을 알게 되었다.
     
     * 위 코드에서 next() 함수는 response와 response1 리스트에서 첫 번째 항목의 'id' 값을 가져오고 만약 리스트가 비어있다면 None을 반환한다. 

     * next는 기본값을 지정할 수 있는데, 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력하는 함수이다.

   ```python
   my_list = [{'a' : 1}, {'b' : 2}, {'c' : 3}]
   my_list['b'] # 에러 발생
   ```
     * 위와 같이 리스트 안에 여러 딕셔너리가 값으로 있을 때는 키 값으로 그 딕셔너리를 꺼낼 수 없기 때문에 새로 배운 next()함수를 유용하게 쓸 수 있을 것 같다.

2. sorted() 사용하기 

   * 처음에 리스트 안에 자료들이 모두 str형이고 사이사이에 '-'가 들어있기 때문에 바로 sorted를 쓰면 안되는 줄 알고 있었다. 따라서 replace를 이용해서 -를 지운 다음에 int로 변환을 하여 정렬을 한 다음, 다시 원본형과 같은 형식으로 만들어서 result에 append하려고 했다.
   ```python
   my_list = ['2020-08-23', '2023-04-09', '2023-04-01', '2010-01-01']
   print(sorted(my_list, reverse=True))
   # ['2023-04-09', '2023-04-01', '2020-08-23', '2010-01-01']
   ```
   * 하지만 위의 코드와 같이 리스트 안에 str형만 있을 때 그냥 바로 sorted를 써도 정렬이 잘 되서 나온다는 사실을 알게 되었다. 이 덕분에 코드길이를 3줄 정도 줄일 수 있었다!





