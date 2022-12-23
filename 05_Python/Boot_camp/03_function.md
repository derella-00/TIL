# Function
## 목차
- 함수의 정의
- 함수의 Output
- 함수의 Input


## 함수를 쓰는 이유
- 가독성
- 재사용성
- 유지보수

## 함수의 선언과 호출
- 함수의 선언은 `def` 키워드
- 들여쓰기(4 spaces)로 함수의 body를 작성(Docstring은 함수 body 앞에 선택적으로 작성 가능)
- 함수는 매개변수(parameter)를 넘겨줄 수도 있다
- 함수는 동작 후 `return`을 통해 결과값을 전달
- 반드시 하나의 객체를 반환(`return` 값이 없으면, `None`을 반환)
- 함수의 호출은 `함수명()`


---
</br>

### 활용법

```python
def <func>(parameter1, parameter2):
    <코드 블럭>
    return value
```

```python
# 내장함수 목록 확인
dir(__builtins__)
```
</br>

## 함수의 선언과 호출
```python
# 좋은 교보재인듯
num1 = 0
num2 = 1

def func1(a, b):
    return a + b
    
def func2(a, b):
    return a - b
    
def func3(a, b):
    x = 1
    return func1(a, 5) + func2(5, b)

result = func3(num1, num2)
print(result)    # 9
```
</br>

## 함수의 Output
함수는 반환되는 값이 있으며, 어떤 종류라도 상관없다. 다만 **오직 한 개의 객체**만 만 반환된다.
함수가 return 되거나 종료되면, 함수를 호출한 곳으로 돌아간다.

```python
def my_list_max(list_a, list_b):
    total_a, total_b = sum(list_a), sum(list_b)
    if total_a > total_b:
        return list_a
    elif total_a < total_b:
        return list_b
    else:
        return '같음'

my_list_max([10, 3, 1], [5, 9])

# 같음

# 삼항연산
def my_list_max(list_,a list_b):
    return list_a if list_a > list_b else list_b
```

</br>

## 함수의 입력(Input)

### 1. 매개변수
```python
def func(x):
    return x + 2
```
- `x`는 매개변수(parameter)
- 입력을 받아 함수 내부에서 활용할 `변수`
- 함수를 정의하는 부분에서 확인
  </br></br>

### 2. 전달인자(argument)
```python
func(2)
``` 
- `2`는 전달인자(argument)
- 실제로 전달되는 값
- 함수를 호출하는 부분에서 볼 수 있다
</br></br>
## 함수의 인자
함수는 입력값으로 인자를 넘겨줄 수 있다.
</br></br>
### 위치 인자(Positional Argument)
기본적으로 인자는 위치에 따라 함수 내에 전달
```python
def cylinder(r, h):
    return 3.14 * r * r * h

print(cylinder(5, 2))    # 157.0 
print(cylinder(2, 5))    # 62.8

```
</br></br>
### 기본 인자 값(Default Argumnet Values)

함수를 정의할 때, 기본값을 지정하여 함수를 호출할 때 인자의 값을 설정하지 않도록하여, 정의된 것 보다 더 적은 개수의 인자들로 호출 될 수 있습니다.
```python
def func(p1 = v1):
    return p1
```

</br><br>
**기본 인자 값** 활용

> 이름을 받아서 다음과 같이 인사하는 함수 greeting()을 작성하세요. 이름이 길동이면, "길동, 안녕?" 이름이 없으면 "익명, 안녕?" 으로 출력하세요.

```python
def greeting(name = '익명'):
    print(f'{name}, 안녕?')

print(greeting('철수'))     # 입력 있으니까 name = '철수'
print(greeting())     # 입력값이 없으니까 name = '익명'
```
- 기본 인자 값이 설정되어 있더라도 기존의 함수와 동일하게 호출 가능
- 호출 시 인자가 없으면 기본 인자 값이 활용된다.

</br></br>
### **단, 기본 인자값을 가지는 인자 다음에 기본 값이 없는 인자를 사용할 수는 없다.**

```python
def greeting(name='john', age):
    return f'{name}은 {age}살입니다.'

greeting('john', 20)

#  Cell In[10], line 5
    def greeting(name='john', age)
                              ^
# SyntaxError: non-default argument follows default argument
# 
```
</br></br>
### 키워드 인자(keyword Arguments)
**함수를 호출할 때** 키워드 인자를 활용하여 직접 변수의 이름으로 특정 인자를 전달 가능

```python
def greeting(age, name, address, major):
    return f'{name}은 {age}살입니다. 전공은 {major}, 주소는 {address}입니다.'


greeting(20, 'neo', '강남', '사회학')
# 'neo은 20살입니다. 전공은 사회학, 주소는 강남입니다.'

# 아래와 같이 키워드 인자를 사용해서 함수를 호출할 수 있습니다.
greeting(name='neo', age=20, major='사회학', address='강남')

# 위치 인자와 함께 사용할 수 있습니다.
greeting(20, 'neo', major='사회학', address = '강남')

# 키워드 인자를 활용한 다음 위치 인자를 활용 X
```
</br></br>

## 정해지지 않은 여러 개의 인자 처리

```python
print('첫번째 문장')
print('두번째 문장', end='=')
print('세번째 문장', '네번째 문장')
print('a', 'b', 'c', 'd', sep='  ')
print('다섯번째 문장', '마지막 문장', sep='/', end='끝!')

# 첫번째 문장
# 두번째 문장=세번째 문장 네번째 문장
# a  b  c  d
# 다섯번째 문장/마지막 문장끝!
```
</br></br>

### 가변 인자 리스트(Arbitarary Argumnet Lists)
- 앞서 설명한 print()처럼 개수가 정해지지 않은 임의의 인자를 받기 위해서는 함수를 정의할 때 가변 인자 리스트`*args`를 활용

- 가변 인자 리스트는 `tuple` 형태로 처리가 되며, 매개변수에 *로 표현

```python
def my_func(*numbers):
    return numbers

print(my_func(1, 'a', True, [1, 2]))

# (1, 'a', True, [1, 2])
```

</br></br>
### 가변 키워드 인자(Arbitrary Keyword Arguments)


