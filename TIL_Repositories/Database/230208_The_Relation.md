# The Relation

## 학습 목표

> 데이터베이스상에서 `관계`가 의미하는 바를 정의할 수 있다.

> 관계형 데이터베이스 용어 중 scheme, record, field의 역할과 특징을 설명할 수 있다.

> DBMS의 정의와 역할을 설명할 수 있다.

## 1. Relational Database
- 관계형 데이터베이스: 데이터 간에 `관계`가 있는 데이터 항목들의 모음
- 테이블, 행, 열의 정보를 구조화하는 방식
- `서로 관련된 데이터 포인트를 저장`하고 이에 대한 `엑세스`를 제공

- 관계: 여러 테이블 간의 (논리적) 연결

### 관계로 인해 할 수 있는 것
- 이 관계로 인해 두 테이블을 사용하여 데이터를 다양한 방식으로 조회할 수 있음

### 고객 데이터 간 비교를 위해서는 어떠한 값을 활용해야 할까?

- `기본 키`(PK, Primary Key)

### 누가 어떤 주문을 했는지 어떻게 식별할 수 있을까?

- `외래 키`(FK, Foreign Key)

## 관계형 데이터베이스 용어
1. Table(Relation)
    - 데이터를 기록하는 곳
2. Field(Column, Attribute)
    - 각 필드에는 고유한 데이터 형식(타입)이 지정됨
3. Record(Row, Tuple)
    - 각 레코드에는 구체적인 데이터 값이 저장됨

4. Database(Schema)
    - 테이블의 집합(set of tables)
5. Primary Key
    - 각 레코드의 고유한 값
    - 관계형 데이터베이스에서 `레코드의 식별자`로 활용
6. Foreign Key
    - 테이블의 필드 중 다른 테이블의 레코드를 식별할 수 있는 키
    - 각 레코드에서 서로 다른 테이블 간의 `관계를 만드는 데` 사용

## 2. RDBMS

- DBMS(Database Management System): 데이터베이스를 관리하는 소프트웨어 프로그램
- `R`DBMS(`Relational`Database Management System): `관계형` 데이터베이스를 관리하는 소프트웨어 프로그램
- 데이터 저장 및 관리를 용이하게 하는 시스템
- 데이터베이스와 사용자 간의 인터페이스 역할
    - 사용자가 데이터 구성, 업데이트, 모니터링, 백업, 복구 등을 할 수 있도록 도움

### 대표적인 RDBMS
- `MySQL`
- PostgreSQL
- Oracle Database
- MS SQL Server

### MySQL
- 가장 널리 사용되는 오픈소스 RDBMS
- 다양한 운영체제에서 실행 가능
- 여러 프로그래밍 언어를 위한 다양한 API 제공
- MySQL Workbench Tool을 통해 그래픽 인터페이스를 제공

### MySQL 구조
- Table ⊂ Database ⊂ Database Server

## 정리
- Table은 데이터를 기록하는 최종 위치
- 모든 Table에는 행에서 고유하게 식별 가능한 `기본 키`라는 속성이 있으며, `외래 키`를 사용하여 각 행에서 서로 다른 테이블 간의 관계를 만들 수 있음
- 데이터는 기본 키 또는 외래 키를 통해 결합(join)될 수 있는 여러 테이블에 걸쳐 구조화 됨
- 각 Table은 Database로 그룹핑됨
- MySQL은 이러한 Database들을 그룹핑하여 관련된 작업을 수행하는 Database Server