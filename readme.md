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


### 0522

#### 오늘의 진행과정

1. 로그인 시 새로고침, 타인의 홈 이동 시 새로고침
2. 영화 추천 기능 완성 
   1. 내가 선호하는 장르의 영화
   2. 다른 장르의 영화
3. 회원가입 이미지 디폴트값 설정
4. 사용하지 않는 함수, 데이터들 정리 및 코드 정리
5. 댓글 작성, 수정, 삭제 기능 완성
6. 영화 세부정보 페이지 완성
7. 리뷰 작성, 수정, 삭제 기능 완성

#### 어려웠던 점

1. 이중 axios
  - 로그인을 하자마자 my home이 보이게 하려면 userId를 바로 받아왔어야 하는데, 어디에서 받아오는지를 몰라서 헤맸다.
	- 로그인을 하면 MainView에서 create로 getUserInfo가 실행되는 부분에서 갱신이 성공했다.
	갱신을 성공하면 router로 main을 요청하는데, 해당 부분에서 userId를 받아오지 못하고 있었다.
	- 따라서 로그인 axios 안에 getuserinfo 부분의 axios를 하나 더 만들어서 then으로 data의 userid를 전달했다.
	- 그 뒤에 또 라우터에 한번 더 전달해 주어서 이제 로그인하자마자 나온다!
	```axios({  
          // get user info에 대한 axios 요청을 보낸다
          
            method: 'get',
            url: `${API_URL}/accounts/user/myprofile/`,
            headers: {
              'Authorization': `Token ${context.state.token}`
            }
          })
						// 보내고서 .then에서 user id를 담아서 push한다.
            .then((response) => {
              console.log(response)
              context.commit('GET_USER_INFO', response.data)
              // userid라는걸 여기서 비로소 받을 수 있는데, params로 전달
              router.push({ name: 'main', params: {userId : response.data.id} })
      
            })```
2. 라우터를 통해 이동했을 때 새로고침이 안 되는 것
	- router.go(0) 을 통해 해결
3. 회원가입 이미지 디폴트값 설정. 
  - /media는 기본으로 설정되어 있는데 자꾸 경로를 두 번 줘서 오류가 났었음
4. 본인의 홈피에서만 추천, 둘러보기 가능. 타인의 홈피에서는 불가능
5. 방명록 (Guestbook 모델을 Vue로 연결해서 화면에 나타내기 힘들었음)
  - 아직 미완성, 5월 23일 진행 예정