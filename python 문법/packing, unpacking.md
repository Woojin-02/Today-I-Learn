# packing/unpacking

* 묶거나 풀거나
* 한쪽으로 묶을때 packing, 풀땐 unpacking

### 1. list에서의 packing/unpacking

* packing
```python
a = [1, 2, 3, 4]
print(a)
b, *c = [1, 2, 3, 4] # b에는 1을 받고, c에는 나머지를 받고 싶음
print(b,c)
# c에 *를 하면 패킹을 해서 나머지를 받을 수 있음
```
```
# 결과
[1, 2, 3, 4]
1 [2, 3, 4]
```

* unpacking
```python
#unpacking
# d는 2, 3, 4, 5, 6을 받고 싶을 때,
d = [*c, 5, 6]
print(d)
# c가 2, 3, 4가 있으니까 *c를 하면 a에 있는 내용이 풀린다.
d = [c, 5, 6] # 이렇게 언패킹을 하지 않고 c를 그대로 삽입하면
print(d) # 리스트가 그대로 삽입된다. 리스트를 풀어해쳐서 삽입하려면 언패킹 필요
```
```
# 결과
[2, 3, 4, 5, 6]
[[2, 3, 4], 5, 6]
```

### 2. dictionary에서의 unpacking

* unpacking
* packing은 지원하지 않음
```python
#dicionary에서의 unpacking
a = {"a":1, "b":2, "c":3}
b = {**a, "d":4, "e":5} # dicionary unpacking
print(b)

#이건 안됨
# a, **b = {"a":1, "b":2, "c":3}
# print(a, b)

data = [
    {"name": "김민석", "age": 21},
    {"name": "천영성", "age": 20},
]

data = [{**d, "aivler": True} for d in data] # 상당히 많이 사용되는 기술
print(data)
```
```
# 결과
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
[{'name': '김민석', 'age': 21, 'aivler': True}, {'name': '천영성', 'age': 20, 'aivler': True}]
```

### 3. 함수의 packing/unpacking

* 함수에서 list 사용
```python
# unpakcing
#list
def add(a, b, c):
    return a + b + c

d = [1, 2, 3]
print(add(*d)) # print(add(d[0], d[1], d[2]))와 같음

# packing
# list
# packing
def add(*a):
    print(a)
    return sum(a)
# add에 데이터를 여러개 보낼 수 있게 된다. 이 경우 튜플로 데이터를 받는다.

print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
```
```
# 결과
6
(1,)
1
(1, 2)
3
(1, 2, 3)
6
```

* 함수에서 dictionary 사용
```python
# unpacking
# dictionary
def add(a, b, c):
    return a + b + c

d = {"a": 1, "c": 3, "b": 2} # 순서대로 add 함수로 가는게 아니라 a, b, c 키값대로 전송됨
print(add(**d)) # unpacking

# packing
# dictionary
def add(**a) :
    print(a)
    return sum(a.values())

print(add(a=1))
print(add(a=1, c=3, b=2))
# 어떤 값을 파라미터로 쓸지 명시해야만 사용 가능 a=1, optimizer="adam" 이런 식으로 키를 명시해야 함
```
```
# 결과
6
{'a': 1}
1
{'a': 1, 'b': 2, 'c': 3}
6
```
