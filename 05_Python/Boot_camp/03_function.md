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
### 활용법

```python
def <func>(parameter1, parameter2):
    <코드 블럭>
    return value
```

