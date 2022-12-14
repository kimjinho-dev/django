import requests
from pprint import pprint


def ranking():
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '0bdf8c1af69dea38be1f8564ad3e8265',
        'region': 'KR',
        'language': 'ko',
    }
    avg_sort_5 = []  # 상위 5개 영화을 담을 리스트
    avg_list = []  # 평점을 담기위한 리스트

    # popular_movies = requests.get(BASE_URL + path, params=params).json()
    popular_movies = requests.get(BASE_URL + path, params=params)
    popular_movies = popular_movies.json()
    for popular_movie in popular_movies["results"]:
        avg_list.append(popular_movie["vote_average"])  # B의 코드 재사용. 평점을 모두 넣어준다

    avg_temp = sorted(avg_list, reverse=True)[0:5]  # 내림차순으로 정렬된 평점 리스트를 하나 생성한다
    # 상위 5만 남도록 앞에서부터 슬라이싱

    for avg in avg_temp:  # 상위 평점 영화를 담기위한 반복분
        idx = avg_list.index(avg)  # 평점 리스트의 인덱스를 가져온다
        avg_list[idx] = 0  # 중복을 피하기위해 사용한 평점은 초기화한다
        avg_sort_5.append(popular_movies["results"][idx])
        # 최대 평점이 있던 인덱스를 이용하여 해당 영화 정보를 담아준다

    return avg_sort_5


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """
