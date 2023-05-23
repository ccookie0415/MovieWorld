<template>
  <div class="recommend">
    <h5>{{ this.$store.state.nickname }}님의 취향인 장르의 영화</h5>

    <div class="all-movie">
      <button @click="toBefore">
        <font-awesome-icon icon="fa-solid fa-chevron-left" />
      </button>
      <transition-group name="fade">
        <div class="movie" v-for="movie in myGenreMovies" :key="movie.id">
          <div class="poster-wrapper">
            <img
              @click="goToDetail(movie.id)"
              :src="movie.poster_URL"
              alt=""
              class="poster-image animate__animated animate__fadeIn"
            />
          </div>
        </div>
      </transition-group>
      <button @click="toNext">
        <font-awesome-icon icon="fa-solid fa-chevron-right" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "UserRecommend",
  computed: {
    myGenreMovies() {
      return this.$store.state.myGenreMovies.slice(this.num, this.num + 3);
    },
  },
  data() {
    return {
      showLink: true,
      num: 0,
    };
  },
  methods: {
    toBefore() {
      if (this.num > 0) {
        this.num = this.num - 1;
      }
    },
    toNext() {
      if (this.num < this.$store.state.myGenreMovies.length - 3) {
        this.num = this.num + 1;
      }
    },
    goToDetail(id) {
      this.$router.push({ name: "movie_detail", params: { movie_id: id } });
    },
  },
};
</script>

<style scoped>

button {
  background-color: #55b2d4;
  border: none;
  border-radius: 4px;
  color: #e6e6e6
}

.movie {
  display: inline-block;
  width: 20%;
  position: relative;
  text-align: left;
  padding: 0;
  margin: 2px;
}

.poster-wrapper {
  width: 100%;
  padding-bottom: 150%;
  position: relative;
}

.poster-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border: 2px solid #e6e6e6;
  border-radius: 10px;
  object-fit: cover;
  box-shadow: 2px 2px 5px 0px rgb(44, 44, 44);
  transition: transform 0.4s;
}

.poster-image:hover {
  transform: scale(1.1);
  z-index: 1 !important;
}
</style>