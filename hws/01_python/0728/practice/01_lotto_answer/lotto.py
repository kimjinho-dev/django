import json
import random


class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []  # 인스턴스 변수에 빈 리스트 할당

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for _ in range(n):
            # 1부터 45까지의 번호 중 랜덤하게 6개 출력하여 오름차순 정렬 후 삽입
            line = sorted(random.sample(range(1, 46), 6))
            self.number_lines.append(line)

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드
    def print_number_lines(self, draw_number):
        year, month, day = self.get_draw_date(draw_number)  # 추첨일의 년, 월, 일

        print('==========================================')
        print(f'             제 {draw_number} 회 로또')
        print('==========================================')
        print(f'추첨일 : {year}/{month}/{day} (토)')
        print('==========================================')

        for i, line in enumerate(self.number_lines):
            print(f'{chr(i + 65)} : {line}')  # 아스키코드를 이용해서 A ~ E로 줄 번호 출력

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        # 메인 번호 리스트, 보너스 번호
        main_numbers, bonus_number = self.get_lotto_numbers(draw_number)

        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')

        for i, line in enumerate(self.number_lines):
            # 당첨 번호와 일치하는 개수, 보너스 번호 일치 여부
            same_main_counts, is_bonus = self.get_same_info(
                main_numbers, bonus_number, line
            )

            ranking = self.get_ranking(same_main_counts, is_bonus)  # 당첨 결과

            # 각 로또 번호 줄에 대해 당첨 결과 출력
            result = f'{chr(i + 65)} : {same_main_counts}개 '
            if is_bonus:
                result += '+ 보너스 '
            result += '일치 '
            result += '(낙첨)' if ranking == -1 else f'({ranking}등 당첨!)'

            print(result)

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json')  # 해당 회차에 맞는 json 파일 열기
        lotto_dict = json.load(lotto_json)  # json -> dict
        draw_date = lotto_dict.get('drwNoDate')  # 추첨일 정보 추출
        year, month, day = draw_date.split('-')  # '-'를 기준으로 년, 월, 일 분리

        return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        lotto_json = open(f'data/lotto_{draw_number}.json')  # 해당 회차에 맞는 json 파일 열기
        lotto_dict = json.load(lotto_json)  # json -> dict

        # 메인 번호에 해당하는 키는 6개이며 'drwt'로 시작. 이를 추출하여 하나의 리스트에 담아 오름차순 정렬
        main_numbers = sorted(
            [value for key, value in lotto_dict.items() if key.startswith('drwt')]
        )
        # main_numbers = sorted([lotto_dict.get(f'drwtNo{i + 1}') for i in range(6)])

        bonus_number = lotto_dict.get('bnusNo')  # 보너스 번호 추출

        return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        # 한 줄의 로또 번호와 메인 번호가 일치하는 개수
        same_main_counts = len(set(main_numbers) & set(line))

        # 보너스 번호 일치 여부
        is_bonus = True if bonus_number in line else False

        return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        ranking = -1

        if same_main_counts == 6:
            ranking = 1
        elif same_main_counts == 5:
            ranking = 2 if is_bonus else 3
        elif same_main_counts == 4:
            ranking = 4
        elif same_main_counts == 3:
            ranking = 5

        return ranking
