import random


def play():
    user = input("----- 가위(scissor): s, 바위(rock): r, 보(paper): p -----\n 입력: ")
    computer = random.choice(['r', 'p', 's'])

    if user.lower() == computer:
        return "비겼습니다."

    if is_win(user, computer):
        return "이겼습니다!"

    return "졌습니다.."


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') \
            or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    return False


if __name__ == '__main__':
    print(play())
