# JavaScript 기본


### 1. 프로그래밍 기본

* 프로그래밍 언어의 종류 : 컴파일러(C, C++, fortran 등), 인터프리터(파이썬, javascript 등)
    * 컴파일러 : 코드 실행 속도가 빠름, 코드 실행 전에 빌드 과정이 필요 (번역본을 만들어서 그 번역본을 읽음)
    * 인터프리터 : 코드 실행 속도가 느림, 코드 실행 전에 빌드 과정이 불필요 (한줄씩 해석하면서 읽음)
* 프로그래밍 언어를 배우는 이유 : 컴퓨터의 CPU, RAM, SSD(HDD)를 사용하기 위해
1. 변수 선언 : RAM을 사용하는 문법
2. 데이터타입 : RAM을 효율적으로 사용하는 문법
3. 연산자 : CPU를 사용하는 문법
4. 조건문 : 조건에 따라 코드를 실행하는 문법 : 코드를 효율적으로 작성 및 실행하는 문법
5. 반복문 : 특정 코드를 반복적으로 실행하는 문법 : 코드를 효율적으로 작성 및 실행하는 문법
6. 함수 : 중복 코드를 묶어서 코드를 작성하고 실행 : 코드를 효율적으로 작성 및 실행하는 문법
7. 객체 : 식별자 1개에 데이터를 여러개 저장하는 문법 : 클래스, 데이터 타입 문법(바닐라 자바스크립트는 객체가 없음)



### 2. Javascript
* 브라우저에서 이벤트를 처리하는 목적으로 만들어진 언어

**1. 변수 선언**
* 식별자 : 저장공간을 구별하는 문자열
* 식별자 문법(어기면 오류남) : 대소문자, 숫자, _, $ : 숫자가 가장 앞에 올 수 없음 : 예약어 사용 불가
* 식별자 컨벤션(어기면 오류는 안나지만 이상해짐) : 상수(UPPER_SNAKE_CASE) : 변수/함수(camelCase) : 모듈(PascalCase)

```javascript
//식별자 1개, 데이터 1개
var data1 = 10;
var data2 = 'js';
// int data1 = 'js'; <- 컴파일러 언어 사용 시
//인터프리터 언어 특징 : 동적 타이핑 : 데이터 타입의 선언 없이 자동으로 데이터 타입 선언

//식별자 n개, 데이터 n개
var data3 = 20, data4 = 'node';
var data3 = 20, 
    data4 = 'node';

//식별자 n개, 데이터 1개
var data5 = data6 = 'web';

// console.log() : 파이썬의 print()
console.log(data1, data2, data3, data4, data5, data6)
```


**2. 데이터 타입**
* number : 숫자(정수, 실수)
* string : 문자열
* boolean : 논리값 : true, false
* function : 코드 저장하는 함수 데이터 타입
* object : 객체

```javascript
var data1 = 1;
var data2 = 'js';
var data3 = true;
var data4 = function(){console.log('function');}
var data5 = {key:'value'};
var data5 = {'key':'value'};
// typeof : 명령어를 사용해서 타입 출력
console.log(typeof data1, typeof data2, typeof data3, typeof data4, typeof data5)
```


* 없는 데이터의 표현
    * undefined(선언은 되었으나, 값이 할당되지 않음)
    * null(선언이 되어 값이 없음이 할당됨)
    * NaN(Number 데이터 타입에서 데이터 없음)
    * 구별해야 하는 이유는 데이터 타입이 다르기 때문
```javascript
var data1 = undefined;
var data2 = null;
var data3 = NaN;
console.log(typeof data1, data1, typeof data2, data2, typeof data3, data3)
```


**3. 연산자**
* 산술 : 데이터 + 데이터(데이터와 데이터를 산술하면) = 데이터(데이터가 나옴) : +, -, *, /, %, **, ++, --
* 비교 : 데이터 + 데이터(데이터와 데이터를 비교하면) = 논리값(논리값이 나옴) : 조건 1개를 비교해서 조건이 참인지 거짓인지 확인 : ==, ===, !=, !==, >, <, <=, >=
* 논리 : 논리값 + 논리값 = 논리값 : 조건 2개 이상을 비교해서 조건이 참인지 거짓인지 확인 : !, &&, ||
* 할당 : 변수(식별자) 산술 = 데이터 : 변수에 누적해서 연산을 수행
* 삼항 : condition ? true : false :: 간단한 조건문을 구현

```javascript
// 산술
var data1 = 10;
var data2 = 20;
// data2에 +1을 하고 data1에 대입
data1 = ++data2;
console.log(data1, data2);
//data1에 대입하고 +1을 연산
data1 = data2++;
console.log(data1, data2);

// 비교
// ===(데이터 타입, 데이터 둘 다 비교), ==(데이터 타입 비교 X, 데이터만 비교)
var data1 = 1, data2 = '1';
console.log(data1, data2);
console.log(typeof data1, typeof data2);  // number 1 string 1
console.log(data1 == data2, data1 === data2);

// 논리연산자 : !, &&(T && T = T) : 2가지 조건 모두 만족, ||( F || F = F) : 둘 중 하나만 만족
console.log(!true, true && false, true || false);

// 퀴즈 1 : 예금 잔고에서 인출 금액을 인출 가능하면 true, 불가능하면 false 출력하는 코드 작성
var balance = 10000;
var withdraw = 6000;
console.log(balance >= withdraw);
// 퀴즈 2 : 1회 최대 인출금액이 5000원 조건 추가
console.log( (withdraw < 5000) && (balance >= withdraw))

// 조건
// if, else if, else
// 예금 잔고에서 인출 금액이 인출 가능하면 '인출가능' 출력하는 코드 작성
var balance = 10000;
var withdraw = 6000;
if(balance >= withdraw){
    console.log('인출가능');
} else{
    console.log('인출불가');
}
// 최대 인출 금액 5000원 조건 추가
// 인출이 불가하면 인출 불가 사유를 출력하는 코드 작성
// 인출불가:잔액 부족, 인출불가:최대 인출금액 초과
if(balance <= withdraw){
    console.log('인출불가:잔액 부족');
}else if(withdraw > 5000){
    console.log('인출불가:최대 인출금액 초과')
}else{
    console.log('인출가능')
}

// 반복
// while, for, break, continue
var count = 3;
while(count > 0){
    count -= 1;
    console.log('js');
}

for(var i = 0; i<3; i++){  // i = 0, i = 1, i = 2, i = 3 < break
    console.log('js', i)
}
```

**주의**
* 부동소수점 문제 : 실수하기 쉬운 코드
```javascript
var data1 = 0.1, data2 = 0.2;
console.log((data1 + data2) === 0.3);
console.log(data1 + data2);
// 해결 방법 1 : 반올림
console.log(Math.round(0.123));
console.log(Math.round(0.523 * 10) / 10);
console.log(Math.round((data1 + data2) * 10) / 10 === 0.3);
```

### 4. 함수 : function
* 중복코드를 묶어서 코드 작성 및 실행
* 사용법 : 함수선언(코드작성) > 함수호출(코드실행)

```javascript
// 로또번호 출력
var count = 6, lotto = '';
for (var i = 0; i<count; i++){
    var randomNumber = Math.ceil(Math.random() * 44) + 1;  // ceil : 버림
    lotto = lotto + randomNumber + ' ';
}
console.log(lotto);
// js 출력
console.log('js');
// 로또 번호 출력
var count = 6, lotto = '';
for (var i = 0; i<count; i++){
    var randomNumber = Math.ceil(Math.random() * 44) + 1;  // ceil : 버림
    lotto = lotto + randomNumber + ' ';
}
console.log(lotto);

// 함수선언 : 코드작성
function show_lotto(count){
    lotto = '';
    for (var i = 0; i<count; i++){
        var randomNumber = Math.ceil(Math.random() * 44) + 1;  // ceil : 버림
        lotto = lotto + randomNumber + ' ';
    }
    console.log(lotto);
}
// 함수호출 : 코드실행
show_lotto(6);
console.log('js');
show_lotto(7);

console.log(typeof show_lotto);

// 함수 선언 1 : 함수 선언식
function plus1(n1, n2){
    return n1 + n2;
}
console.log(plus1(1, 2));

// 함수 선언 2 : 함수 표현식
var plus2 = function(n1, n2){
    return n1 + n2;
}
console.log(plus2(1, 2));

// 선언식과 표현식의 차이
// 선언식은 코드의 최상단으로 올라가서 선언됨 > 호이스팅(인터프리터가 코드를 실행하기 전에 함수, 변수, 클래스 또는 임포트(import)의 선언문을 해당 범위의 맨 위로 이동시키는 과정)
// 호출 후 선언 순으로 코드를 작성해도, 선언 후 호출로 동작함
console.log(plus1(1, 2));
function plus1(n1, n2){
    return n1 + n2;
}
// 표현식은 코드의 순서대로 실행됨
console.log(plus2(1, 2));
var plus2 = function(n1, n2){
    return n1 + n2;
}
```

### 5.익명함수
* 선언과 동시에 호출하는 함수

```javascript
function minus1(n1, n2){
    console.log(n1 - n2);
}
minus1(4, 1);
```

* 전역 영역, 지역 영역 : global, local
* 익명함수는 전역 영역에서 쓸 수 없기 때문에 외부에서 함수를 가져다가 사용하지 못하게 막는다.
```javascript
(function minus2(n1, n2){
    console.log(n1-n2);
}(4, 1));
minus2(5, 1);  // << 이 부분은 사용 불가
```

### 6. 스코프
* 함수 안과 함수 밖의 선언된 변수는 다른 영역의 메모리를 사용
* 함수 안 : 지역 영역 : local area
* 함수 밖 : 전역 영역 : global area

```javascript
var data = 10;
function change(){
    var data = 20;
}
change();
console.log(data);

var data = 10;
function change(){
    data = 20;  // global var
}
change();
console.log(data);
```


### 7. 객체 : Object
* Array : 배열 : list
* Class : 클래스 : class

```javascript
var data = [1, 2, 3, 'A', 'B'];
data.push('C');
console.log(typeof data, data, data[3]);  // data[3:] 이런 기능은 없음

// 객체생성 1
var account = {
    balance: 10000,
    withdraw: function(amount){
        account.balance -= amount;
    }
}
account.withdraw(2000);
console.log(account);

// 객체생성 2
function Person(name){
    this.name = name
}
var person = new Person('andy');
console.log(person);


// json 객체 : 웹서비스에서 데이터를 주고 받을때 사용하는 포멧
// 웹서비스에서는 문자열만 사용 가능
// 객체 > 문자열
var data = {name: 'andy', addr: 'seoul'}
console.log(typeof data, data)
var json = JSON.stringify(data);
console.log(typeof json, json)
// 문자열 > 객체
var jsonObj = JSON.parse(json);
console.log(typeof jsonObj, jsonObj, jsonObj.addr)

console.log(NaN == NaN, NaN === NaN);
```


### 8. 클로저 : 함수 안에 선언된 함수 : 지역 함수
* 특징 : 전역변수 사용 억제, 정보은닉(전역영역에서 접근 X)
* 웹사이트는 전역변수를 사용하면 사용자가 마음대로 페이지를 바꿔버릴 위험이 있음

```javascript
var Account = function(){
    var balance = 10000;
    this.deposit = function(amount){    // 클로저
        balance += amount;
    }
    this.show = function(){    // 클로저
        return balance;
    }
}

var account = new Account();
console.log(account);  // 실행결과 확인시 balance가 뜨지 않음. 정보가 은닉됨
console.log(account.show());  // balance를 보기 위함
// conslow.log(account.balance); balnace를 직접 볼 수 없음
account.deposit(2000)  // +2000
console.log(account.show()) // 12000


var Account = function(){
    this._balance = 10000;
    this.deposit = function(amount){    // 클로저
        this._balance += amount;
    }
    this.show = function(){    // 클로저
        return this._balance;
    }
}
```

* this.을 붙이면 접근 가능
* 이 경우 통상적으로 _를 붙이는 것이 관념(변수를 감추려고 써놓은 변수라는 표시)
```javascript
var account = new Account();
console.log(account, account._balance);
```

* 웹브라이저에서 사용하는 객체
* window : 전역객체 : 모든 전역변수를 저장하는 객체. window를 입력해서 전역변수, 함수를 알아내고 사용 가능. 이를 방지하고 싶다면 클로저나 익명함수 사용
* location : url 데이터를 저장하는 객체
* document : 페이지의 문서 정보를 저장하는 객체