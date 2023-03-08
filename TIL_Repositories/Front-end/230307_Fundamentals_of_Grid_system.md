# 08. Fundamentals_of_Grid_system

## 목차

> Grid system의 클래스 및 기본 구조를 사용하는 방법을 이해할 수 있다.

> Grid system을 사용하여 이미지와 텍스트를 조합한 카드 레이아웃을 구성할 수 있다.

> Grid 구성 안에 중첩된 Grid 행을 구성할 수 있다.

# 1. 개요
## Bootstrap Grid system
- 웹 페이지의 레이아웃을 조정하는 데 사용되는 12개의 컬럼으로 구성된 시스템
  - `반응형 디자인을 지원해 웹 페이지를 모바일, 테블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움`

# 2. Grid system 클래스와 기본 구조

## Grid system 핵심 클래스
- 1개의 row 안에 12칸의 column 영역이 구성
- 각 요소는 12칸 중 몇 개를 차지할 것인지 지정됨

### Grid 실습 - 기본

``` HTML
<div class="container">
  <div class="row">
    <div class="box-col">col</div>
    <div class="box-col">col</div>
    <div class="box-col">col</div>
  </div>
  <div class="row">
    <div class="box-col-4">col-4</div>
    <div class="box-col-4">col-4</div>
    <div class="box-col-4">col-4</div>
  </div>
  <div class="row">
    <div class="box-col-2">col-2</div>
    <div class="box-col-8">col-8</div>
    <div class="box-col-2">col-2</div>
  </div>
</div>
```

### Gutters
- Grid system에서 column 사이에 padding 영역

