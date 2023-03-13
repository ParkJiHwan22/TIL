# 1. JS - History_of_JavaScript

## 학습 목표

> JavaScript의 탄생과 초기 개발 과정을 이해할 수 있다.

> 현재 웹 개발에서 JavaScript가 가지는 역할과 중요성을 인식할 수 있다.

# 1. 웹 브라우저와 JavaScript
### 웹 브라우저의 상용화
- 1994년, Netscape사의 최초 상용 웹 브라우저인 Netscape Navigator 출시
- 당시 약 90% 이상의 시장 점유율을 가졌을 것이라 추정

### 웹 브라우저 경쟁
- 1995년, Microsoft의 Internet Explorer(IE)출시
- Netscape는 IE와 경쟁할 차기 웹 브라우저 개발을 착수
- 당시에는 웹 페이지에 동적인 기능이 없었기 때문에 Netscape는 웹 페이지의 동적인 기능을 제공하기 위한 새로운 언어를 개발하기 시작

### JavaScript의 탄생
- 당시 Netscape 소속 개발자 Brandon Eich는 회사의 요구사항을 넘어 Mocha라는 언어를 개발
- 이후 LiveScript로 이름을 변경 했으나 당시 인기있던 프로그래밍 언어인 JAVA의 명성에 기대보고자 JavaScript로 이름 변경
- JavaScript는 Netscape Navigoator 2.0에 탑재되어 큰 인기를 누림

### JavaScript의 파편화
- Microsoft는 JavaScript의 파생버전인 Jsscript를 IE 3.0에 채택
- 이 과정에서 NEtscape와 Microsoft 그리고 많은 회사들이 자체적으로 JavaScript를 탑재해 독자적으로 업데이트
- 이로 인해 같은 코드가 브라우저마다 다르게 동작하는 등의 문제가 발생
  - 추후 JavaScript 표준화의 배경이 됨

### 1차 브라우저 전쟁
- Microsoft는 IE를 자사 윈도우 운영체제에 내장하여 무료로 배포
- 빌 게이츠를 필두로 한 Microsoft의 공격적인 마케팅, 자금력 그리고 막강한 윈도우 운영체제 점유율 앞에 Netscape는 빠르게 몰락하기 시작
- 결국 IE의 시장 점유율을 2002년 약 96%에 달하며 Microsoft의 승리로 종료
- 추후 Brandon Eich와 함께 Netscape에서 나온 핵심 개발진은 모질라 재단을 설립하여 Firefox 브라우저를 출시(2003)
- 이후 많은 브라우저들이 IE에 도전했지만 모두 실패하며, IE의 영원한 지배가 예상됨

### 2차 브라우저 전쟁
- 2008년 구글에서 Chrome 브라우저를 출시
- 출시 3년만에 10년간 쌓아온 Firefox의 점유율을 넘어섰고 그로부터 반년 뒤 IE의 점유율을 넘어섬
- 빠른 속도, 압도적인 성능, 엄격한 웹 표준 준수, 강력한 개발자 도구를 제공
- 웹 표준의 발전과 웹 애플리케이션의 대중화에 큰 역할을 하게 됨

### JavaScript 현황
- 현재는 Chrome, Firefox, Safari, Microsoft Edge 등 다양한 웹 브라우저가 출시되어 있으며, 웹 브라우저 시장이 다양화 되어있음
- 기존에 JavaScript는 브라우저에서만 웹 페이지의 동적인 기능을 구현하는 데 사용
  - 예를 들어, 사용자의 입력에 따라 웹 페이지의 내용이 동적으로 변경되거나, 애니메이션 효과가 적용되는 등의 기능
- 이후 브라우저에서 벗어나 Node.js와 같은 서버 사이드 분야 뿐만 아니라, 다양한 프레임워크와 라이브러리들이 개발되면서, 웹 개발 분야에서는 필수적인 언어로 자리 잡게 됨

# 2. JavaScript의 표준화

## ECMAScript
- ECMA International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어

- JavaScript의 파편화를 막기 위해 1997년 ECMA에서 ECMAScript라는 표준 언어를 정의 
- 이후 ECMAScript는 독자적으로 발전하며 JavaScript보다 더 많은 기능을 제공하게 됨
- 2009년에는 ECMAScript5(ES5)에서 안정성과 생산성을 크게 높임
- 2015년에는 ECMAScript 2015(ES6)에서 객체지향 프로그래밍 언어로써 많은 발전을 이루어, 역사상 가장 중요한 버전으로 평가됨
- JavaScript는 ECMAScript의 구현 언어 중 하나

