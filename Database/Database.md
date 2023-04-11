# N:1 (Comment-User)
- Comment(N) - User(1)
- Comment 모델과 User 모델 간 관계 설정
- "0개 이상의 댓글은 1개의 회원에 의해 작성 될 수 있음"

## 모델 관계 설정

![Comment User 간 모델 관계 설정](../assets/Comment_User_간_모델_관계_설정_1.png)

![Comment User 간 모델 관계 설정](../assets/Comment_User_간_모델_관계_설정_2.png)

> Migration 진행
1. 이전에 User와 Article 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정이 필요

```
$ python manage.py makemigrations
```

![Migrations 진행](../assets/Migrations_진행_1.png)

![Migrations 진행](../assets/Migrations_진행_2.png)

2. migrations 파일 생성 후 migrate 진행 & superuser 만들기

```
$ python manage.py migrate
$ python manage.py createsuperuser
```

   - comment 테이블 스키마 변경 및 확인

![Migrations 진행](../assets/Migrations_진행_3.png)

</br>

## CREATE

> 개요
- 인증된 회원의 댓글 작성 구현하기
- 작성하기 전 로그인을 먼저 진행한 상태로 진행

![CommentForm](../assets/CommentForm_1.png)

![CommentForm](../assets/CommentForm_2.png)

![CommentForm](../assets/CommentForm_3.png)

![외래 키 데이터 누락](../assets/외래키_데이터누락_1.png)

![외래 키 데이터 누락](../assets/외래키_데이터누락_2.png)

![외래 키 데이터 누락](../assets/외래키_데이터누락_3.png)

</br>

## READ

![댓글 작성자 출력](../assets/댓글_작성자_출력_1.png)

![댓글 작성자 출력](../assets/댓글_작성자_출력_2.png)

</br>

## DELETE

![댓글 삭제 시 작성자 확인](../assets/댓글_삭제_시_작성자_확인_1.png)

![댓글 삭제 시 작성자 확인](../assets/댓글_삭제_시_작성자_확인_2.png)

![댓글 삭제 시 작성자 확인](../assets/댓글_삭제_시_작성자_확인_3.png)

</br>

## 인증된 사용자에 대한 접근 제한하기

> 개요
- is_authenticated 와 View decorator를 활용하여 코드 정리하기

![인증된 사용자인 경우만 댓글작성 및 삭제하기](../assets/인증된_사용자인_경우만_댓글작성_및_삭제하기_1.png)

![인증된 사용자인 경우만 댓글작성 및 삭제하기](../assets/인증된_사용자인_경우만_댓글작성_및_삭제하기_2.png)

![인증된 사용자인 경우만 댓글작성 및 삭제하기](../assets/인증된_사용자인_경우만_댓글작성_및_삭제하기_3.png)

</br>

# Many to many relationship

> Intro
- 병원에 내원하는 환자와 의사의 예약 시스템을 구축하라는 업무를 지시 받음
  - 필요한 데이터 베이스 모델을 고민해보고 모델링 진행하기
  - 모델링을 하는 이유는 현실 세계를 최대한 유사하게 반영하기 위함
- 무엇보다 고민해야 할까?
  - 병원 시스템에서 가장 핵심이 되는 것은? -> 의사와 환자
  - 이 둘의 관계를 어떻게 표현할까?
- 우리 일상에 가까운 예시를 통해 DB를 모델링하고 그 내부에서 일어나는 데이터의 흐름을 어떻게 제어할 수 있을지 고민해보기

</br>

> 데이터 모델링
- 주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
- 물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업

</br>

> 용어 정리
- target model : 관계 필드를 가지지 않은 모델
- source model : 관계 필드를 가진 모델

![N:1의 한계](../assets/N_1의_한계_1.png)

![N:1의 한계](../assets/N_1의_한계_2.png)

> shell_plus 사용 시 'settings.py'의 'INSTALLED_APPS'에 'django_extensions', 추가

![N:1의 한계](../assets/N_1의_한계_3.png)

![N:1의 한계](../assets/N_1의_한계_4.png)

> 데이터 중복 시 수정이 용이하지 않고, 이름만 같고 다른 carol이면 구분이 안 된다.

![N:1의 한계](../assets/N_1의_한계_5.png)

> 제 1 정규화 규정 위반

![N:1의 한계](../assets/N_1의_한계_6.png)

![중개 모델](../assets/중개_모델_1.png)

![중개 모델](../assets/중개_모델_2.png)

![중개 모델](../assets/중개_모델_3.png)

![중개 모델](../assets/중개_모델_4.png)

![중개 모델](../assets/중개_모델_5.png)

![중개 모델](../assets/중개_모델_6.png)

![중개 모델](../assets/중개_모델_7.png)

![Django ManyToManyField](../assets/Django_ManyToManyField_1.png)

![Django ManyToManyField](../assets/Django_ManyToManyField_2.png)

![Django ManyToManyField](../assets/Django_ManyToManyField_3.png)

![Django ManyToManyField](../assets/Django_ManyToManyField_4.png)

![Django ManyToManyField](../assets/Django_ManyToManyField_5.png)