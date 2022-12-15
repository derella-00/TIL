# 시퀀스(sequence) 자료형
### 시퀀스 타입
  - list
  - tuple
  - ragne
  - string
  - binary

## 1. `list`
`list`는 대괄호 `[]` 및 `list()`로 만들 수 있다.
값에 대한 접근은 `list[i]`를 통해 한다.
> list 변수는 복수형 단어로 지어주자. 

```python
locations = ['강남', '서초', '송파','광진','마포']
locations[0] # '강남' 
locations[0] = '양천' # locations[0] ->  '양천'
locations.append('동탄') # locations -> ['양천', '서초', '송파','광진','마포', '동탄']

locations[5][0] # '동'

print(locations)
```

---

## 2. `tuple`
- 튜플은 리스트와 유사하지만, ()로 묶어서 표현
- tuple은 수정 불가능(불변, immutable), 읽기만 가능


```python
# tuple 만들기
t2 = 1, 2, 3 
t2      # (1, 2, 3)

# 활용
x, y = 1, 2
z = 'abc'
x, y, z     # (1, 2, 'abc')

# 변수 값 swap
x = 1
y = 2
x, y = y, x
print(x, y)     # 2 1 

# 빈 튜플
l = []
t = ()
l, t    # ([], ())

# 하나의 항목으로 구성된 튜플
t = (1)     # 1
t2 = (1,)   # (1,) 뒤에 콤마를 붙여줘야 튜플로 인식
```

---
## 3. `range()`
- `range`는 숫자의 시퀀스를 나타낸다.
```python
range(n)        # 0 ~ n-1
range(n, m)     # n ~ m-1
range(n, m, s)  # n ~ m-1까지 +s만큼 증가
```

```python
# range

range(1)    # range(0, 1)
list(range(1))  # [0]

r1 = range(4, 9)
list(r1)    # [4,5,6,7, 8
r2 = range(0, -10. -1)
list(r2)    # [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
r3 = range(0, 20, 2)
list(r3)    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# random

import random

numbers = [1,2,3,4,5]   

random.choice(numbers)      # 1개 랜덤 뽑기
random.sample(numbers, 2)   # n개 랜덤 뽑기


# lotto

numbers = range(1, 46)

lotto = random.sample(numnbers, 6).sort()   # sort(): 크기대로 정렬
lotto   # [7, 16, 18, 33, 39, 44]
```
---
## 4. 시퀀스에서 활용할 수 있는 `연산자/함수`
|operation|description|
|---------|---|
|x `in` s	|containment test|
|x `not in` s|containment test|
|s1 `+` s2|concatenation|
|s `*` n|n번만큼 반복하여 더하기
|`s[i]`|indexing|
|`s[i:j]`|slicing|
|`s[i:j:k`]|k간격으로 slicing|
|len(s)|길이|
|min(s)|최솟값|
|max(s)|최댓값|
|s.count(x)|x의 개수|

```python
# containment
s = 'string'
'a' in s    # False

l = [1, 2, 3, 4, 5]
2 in l    # True

# concatenation
print('Hello ' + 'everyone')    # Hello everyone
print([1, 2] + [3, 4])    # [1, 2, 3, 4]

# *
[0] * 5    # [0, 0, 0, 0, 0]

# indexing
locations = ['강남','서초','송파','광진','마포']
locations[1: 3]    # ['서초', '송파']

list[x:y]    # idx x ~ idx y-1
list[x:y:z]    # idx x ~ idx y-1인데, step z
list[x::z]    # idx x ~ 끝까지 step z
list[::z]    # idx 0 ~ 끝까지 step z
list[x:y:]    # idx x ~ idx y-1 step 1

# list[::] => 그대로? 나중에 다시 보자

numbers = range(0, 11)
tri = numbers[0::3]
list(tri)    # [0, 3, 6, 9]

len(tri)    # 4
print(min(tri)), print(max(tri))    # 0, 9
```

--- 
## 5. `set`, `dictionary`
### `set({})`
- 수학에서의 집합과 동일하게 처리, 순서가 없는 자료구조
- {}를 통해 만들며, 순서가 없고 `중복`된 값이 없다.
- 빈 집합을 만들려면 set()을 사용해야 한다. {}로 사용 불가능

```python
set1 = {value1, value2, value3}
```

|연산자/함수|설명|
|---|---|
|a `-` b|차집합|
|a `\|` b|합집합|
|a `&` b|교집합|
|a`.difference(b)`|차집합|
|a`.union(b)`|합집합|
|a`.intersection(b)`|교집합|

### `dictionary`는 아이템이 삽입되는 순서를 가지고 있다

```python
set1 = {1, 2, 3}
set2 = {3, 6, 9}

print(set1 - set2)    # {1, 2} 차집합
print(set1 | set2)    # {1, 2, 3, 6, 9}  합집합
print(set1 & set2)    # {3} 교집합
set1.differnce(set2)  # {1, 2} 차집합
set1.union(set2)      # {1, 2, 3, 6, 9} 합집합
set1.intersection(set2) # {3} 교집합

# set은 중복 값이 없다
set3 = {1, 1, 1, 1, 1}
print(set3) = {1}

# set을 이용해 list의 중복값 제거
numbers = [1, 2, 3, 3, 2, 4, 1, 1]

uniq = []
for number in numbers :
    if number not in uniq:
        uniq.append(number)
print(uniq)    # [1, 2, 3, 4]

uniq = set(numbers)
uniq    # {1, 2, 3, 4}

list(uniq)    # [1, 2, 3, 4]
```


### (2) dictionary
- `key`와 `value`가 쌍으로 이루어져 있으며, 궁극의 자료구조
- `{}`를 통해 만들며, `dict()`로 만들 수도 있다.
- `key`는 불변(immutable)한 모든 것이 가능.(불변값 : string. integer,  float, boolean, tuple, range)
- `value`는 `list`, `dictionary` 를 포함한 모든 것이 가능
- 리스트는 인덱스가 정해져 있어 순서가 중요하지만, 딕셔너리는 순서가 없다.
- 중요한 것은 `key` 값으로 `value`를 호출한다는 것
```python
dict_a = {}    # {}
dict_b = dict()    # {}

d = {'a':'에이', 'b':'삐', 'a':'에에이'}    # {'a': '에에이', 'b': '삐'}


phone_book = {'서울':'02', '경기':'031'}
phone_book['서울']    # '02'

# key - value 추가하기
phone_book['경주'] ='054'
phone_book     # {'서울': '02', '경기': '031', '경주': '054'}

# .key 메소드
phone_book.keys()    # dict_keys(['서울', '경기', '경주'])

# .value 메소드
phone_book.values()     # dict_values(['02', '031', '054'])

# .item 메소드
phone_book.item()    # dict_items([('서울', '02'), ('경기', '031'), ('경주', '054')])


```
