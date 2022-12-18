# python 1주차 제어문 첫번째 문제

## 1. 모음 제거하기
</br>
> 다음 문장의 모음을 제거한 새로운 문자열 출력

[입력 예시]

`'Life is too short, you need python'`

[출력 예시]

`Lf s t shrt, y nd pythn`

```python
my_str = 'Life is too short, you need python'

# 아래에 코드를 작성하세요.

# 1. 새로운 문자열을 담을 변수를 두고,
# 2. my_str에서 한 문자씩 뽑아서, 
# 3. 해당 문자열이 'aeiou'에 있으면(True) 지나가고(continue),
# 4. 없으면(False) 새 변수에 담아야지

new_str = ''
for char in my_str :
    if char in 'aeiou' :
        continue
    else :
        new_str += char

print(new_str)
# Lf s t shrt, y nd pythn
```
</br>

### 왜 못 풀었을까?
`문자열` 비교

- 완전 일치 : `==`, `!=`
- 부분 일치 : `in`, `not in`
- 전방 일치 : `startswith`
- 후방 일치 : `endswich`

</br></br>

## 2. 과일 개수 골라내기
</br>

> 내 장바구니에 과일이 몇 개인지, 과일이 아닌 것은 몇개인지 출력하세요.
>
> 장바구니에 담긴 과일과, 과일 판별 리스트는 다음과 같습니다.
> ```python
> basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
> fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']
> ```

---

</br>**[출력 예시]**

과일은 23개이고, 11개는 과일이 아닙니다.

```python
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

# 아래에 코드를 작성하세요.

# 1. 값을 더할 'x', 'y' 변수를 두고,
# 2. basket_items의 key를 하나씩 뽑아서,
# 3. fruits 리스트와 비교하여 friuts에 있으면 'x' 변수에, 없으면 'y' 변수에 누적합
# 4. F-string 으로 출력

fruits_sum = 0
non_fruits_sum = 0

for wii in basket_items :
    if wii in fruits :
        fruits_sum += basket_items[wii]
    else :
        non_fruits_sum += basket_items[wii]
        
print(f'과일은 {fruits_sum}개이고, {non_fruits_sum}개는 과일이 아닙니다.')
```
</br>

### 왜 못 풀었을까?
누적합 할 때 `변수 = 0` 을 둔다

</br></br>

## 3. 영어 이름 출력하기 

> 영어 이름은 가운데 이름을 가지고 있는 경우가 있습니다.
>
> 가운데 이름은 대문자로 축약해서 나타내는 코드를 작성하세요.

---
</br>**[입력 예시]**

Alice Betty Catherine Davis

**[출력 예시]**

Alice B. C. Davis

```python
name = 'Alice Betty Catherine Davis'
names = name.split()

# 아래에 코드를 작성하세요.

# names
# ['Alice', 'Betty', 'Catherine', 'Davis'] 리스트네?
# 그러면 names 변수에 인덱스로 출력하면 되겠다

print(names[0] + ' ' + names[1][0] + '. ' + names[2][0] +'. ' + names[3])

# Alice B. C. Davis
```
