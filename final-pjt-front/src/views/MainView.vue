<template>
<div id="app">
    <div class="background">
      <div class="outerbox">
        <div class="wrapper">
          <div class="wrapper__left">
            <MainUserInfo/>
          </div>
          <div class="wrapper__right">
            <div class="wrapper__right__header">
              <span class="wrapper__header__main"> 🎥 사이좋은 영화들, 무비월드</span>
              <div class="wrapper__header__title" >
                <!-- y2k -->
                <span @click="play('https://raw.githubusercontent.com/dontk1llme/finalPJT/master/mp3/bgm.mp3')">BGM⏯</span> 
              </div>
            </div>
            <div class="wrapper__right__body">
              <!-- 여기가 오른쪽 박스 -->
                <router-view></router-view>

            </div>
          </div>
          <div class="nav">
            <!-- @click="" -->
            
            <!-- <router-link  :to="{name:'my_home'}"  style="text-decoration: none;">
              <div class="nav__selection" :class="{ 'selected': selectedPage === 1 }" @click="changepage(1)"> 홈 </div>
            </router-link>-->
            <a class="" @click="goHome" style="text-decoration: none;">
              <div class="nav__selection" :class="{ 'selected': selectedPage === 1 }" @click="changepage(1)"> 홈 </div>
            </a>

            <router-link  :to="{name:'movie_zzim_list'}"  style="text-decoration: none;">
              <div class="nav__selection" :class="{ 'selected': selectedPage === 2 }" @click="changepage(2)"> 찜 </div>
            </router-link>

            <router-link  :to="{name:'my_review'}"  style="text-decoration: none;">
              <div class="nav__selection" :class="{ 'selected': selectedPage === 3 }" @click="changepage(3)">리뷰</div>
            </router-link>

            <router-link  :to="{name:'guest_book'}"  style="text-decoration: none;">
              <div class="nav__selection" :class="{ 'selected': selectedPage === 4 }" @click="changepage(4)">방명록</div>
            </router-link>
            <div v-if="user.id === this.$store.state.userId" >
              <router-link  :to="{name:'movie_recommend_list'}"  style="text-decoration: none;">
                <div class="nav__selection" :class="{ 'selected': selectedPage === 5 }" @click="changepage(5)">추천</div>
              </router-link>

              <router-link  :to="{name:'movie_list'}"  style="text-decoration: none;">
                <div class="nav__selection" :class="{ 'selected': selectedPage === 6 }" @click="changepage(6)">둘러보기</div>
            </router-link>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import MainUserInfo from '@/components/MainUserInfo'

// import axios from 'axios'

export default {
  name: "MainView",
  components: {
    MainUserInfo,
  },
  data() {
    return {
      selectedPage: null,
      playBgm: true,
      audio:null,
    }
  },
  computed: {
    user(){
      return this.$store.state.user
    },
  },
  methods: {
    changepage(page) {
      this.selectedPage = page;
     },
    play(sound) {
      if (sound) {
        if (this.audio && !this.audio.paused) { // 이미 재생 중인 경우
          this.audio.pause();
          this.playBgm = false;
        } else {
          if (this.audio) {
            this.audio.currentTime = 0; // 이전 위치에서 재생할 수 있도록 현재 재생 위치를 초기화합니다.
          } else {
            this.audio = new Audio(sound);
          }
          this.audio.play();
          this.playBgm = true;
        }
      } else {
        if (this.audio) {
          this.audio.pause();
          this.playBgm = false;
        }
      }
    },
    goHome(){ //새로고침할일없으면 없애고 다시 원래 라우터로 ㄱㄱ
      this.$router.push({ name: 'my_home' })
      setTimeout(()=>{ // 받아오는건 정상이니까 조금 느리게 받아와서 새고하는 기분
        this.$router.go(0)
        }, 10)
    }
  },
  created() {
    this.$store.dispatch("getUserInfo"); //이거지우면프로필자살함제발지우지마
  },
};
</script>

<style>
* {
    box-sizing: border-box;
}



.background {
    width: 1024px;
    height: 600px;
    background-image: url("../assets/back.PNG");
    padding: 20px 0px 0px 20px;
}

.outerbox {
    background-image: url("../assets/outerbox.png");
    width: 808px;
    height: 544px;
}

.wrapper {
    padding: 32px 0px 0px 32px;
    display: flex;
}

.wrapper__left {
    width: 208px;
    height: 472px;
    padding: 0px 0px 25px 0px;

}

.wrapper__right {
    width: 524px;
    height: 472px;
    padding: 0px 0px 25px 0px;
}

.wrapper__left__header {
    color: #A5D1E1;
    font-size: 7px;
    width: 100%;
    height: 30px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.wrapper__left__body {
    border: 1px solid black;
    border-radius: 20px;
    width: 100%;
    height: 447px;
    background-color: white;
    padding: 15px 30px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.body__head__color {
    width: 150px;
    height: 150px;
    background-color: #C4C4C4;
}


.left__body__lists {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    font-size: 10px;
    margin-bottom: 25px;
    text-align: center; /* 가운데 정렬 */
    white-space: nowrap; /* 줄 바꿈 방지 */
}

.lists__list {
    margin-bottom: 10px;
}

.left__body__footer {
    width: 100%;
}

.footer__title {
    margin-bottom: 10px;
    color: gray;
    font-size: 12px;
}

.footer__selection {
    width: 100%;
    color: gray;
    padding: 2px;
}

.wrapper__right__header {
    height: 30px;
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    color: #55B2D4;
    padding-bottom: 10px;

}

.wrapper__header__main {
    padding-left: 30px;
    font-weight: 600;
}

.wrapper__header__title {
    font-size: 12px;
}

.wrapper__right__body {
    width: 100%;
    height: 100%;
    border: 1px solid black;
    border-radius: 20px;
    margin-left: 3px;
    padding: 10px 30px;
    background-color: white;
    overflow: auto; /* 스크롤 생성 */
}


.nav {
    width: 60px; /* 넓이를 조정해주세요 */
    height: 190px; /* 높이를 조정해주세요 */
    display: flex;
    flex-direction: column;
    /* justify-content: space-between; */
    justify-content: stretch;
    position: absolute;
    left: 787px;
    top: 100px;
}

.nav__selection {
    background-color: #55B2D4;
    border: 1px solid #4d9fbd;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 30px;
    font-size: 13px;
    cursor: pointer;
    color: white;
}

.nav__selection.selected {
    background-color: white;
    color: black;
}


</style>