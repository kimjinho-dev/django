# 여기에 필요한 모듈을 추가합니다.
import random
import json

from black import main


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for _ in range(n):
            self.number_lines.append(sorted(list(random.sample(list(range(1, 46)), 6))))
            # 1줄 6개 로또번호를 받는 한줄코딩.
            # 순서대로 1~45중 6개를 중복이 없이 set형식으로 뽑는 random.sample()
            # set 형식을 list로 변경시키고 정렬 후 인스턴스.number_lines에 리스트형식으로 추가

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        (
            year,
            month,
            day,
        ) = self.get_draw_date(  # get_draw_data 스태틱 메소드에서 반환된 연도,월,일 값 받아오기
            draw_number
        )
        print('==============================================')
        print(f'                제 {draw_number}회 로또                 ')
        print('==============================================')
        print(f'추첨일 : {year}/{month}/{day} (토)')
        print('==============================================')
        for i, line in enumerate(self.number_lines):  # 뽑은 로또번호 출력을 위한 for문
            print(f'{chr(65+i)} : {line}')  # 인덱스값으로 A~E까지 변경되도록 아스키코드를 사용하여 표현

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        main_numbers, bonus_number = Lotto.get_lotto_numbers(
            draw_number
        )  # get_lotto_numbers 클래스 메소드에서 추첨번호+보너스번호 받아오기
        rank_info = {}
        print('==============================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number} ')
        print('==============================================')

        for i, line in enumerate(self.number_lines):
            (
                same_main_counts,
                is_bonus,
            ) = Lotto.get_same_info(  # get_same_info 클래스 메소드에서 맞은 자리수, 보너스 일치 여부 받아오기
                main_numbers, bonus_number, line
            )
            ranking = Lotto.get_ranking(
                same_main_counts, is_bonus
            )  # get_ranking 클래스 메소드에서 해당 로또번호 순위 받아오기

            print(f'{chr(65+i)} : {same_main_counts}개 일치 ', end='')  # 형식에 맞추어 print문 가공

            if is_bonus == True:  # 보너스 일치시 해당 문구 출력
                print('+ 보너스 일치 ', end='')

            if ranking == -1:  # 낙첨인경우와 당첨된 경우를 구분하여 출력
                print('(낙첨)')
            else:
                print(f'({ranking}등 당첨!)')

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        f = open(f'./data/lotto_{draw_number}.json', 'r')  # f포맷을 사용하여 파라미터값을 이용하여 파일 오픈
        lotto_file = json.load(f)
        f.close()
        year, month, day = map(
            str, lotto_file['drwNoDate'].split('-')
        )  # 연도-월-일 구조인것을 이용하여 split('-')을 이용하여 연도, 월, 일 자료 가공
        return year, month, day  # 이후 print_number_lines 인스턴스 메소드에서 사용가능하도록 튜플형으로 리턴

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 "튜플"을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        f = open(f'./data/lotto_{draw_number}.json', 'r')
        lotto_file = json.load(f)
        f.close()
        main_numbers = []
        for i in range(1, 7):  # drwtNo1~6이므로 문자열 메소드 대신 + 연산자로 키값 만들어주기
            text = 'drwtNo'
            text += str(i)
            main_numbers.append(lotto_file[text])  # 만들어진 키값으로 당첨번호 리스트에 넣어주기
        bonus_number = lotto_file['bnusNo']  # 보너스 번호 넣어주기
        return main_numbers, bonus_number  # get_same_info 스태틱 메소드에서 사용될 값 튜플형으로 반환

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        for num in main_numbers:  # 당첨번호 하나씩 확인하기 위해 리스트에서 꺼내오기
            if num in line:  # num이 line 리스트안에 있는지 확인. 하나의 번호가 일치하는것
                same_main_counts += 1  # 당첨갯수 카운트 증가
        is_bonus = bonus_number in line  # 보너스 번호 일치시 True, 불일치시 False bool값 저장

        return same_main_counts, is_bonus  # get_ranking 스택틱 메소드에서 사용될 값 튜플형으로 반환

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):

        if same_main_counts == 6:  # 모든 값 일치시 1(등) 저장
            ranking = 1  ## 제발 당첨되고싶다...프로그램으로도 못성공함..
        elif (
            same_main_counts == 5 and is_bonus == True
        ):  # 2등 조건인 5개 일치 + 보너스 일치시 2(등) 저장
            ranking = 2  # 이후 3~5 저장
        elif same_main_counts == 5:
            ranking = 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5
        else:  # 2개이하는 -1로 저장
            ranking = -1
        return ranking
