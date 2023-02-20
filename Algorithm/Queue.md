# 큐(Queue)

- 큐(Queue)의 특성
  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
  - 선입선출구조(FIFO: First In First Out)
    - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First In)된 원소는 가장 먼저 삭제(First Out)된다.

</br>

- 큐의 선입선출 구조

![큐의 선입선출 구조](assets/Queue_FIFO.png)

-  큐의 기본 연산
   -  삽입: enQueue
   -  삭제: deQueue

</br>

> 큐의 주요 연산

![큐의 주요 연산](assets/Queue_calc.png)

</br>

> 큐의 연산 과정

- front : 디큐 위치, 마지막으로 디큐된 인덱스
- rear: 인큐 위치, 마지막으로 인큐된 인덱스
- 기본값은 -1로 설정

1) 공백 큐 생성: createQueue();
2) 원소 A 삽입: enQueue(A);
3) 원소 B 삽입: enQueue(B);



> 공백 상태 및 포화 상태 검사: isEmpty(), isFull()



> 검색: Qpeek()
- 가장 앞에 있는 원소를 검색하여 반환하는 연산
- 현재 front의 한자리 뒤(front + 1)에 있는 원소, 즉 큐의 첫번째에 있는 원소를 반환

```python
def Qpeek():
  if isEmpty() : print("Queue_Empty")
  else : return Q[front + 1]
```


> 연습문제1
- 큐를 구현하여 다음 동작을 확인해보자
  - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고
  - 큐에서 세 개의 데이터를 차례로 꺼내서 출력 (1, 2, 3 출력)

```python
def enqueue(data):
  global rear
  rear += 1
  queue[rear] = data

def dequeue()"
  global front
  front += 1
  return queue[front]

queue = [0]*10
front = -1
rear = -1

enqueue(1)
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
  print(dequeue())
if front != rear: # 안전장치
  print(dequeue()) # IndexError
```

```python
# 단순히 append와 pop(반드시 pop(0)으로 사용)으로 만들면 느려짐
# Queue와 비슷한 속도, but import 금지 상황에선 못 씀
from collections import deque

q1 = deque()
q1.append(100)
q1.append(100)
q1.append(100)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())
```

</br>

## 선형 큐 이용시의 문제점

- 잘못된 포화상태 인식
  - 선형 큐를 이용하여 원소의 삽입과 삭제를 계쏙할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear = n -1 인 상태, 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨
- 해결방법 1
  - 매 연산이 이루어질 때마다 저장된 원소들을 배열의 앞부분으로 모두 이동
  - 원소 이동에 많은 시간이 소요되어 큐희 효율성이 급격히 떨어짐
- 해결방법 2
  - 1차원 배열을 사용하되, 논리적으로는 배열의 처음과 끝이 연결되어 원형 형태의 큐를 이룬다고 가정하고 사용
  - 원형 큐의 논리적 구조