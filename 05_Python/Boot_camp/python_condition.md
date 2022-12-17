# 제어문(Control Statement)

순차적인 코드의 흐름을 제어하는 것을 제어문이라고 하고, 제어문은 크게 조건문과 반복문으로 나눌 수 있다.

## `조건문`(Condition Statement)
 `if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용

### 조건문의 구성

```python
# 문법
if <expression>:
    <코드 블럭>
else:
    <코드 블럭>

# 예시
if a > 0:
    print('양수입니다.')
else:
    print('음수입니다.')
```

```python
# 크리스마스 판독기

date = input('날짜를 입력해주세요 ex)12/24 : ')

if date == '12/25':
    print("크리스마스 입니다 :)")
else:
    print("크리스마스가 아닙니다 :(")d
```


```python

#홀짝 판독기

num = int(input('숫자를 입력하세요 : '))

if num % 2 == 0 :    # modulo
    print('홀')
else :
    print('짝')

# num % 2 -> 연산의 결과는 하나, 따라서 저건 num % 2 가 아니라, 0 임
# 그래서 num % 2 => bool(1) 이면 True가 나오고, bool(2)이면 False가 나오겠지?
# 이건 boolean을 이용해 조건문을 이요한 것


# bool과 len 이용
l = []

if len(l) != 0 :
    print('안비어있음')
else :
    print('비어있음')

```

### `elif` 복수조건
2개 이상의 조건을 활용할 경우 `elif<조건>:`을 활용한다.
```python
# 미세먼지
dust = int(input('점수를 입력하세요 : '))

if dust > 150 :
    print("매우 나쁨")
elif dust > 80 :
    print("나쁨")
elif dust > 30 :
    print("보통")
else :
    print("좋음") 

# 연산자 조건 쓸 때 '150 >= dust > 80:' 이렇게도 가능

```

## `중첩`조건문(Nested Conditional Statement)

```python
# 심한 미세먼지

dust = 400

if dust > 150:
    print('매우 나쁨')
    if dust > 300 :
        print('실외활동을 자제하세요.')
elif dust > 80 :
    print('나쁨')
elif dust > 30 : 
    print('보통')
elif dust >= 0 :
    print('좋음')
else :
    print('값이 잘못되었습니다.')

```

## `조건 `표현식(Conditional Expression)
- 조건 표현식은 일반적으로 조건에 따라 값을 정할 때 활용
- **삼항 연산자(Ternary Operator)** 라고 부르기도 하다.


### 활용법
- true_value if <조건식> else false_value
```python
num = int(input('숫자를 입력하세요 : '))

print('양수') if (num > 0) else print('음수')

```

```python
# fizz buzz Quiz

v = int(input("number? "))

if v % 15 == 0 :
    print("fizzbuzz")
elif v % 5 == 0 :
    print("buzz")
elif v % 3 == 0 :
    print("fizz")
else :
    print(v)
```

## `반복문`(Loop Statement)
```python
while True :
    print('조건식이 참일 때까지')
    print('계속 반복')

# 주의사항
while 문 역시 조건식 뒤에 콜론(:)이 반드시 필요하며, 이후 실행될 코드 블럭은 4spaces로 들여쓰기를 합니다.
반드시 종료조건을 설정해야 합니다.

# 반복문은 수동이다
while을 하려면 시작과 끝을 설정해주어야 한다.

# 예시
menus = ['돈까스','떡볶이','닭칼국수','햄버거','탕수육']

idx = 0    # 시작
while n < 5:    # 끝
    print(menus[idx])
    n += 1     
```

```python
# 인사 받아 줄 때까지 인사하기
user_input = ''

while user_input != '안녕':    # while not user_input == '안녕' :
    print('안녕?')
    user_input = input('안녕? \n')

# 그런데 여기서 이 시스템을 받아들이는 사람 입장에서 생각해보면,
# 가이드를 더 추가해줄 수 있지 않겠어?
```

```python

# 한 자리씩 출력하기
# 사용자로부터 숫자 입력 받은 양의 정수의 각 자리 수를 1의 자리부터 차례대로 출력하는 코드를 작성

num = input('어떤 숫자를 원해?')

num = '185'

idx = len(num) -1
while 


# 정수로 풀이하는 방법
while 

```
```python
# Total의 두둥등장

# num = int(input())

num = 5     # 코드를 작성할 때 imput 값을 넣어서 계속 input 넣고 하지 말고 임의의 작은 숫자를 넣어서 원하는 결과가 나오는지 확인한 후, 다시 num = ,,, 을 살려서 원래 의도한 코드를 작성한다

i = 1    # i를 계속 더해나감. num보다 작거나 같을 때까지
total = 0    # i를 더한 값을 담아줄 박스를 구비해 놓고
while i <= num :
    total += i
    i += 1
    
print(total)

```

## `for` 문
`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회한다.

```python
# 예시

for fruit in ['apple', 'mango', 'banana']:
    print(fruit)
print('끝')
```

```python
# while로 반복

idx = 0
numbers = [1, 2, 3, 4, 5]

while idx < len(numbers) :
    print(number[idx])
    idx += 1


# for로 반복

numbers = [1, 2, 3, 4, 5]

for number in numbers :
    print(number)


# for 문으로 사용자가 입력한 문자를 한글자씩 출력

chars = input('문자를 입력하세요 : ')

for char in chars :
    print(char)
```

### `문자열`(String) 순회
range(문자열의 길이)
range()와 순회할 srting의 길이를 활용하여 index를 조작 가능

```python
chars = ['a', 'b', 'c', 'd']

for idx in range(len(chars)) :
    chars[idx] = 1

print(chars)    # [1, 1, 1, 1]
```

### `딕셔너리` 순회(반복문 활용)
딕셔너리에 `for`문을 실행하면 기본적으로 다음과 같이 동작

```python
grades = {'john' : 80, 'eric' : 90}

# for문을 통해 딕셔너리 grades를 순회하면서 출력 값을 확인
for student in grades :
    print(student)    # john, eric
                      # dictionary를 넣으니까 key가 나오네


# 위에서 출력한 학생 이름(key)을 활용하여 점수(value)를 출력해봅시다.
for student in grades:
    print(f'{student} => {grades[student]}')

# john => 80
# eric => 90
```

#### 딕셔너리 `.items()` 메서드
```python
# (1) k에 딕셔너리 key, value 튜플로 변환
for k in grades.items():
    print(k)

# ('john', 80)
# ('eric', 90)

# (2) k, v 에 key, value 각각 할당
for k, v in grades.items():
    print(k, v)

# john 80
# eric 90
```

#### dictionary 에서 `for`를 활용하는 네 가지 방법
```python

dict = {'john':  80, 'eric': 90}

# 0. dictionary 순회(key 활용)
for key in dict:
    print(key)    # john, eric -> 기본 출력은 key 값?
    print(dict[key])    # 80, 90 -> dic의 key 값을 넣어주면 해당 value 출력?

# 1. `.keys()` 활용
for key1 in dict.keys():    # dict의 key를 뽑아서 'key1'에 넣어주고,
    print(key)    # 'key1'에 들어 있는 key 출력 
    print(dict[key])    # 'key1'에 들어 있는 key의 value 출력

# 2. `.values()` 활용
# # 이 경우 key는 출력할 수 없음
for val in dict.values():    # value 들 뽑아 주는 메서드
    print(val)    

# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)

```

## `enumerate()` 
$$ enumerate()\ 모르겠다$$
- index와 value를 함께 활용
- enumerate()를 활용하면, 추가적인 변수를 활용할 수 있다.
- enumerate()는 내장 함수 중 하나

```python
members = ['민수', '영희', '철수']

list(enumerate(members))

# [(0, '민수'), (1, '영희'), (2, '철수')]
# index와 해당 리스트 값 출력
```
```python
# enumerate() 에 의해 반환되는 인덱스와 값(value)를 함께 출력하는 for 반복문

for idx, member in enumerate(members):
    print(idx, member)

# 0 민수
# 1 영희
# 2 철수
```

```python
print(enumerate(members))
print(list(enumerate(members)))
```

## List Comprehension
- List Comprehension은 표현식과 제어문을 통해 리스트를 생성
- 여러 줄의 코드를 한 줄로 줄일 수 있습니다.

### 활용법
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
### 세제곱 리스트
1~3 까지의 숫자로 만든 세제곱 담긴 리스트 `cubic_list`
```python
cubic_numbers = []

for num in range(1, 4):
    cubic_numbers.append(num ** 3)

cubic_numbers
# [1, 8, 27]

# 이를 List Comprehension을 활용하여 작성

cubic_list = [num ** 3 for num in range(1, 4)]
cubuc_list
# [1, 8, 27]
```

```python
# 10 * 10 체스판
pan = [0 for _ in range(10)]
pan = [[0 for _ in range(10)] for _ in range(10)]  # _ 가 무슨 관례,,?
pan

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

```

## Dictionary comprehension
### 활용법
`iterable`에서 `dict`를 생성할 수 있습니다.

{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})
```python
cubic = {}

for number in range(1, 4 ):
    cubic[number] = number ** 3
print(cubic)

# {1: 1, 2: 8, 3: 27}
```

```python
# Dictionary comprehension 활용
cubic = {n: n ** 3 for n in range(1, 4)}
print(cubic)

# {1: 1, 2: 8, 3: 27}
```

## `break`
반복문 종료
- `for`나 `while` 문에서 빠져나간다.

```python
# 종료 조건이 있는 while 문을 작성
# n의 초기값을 0으로 할당,
# n의 값이 3보다 작은 경우 n을 출력한 후, n을 1씩 증가시키는 while 반복문 코드 작성 

n = 0
while n < 3:
    print(n)
    n += 1

# 0
# 1
# 2


# 종료 조건이 없는 while 문 break을 활용하여 종료

n = 0
while True:
    if n == 3:
        break
    print(n)
    n += 1
```

```python
# for문 break

for num in range(10):
    print(num)
    if num > 0 :
        print('끝')
        break
# 0
# 1
# 끝

for num in range(10) :
    if num > 1 :
        print('끝')
    print(num)
# 0
# 1
# 끝

```


```python
# 조건문과 반복문, break를 활용하여 리스트에서 쌀이 나왔을 떄 for 문을 멈추는 코드 작성

rice = ['보리', '보리', '보리', '쌀', '보리']

for grain in rice :
    if grain != "쌀" :
        print(grain)
    else :
        print(grain)
        print("잡았다!")
        break

# 코드 비교
for grain in rice:
    print(grain)    # 일단 뭐가 나왔는지, 출력은 해야지 그럼 위처럼 else가 필요없겠구나
    if grain == '쌀':
        print('잡았다')
        break
```
## `continue`
continue문은 continue 이후의 코드를 수행하지 않고, `다음 요소부터 계속(continue)`하여 반복을 수행합니다.

```python
# for문을 통해 0~5까지의 숫자를 반복하며,
# 짝수인 경우 continue하고,
# 홀수인 경우 해당 숫자를 출력하는 코드를 작성

nums = range(6)

for num in nums:
    if num % 2 == 0 :
        continue
    print(num)

# 코드 비교

for i in range(6):
    if i % 2 == 0:
        continue
        # continue 이후의 코드는 실행되지 않습니다.
    print(f'{i}는 홀수다.')

```

```python
#나이가 입력된 리스트가 있을때, 조건문과 반복문, continue문을 활용하여 20살 이상일때만 "성인입니다"라는 출력을 하는 코드를 작성하시오.

ages = [10, 23, 8, 30, 25, 31]

for age in ages:
    if age >= 20:
        print(f'{age}살은 성인입니다.')
        continue

# continue 를 이용하려면 좀 억지이긴 하지만, 20살 미만이 나왔을 때 continue로 넘겨서 20살 이상만 출력되도록 유도...


for age in ages:
    if age < 20:
        continue
    print(f'{age} 살은 성인입니다. \n')

```

## `pass`
아무 것도 하지 않는다.

## `else`
끝까지 반복문을 실행한 이후에 실행된다.

반복문이 `break` 문으로 종료될 때는 실행되지 않는다.

```python
# 'apple' 이라는 문자열을 순회하면서
# 'b'가 있으면 'b!'를 출력한 후 break에 의해 순회를 종료,
# 문자열 끝까지 순회해도 'b'가 없는 경우, 'b가 없습니다.'를 출력

for char in 'apple':    # char는 관례
    if char == 'b' :
        print('b!')
        break
else:
    print('b가 없습니다.')
```

```python
# numbers 리스트에 4가 있을 경우 True를 출력하고, 없을 경우 False를 출력

for number in numbers :
    if number == 4: 
        print('True')
        break
else :
    print('False')
```