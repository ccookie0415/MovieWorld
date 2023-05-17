### 0519 

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