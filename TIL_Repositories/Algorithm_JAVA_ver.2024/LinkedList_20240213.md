# 연결 리스트

### 특성
- 자료의 논리적인 순서와 메모리 상의 물리적인 순서가 일치하지 않고, 개별적으로 위치하고 있는 원소의 주소를 연결하여 하나의 전체적인 자료구조를 이룬다.
- 링크를 통해 원소에 접근하므로, 순차 리스트에서처럼 물리적인 순서를 맞추기 위한 작업이 필요하지 않다.
- 자료구조의 크기를 동적으로 조정할 수 있어, 메모리의 효율적인 사용이 가능하다.

### 노드
- 연결 리스트에서 하나의 원소에 필요한 데이터를 갖고 있는 자료단위
- 구성요소
- 1. 데이터 필드: 원소의 값을 저장하는 자료구조, 저장할 원소의 종류나 크기에 따라 구조를 정의하여 사용함
- 2. 링크 필드: 다음 노드의 주소를 저장하는 자료구조

### 헤드
- 리스트의 처음 노드를 가리키는 레퍼런스

# 단순 연결 리스트(Singly Linked List)

### 연결 구조
- 노드가 하나의 링크 필드에 의해 다음 노드와 연결되는 구조를 가진다.
- 헤드가 가장 앞의 노드를 가리키고, 링크 필드가 연속적으로 다음 노드를 가리킨다.
- 최종적으로 NULL을 가리키는 노드가 리스트의 가장 마지막 노드이다.

### 'A', 'C', 'D'를 원소로 갖고 있는 리스트의 두 번째에 'B'노드를 삽입할 때
- 1. 메모리를 할당하여 새로운 노드 new 생성
- 2. 새로운 노드 new의 데이터 필드에 'B' 저장
- 3. 삽입될 위치의 바로 앞에 위치한 노드의 링크 필드를 new에 복사
- 4. new의 주소를 앞 노드의 링크 필드에 저장

### 'A',  'B', 'C', 'D' 리스트의 'B'노드를 삭제할 때
- 1. 삭제할 노드의 앞 노드(선행노드)탐색
- 2. 삭제할 노드의 링크 필드를 선행노드의 링크 필드에 복사

# 이중 연결 리스트(Doubly Linked List)

### 특성
- 양쪽 방향으로 순회할 수 있도록 노드를 연결한 리스트
- 두개의 링크 필드와 한 개의 데이터 필드로 구성
- 모든 삽입, 삭제 연산이 중간 삽입, 중간 삭제

### cur가 가리키는 노드 다음으로 D값을 가진 노드를 삽입하는 과정
- 1. 메모리를 할당하여 새로운 노드 new 생성하고 데이터 필드에 'D'를 저장
- 2. cur의 next를 new의 next에 저장하여 cur의 오른쪽 노드를 삽입할 노드 new의 오른쪽 노드로 연결
- 3. new의 주소를 cur의 next에 저장하여 노드 new를 cur의 오른쪽 노드로 연결한다.
- 4. cur에 있는 링크 값을 new의 prev에 저장하여 cur를 new의 왼쪽 노드로 연결한다.
- 5. new의 주소를 new의 오른쪽노드의 prev에 저장하여 노드 new의 오른쪽노드의 왼쪽노드로 new를 연결한다.

### cur가 가리키는 노드를 삭제하는 과정
- 1. 삭제할 노드 cur의 next에 저장되어 있던 주소를 cur의 왼쪽 노드의 next에 저장
- 2. cur의 prev에 저장되어 있던 주소를 cur의 오른쪽 노드의 prev에 저장되어 있던 주소와 바꿈 
- 3. cur가 가리키는 노드에 할당된 메모리를 반환

# 연결 스택(Linked Stack)

### 스택의 원소: 리스트의 노드
- 스택 내의 순서는 리스트의 링크를 통해 연결됨
- Push: 리스트의 마지막에 노드 삽입
- Pop: 리스트의 마지막 노드 반환/삭제


# 연결 큐(Linked Queue)

### 단순 연결 리스트(Linked List)를 이용한 큐
- 큐의 원소: 단순 연결 리스트의 노드
- 큐의 원소 순서: 노드의 연결 순서, 링크로 연결되어 있음
- front: 첫 번째 노드를 가리키는 리크
- rear: 마지막 노드를 가리키는 링크

# 우선순위 큐

### 우선순위 의 구현
- 배열을 이용한 우선순위 큐
- 리스트를 이용한 우선순위 큐

### 배열을 이용하여 우선순위 큐 구현
- 배열을 이용하여 자료 저장
- 원소를 삽입하는 과정에서 우선순위를 비교하여 위치에 삽입하는 구조
- 가장 앞에 최고 우선순위의 원소가 위치하게 됨

### 문제점
- 배열을 사용하므로 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생함
- 이에 소요되는 시간이나 메모리 낭비가 큼

### 리스트를 이용하여 우선순위
- 연결 리스트를 이용하여 자료 저장
- 원소를 삽입하는 과정에서 리스트 내 노드의 원소들과 비교하여 적절한 위치에 노드를 삽입하는 구조
- 리스트의 가장 앞쪽에 최고 우선순위가 위치하게 됨