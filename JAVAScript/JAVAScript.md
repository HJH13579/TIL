bㅠb> JavaScript란?
- JavaScript는 클라이언트 측 웹(<span style='color:red'>브라우저</span>)에서 실행
- <span style='color:red'>쉽게 배울 수 있고</span> 강력한 스크립트 언어
- 웹 페이지가 <span style='color:red'>이벤트</span> 발생 시 어떻게 작동하는 지 <span style='color:red'>디자인 / 프로그래밍</span>
- <span style='color:red'>웹 페이지 동작을 제어</span>하는 데 사용

![웹 클라이언트 관계](../assets/웹_클라이언트_관계.png)

<br>

1. HTML에 변화를 줄 수 있다.
2. CSS에 변화를 줄 수 있다.
3. 백앤드에 변화를 줄 수 있다.

</br>

- HTML 문서의 컨텐츠를 동적으로 변경할 수 있는 언어
- Web이라는 공간에서 다양한 동작을 할 수 있게 된 기반
- 언어의 확장성 덕분에 큰 인기

## JavaScript Engine
> 개요
- JavaScript Engine은 자바스크립트 코드를 실행하는 프로그램 또는 인터프리터
- 대체적으로 웹 브라우저에서 사용

</br>

> 웹 브라우저의 역활
- URL을 통해 Web(WWW)을 탐색함
- HTML/CSS/JavaScript를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
- 웹 서비스 이용 시 클라이언트의 역활을 함
- 웹 페이지 코드를 이해하고, 보여주는 역활을 하는 것이 바로 웹 브라우저

</br>

> JavaScipt Engine
- HTML/CSS/JavaScript를 이해한 뒤 해석
  - JavaScript를 해석하는 것이 Engine의 역활
- 각 브라우저마다 자체 JavaScript Engine을 개발, 사용하고 있음
  - V8 - Chrome
  - SpiderMonkey - FireFox

- 대체적으로 웹 브라우저에서 사용
- 웹 브라우저 외에는 어떻게 할용?
  - Node.js : V8 엔진을 사용하여 서버 측에서 자바스크립트 코드를 실행 가능, 브라우저 조작 이외의 역활도 수행

</br>

## JavaScript 실행 환경 구성
> Web Browser로 실행하기
1. HTML 파일에 포함시키기
2. 외부 JavaScript 파일 사용하기
3. Web Browser에서 바로 입력하기
  
![Web Browser로 실행하기](../assets/Web_Browser로_실행하기_1.png)

![Web Browser로 실행하기](../assets/Web_Browser로_실행하기_2.png)

![Web Browser로 실행하기](../assets/Web_Browser로_실행하기_3.png)

![Web Browser로 실행하기](../assets/Web_Browser로_실행하기_4.png)

![Web Browser로 실행하기](../assets/Web_Browser로_실행하기_5.png)

</br>

> 정리
- 웹 브라우저는 JavaScript를 해석하는 엔진을 가지고 있음
- 특히 Chrome의 V8의 경우 JavaScript를 번역하는 속도가 매우 빠름
  - 다른 개발에도 활용 가능
  - node.js, react.js, electron 등의 내부 엔진으로 사용됨
  - back-end, mobile, desktop app등을 모두 JavaScript로 개발이 가능해짐

</br>

## Before we start JavaScript
> EcmaScript
- Ecma International(전자 정보 통신 시스템 표준화 기구)이 ECMA-262 규격에 따라 정의하고 있는 표준화된 스크립트 프로그래밍 언어를 뜻함
- <span style='color:red'>JavaScript를 표준화</span>하기 위해 만들어짐
- JavaScript의 기본적인 문법, 데이터 타입, 객체 모델, 함수, 연산자 등을 정의
  - ES6+(2015년 이후) 정의된 내용을 토대로 진행
  
</br>

> 주석 
- 한 줄 주석(//)과 여러 줄(/* */) 주석
```JavaScript
// hello.js

// console.log('화면에 표시되지 않아요.')
```

```JavaScript
/* hello.js

여러 줄 주석 사용법 */
```

</br>

> 들여쓰기와 코드 블럭
- JavaScript는 2칸 들여쓰기 사용
- 블럭(block)은 if, for, 함수에서 <span style='color:red'>중괄호 {}</span>내부를 말함
- 즉, 중괄호 {}를 사용해 코드 블럭을 구분

```JavaScript
if (isClean){ // 중괄호를 사용해서 코드 블럭 구분
  console.log('clean')  // 2칸 들여쓰기 
}
```

</br>

> 코드 스타일 가이드
- 회사마다 코드 스타일 가이드 존재
  - Airbnb JavaScript Style Guide (진행에 쓸 것)
  - Google JavaScript Style Guide
  - JavaScript Standard Style

</br>

> 세미콜론(semicolon)
- 자바스크립트는 세미콜론을 선택적으로 사용 가능
- 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
  - ASI(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
- TC39(ECMAScript 기술 위원회)는 세미콜론 사용을 권장
- JavaScript 개발자는 세미콜론 사용 반대

# JavaScript 기초 문법
## 변수와 식별자
> 식별자 정의와 특징
- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작
- 예약어 사용 불가능
  - 예약어 예시: for, if, function 등

</br>

- 카멜 케이스(camelCase)
  - 변수, 객체, 함수에 사용

```JavaScript
// 변수
let dog
let variableName

// 객체
const userInfo = { name:'Tom', age:20 }

// 함수
function add() {}
function getName() {}
```

- 파스칼 케이스(Pascal Case)
  - 클래스, 생성자에 사용

```JavaScript
// 클래스
class User {
  constructor(options){
    this.name = options.name
  }
}
```

- 대문자 스네이크 케이스(SNAKE_CASE)
  - 상수(constants)에 사용
  - 상수: 개발자의 의도와 상관없이 변경될 가능이 없는 값을 의미

```JavaScript
// 값이 바뀌지 않을 상수
const API_KEY = 'my-key'
const PI = Math.PI

// 재할당이 일어나지 않는 변수
const NUMBERS = [1,2,3]
```

</br>

> 변수 선언 키워드
- Python과 다르게 JavaScript는 변수를 선언하는 키워드가 정해져 있음
1. let
   - 블록 스코프 지역 변수를 선언 (추가로 동시에 값을 초기화)
2. const
   - 블록 스코프 읽기 전용 상수를 선언 (추가로 동시에 값을 초기화)
3. var
   - 변수를 선언 (추가로 동시에 값을 초기화)

</br>

> [참고] 선언, 할당, 초기화
- 선언(Declaration)
  - 변수를 생성하는 행위 또는 시점
- 할당(Assignment)
  - 선언된 변수에 값을 저장하는 행위 또는 시점
- 초기화(Initialization)
  - 선언된 변수에 <span style='color:red'>처음으로</span> 값을 저장하는 행위 또는 시점

```JavaScript
let foo // 선언
console.log(foo)  // undefined

foo = 11  // 할당
console.log(foo)  // 11

let bar = 0 // 선언 + 할당
console.log(bar)  // 0
```

</br>

> 변수 선언 키워드 - let
- let
  - 재할당 가능 & 재선언 불가능

```JavaScript
let number = 10 // 1. 선언 및 초기값 할당
number = 20 // 2. 재할당
```

```JavaScript
let number = 10 // 1. 선언 및 초기값 할당
let number = 20 // 2. 재선언 불가능
```
  - <span style='color:red'>블록 스코프</span>를 갖는 지역 변수를 선언, 선언과 동시에 원하는 값으로 초기화 할 수 있음

</br>

> 변수 선언 키워드 - const
- const
  - 재할당 불가능 & 재선언 불가능

```JavaScript
const number = 10 // 1. 선언 및 초기값 할당
number = 20 // 2. 재할당 불가능
```

```JavaScript
const number = 10 // 1. 선언 및 초기값 할당
const number = 20 // 2. 재선언 불가능
```

  - 선언 시 반드시 초기값을 설정 해야 하며, 이후 값 변경이 불가능
  - let과 동일하게 <span style='color:red'>블럭 스코프</span>를 가짐

</br>

![블럭 스코프(blcok scope)](../assets/block_scope.png)

</br>

> 변수 선언 키워드 - var
- var
  - 재할당 가능 & 재선언 가능
  - ES6 이전에 변수를 선언할 때 사용되던 키워드
  - <span style='color:red'>"호이스팅"</span>되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 따라서 ES6 이후부터는 var 대신 <span style='color:red'>const와 let을 사용하는 것을 권장</span>
  - 함수 스코프(function scope)를 가짐   
<span style='color:red'>※ 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨</span>

</br>

![함수 스코프(function scope)](../assets/function_scope.png)

</br>

> 호이스팅 (hoisting)
- 변수를 선언 이전에 참조할 수 있는 현상
- var로 선언된 변수는 선언 이전에 참조할 수 있으며,  이러한 현상을 호이스팅이라 함
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환

```JavaScript
console.log(name) // undefined => 선언 이전에 참조

var name = '홍길동' // 선언
```

```JavaScript
// 위 코드를 암묵적으로 아래와 같이 이해함
var name // undefined로 초기화
console.log(name)

var name = '홍길동'
```



- NaN : Not a Number, 이지만 사실상 number로 취급!


- Template Literal : 정말 중요!
- 백틱(`${}`)


- null : 값이 없는 것, 정상적인 상황
- undefined : 값을 안 넣은 것, 비정상적인 상황
- 설계 실수가 아니다.

```JavaScript
const instance = {
  name : 'haha',
  age : 20,
  region : null
}

console.log(instance.name)  // haha
console.log(instance.age) // 20
console.log(instance.region)  // null
console.log(instance.area) // undefined
```


- 진짜 설계 실수 
  - null 
    - 의미론적 : primitive
    - 구현 : object (type of null = object)

- Boolean
  - Python : 대문자
  - JavaScript : 소문자

- Object는 항상 True!

- 동등 연산자 절대 기억도 하지마셈!
- 일치 연산자(===) : 무조건 3개만 쓴다!
- 삼항 연산자 : 생각보다 많이 쓴다. 왜냐하면 코드 가독성 때문

- for ~ in vs. for ~ of
  - for ~ in : 객체를 순회 & property를 출력

  ```JavaScript
  const lst = {'a', 'b', 'c'}

  for (let i in lst){
    console.log(i)
  }

  0
  1
  2
  ```

  - for ~ of : iterable을 순회(object는 객체이므로 iterable이 아니다.)

  ```JavaScript
  const lst = {'a', 'b', 'c'}

  for (let i of lst){
    console.log(i)
  }

  a
  b
  c
  ```

> Optional Chaining

```JavaScript
const a = obj.b?.value ?? 'http404' // ?? : 앞에 것이 null이나 undefined 면 뒤에 것을 가져가
 
const obj = {
  a:1
}

console.log(obj.a) // 1
console.log(obj.b) // undefined
console.log(obj.a.b) // undefined
                     // undefined
console.log(obj.a.value) // obj.a까지 존재
console.log(obj.b.value)  // obj까지 존재
// 터져버림
console.log(obj.b?.value) // ?. 뒤에는 다 무시해버림 
// undefined
```

```JavaScript
let a = 3
console.log(a, 1)

function func(){
  console.log(a, 2)
  a = 5
  console.log(a, 3)
}
func()
console.log(a, 4)

3 1
3 2
5 3
5 4
```

```JavaScript
let a = 3
console.log(a, 1)

function func(){
  // console.log(a, 2)
  let a = 5
  console.log(a, 3)
}
func()
console.log(a, 4)

3 1
5 3
3 4
```