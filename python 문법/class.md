# 클래스 : class

* 변수, 함수를 묶어서 코드 작성해서 실행하는 문법
* 코드를 효율적으로 작성할 수 있게 함
* 또한 객체지향 구현에 필수
    * 객체지향 : 실제세계를 모델링하여 프로그램을 개발하는 개발방법론
* 클래스 선언(코드 작성) > 객체생성(메모리 사용) > 메서드 호출(코드 실행)
* `클래스는 사용자정의 데이터타입이다.`
* 클래스 식별자 컨벤션 : snake_case(X), PascalCase(O), UpperCamelCase(O)

1. 예시 코드
```python
class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"안녕하세요, 제 이름은 {self.name}이고, 나이는 {self.age}살입니다.")

# Person 클래스의 인스턴스 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 인스턴스 메서드 호출
person1.introduce()
person2.introduce()
```

* self : 자기 자신
* 스페셜 메서드 : 메서드 식별자 앞뒤로 __가 붙음. 특별한 기능을 하는 메서드
* 생성자 메서드 : __init__(). 스페셜 메서드 중 하나
    * 객체가 생성될 때 실행되는 메서드
    * 다른 메서드에서 사용할 변수를 검사하거나 초기값을 설정할 때 사용
