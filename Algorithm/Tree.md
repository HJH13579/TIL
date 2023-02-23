# 트리(Tree)

## 트리의 개념
  - 비선형 구조
  - 원소들 간에 1:n 관계를 가지는 자료구조
  - 원소들 간에 계층관계를 가지는 계층형 자료구조
  - 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무)모양의 구조

## 트리 - 정의
- 한 개 이사의 노드로 이루어진 유한 집합
  - 노트 중 최상위 노드를 루트(root)라 한다.
  - 나머지 노드들은 n(>= 0)개의 분리 집합 T1,


## 트리 - 용어 정리
- 노드(node) - 트리의 원소
- 간선(edge) - 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
- 루트 노드(root node) - 트리의 시작 노드
- 형제 노드(sibling node) - 같은 부모 노드의 자식 노드들
- 조상 노드 - 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
- 서브 트리(subtree) - 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
- 자손 노드 - 서브 트리에 있는 하위 레벨의 노드들



# 이진 트리
- 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
- 각 노드가 자식 노드를 최대한 2개 까지만 가질 수 있는 트리
  - 왼쪽 자식 노드(left child node)
  - 오른쪽 자식 노드(right child node)

## 이진 트리 - 종류
> 포화 이진 트리(Full Binary Tree)
- 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
- 높이가 h일때, 최대의 노드 개수인 (2^(h+1) - 1)의 노드를 가진 이진 트리
  - 높이가 3일 때 15개의 노드
- 루트를 1번으로 하여 (2^(h+1) - 1)까진 정해진 위치에 대한 노드 번호를 가짐

> 완전 이진 트리(Complete Binary Tree)
- 높이가 h이고 노드 수가 n개일 때(단, 2^h(h-1 레벨까지 꽉 차있고, h레벨에 1개 이상) <= n <= 2^(h+1) - 1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리


> 편향 이진 트리(Skewed Binary Tree)
- 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
  - 왼쪽 편향 이진 트리
  - 오른쪽 편향 이진 트리

## 이진 트리 - 순회(traversal)
- 순회(traversal)란 트리의 각 노드를 중복되지 않게 전부 방문(visit)하는 것을 말하는데 트리는 비선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계를 알 수 없다.
- 특별한 방법 필요



> 전위 순회(preorder traversal)
- 수행 방법
1) 현재 노드 n을 방문하여 처리한다. -> V
2) 현재 노드 n의 왼쪽 서브트리로 이동한다. -> L
3) 현재 노드 n의 오른쪽 서브트리로 이동한다. -> R

- 전위 순회 알고리즘

```python
def preorder_traverse(T): # 전위순회
  if T: # T is not None
    visit(T)  # print(T.item)
    preorder_traverse(T.left)
    preorder_traverse(T.right)
```

```python
preorder(i)
  if 0 <= i <= N:
    print(i)
    preorder(i * 2) # 왼쪽 자식 방문
    preorder(i * 2  + 1)  # 오른쪽 자식 방문
```

<연습문제>
- 다음 이진 트리 표현에 대하여 전위 순회(root부터)하여 정점의 번호를 출력하시오.
  - 13 : 정점의 개수
  - 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 13 11 13

```python
def preorder(i):
  if i: # 존재하는 정점이면
    print(i, end= ' ')
    preorder(left[i])
    preorder(right[i])
  return

def inorder(i):
  if i: # 존재하는 정점이면
    inorder(left[i])
    print(i, end= ' ')
    inorder(right[i])
  return

def postorder(i):
  if i: # 존재하는 정점이면
    postorder(left[i])
    postorder(right[i])
    print(i, end= ' ')
  return

V = int(input())
arr = list(map(int, input().split()))
E = V - 1 # 간선 수
# 부모를 인덱스로 자식번호 저장
left = [0] * (V + 1)  # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V + 1) # 부모를 인덱스로 오른쪽 자식 저장
par = [0] * (V + 1) # 자식을 인덱스로 부모 저장
# child = [[] for _ in range(V+1)]
for i in range(E):
  p, c = arr[i*2], arr[i*2+1]
  if left[p] == 0:
    left[p] = c
  else:
    right[p] = c
  par[c] = p
  # child[p].append(c)

root = 1
while par[root] != 0: # root 찾기
  root += 1
print(root)

preorder(root)
print()
inorder(root)
print()
postorder(root)
print()
```


```python
# 최대 100개의 key
# 최대힙

def enq(n):
  global last
  last +=1  # 완전이진트리에 마지막 정점을 추가하고
  heap[last] = n  # 마지막 정점에 저장
  c = last  # 부모가 있고, 부모 > 자식 조건 검사를 위해
  p = c // 2
  while p > 0 and heap[p] < heap[c]:
    heap[p], heap[c] = heap[c], heap[p]
    c = p   # 옮긴 자리에서 부모와 비교하기 위해
    p = c // 2
  return

def deq():
  global last
  tmp = heap[1] # 루트 임시저장
  # 마지막 정점의 값을 루트로 이동
  heap[1] = heap[last]  # 마지막 정점의 값을 루트로 이동
  last -= 1   # 마지막 정점 삭제
  p = 1
  c  = p * 2  # 왼쪽 자식 번호
  while c <= last:  # 자식이 하나 이상 있으면
    if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식도 있고, 오른쪽 자식의 키가 더 크면
      c += 1 # 비교 대상을 오른쪽 자식으로 변경
    if heap[c] > heap[p]: # 자식이 부모보다 크면
      heap[c], heap[p] = heap[p], heap[c]
      p = c
      c = p * 2
    else:
      break
  return tmp

heap = [0] * 101 # 완전이진트리 1번 ~ 100번 인덱스 준비
last = 0  # 완전이진트리의 마지막 정점 번호
enq(5)
print(heap[1])
enq(15)
print(heap[1])
enq(8)
print(heap[1])
enq(20)
print(heap[1])

while last > 0:
  print(dep())
```