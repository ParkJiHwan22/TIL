# File Upload

### 파일 업로드
- 클라이언트가 서버로 파일을 전송하는 과정을 말함
- 여러 개의 파일을 업로드 할 수 있음

### 기존 방식의 Form
- 기존에 사용하던 <form>은 문자 위주의 데이터를 사용함
- enctype = "application/x-www-form-urlencoded" 기본 값 (생략 가능)
- HTTP Body에 문자로 key=value 형태로 전송하고, 여러 개의 데이터라면 & 기호를 통해 구분 하였음

``` HTML
<h3>기존 Form 사용법</h3>
<form action="..." method="GET or POST" enctype="application/x-www-form-urlencoded">
    <input type = "text" name="...">
    <input type = "text" name="...">
    <input type = "text" name="...">
    <input type = "text" name="...">
    <input type = "submit">
</form>

### 파일 업로드 방식의 Form
- 파일은 문자가 아닌 바이너리 데이터를 전송
- 파일만 전송하는 것이 아니라 다른 데이터를 같이 전송하기도 함
- `enctype` = "multipart/form-data", `method="POST"` 필수
- 여러 개의 파일을 업로드 하고 싶다면 multiple="multiple" 속성 추가 필요

``` HTML
<h3>파일 업로드 Form 사용법<h3>
<form action="..." method="POST" enctype="multipart/form-data">
    <input type = "text" name="...">
    <input type = "file" name="..." multiple="multiple">
    <input type = "submit">
</form>
```

### MultipartFile
- Spring FrameWork에서 파일 업로드를 처리하기 위한 인터페이스
- 파일의 내용은 메모리에 저장되거나, 디스크에 임시로 저장
- 사용자가 원하는 대로 `세션 수준`
 또는 영구 저장소에 파일의 내용을 복사할 책임이 있음
- 임시 저장소는 요청이 끝나면 삭제
- getOriginalFilename(): 업로드 파일 명
- transferTo(): 파일 저장

### 파일 업로드 추가 설정
- servlet-context.xmml 파일에 Multipart를 처리하기 위한 Resolver 등록
- `StandardServletMultipartResolver` -> MultipartResolver의 구현체 중 하나 `Spring MVC` 권장

``` Java
<beans:bean id="multipartResolver" class="org.springframework.web...">
```

- tomcat의 context.xml에서 allowCasualMultopartParsing="true"을 작성한다.
- 용량의 기본은 1MB/web.xml에서 용량을 지정할 수 있다.

``` Java
<multipart-config>
    <max-file-size>10485760</max-file-size>
    <max-request-size>20971520</max-request-size>
</multipart-config>
```

# File Download

### 파일 다운로드
- 서버에 있는 파일을 클라이언트에게 전송하는 과정을 말함

### 파일 다운로드 view 생성하기
- AbstractView를 상속하여 FileDownLoadView 작성하기

``` Java
    public class FileDownloadView extends AbstractView {
    }
```

- renderMergedOutputModel 메서드 재정의 하기

``` Java

@Override
protected void renderMergedOutputModel(Map<String, Object> model, HttpServletRequest request, HttpServletResponse response) throws Exception {
}
```

### 파일 다운로드 view 등록하기
- servlet-context.xml 에 FileDownloadView를 Bean으로 등록하기
- Bean의 이름으로 View를 찾을 수 있는 BeanNameViewResolver 등록하기