### 0517

#### 오늘의 진행과정

1. 계획서 작성
2. django pjt 생성
3. user model 작성
4. 로그인 & 회원가입 구현

#### 어려웠던 점

1. models.py와 profileserializer에서 field를 수정한 뒤에, setprofile.vue를 통해서 데이터를 받아야 하는데, CORS 오류와 400 오류 발생함
  - 400 오류는 migration을 새로 해서 해결함.
  - CORS 오류는 setprofile.vue에서 form을 수정해서 해결함.

---

### 0518

#### 오늘의 진행과정

1. cyworld html을 vue에 적용시켰다.
2. 홈 화면 구성하기
  - 프로필 화면 설정
  - 유튜브 영상 불러오기
  - 미니홈피 브금 불러오기
3. 둘러보기 구성하기
  - 영화목록 화면에 6개씩 나오도록 구성
  - searchBar 화면 배치

#### 어려웠던 점

1. axios 사용하지않을때 import 하면 오류 발생함
  - 사용할 때 import axios 하면 오류 발생하지 않음
2. iframe을 사용해본적이 없어서 default로 어느 요소와 연결되는지 확인하지 못해서 코드가 꼬였다.
	- 해결했다.
3. searchBar 기능이 작동하지 않음
  - emit 한번 더 받아서 5/19에 해결하기로 함.
4. 둘러보기 구성할 때 화면 크기에 제대로 맞지 않았음
  - MovieList.vue의 카드 사이즈를 수정해 주었음.

---

### 0519

#### 오늘의 진행과정

1. 내가 찜한 영화들 불러와서 표시
2. 내가 쓴 리뷰들 불러와서 표시
3. 내가 선호하는 장르의 영화 추천 받아와서 표시하기(미완성)
  - 몇 개의 영화를 추천할지 정해서 수정해야 함
4. 중첩 라우터를 사용해서 navigation-bar를 통해 열 수 있는 페이지를 원하는 위치에 불러올 수 있도록 만들었다.

#### 어려웠던 점


1. searchbar 오류
  - searchbar를 만들면서 props & emit의 사용에서 method에 같은 변수를 전달해 주어야 하고, 한번 전달받은 변수에는 value를 줄 필요가 없는데 괜히 줬다가 코드가 꼬였다. 키워드를 수정해서 해결했다!
2. 진행과정 중 4번을 진행할 때 어려웠던 점
  - 중첩 라우터를 사용해야 해서 https://v3.router.vuejs.org/guide/essentials/nested-routes.html
3. 로그인 시 userId를 못받아와서 로드를 못해줬는데 수정해야 홈화면이 뜬다...
  - http://localhost:8080/1/main/myhome < 1 부분
