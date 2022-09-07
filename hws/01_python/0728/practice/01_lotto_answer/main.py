from lotto import Lotto  # lotto.py에서 Lotto 클래스 import

draw_number = 1023  # 회차 번호(1023, 1024, 1025회차)
lotto = Lotto()  # Lotto 클래스의 인스턴스 선언

# 1. 생성할 로또 번호의 줄 개수 입력받기
while True:
    n = int(input('생성할 로또 줄 개수를 입력하세요.(1줄에서 5줄까지 생성 가능) : '))

    # n이 정상 범위에 있으면 반복문 탈출
    if 1 <= n <= 5:
        break

    # n이 정상 범위에 있지 않으면 문구 출력 후 입력 반복
    print('1줄에서 5줄까지만 생성 가능합니다. 다시 입력하세요.')
    print()

# 2. 로또 번호 생성하기
lotto.generate_lines(n)

# 3. 회차, 추첨일, 로또 번호 출력하기
lotto.print_number_lines(draw_number)

# 4. 당첨 번호와 당첨 결과 출력하기
lotto.print_result(draw_number)
