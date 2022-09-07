import re
import requests
from pprint import pprint


def recommendation(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '0bdf8c1af69dea38be1f8564ad3e8265',
        'region': 'KR',
        'language': 'ko',
        'query': title,  # 해당 api는 query값을 필요로 하기때문에 추가
    }

    serch_movies = requests.get(BASE_URL + path, params=params).json()

    if not serch_movies["total_results"]:
        return None

        # 존재하지 않는 영화인경우 예외처리

    path2 = f'/movie/{serch_movies["results"][0]["id"]}/recommendations'
    # 추천영화를 찾는 api 경로값 path2 생성

    recommend_movies = requests.get(BASE_URL + path2, params=params).json()
    # 가운데 path2와 변수만 바꿔서 데이터 추출

    if recommend_movies["total_results"] == 0:
        return recommend_movies["results"]
        # 추천영화가 없을때 빈 리스트를 반환하도록

    result = []
    for recommend_movie in recommend_movies["results"]:
        result.append(recommend_movie["title"])
        # 추천영화가 있을때, 해당 영화의 타이틀만 추출하여 리스트에 저장

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
