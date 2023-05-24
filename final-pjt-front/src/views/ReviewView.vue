<template>
  <div>
    <div>
      <!-- <h2> REVIEW </h2> -->
      <!-- <h2 @click="moveToMovie(movie.id)">{{ this.$store.state.movie.title }}</h2> -->
      <h2 @click="moveToMovie(review.movie)">{{ title }}</h2>
    </div>
    <div class="review">
      <div class="title">
        <h1>{{ review.title }}</h1>

        <span @click="likeUnlike">
          <font-awesome-icon icon="fa-solid fa-heart" class="heart" v-show="is_liked"/>
          <font-awesome-icon icon="fa-regular fa-heart" class="heart" v-show="!is_liked"/>
        </span>
        <span>{{ like_users_count }} 명이 좋아합니다</span>

        <div class="back-to-movie">
          <div>
            <p><span class="name">작성자</span>
              <!-- <router-link :to="`/${review.user}/main/myhome`" class="value">{{ review.username }}</router-link> -->
              <a class="value" @click="redirectToUserHome">{{ review.username }}</a>
            </p>
          </div>
        </div>

        <span class="day-name">작성일</span><span class="day">{{ review?.created_at.substr(0, 10) }}</span>
        <span class="day-name">수정일</span><span class="day">{{ review?.updated_at.substr(0, 10) }}</span>
        
        <br>

        <!-- 버튼 리뷰 작성자에게만 보임 -->
        <button
          v-show="this.$store.state.userId === review.user" 
          @click="updateReview"
          class="update"
        >리뷰 수정</button>
        <ReviewUpdate v-show="popAva" @pop-exit="popExit" :review="review"/>

        <button 
          v-show="this.$store.state.userId === review.user" 
          @click="popAlert"
        >리뷰 삭제</button><br>
        <div v-show="alert" class="alert alert-danger" role="alert">
          정말 삭제하시겠습니까?<br>
          <button @click="noDelete" class="no">아니요</button>
          <button @click="DeleteReview(review.id, review.movie)">네</button>
        </div>

        <hr>
      </div>
      <div class="content">
        <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
        <h4>{{ review.content }}</h4>
      </div>


      <div class="comment-create">
        <hr>
        <p v-if="this.$store.state.reviewComments.length !== 0">{{ this.$store.state.reviewComments.length }}개의 댓글이 있습니다.</p>
        <p v-else>댓글이 아직 없습니다.</p>
        <form @submit.prevent="createComment">
          <input type="text" v-model.trim="comment" maxlength="50">
          <input type="submit" value="작성">
        </form>
      </div>
      <CommentList />
    </div>
    <!-- <p>이 영화의 다른 리뷰 보기 (시간있으면 하겠음)</p>
    <div v-for="review in otherReview" :key="review.id">
      {{ review.title }}
    </div> -->
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import ReviewUpdate from '@/components/ReviewUpdate.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewView',
  components: {
    CommentList,
    ReviewUpdate,
  },
  computed: {
    movie(){
      return this.$store.state.movie
    },
    review() {
      return this.$store.state.review
    },
    otherReview() {
      return this.$store.state.movieReviews
    },
    is_liked() {
      if (this.$store.state.review.like_users.indexOf(this.$store.state.userId) === -1) {
        return false
      } else {
        return true
      }
    },
    like_users_count() {
      return this.$store.state.review.like_users.length
    },
    
  },
  data() {
    return {
      comment: null,
      alert: false,
      popAva: false,
      title: null,
    }
  },
  methods: {
    moveToMovie(movieId) {
      this.$router.push({ name: 'movie_detail', params: { movie_id: movieId } });
    },
    getOneReview(reviewId) {
      this.$store.dispatch("getOneReview", reviewId)
    },
    getMovieReview(movie_id) {
      this.$store.dispatch("getMovieReview", movie_id)
    },
    getReviewComment(reviewId) {
      this.$store.dispatch("getReviewComment", reviewId)
    },  
    createComment() {
      const content = this.comment
      const reviewPk = this.$route.params.review_id

      if (!content) {
        alert('내용을 입력하세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${reviewPk}/comments/`,
        headers: {
          'Authorization' : `Token ${this.$store.state.token}`
        },
        data: {content: content},
      })
        .then((response) => {
          this.getReviewComment(this.$route.params.review_id)
        })
        .catch((error) => {
          console.log(error)
        })
      this.comment = null
    },
    getReviewLike(movie_id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${movie_id}/likes/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.is_liked = response.data.is_liked
          this.like_users_count = response.data.like_users_count
          this.$store.dispatch('getOneReview', this.$route.params.review_id)
        })
        .catch((error) => {
          console.log(error)
        })
      },
    likeUnlike() {
      this.getReviewLike(this.$route.params.review_id)
    },
    popAlert() {
      this.alert = true
    },
    noDelete() {
      this.alert = false
    },
    DeleteReview(review_id, movie_id) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/reviews/${review_id}`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.$router.push({name: 'movie_detail', params: {movie_id: movie_id}})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateReview() {
      this.popAva = true
    },
    popExit() {
      this.popAva = false
    },
    redirectToUserHome() {
      const path = `/${this.review.user}/main/myhome`;
      this.$router.push(path).catch(err => {
        if (err.name !== "NavigationDuplicated") {
          throw err;
        }
      });
      this.$router.go(0)
    },
    getMovieTitle(rmovie) { //rmovie = review.movie -> id
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${rmovie}`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.title =  response.data.title
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
  created() {
    this.getOneReview(this.$route.params.review_id)
    this.getMovieReview(this.review.movie)
    // this.getReviewComment(this.$route.params.review_id)
    // this.$store.dispatch('getReviewComment', this.$route.params.review_id)
    this.$store.dispatch('FirstFollow', this.$route.params.userId)
    setTimeout(()=>{ // 받아오는건 정상이니까 조금 느리게 받아와서 새고하는 기분
      this.getMovieTitle(this.review.movie)
        }, 50)
  },
}
</script>

<style scoped>

body {
  display: flex;
  justify-content: center;
  
}

hr {
  margin-top: 0; 
  width: 450px;
}
h2 {
  color: rgb(0, 0, 0);
  text-shadow: 1px 1px #908581;
  font-size: 20px;

  display: inline-block;
  text-align: center;

  padding-bottom: 10px;
  margin-bottom: 10px;
  border-bottom: 1px solid black;
}

.review {
  display: inline-block;
  position: relative;
  text-align: left;
  width: 450px;
  height: 450px;
  /* border: 2px solid rgb(203, 120, 134); */
  /* border-top-left-radius: 30px; */
  /* border-bottom-right-radius: 30px; */
  /* box-shadow: 1px 1px 3px 3px rgb(136, 136, 136); */
  /* padding: 20px; */
  /* margin-bottom: 50px; */
}

span {
  font-size: 14px;
  /* margin-left: 5px; */
  margin-right: 10px;
}

a {
  color: black;
  text-decoration: none;
}

button {
  border: 0px;
  background-color: transparent;
  color: red;
  padding: 0;
  font-size: 15px;
  margin-top: 10px;
  margin-bottom: 5px;
  margin-right: 20px;
  /* font-weight: bold; */
}

.update {
  color: rgb(58, 58, 248);
}

.heart {
  color: rgb(208, 93, 93);
  font-size: 150%;
}

/* BACK 버튼 */
.back-to-movie {
  display: flex;
  justify-content: space-between;
  vertical-align: middle;
  margin: 0;
}

.back-to-movie > a {
  display: inline-block;
  height: 32px;
  background-color: #E6E6E6;
  /* border: 1px solid gray; */
  border-radius: 10px;
  padding: 5px 10px;
  font-size: 15px;
}
.back-to-movie > a:hover {
  color: black;
  font-weight: bold;
}

.back-to-movie > div > p {
  font-size: 20px;
  margin: 0;
}
.no {
  color: blue
}

.title {
  display: inline-block;
  height: 100px;
  width: 450px;
  text-align: left;
  margin-left: 5px;
  margin-right: 5px;
  margin-bottom: 50px;
}


/* 리뷰제목 */
.title > h1 {
  margin-bottom: 15px;
  /* margin-bottom: 30px; */
  font-size: 25px;
  text-shadow: 2px 2px  #746a6a61;
}

.title > p {
  font-size: 20px;
  /* margin-top: 5px;
  margin-bottom: 5px; */
  margin: 0;
}
.content {
  display: inline-block;
  width: 90%;
  margin-left: 5px;
  margin-right: 5px;

}

.content > img {
  max-width: 100px;
  max-height: 100px; 

}

.content > h4 {
  display: inline-block;
  vertical-align: top;
  margin-left: 15px;
  margin-right: 15px;
  margin-top: 10px;
  font-size: 20px;
}


.comment-create {
  display: inline-block;
  width: 90%;
  text-align: left;
  margin-left: 5px;
  margin-right: 5px;
  margin-bottom: 20px;
  margin-top: 30px;
}



.comment-create > p {
  font-size:14px;
}

.comment-create > form {
  display: flex;
}
.comment-create > form > input[type='text'] {
  width: 450px;
  height: 35px;
  border-radius: 10px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  
}

.comment-create > form > input[type='submit'] {
  color: black;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 40%;
  padding-right: 10px;
  width: 45px;
  height: 35px;
  text-decoration: none;
  background-color: 55b2d4;
}

.name {
  display: inline-block;
  width: 50px;
  text-align: left;
  font-size: 16px;
  font-weight: 600;
}

.value {
  font-size: 16px;
  background-color: #55b2d467;
  border-radius: 10px;
  padding-left: 10px;
  padding-right: 10px;
}

.value:hover {
  color: rgb(73, 44, 44);
  font-weight: bold;
}

.day-name {
  display: inline-block;
  width: 50px;
  text-align: left;
  font-size: 14px;
  font-weight: 600;
}

.day {
  margin-right: 50px;
  font-size: 14px;
}

</style>