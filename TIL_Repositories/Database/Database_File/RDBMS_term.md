## 관계형 데이터베이스 용어

1. Table(Relation)
    - 하나하나의 관계, 데이터를 기록하는 곳

2. Field(Column, Attribute)
    - 각 필드에는 고유한 `데이터 형식(타입)`이 지정됨
    - 어떠한 데이터 속성이 들어갈지 결정하기 때문에 속성이라고도 부름
    - ex) 필드명: id -> int, 이름 -> str

3. Record(Row, Tuple)
    - 각 레코드에는 구체적인 데이터 값이 저장됨

4. Database(Schema)
    - 테이블의 집합(set of tables)
    - Table ⊂ Database

5. Primary Key
    - 각 레코드의 고유한 값
    - 관계형 데이터베이스에서 `레코드의 식별자`로 활용
    
6. Foreign Key
    - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
    - 각 레코드에서 서로 다른 테이블 간의 `관계를 만드는 데` 사용