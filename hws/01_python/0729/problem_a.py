import re
import requests


def popular_count():
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '0bdf8c1af69dea38be1f8564ad3e8265',
        'region': 'KR',
        'language': 'ko',
    }

    popular_movies = requests.get(BASE_URL + path, params=params).json()
    # 인기영화 목록 자료 json() 사용하여 튜플형으로 저장

    return len(popular_movies["results"])  # 리스트의 길이로 몇개의 인기영화가 있는지 확인


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
