# python 1주차 제어문 두번째 문제

## 구구단 출력하기
> 2단부터 9단까지 반복문을 사용하여 구구단을 출력하세요.
---
**[출력 예시]**
```
------- [2 단] -------
2 X 1 = 2
2 X 2 = 4
2 X 3 = 6
2 X 4 = 8
2 X 5 = 10
2 X 6 = 12
2 X 7 = 14
2 X 8 = 16
2 X 9 = 18

------- [3 단] -------
...
```

```python
# 1. ------ [x 단] ------ 은 단수가 바뀔 때 한 번 출력
# 2. 단수는 변하면 곱하는 수가 9번 나올 때까지 고정
# 3. 곱하는 수는 1부터 9까지

for x in range(2, 10) :
    print('\n')
    print(f'------- [{x} 단] -------')
    for y in range(1,10) :
        print(f'{x} x {y} = {x * y}')

```
<br/><br>
### 고민한 내용
몇 단인지 구분할 때 어떻게 각 단 마다 한 번씩만 출력할 수 있을까?

`x에 숫자가 들어가면 한 줄 띄고, x 단 출력하고, x 값이 들어간 상태에서 y 반복`

<br/><br>
## 개인정보보호
> 사용자의 핸드폰번호를 입력 받고, 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리하세요.
> * 핸드폰번호는 010으로 시작해야하고 11자리여야한다.
> * 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다.

---

**[입력 예시]**

01012341234

**[출력 예시]**

*******1234

```python
# 1. 번호를 받고 -> str -> 뒷 네자리를 담을 빈 문자열
# 2. 그 번호가 정말 핸드폰 번호가 맞는지 확인
# -> 11자리가 아니거나, 앞 세 자리가 010으로 시작하지 않으면
# 3. 번호가 맞다면, 뒷 네 자리만 뽑아서 빈 문자열에 저장
# 4. 앞에는 * 7개 두고, 뒷 네자리 출력

pr_nums = ''

ph_number = input('')

if len(ph_number) != 11 or ph_number.startswith('010') == False:
    print('핸드폰번호를 입력하세요')
else:
    for num in range(7,11):
        nums = ph_number[num]
        pr_nums += nums
        
print(f'*******{pr_nums}')

```

</br></br>
### 고민한 내용
입력받은 번호를 어떤 형태로 저장해두어야 할까?

`리스트를 이용하기 위해 빈 문자열을 두어야 할 듯?`

0~6번째 번호를 *로 교체? 아니면 뒤에 네 자리만 저장하고 앞에는 날려?

`날려` `= 뒤 4자리 번호만 이용`

그러면 교체하는 방법은?

`아 있어봐;`


</br></br>


## 정중앙
> 사용자가 입력한 문자열중 가운데 글자를 출력하세요. 
> * 단, 문자열이 짝수라면 가운데 두글자를 출력하세요.

---

**[입력 예시]**

abc

**[출력 예시]**

b

```python
# 1. 가운데 글자는(= 중앙값), 받은 문자열이 홀수면 `(n+1)/2-1`번째, 짝수면 `n/2-1, (n/2+1)-1 번째 문자
# 2. 받은 문자열이 홀수면, 
# 3. 받은 문자열이 짝수면, 

char = input('')

if len(char) % 2 == 1:
    num = int((len(char) + 1) / 2 - 1)
    print(char[num])
else :
    num = int(len(char) / 2 - 1)
    nums = int((len(char)/2))
    print(char[num], char[nums])

```

</br>
### 고민한 내용

`리스트 인덱스를 뽑을 때는 integer가 필요하다`

</br></br>

## 소수 찾기

> 조건, 반복문을 응용하여 numbers 리스트의 요소들이 소수인지 아닌지 판단하는 코드를 작성하세요.

---


**[입력 예시]**

26, 39, 51, 53, 57, 79, 85

**[출력 예시]**
```python
26 는 소수가 아닙니다. 2 는 26 의 인수입니다.
39 는 소수가 아닙니다. 3 는 39 의 인수입니다.
51 는 소수가 아닙니다. 3 는 51 의 인수입니다.
53 는 소수입니다.
57 는 소수가 아닙니다. 3 는 57 의 인수입니다.
79 는 소수입니다.
85 는 소수가 아닙니다. 5 는 85 의 인수입니다.
```

</br></br>

## 로또 등수

> 로또 번호를 입력 받아 당첨 등수 맞추기

- 1등 : 모두 일치
- 2등 : 5개 일치, 나머지 하나는 보너스 숫자 일치
- 3등 : 5개 일치
- 4등 : 4개 일치
- 5등 : 3개 일치
---

**[입력 예시]**

my_numbers = [1, 2, 3, 4, 5, 6]

jackpots_numbers = [2, 1, 4, 5, 6, 7]

bonus_number = 8

**[출력 예시]**

3등

```python
jackpots_numbers = [1, 2, 4, 5, 6, 7]
bonus_number = 8
```

```python
my_numbers = list(input(''))
win_nums = []
let_second = ''

for my_number in my_numbers :
    int_my_number = int(my_number)
    if int_my_number in jackpots_numbers :
        win_nums.append(int_my_number)
    if int_my_number == bonus_number :
        let_second = 'same'

if len(win_nums) == 6:
    print('1등')
elif len(win_nums) == 5 and let_second == 'same' :
    print('2등')
elif len(win_nums) == 5:
    print('3등')
elif len(win_nums) == 4:
    print('4등')
elif len(win_nums) == 3:
    print('5등')
else :
    print('낙첨')

```

</br>
