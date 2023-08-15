# 시각화 라이브러리

### 1. matplotlib
```python
# 시각화 라이브러리
import matplotlib.pyplot as plt
```
```python
# 1. 그래프 크기(생략가능 / 기본 6.4, 6.4)
plt.figure(figsize = (12, 8))

# 2. 그래프 그리기(한번에 여러 그래프 표현 가능)
plt.plot('Date', 'Ozone', data = data, label = 'Ozone') # x축 데이터, y축 데이터, data=df 이름, label 설정
plt.plot(data['Date'], data['Temp'], label = 'Temp') # 그래프 그리는 방법 2
plt.plot('Date', 'Wind', data = data, label = 'Wind', 
        color='r',  # 컬러
        linestyle='-', # 라인 스타일
        marker='s' # 마커 모양
)

# 3. 그래프 꾸미기(생략가능)
plt.xlabel('Date') # x축 이름 추가
plt.ylabel('Ozone, Temp, Wind') # y축 이름 추가
plt.title('Airquality') # 제목 추가
plt.xticks(rotation=45) #  x축 값 꾸미기 : 방향을 45도 틀어서
plt.legend(loc = 'upper right') # 범례 추가
plt.grid() # 그리드 추가

# 4. 마무리
plt.show()


# 크기 지정 -> 그리기 -> 꾸미기 -> 마무리 순서
# 그리기 빼고 생략은 가능, 마무리는 생략 안하는 것 매우 권장
```

1. 라인 스타일 조정
* color=  
    * 'red','green','blue' ...
    * 혹은 'r', 'g', 'b', ...
    * https://matplotlib.org/stable/gallery/color/named_colors.html
* linestyle= 
    * 'solid', 'dashed', 'dashdot', 'dotted'
    * 혹은 '-' , '--' , '-.' , ':' 
* marker=

| marker |	description |
| ---- | ---- |
|"." |	point |
|"," |	pixel |
|"o" |	circle |
|"v" |	triangle_down |
|"^" |	triangle_up |
|"<" |	triangle_left |
|">" |	triangle_right |
|"s" |	square |

2. 데이터프레임.plot()
```python
data.plot(x = 'Date', y = ['Temp','Ozone'], title = 'Daily Airquality', figsize=(12, 8))
plt.show()
```

3. 축 범위 조정
```python
plt.plot(data['Ozone'])

plt.ylim(0, 100) # y축 범위 조정
plt.xlim(0,10) # x축 범위 조정

plt.show()
```

4. 수평선 수직선, 텍스트 추가
```python
plt.plot(data['Ozone'])

plt.axhline(40, color = 'grey', linestyle = '--')  # ax 축, h 수평선, line 추가
plt.axvline(10, color = 'red', linestyle = '--')  # ay 축, v 수평선, line 추가

plt.text(5, 41, '40') # 좌표에 ''에 적힌 값을 입력
plt.text(10.1, 20, '10')

plt.show()
```

5. **여러 그래프에 나눠서 그리기**

* plt.supplot(row, column, indx)
    * row : 고정된 행 수
    * columns : 고정된 열 수
    * index : 순서

```python
# 위 아래 1행 3열 그래프
plt.figure(figsize = (12,8))
plt.subplot(3,1,1)  # 전체 프레임의 수는 변하지 않음 (3, 1)
plt.plot('Date', 'Temp', data = data)
plt.grid()

plt.subplot(3,1,2)  # 전체 프레임의 수는 변하지 않음
plt.plot('Date', 'Wind', data = data)

plt.subplot(3,1,3)  # 전체 프레임의 수는 변하지 않음
plt.plot('Date', 'Ozone', data = data)
plt.ylabel('Ozone')

plt.tight_layout() # 그래프간 간격을 적절히 맞추기
plt.show()
```

```python
# 옆으로 3행 1열 그래프
plt.figure(figsize = (15,5))

plt.subplot(1,3,1)
plt.plot('Date', 'Temp', data = data)
plt.title('Temp')
plt.grid()

plt.subplot(1,3,2)
plt.plot('Date', 'Wind', data = data)
plt.xticks(rotation = 40)
plt.grid()

plt.subplot(1,3,3)
plt.plot('Date', 'Ozone', data = data)
plt.title('Ozone')

plt.tight_layout() # 그래프간 간격을 적절히 맞추기
plt.show()
```
