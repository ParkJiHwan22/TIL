# MySQL Workbench

## 1. Workbench의 주요한 기능

- 데이터베이스 연결 기능
- 인스턴스 관리
- 통합된 기능의 SQL 편집기
- 데이터베이스 모델링 기능

- 포워드/리버스 엔지니어링 기능
- 데이터 내보내기/가져오기
- 데이터베이스 계정 관리

---

## 2. MySQL 연결 창
- Connection Name: 접속하는 이름, 사용자가 지어주면 됨

- #### **[Connection]탭**
- 대부분 Standard(TCP/IP)를 사용

- #### **[Parameters]탭**
- Hostname: Localhost로 설정하면 자신을 의미
- Default Schema: 접속하자마자 사용할 데이터베이스를 지정할 수 있음

- #### **[SSL]탭 (Secure Socket Layer)**
- 보안을 위한 암호 규약으로, 서버와 클라이언트가 통신할 때 암호화를 통해서 비밀을 유지시켜주고 보안을 강화시킴

---

## 3. MySQL Workbrench의 화면 구성
- 우측 상단에 아이콘을 눌러서 패널의 구성을 변경할 수 있음

- ### **[네비게이터]**
- #### **[Schemas]탭**
    - 데이터베이스(=스키마) 생성 및 삭제
    - 데이터베이스 개체(테이블, 뷰, 인덱스, 저장 프로시저, 함수 등)를 생성하고 관리
    - 데이터베이스의 속성을 조회

- #### **[Administration]탭**
- MANAGEMENT
    - 사용자의 생성, 삭제 및 권한 관리
    - 서버 변수값의 확인
    - 데이터 내보내기 가져오기 기능

- INSTANCE(서비스 기능)
    - MySQL의 연결 정보 관리
    - MySQL 인스턴트의 중지, 시작
    - Server에 기록된 로그 조회

- PERFORMENCE
    - 성능 상태의 보고서 작성
    - 성능 구성의 설정