"""
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
max(), min(), sort() 함수 사용 자제
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))


    def my_sub(numbers):
        max_value = numbers[0]
        min_value = numbers[0]

        for number in numbers:
            if max_value < number:
                max_value = number

        for number in numbers:
            if min_value > number:
                min_value = number

        return max_value - min_value

    # print(numbers)

    print(f'#{tc} {my_sub(numbers)}')


# 최대값은 가장 작은 값으로 잡아야 갱신이 이뤄짐
# 반대로 최소값은 가장 작은 값으로 잡아야 갱신이 이뤄짐




