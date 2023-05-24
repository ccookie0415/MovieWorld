<template>
  <div>
    <div class="wrapper__body__news">
      <div class="header news__header">
        <span>Updated news</span>
        <span>TODAY STORY</span>
      </div>
      <div class="news__main">
        <div class="news__main__left">
          <div v-if="myReviews.length != 0">
            <div class="content news__content"  v-if="myReviews[0]">
              <span> review  </span>
              <span>{{ myReviews[0].title }}</span>
            </div>
            <div class="content news__content" v-if="myReviews[1]">
              <span> review  </span>
              <span >{{ myReviews[1].title }}</span>
            </div>
          </div>
          <div v-else>
            <span> 리뷰 작성 기다리는 중 . . . </span>
          </div>
          
        </div>
        <div class="news__main__right">
          <div class="content news__content">
            <span> new ▷  </span>
            <span>찜한 영화 {{myMovies.length}}개 </span>
          </div>
          <div class="content news__content">
            <span> new ▷ </span>
            <span> 작성한 리뷰 {{myReviews.length}}개 </span>
          </div>

        </div>
      </div>
    </div>
    <div class="wrapper__body__video">
      <div class="header">
        <span>My Video</span>
        <span>INTRODUCE YOURSELF</span>

        <!-- <div class="button-wrapper">
          <button @click="updateYtb" class="update-info"><span style="display: block;">영상 수정</span></button>
          <UpdateUserYoutube :user="user" v-show="updateAva" @pop-exit="popExit"/>
        </div> -->
      </div>
      <div class="video__main">
        <iframe width="100%" height="100%" :src="user.ytb" frameborder="0" allowfullscreen></iframe>
      </div>
    </div>
  </div>
</template>


<script>
// import UpdateUserYoutube from '@/components/UpdateUserYoutube'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MyHomeView',
  components: {
    // UpdateUserYoutube,
  },
  data(){
    return {
      updateAva: false,
      popAva: false,
    }
  },
  computed: {
    user(){
      return this.$store.state.user
    },
    myMovies() {
      return this.$store.state.likedMovies;
    },
    myReviews() {
      return this.$store.state.myReviews;
    },
  },
  methods:{
    updateYtb() {
      this.updateAva = !this.updateAva
    },
    popExit() {
      this.updateAva = false
    },
  },
  created(){
    this.$store.dispatch('userLikedMovie', this.$route.params.userId)
    this.$store.dispatch('MyReviews', this.$route.params.userId)
    this.$store.dispatch("getUserInfo");
  }
}
</script>

<style>
.wrapper__body__news {
  height: 150px;
}

.header {
  display: flex;
  align-items: flex-end;
  padding-bottom: 10px;
}

.news__header {
  border-bottom: 1.5px solid rgba(0, 0, 0, 0.5);
}

.header span:first-child {
  font-size: 15px;
  margin-right: 5px;
  font-weight: 600;
  color: #55B2D4;
}

.header span:last-child {
  font-size: 6px;
  font-weight: 600;
}

.content {
  display: flex;
  align-items: flex-end;
  padding-bottom: 10px;
}

.news__content {
  border-bottom: 1.5px solid rgba(156, 156, 156, 0.5);
}

.content span:first-child {
  font-size: 6px;
  
  margin-right: 5px;
  margin-top: 5px;
  font-weight: 600;
  color: #55B2D4;
}

.content span:last-child {
  font-size: 12px;
  font-weight: 600;
}


.news__main {
  display: flex;
  height: 130px;
}

.news__main__left,
.news__main__right {
  flex: 1;
  padding: 0 10px;
  font-size: 12px;
  color: gray;
}

.wrapper__body__video {
  height: 260px;
}

.video__main {
  height: 80%;
  background-color: #C4C4C4;
}
</style>
