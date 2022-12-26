# N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.

numbers = [477162, 658880, 751280, 927930, 297191]

def my_max(numbers):
    max_value = numbers[0]
    for num in numbers:
        if max_value < num:
            max_value = num
    return max_value

print(my_max(numbers))

def my_min(numbers):
    min_value = numbers[0]
    for num in numbers:
        if min_value > num:
            min_value = num
    return min_value

print(my_min(numbers))

# list 값을 하나씩 뽑는 것은 for문의 인덱스 순회로 할 수도 있지만
# 인덱스 없이도 뽑을 수 있다


