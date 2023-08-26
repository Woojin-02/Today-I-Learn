# selenium

- `https://www.selenium.dev`
- 자동화를 목적으로 만들어진 다양한 브라우져와 언어를 지원하는 라이브러리
- 크롬 브라우져 설치
    - 크롬 브라우져 드라이버 다운로드 (크롬 브라우져와 같은 버전)
    - 다운로드한 드라이버 압축 해제
    - chromedriver.exe 생성
    - windows : 주피터 노트북 파일과 동일한 디렉토리에 chromedriver.exe 파일 업로드
- ***selenium을 직접 만지는건 최소한으로 함. 만지면 연결이 끊길 수 있기 때문에 지양***

### 1. 설치 및 패키지 실행
```python
# jupyter notebook 에서
# !pip install selenium
```
```python
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
```

### 2. selenium 실행
```python
# 브라우저 띄우기
driver = webdriver.Chrome()
```
```python
# 페이지 이동
driver.get('https://www.ted.com/talks')
```
```python
# 브라우저 사이즈 조절(웹페이지 크기 변경)
driver.set_window_size(200, 600)
```
```python
# 브라우저 javascript 코드 실행
driver.execute_script('window.scrollTo(200, 300);')
```
```python
# id=q # css_selector로 아이디(# 에 셀레니움 입력)
driver.find_element(By.CSS_SELECTOR, '#q').send_keys('셀레니움')
```
```python
# 검색버튼 클릭
# ico_pctop, btn_search 둘 다 가지고 있는 엘리멘트 선택
selector = '.ico_pctop.btn_search'
driver.find_element(By.CSS_SELECTOR, selector).click()
```
```python
selector = '.talks-header__title'
driver.find_element(By.CSS_SELECTOR, selector).text
```
```python
# 브라우저 종료
driver.quit()
```
```python
# id=q # css_selector로 아이디(# 에 셀레니움 입력)
driver.find_element(By.CSS_SELECTOR, '#q').send_keys('셀레니움')
```

### 3. Headless
- 브라우져를 화면에 띄우지 않고 메모리상에서만 올려서 크롤링하는 방법 
- window가 지원되지 않는 환경에서 사용이 가능
    - 명령 프롬프트 등만 지원되는 서버 컴퓨터 등

***코드 다 만들고 코드 실행할때만 headless로 실행하도록 코드를 작성합니다.***
```python
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

driver.get('https://www.ted.com/talks')
selector = '.talks-header__title'
txt = driver.find_element(By.CSS_SELECTOR, selector).text

driver.quit()
print(txt)
```
