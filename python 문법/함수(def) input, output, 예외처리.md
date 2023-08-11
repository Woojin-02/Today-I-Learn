# 함수 생성 및 활용

### 1. input(입력 매개변수)
```python
def hello_world() : 
    내용
```

```python
def hello_world(name, loud = 1) : # loud = 1 : 값이 전달되지 않을 경우 defalut 적용값 설정
    내용
```

```python
def hello_world(*num) : # 입력 매개변수 앞에 *이 붙으면 갯수 제한 없이 값을 받음
    내용
```

### 2. output(출력 매개변수)

 * print : 화면에 출력만 수행
```python
def hello_world() :
    print(1)

hello = hello_world()
```
    * 화면에 1 출력
    * hello에 저장되는 값 없음

 * return : 화면 출력(생략됨) + 함수 외부로 결과 반환
```python
def hello_world() :
    return 1

hello = hello_world()
```
    * 화면에 1 출력
    * hello에 1 저장

 * 여러 개 output
 ```python
def hello_world() :
    return a, b

ra, rb = hello_world()
ra, _ = hello_world()
```
    * 결과값 중하나만 필요하면 '_'를 사용해서 생략 가능

### 2. 예외처리

 * try - except
  ```python
def print_x(num) :
    try :
        return result
    
    except Exception as e:
        print("오류가 발생하였습니다:", e)
        
divide(10, 0)
```