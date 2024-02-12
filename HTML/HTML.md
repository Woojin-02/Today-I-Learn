
# HTML
HTML(Hyper Text Markup Language) : 웹 문서를 작성하는 마크업 단어

### 1. HTML 구성 요소
- Document : 한페이지를 나타내는 단위
- Element : 하나의 레이아웃을 나타내는 단위 : 시작태그, 끝태그, 텍스트로 구성
- Tag : 엘리먼트의 종류를 정의 : 시작태그(속성값), 끝태그
- Attribute : 시작태그에서 태그의 특정 기능을 하는 값
    - id : 웹 페이지에서 유일한 값
    - class : 동일한 여러개의 값 사용 가능 : element를 그룹핑 할때 사용
    - attr : id와 class를 제외한 나머지 속성들s
- Text : 시작태그와 끝태그 사이에 있는 문자열
- 엘리먼트는 서로 계층적 구조를 가질수 있음

### 2. HTML 구조
- DOCTYPE
  - 문서의 종류를 선언하는 태그
- html
  - head
    - meta
      - 웹페이지에 대한 정보
    - title
      - 웹페이지의 제목 정보
  - body
    - 화면을 구성하는 엘리먼트

```
<!-- HTML 웹문서의 기본적인 구조 -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title></title>
</head>
<body>

</body>
</html>
```

### 3. HTML 태그
* html에서 문자를 나타내는 태그들

#### 1. 문자 HTML 태그
---

`head`
 * title을 나타낼 때 사용
 * h1(제일 큼) ~ h6(제일 작음) 의 6종류 태그
 * `<h1>title</h1>`

---

`p`
 * 한줄의 문자열을 출력
 * 다음 줄로 자동 줄바꿈
 * `<p>html 1</p> <p>html 2</p>`

---

`span`
 * 한 블럭의 문자열을 표현
 * 연속해서 출력
 * `<span>html 1</span> <span>html 2</span>`

---

`pre`
 * 줄바꿈이나 띄어쓰기가 적용되는 태그
```
<pre>html 1
hello world</pre>
```

`code`
 * 코드를 작성하는 태그
 * 들여쓰기나 두칸 이상의 공백은 적용 안됨
 ```
<p>다음은 파이썬 코드입니다</p>
<code>print('Hello World!)</code>
 ```

#### 2. 문자 이외의 HTML 태그

---

`div`
 * 레이아웃을 나타내는 태그
 * 계층적 구조
 * 영역을 나타낸 때 사용
```
<div>
    <p>hello</p>
    <p>world</p>
</div>
<div>
    <p>img_smile</p>
</div>
```

---

`table`
 * Low와 Calumn 이 있는 테이블 모양
 * tr : 표의 행
 * td : 표의 열. tr 태그 하위에 위치
 * 2 X 2 테이블 생성 예시
```
<table>
	<tr>
		<td>섹션1</td>
		<td>섹션2</td>
	</tr>
	<tr>
		<td>섹션3</td>
		<td>섹션4</td>
	</tr>
</table>
```

---

`ul, li, dl`
* 리스트를 나타내는 태그
* ol : 숫자나 알파벳 등 순서가 있는 목록 생성
* ul : 순서가 필요 없는 목록 생성
* dl : 용어를 설명하는 목록
```
<ul>
<li>html 1</li>
<li>html 2</li>
<li>html 3</li>
</ul>
```

---

`a`
 * 링크를 나타내는 태그
 * href 속성에 url/상대경로 입력
    * target="_blank" 옵션 : 링크를 열 때 새탭에서 열기
`<a href='http://google.com' target='_blink'>open google</a>`

---

`image`
 * 이미지를 나타내는 태그
 * alt 옵션 : 이미지가 깨져도 글자로 이미지가 무엇인지 표시

`<image src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT1rzyInx_V3eEfksd7Ycwp255OxM3X0WMeJ3Vt7BU&s=0' alt='kt_logo'>`

---

`iframe`
* 외부 url 페이지를 보여주기 위한 엘리먼트
* 모든 웹 페이지를 보여줄 수 있는건 아님
* selenium 으로도 데이터 선택이 안되는 경우, iframe으로 구성되었을 수 있음
  * 그 경우 iframe 선택 후 내부의 요소에 접근해야함
`<iframe src='https://cafe.naver.com/joonggonara.cafe?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10050146%26search.boardtype=L%26viewType=pc' width='100%' height='400px'></iframe>`

---

#### 3. input 태그

---

`text`
* 문자열을 입력
* placeholder : 입력 필드 설명
`<input type='text' placeholder='아이디'>`

---

`password`
* 비밀번호를 입력
* placeholder 사용 가능
`<input type='password' placeholder='password'>`

---

`radio`
* 여러개의 버튼 중에서 한개의 버튼만 체크되는 버튼
* name 속성값을 기준으로 그룹핑함
```
<input type='radio' name='no1'>btn 1</input>
<input type='radio' name='no1'>btn 2</input>
<input type='radio' name='no2'>btn 3</input>
```

---

`checkbox`
* 여러개의 버튼이 체크되는 버튼
```
<input type='checkbox'>btn 1</input>
<input type='checkbox'>btn 2</input>
<input type='checkbox'>btn 3</input>
```

---

`select, option`
* 옵션 선택을 할 수 있는 드랍다운 태그
```
<select>
    <option>사과</option>
    <option>바나나</option>
</select>
```

---

`textarea`
* 여러줄을 입력이 가능한 태그
`<textarea name="opinion" cols="30" rows="5" placeholder='메모'></textarea>`

---

`button`
* 마우스 클릭을 입력받는 버튼 태그
`<button id = btn1, class='btn_no1, type='button>button</button>`
