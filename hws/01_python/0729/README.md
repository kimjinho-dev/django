# PJT 02

### 이번 pjt 를 통해 배운 내용

* 이전 첫번째 관통프로젝트에서 자료를 사용하는것에서 나아가 실제 서버의 api를 활용하여 데이터를 받고, 이를 사용하여 원하는대로 프로그래밍을 한다. 


## A. 인기 영화 조회 (problem_a)

* 요구 사항 : 인기 영화 목록을 응답받아 개수 출력

* 결과 : 인기 영화 개수가 출력된다.
  
* 문제 접근 방법 및 코드 설명  

　requests의 `get()` 메소드를 사용하여 인기영화를 조회한다. 이후 인기영화 목록 개수를 반환한다.
　["results"]는 튜플형의 인기영화정보들이 리스트에 담겨있다. 따라서 `len()`을 사용하여 갯수를 알 수 있다.


  
```python
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

    return len(popular_movies["results"]) # 리스트의 길이로 몇개의 인기영화가 있는지 확인
```
  
* 이 문제에서 어려웠던점

　처음 requests를 사용하다보니 익숙하지 않은 형태여서 사용이 쉽지 않았음. 튜플형이여서 ["results"]로 한번 내부에 들어가야한다는것을 몰라서 시간이 걸렸다.

* 내가 생각하는 이 문제의 포인트

　requests를 사용하여 get 메소드를 사용하는 방식.



## B. 특정 조건에 맞는 인기 영화 조회 1 (problem_b)

* 요구 사항 : 인기영화중 평점 8점 이상 영화목록을 출력한다

* 결과 : 평점 8점이상 영화 목록이 딕셔너리 형태로 리스트안에 담겨서 출력된다.
  
* 문제 접근 방법 및 코드 설명  
  A에서 사용한 코드를 활용하여 자료를 가져오고, 평점값을 비교하여 8점 이상인것은 새로운 리스트에 담아서 반환한다.
  A의 코드를 재사용했고, 추가로 평점 8이상인것을 판별하는 if문과 그것을 넣어줄 리스트를 추가하였다.
  
```python
def vote_average_movies():
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '0bdf8c1af69dea38be1f8564ad3e8265',
        'region': 'KR',
        'language': 'ko',
    }
    avg_over_8 = []  # 평점 8이상의 영화를 넣어줄 리스트 할당

    popular_movies = requests.get(BASE_URL + path, params=params).json()
    for popular_movie in popular_movies["results"]: # 모든 인기영화리스트 조회
        if popular_movie["vote_average"] >= 8: # 평점 8이상의 영화 판별
            avg_over_8.append(popular_movie)   # 리스트에 추가

    return avg_over_8
```
  

* 내가 생각하는 이 문제의 포인트

가져온 자료값을 실질적으로 원하는대로 사용하는것.


## C. 특정 조건에 맞는 인기 영화 조회 2 (problem_c)

* 요구 사항 : 인기영화중 5개를 평점이 높은 순으로 출력한다

* 결과 : 평점이 높은 인기영화 5개가 딕셔너리 형태로 리스트안에 담겨서 출력된다.
  
* 문제 접근 방법 및 코드 설명  
  B의 코드를 재사용한다. 평점을 조회하는 방법을 사용해보았으니 이제 평점중 가장 높은 5개를 찾아서 sort,sorted를 사용해서 해당 영화만 출력한다.

  
```python
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

    popular_movies = requests.get(BASE_URL + path, params=params).json()
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
```
  
* 이 문제에서 어려웠던점

  상위 평점 5개인 영화의 목록을 찾는것을 어떻게 구현할지 고민이 되었다. 
  해당 문제를 위해 모든 평점을 가져와 sort 하기로 했지만, 그러면 어느 자리가 해당 평점인지 알수 없기때문에, 인덱스를 참조할 리스트와, 단순히 상위5위만 알수 있는 리스트로 분류하였다. 이를 통해 상위 평점의 영화를 찾을 수 있었고, 이를통해 중복이 되지않도록 예외처리도 할 수 있엇다.

* 내가 생각하는 이 문제의 포인트

  단순히 최대 평점이 아닌, 상위 5개를 찾는 문제이기때문에 어떻게 상위5인지
  알것인지, 어떻게 이를 추출할지가 포인트였던것같다.


## D. 특정 추천 영화 조회 (problem_d)

* 요구 사항 : 제공된 영화 제목으로 조회하여 추천영화 목록을 출력한다

* 결과 : 검색한 영화에 대한 추천영화목록이 리스트로 표시된다. 없을시 [] 검색한 영화정보가 없다면 None을 반환한다.
  
* 문제 접근 방법 및 코드 설명  
  다른 api path를 사용하기때문에 해당 path부분을 변경하여 재사용한다.
  예외의 경우에 예외처리를 해주고, 위 문제와 마찬가지로 빈 리스트에 값을 추출하여 이를 반환한다.
  
```python
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

    if serch_movies["total_results"] == 0:  
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
```
  
* 이 문제에서 어려웠던점

  예외처리에 대해서 신경을 쓰지않다가 계속되는 오류로 인해 시간이 걸렸다. 도중에 가운데 path가 변함에 따라 이를 바꿔주는 과정에서 오류가 발생했다.

* 내가 생각하는 이 문제의 포인트

  필요한 파라미터와 path값 변경시 이를 유동적으로 잘 변경하여
  원하는 값을 추출할 수 있는지.

## E. 출연진, 연출진 데이터 조회 (problem_e)

* 요구 사항 : 영화제목으로 조회하여 해당 영화의 출연진 그리고 스태프 중 연출진 목록만 출력한다

* 결과 : 각각 cast, directing이 키, 출연진과 연출진 목록이 리스트형으로 값인 튜플형으로 담겨서 출력된다.
  
* 문제 접근 방법 및 코드 설명  
  D의 코드에서 더 나아가 영화 관련인을 조건에 따라 딕셔너리에 넣어 반환한다.
  
```python
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

    if serch_movies["total_results"] == 0:
        return None
        # D의 코드 재사용. 조회값이 없으면 None 반환

    path2 = f'/movie/{serch_movies["results"][0]["id"]}/credits'
        # 검색된 영화의 연출진을 조회하기위해 path2 값 생성
        # 검색된 영화의 처음을 사용해야하기때문에 [0]
        # 해당 id를 추출해야하므로 ["id"]로 해당 키값 사용

    movies_peoples = requests.get(BASE_URL + path2, params=params).json()
        # 자료 추출

    people = {'cast': [], 'direction': []} # 스태프 정보를 담을 딕셔너리 빈값 생성 
    for movies_people in movies_peoples["cast"]:    # 모든 출연진 조회
        if movies_people["cast_id"] < 10:           # cast_id가 10미만 판별
            people['cast'].append(movies_people['name']) # 해당 사람 이름 추출

    for movies_people in movies_peoples["crew"]:    # 모든 스태프 조회
        if movies_people["department"] == 'Directing':  # 감독인 사람 판별
            people['direction'].append(movies_people['name'])   # 해당 사람 이름 추출

    return people
```
  
* 이 문제에서 어려웠던점

  자료의 값이 길다보니 해당 정보에 어떤 키값이 있는지, 어떤 키값을 조회해야하는지에 대한 검색 시간이 오래 걸렸다.

* 내가 생각하는 이 문제의 포인트

  여러 자료에 대한 조건 탐색, 이후 추출

-----


# 후기

* 첫번째 관통 프로젝트와 같이 자료에서 데이터를 추출하는것은 같았지만, 실제 서버에서 직접 받아오다보니 더 많은 작업을 수행할 수 있었다.
* 이를 통해 기상청 정보를 이용해 날씨를 알려주는 프로그램같이 실 데이터를 활용한 프로그래밍을 할수있겠다는 생각이 들었다.
