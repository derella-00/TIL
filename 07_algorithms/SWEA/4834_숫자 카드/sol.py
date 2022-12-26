import sys

sys.stdin = open('input.txt')

T = int(input())
count = {}

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(input())

    count = {}

    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1

    # 가장 많이 나온 숫자
    # 배열로 설정할 시 인덱스로 접근하는 것이 필요하다?
    for key, value in count.items():
        if value == max(count.values()) and key == max(count.keys()):
                Any = key

    print(f'#{tc} {Any} {max(count.values())}')

