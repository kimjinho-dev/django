import requests
from pprint import pprint


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '0bdf8c1af69dea38be1f8564ad3e8265',
        'region': 'KR',
        'language': 'ko',
        'query': title,
    }

    serch_movies = requests.get(BASE_URL + path, params=params).json()
    # D의 코드 재사용

    if not serch_movies["total_results"]:
        return None
        # D의 코드 재사용. 조회값이 없으면 None 반환

    path2 = f'/movie/{serch_movies["results"][0]["id"]}/credits'
    # 검색된 영화의 연출진을 조회하기위해 path2 값 생성
    # 검색된 영화의 처음을 사용해야하기때문에 [0]
    # 해당 id를 추출해야하므로 ["id"]로 해당 키값 사용

    movies_peoples = requests.get(BASE_URL + path2, params=params).json()
    # 자료 추출

    people = {'cast': [], 'direction': []}  # 스태프 정보를 담을 딕셔너리 빈값 생성
    for movies_people in movies_peoples["cast"]:  # 모든 출연진 조회
        if movies_people["cast_id"] < 10:  # cast_id가 10미만 판별
            people['cast'].append(movies_people['name'])  # 해당 사람 이름 추출

    for movies_people in movies_peoples["crew"]:  # 모든 스태프 조회
        if movies_people["department"] == 'Directing':  # 감독인 사람 판별
            people['direction'].append(movies_people['name'])  # 해당 사람 이름 추출

    return people


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
