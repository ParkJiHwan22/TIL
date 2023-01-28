### 스택 구현 예제 (Python)
# stack = []

# # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack[::-1]) # 최상단 원소부터 출력
# print(stack) # 최하단 원소부터 출력

# ### 스택 구현 예제 (Python)
# from collections import deque

# # 큐(Queue) 구현을 위해 deque 라이브러리 사용
# queue = deque()

# # # 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()

# print(queue) # 먼저 들어온 순서대로 출력
# queue.reverse() # 역순으로 바꾸기
# print(queue) # 나중에 들어온 순서대로 출력

### 우선순위 큐 라이브러리를 활용한 힙 구현 예제 (Python)
import heapq

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value) # value에 - 붙이고 heapq에 - 붙이면 최대 힙
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# res = heapsort(arr)

# for i in range(n):
#     print(res[i])