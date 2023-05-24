# Final Pjt
## __🎥 Movie World__; 싸이월드와 영화
### by 서울 1반 이예슬, 임혜진
------------------
------------------



# 1. Contributors 
|                                      👾 [이예슬](https://github.com/dontk1llme)                                      |                                    🐣 [임혜진](https://github.com/ccookie0415)                                    |
| :--------------------------------------------------------------------------------: | :----------------------------------------------------------------------------: |
| <img src="https://avatars.githubusercontent.com/u/89983177?v=4" alt="예슬" border="0" width="180"> | <img src="https://avatars.githubusercontent.com/u/114826382?v=4" alt="혜진" border="0" width="180">| 
|  Back - movies | Back - accounts |
| Front - router, store, components, home | Front - views, components, detail

<br><br>

# 프로젝트 개요

## 1️⃣ What

### 🎥 추억의 싸이월드를 떠올리게 하는 영화 커뮤니티

▫ 사용자 맞춤형 영화 추천  
▫ 좋아하는 영화로 직접 꾸미는 내 홈피

<br>

## 2️⃣ For Whom

▫ 영화를 사랑하는 모든 사람들  
▫ 내가 본 영화에 대한 기록을 남기고 싶은 사람들  
▫ 추후 볼 영화를 저장해두고 싶은 사람들  
▫ 영화에 대한 다른 사람들의 평가와 감상이 궁금한 사람들

<br>

## 3️⃣ Why

▫ OTT 시장이 성장하며, 영화관에 가지 않고도 다양한 영화를 손쉽게 감상할 수 있다.

▫ 그러나 기존의 영화 OTT는 영화 시청에 목적이 있기 때문에 이미 감상한 영화에 대한 기록에 대해서는 부족함이 있다.

▫ 그렇기 때문에 감상한 영화를 기록하고 보관하는 일종의 다이어리의 필요성이 대두된다.

▫ 특히나 더더욱 영화를 사랑하고, 영화에 대한 후기와 감상평을 남기는 사람들에게는 자신이 시청한 영화와 그에 대한 리뷰를 한 번에 관리하고 열람할 수 있는 공간이 필요할 것이다.

▫ 그 공간에서는 영화에 대한 추억을 찾게 되는데, 우리의 추억의 공간인 싸이월드와 접목시켜 보았다.


<br>

## 4️⃣ How (구현 기능)

❶ 사용자 맞춤형 사이트이므로 로그인 유저를 대상으로 함

- 회원가입
- 로그인 & 로그아웃 & 프로필 정보 등록
- 회원 정보 수정

<br>

❷ 사용자 프로필, 홈

- 닉네임, 자기소개, 사진, 
- 오늘의 기분
- 팔로우, 팔로잉 수
- 최근 작성한 리뷰
- 찜한 영화, 작성한 리뷰 개수
- 내가 좋아하는 영상 설정
- bgm 재생
  
<br>

 추천 - 영화 추천 알고리즘

- 선호 장르별 추천
- 선호하지 않는 장르의 새로운 영화 추천

<br>

❸ 둘러보기 - 영화 열람 기능

- 전체 영화 목록
- 검색한 영화 목록

<br>

❹ 개별 영화 정보

- 영화 제목, 포스터, 장르, 줄거리, 평점 등
- 영화별 리뷰 목록
- 영화 좋아요 (찜)

<br>

❺ 리뷰 작성
- 작성자만 수정, 삭제 가능
- 좋아요 (저장)
- 댓글 작성
- 리뷰 작성자의 홈피로 이동 가능

<br>

❻ 방명록
- 누구나 방명록 작성 가능
- 홈피 주인만 수정, 삭제 가능
- 작성한 리뷰 피드

<br><br>


# 프로젝트 기반

### ⚙ 기술 스택

<img src="https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=Vue.js&logoColor=white">
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">


<br>

### 🔩 프로젝트 활용 도구
<img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white">
<img src="https://img.shields.io/badge/GiTHub-181717?style=for-the-badge&logo=GitHub&logoColor=white">


<br>

### 📋 ERD
![ERD](https://raw.githubusercontent.com/dontk1llme/finalPJT/master/mp3/movieworldERD.png)

<br>


# 기능 구현 🔧


<br/><details>
  <summary>
    <b>GET 요청</b>
  </summary>

  <div markdown="2">
  
|          기능명          |                   URL(Back)                   |                         Action & Mutation                         |
| :----------------------: | :-------------------------------------------: | :---------------------------------------------------------------: |
|      전체 영화 조회      |               `api/v1/movies/`                |                      getMovies / GET_MOVIES                       |
|        영화 상세         |        `api/v1/movies/<int:movie_pk>/`        |                    getOneMovie / GET_ONE_MOVIE                    |
|      영화 리뷰 조회      |    `api/v1/movies/<int:movie_pk>/reviews/`    |                getMovieReview / GET_MOVIE_REVIEWS                 |
|        리뷰 상세         |       `api/v1/reviews/<int:review_pk>/`       |                   getOneReview / GET_ONE_REVIEW                   |
|      리뷰 댓글 조회      |  `api/v1/reviews/<int:review_pk>/comments/`   |       getReviewComment / GET_REVIEW_COMMENTS & NO_COMMENTS        |
|      내 프로필 조회      |          `accounts/user/myprofile/`           |                    getUserInfo / GET_USER_INFO                    |
|      유저 리뷰 조회      |     `api/v1/user/<int:user_pk>/reviews/`      |                      MyReviews / MY_REVIEWS                       |
|   좋아요 한 영화 조회    |  `api/v1/movies/<int:user_pk>/like_movies/`   |                 userLikedMovie / USER_LIKED_MOVIE                 |
|     유저 프로필 조회     |    `accounts/user/<int:user_id>/profile/`     |                     getProfile / GET_PROFILE                      |
| 유저 맞춤 장르 영화 조회 |        `accounts/user/genres_movies/`         |               getMyGenreMovie / GET_MY_GENRE_MOVIE                |
|  맞춤 장르 외 새로운 영화 조회   |       `accounts/user/new_kind_movies/`        |          getNewKindGenreMovie / GET_NEW_KIND_GENRE_MOVIE          |
|     유저 팔로우 조회     | `accounts/user/<int:user_id>/profile/follow/` |                    FirstFollow / FIRST_FOLLOW                     |
| 유저 방명록 조회 | `profiles/<int:user_id>/guestbooks/<int:guestbook_id>/` | fetchGuestbooks

  </div>
</details>
<br/><details>
  <summary>
    <b>POST 요청</b>
  </summary>

  <div markdown="3">
  
|      기능명      |                   URL(Back)                   |         Action & Mutation          |
| :--------------: | :-------------------------------------------: | :--------------------------------: |
|     회원가입     |              `accounts/signup/`               | SignUp / SIGNUP_SAVE_TOKEN & LogIn |
|      로그인      |               `accounts/login/`               |  logIn / LOGIN_SAVE_TOKEN & LogIn  |
|   영화 좋아요    |     `api/v1/movies/<int:movie_pk>/likes/`     |            getMovieLike            |
|      팔로우      | `accounts/user/<int:user_id>/profile/follow/` |          follow / FOLLOW           |
|    댓글 작성     |  `api/v1/reviews/<int:review_pk>/comments/`   |           createComment            |
|   리뷰 좋아요    |    `api/v1/reviews/<int:movie_pk>/likes/`     |           getReviewLike            |
|    리뷰 삭제     |       `api/v1/reviews/<int:review_pk>`        |            DeleteReview            |
|   댓글 좋아요    |   `api/v1/comments/<int:comment_pk>/likes/`   |           getCommentLike           |
|    댓글 삭제     |      `api/v1/comments/<int:comment_pk>/`      |           deleteComment            |
|    댓글 수정     |      `api/v1/comments/<int:comment_pk>/`      |           changeComment            |
|   영화 좋아요    |     `api/v1/movies/<int:movie_pk>/likes/`     |            getMovieLike            |
|    리뷰 생성     |    `api/v1/movies/<int:movie_pk>/reviews/`    |            createReview            |
|    리뷰 수정     |       `api/v1/reviews/<int:review_pk>/`       |            updateReview            |
|   프로필 생성    |          `accounts/user/myprofile/`           |            setUserInfo             |
| 프로필 정보 수정 |          `accounts/user/myprofile/`           |            setUserInfo             |
| 방명록 생성 | `profiles/<int:user_id>/guestbooks/<int:guestbook_id>/` | changeGuestbook |
| 방명록 수정 | `profiles/<int:user_id>/guestbooks/<int:guestbook_id>/` | changeInput |
| 방명록 삭제 | `profiles/<int:user_id>/guestbooks/<int:guestbook_id>/` | deleteGuestbook |
<br>


### 6. 기타 (느낀 점, 후기)