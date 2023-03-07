# HTML

## 웹 사이트

</br>

> 웹 사이트는 웹 페이지의 모음
- 웹 브라우저를 통해서 접속하는 웹 페이지들의 모음!
- 웹 페이지는 글, 그림, 동영상 등 여러가지 정보를 담고 있으며, 링크를 통해 다른 웹 페이지로 이동이 가능
- 웹 사이트 = 링크를 통해 여러 웹 페이지를 연결한 것

</br>

> HTML & CSS & JavaScript

![HTML & CSS & JavaScript](../assets/HTML_CSS_JavaScript_1.png)

![HTML & CSS & JavaScript](../assets/HTML_CSS_JavaScript_2.png)

- FrontEnd
  - html : 텍스트, 구조
  - CS : 구조, 꾸미기
  - JavaScript : 상호작용
- BackEnd
  - django : 데이터 불러오기, 데이터베이스

</br>

## HTML : Hyper Text Markup Language

> Hyper Text
- 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

</br>

> Markup Language
- 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  - 대표적인 예 : HTML, Markdown

</br>

> HTML(.html)
- 웹 페이지를 작성(구조화)하기 위한 언어
- 암기로 다가가지 말 것
  - 기본 컨셉을 이해하기
  - MDN: html 성경
  - W3Schools : html 자습서

</br>

> HTML 기본 구조
- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용

```
- <title> : 브라우저 상단 타이틀
- <link> : 외부 리소스 연결 요소(CSS 파일 등)
- <style> : CSS 직접 작성
```

</br>

> head 예시
```html
<head>
  <title>HTML 수업</title>
  <meta charset="UTF-8">
  <link href="style.css" rel = "stylesheet">
  <script src="javascript.js"></script>
  <style>
    p {
      color: black;
    }
  </style>
</head>
```

</br>

> 요소(element)
- HTML의 요소는 태그와 내용(contents)으로 구성되어 있다.
  - 열었으면, 닫아야 한다.
  - 모든 내용은 태그로 감싸져 있어야 한다.

![요소(element)](../assets/요소.png)


</br>

- HTML 요소는 시작 태그와 종료 태그, 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(element, 요소)는 컨텐츠(내용)를 감싼는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br(breaking line, 줄바꿈), hr(수평선), img(이미지), input, link, meta
- 요소는 중첩(nested)될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인해야함
    - 오류를 반환 X
    - 그냥 레이아웃이 깨진 상태로 출력(디버깅이 힘듬)

</br>

> 속성
- 각 태그별로 사용할 수 있는 속성이 다르다.
- 속성은 속성명과 속성값으로 이루어져 있다.

![속성(attribute)](../assets/attribute1.png)

![속성(attribute)](../assets/attribute2.png)


</br>

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성들도 있음

</br>

> Tip for vscode 용
- ctrl + d : 다중선택
- alt + shift + 화살표 : 복사
- alt + 화살표 : 이동
- ! + tab : 기본적인 html 구조 만들어줌

> Tip for pycharm 용
- alt + j : 다중선택
- alt + shift + 화살표 : 복사
- alt + 화살표 : 이동


```html
<body>
  <p>안녕하세요 <span>김싸피

```
  