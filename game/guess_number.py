import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    print(f'----- 1과 {x} 사이의 정수 중에 숫자를 맞추는 게임입니다. -----')

    while guess != random_number:
        guess = int(input('숫자를 입력하세요:  '))

        if guess < random_number:
            print('입력한 숫자보다 큽니다. 다시 입력해주세요')

        elif guess > random_number:
            print('입력한 숫자보다 작습니다. 다시 입력해주세요')

    print(f'WOW! 정답입니다! 축하합니다. \n정답: {random_number}')


guess(10)
