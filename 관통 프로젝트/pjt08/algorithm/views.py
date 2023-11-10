from django.http import JsonResponse
from rest_framework.decorators import api_view
import pandas as pd
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# CSV 파일 읽어와 데이터프레임으로 저장 (서버 시작 시에 한 번만 읽어옴)
csv_path = './data/test_data.csv'
g_df = pd.read_csv(csv_path, encoding='cp949')


# Create your views here.
# @api_view(['GET'])
def CSV_to_DF(request):
# CSV 파일 읽어오기
    data = g_df.to_dict('records')
    return JsonResponse({ 'dat' : data }, json_dumps_params={'ensure_ascii': False})
    

@api_view(['GET'])
def missingValues(request):
    # 결측값은 null로 채워서 반환
    df_filled = g_df.fillna('NULL')
    data = df_filled.to_dict('records')
    
    return JsonResponse({'dat': data})


@cache_page(60 * 2)
def avg_ages(request):
    cache_key = 'avg_ages_result'
    cached_result = cache.get(cache_key)

    if cached_result is None:
        # 캐시가 없는 경우 계산하고 결과를 캐싱
        avg_age = g_df['나이'].mean()
        similar_ages_df = g_df.iloc[(g_df['나이'] - avg_age).abs().argsort()[:10]]
        data = similar_ages_df.to_dict('records')
        cache.set(cache_key, data, 60 * 15)  # 15분 동안 캐싱

    else:
        # 캐시가 있는 경우 캐시된 결과를 사용
        data = cached_result

    return JsonResponse({'dat': data})