# MVC 패턴

### Model
- 동작을 수행하는 코드(service, repository)
- 사용자 View에 어떻게 보일지에 대해서 신경X
- 데이터 질의에 대한 정보를 제공하는 기능 및 데이터에 대한 수정을 담당

### View
- 사용자가 화면에 무엇을 어떻게 볼 것인지를 결정
    - JSP: 내부 Java 코드의 로직을 이용해서 수행할 수 있다.
    - HTML/CSS/JS
    - EL/JSTL

- 사용자가 화면에 보이는 부분
- 모델의 정보를 받아와 사용자에게 보여주는 역할 수행
- 자체적으로 모델의 정보를 보관 X

### Controller
- 요청을 받아 검증하고 비즈니스 로직을 수행 (서비스 호출)
- 모델과 뷰를 연결하는 역할을 수행
- 사용자에게 데이터를 가져오고 수정하고 제공함

# Spring Web MVC
- Servlet API를 기반으로 구축된 Web Framework
- 정식 명칭은 Spring Web MVC이지만, Spring MVC로 주로 알려져 있음
- Spring Framework이 제공하는 DI, AOP 뿐 아니라, WEB 개발을 위한 기능을 제공
- DispatcherServlet(Front-Controller)를 중심으로 디자인 되었으며, View Resolver, Handler Mapping, Controller와 같은 객체와 함께 요청을 처리하도록 구성됨

### Spring MVC 구성요소

- `DispatcherServlet` -> 클라이언트 요청처리(요청 및 처리 결과 전달), 모든 요청과 모든 응답은 얘로 시작해서 얘로 끝남
- HandlerMapping -> 요청을 어떤 Controller가 처리할 지 결정
- Controller -> 요청에 따라 수행할 메서드를 선언하고, 요청처리를 위한 로직 수행(비즈니스 로직 호출)
- ModelAndView -> 바구니, 요청처리를 하기 위해서 필요한 혹은 그 결과를 저장하기 위한 객체
- ViewResolver -> Controller에 선언된 view 이름을 기반으로 결과를 반환할 View를 결정
- View -> 응답화면 생성

### Spring MVC - 요청 처리 흐름
1. 클라이언트 요청이 들어오면 DispatcherServlet이 받는다.
2. HandlerMapping이 어떤 Controller가 요청을 처리할지 결정한다.
3. DispatcherServlet은 Controller에 요청을 전달
4. Controller는 요청을 처리한다.
5. 결과(요청처리를 위한 data, 결과를 보여줄 view의 이름)를 ModelAndView에 담아 반환
6. ViewResolver에 의해서 실제 결과를 처리할 View를 결정하고 반환
7. 결과를 처리할 View에 ModelAndView를 전달
8. DispatcherServlet은 View가 만들어낸 결과를 응답


### Spring Web MVC 구성하기
- Dynamic Web PJT 생성(web.xml 체크)
- maven 프로젝트로 변경
- Spring Web MVC 추가
- DispatcherServlet 등록
- servlet-context.xml / root-content.xml 파일 생성
- web.xml
- root-context.xml 설정 추가
- web.xml
- servlet-context.xml 작성
- 뷰 리졸버 등록
- Controller 작성(Component-Scan 빈 등록)
- index.jsp 작성

# Spring Web MVC 실습

### RequestMapping
- URL을 클래스 또는 특정 핸들러(메서드)에 매핑
- 메서드 Annoatation은 요청 방식(GET, POST)등으로 범위를 좁혀준다.

### Controller parameter

|파라미터 타입|설명|
|--|--|
|HttpServletRequest, HttpServletResponse, HttpSession|Servlet API를 사용할 수 있다.|
|Locale|요청 클라이언트의 Locale 정보를 포함|
|InputStream, Reader OutputStream, Writer|요청으로부터 직접 데이터를 읽어오거나, 응답을 직접 생성하기 위해서 사용|
|Map, Model, ModelMap|View 데이터를 전달하기 위해서 사용|
|RedirectAttributes|리디렉션(쿼리 문자열에 추가)시 사용할 속성 지정|
|Errors, BindingResult|에러와 데이터 바인딩 결과에 접근하기 위해서 사용|
|@pathVariable|URI 템플릿 변수에 대한 엑세스|
|@RequestParam|multipart파일을 포함하여 요청 파라미터에 엑세스|
|@RequestHeader|요청 헤더에 엑세스|
|@CookieValue|쿠키에 대한 엑세스|
|@RequestAttribute|모든 세션 속성에 대한 엑세스|
|@SessionAttribute|요청 속성에 엑세스|
|@ModelAttribute|모델의 속성에 엑세스|
|@ResponseBody|HttpMessageConverter 구현을 통해 변환되어 응답한다.|
|HttpHeaders|헤더가 있고 body가 없는 response를 반환|
|String|뷰 이름 반환(ViewResolver 선언과 함께 사용)|
|Map, Model|명시적으로 모델을 작성하지 않은 경우 사용|
|ModelAndView|사용할 view와 속성을 포함하는 객체|
|void|method에 ServletResponse, HttpServletResponse 인자가 있는 경우, 모든 요청이 처리된 것으로 간주, 그렇지 않으면 요청 URI를 view name으로 처리|
