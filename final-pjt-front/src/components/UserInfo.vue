<template>
  <div>
    <div class="wrapper__left__header">
        <!-- 회원 정보 수정은 나만 가능 -->
      <span v-if="user.id === this.$store.state.userId" class="button-group">
        <div class="button-wrapper">
          <button @click="updateInfo" class="update-info"><span style="display: block;">홈/회원 정보 수정</span></button>
          <UpdateUserInfo :user="user" v-show="updateAva" @pop-exit="popExit"/>
        </div>
        <div class="button-wrapper">
          <button @click="logOut" class="update-info"><span style="display: block;">로그아웃</span></button>
        </div>
      </span>

      <span v-else class="button-group">
        <div class="button-wrapper">
          <button @click="follow" class="follow" v-show="!is_followed">일촌 추가</button>
          <button @click="follow" class="following" v-show="is_followed">일촌 취소</button>
        </div>
        <div class="button-wrapper">
          <button @click="goToMy" class="update-info"><span style="display: block;">내 홈 가기</span></button>
        </div>
      </span>
    </div>

    <div class="wrapper__left__body">
        <div class="left__body__head">
        <img class="profile__img" :src="`http://127.0.0.1:8000${user.img}`" alt="#">
        </div>
        <div class="left__body__lists">
            <h4>{{ user?.nick_name }}</h4>
            <p v-if="user.self_introduction !== 'null'"> {{ user?.self_introduction }}</p>
        
        </div>
        <div class="left__body__footer">
        <div class="footer__title">오늘의 기분</div>
        <select class="footer__selection">
            <option>기쁨 😊</option>
            <option>슬픔 😢</option>
            <option>화남 😠</option>
            <option>분노 😡</option>
        </select>
        </div>
        
        <div class="today">
          <span> 내가 추가한 일촌 {{ followings }} </span>
          <br>
          <span> 나를 추가한 일촌 {{ followers }}  </span>
        </div>
        <!-- 강제 맞팔... -->
        
    </div>
  </div>
</template>

<script>
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'MainUserInfo',
  components: {
    UpdateUserInfo,
  },
  computed: { //읽기 전용
    user(){
      return this.$store.state.user
    },
    userId() {
      return this.$store.state.userId;
    },
    is_followed() {
      return this.$store.state.is_followed
    },
    followers() {
      return this.$store.state.followers
    },
    followings() {
      return this.$store.state.followings
    },
  },
  data(){
    return {
      updateAva: false,
      popAva: false,
    }
  },
  methods: {
    follow() {
      this.$store.dispatch('follow', this.$route.params.userId)
    },
    updateInfo() {
      this.updateAva = !this.updateAva
    },
    popExit() {
      this.updateAva = false
    },
    logOut() {
      this.$store.commit("LOGOUT");
      window.localStorage.clear();
      this.$router.push({ name: "home" });

      this.popAva = false;},
    goToMy(){
      const path = `/${this.userId}/main/myhome`;
      this.$router.push(path).catch(err => {
        if (err.name !== "NavigationDuplicated") {
          throw err;
        }
      });
      console.log('갓음')
      // location.reload();
      setTimeout(()=>{ // 받아오는건 정상이니까 조금 느리게 받아와서 새고하는 기분
        this.$router.go(0)
        }, 5)
      
      console.log('새고')
    }
  },
  created() {
    this.$store.dispatch('FirstFollow', this.$route.params.userId)
  }
}
</script>

<style lang="scss" scoped>

.profile__img{
    width:170px;
    height: 170px;
}

.today{
  margin-top:10px;
  color:rgb(121, 192, 233);
  font-size:13px;
}

p{
  font-size:15px;
  display: inline-block;
  text-align: center;
  
}

.button-group {
  display: flex;
  flex-direction: row;
}

.button-wrapper {
  margin-right: 10px;
}

button {
  width:150px;
  height: 20px;
  background-color: #E6E6E6;
  border: 1px solid #908581;
  border-radius: 10px;
  margin-top:11px;
  margin-bottom:4px;
  padding-left: 4vw;
  padding-right: 4vw;
  padding-top: 0.5vw;
  padding-bottom: 0.5vw;
  text-align: center; /* 가운데 정렬 */
  white-space: nowrap; /* 줄 바꿈 방지 */
}

button.update-info {
  width: auto; /* 버튼 너비 자동 조정 */
  height: auto; /* 버튼 높이 자동 조정 */
  padding: 0; /* 내부 여백 제거 */
  display: flex; /* 텍스트 가운데 정렬을 위해 Flexbox 사용 */
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  // background-color: transparent; /* 배경색 투명으로 설정 */
  border: none; /* 테두리 제거 */
  cursor: pointer;
}

button.follow {
  width: auto; /* 버튼 너비 자동 조정 */
  height: auto; /* 버튼 높이 자동 조정 */
  padding: 0; /* 내부 여백 제거 */
  display: flex; /* 텍스트 가운데 정렬을 위해 Flexbox 사용 */
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  // background-color: transparent; /* 배경색 투명으로 설정 */
  border: none; /* 테두리 제거 */
  cursor: pointer;
}

button.following {
  width: auto; /* 버튼 너비 자동 조정 */
  height: auto; /* 버튼 높이 자동 조정 */
  padding: 0; /* 내부 여백 제거 */
  display: flex; /* 텍스트 가운데 정렬을 위해 Flexbox 사용 */
  justify-content: center; /* 가로 중앙 정렬 */
  align-items: center; /* 세로 중앙 정렬 */
  // background-color: transparent; /* 배경색 투명으로 설정 */
  border: none; /* 테두리 제거 */
  cursor: pointer;
}
</style>