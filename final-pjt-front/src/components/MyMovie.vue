<template>

    <!-- <p v-if="movies.length === 0 && $route.params.userId === $store.state.userId">좋아하는 영화를 저장해보세요</p>
    <p v-else-if="movies.length === 0">아직 저장한 영화가 없습니다.</p> -->

    <div class="all-movies">
      <b-card
        v-for="movie in displayedMovies"
        :key="movie.id"
        :img-src="movie.poster_URL"
        img-alt="Image"
        img-top
        img-size
        class="movie-card"
        @click="moveToMovie(movie.id)"
      >
      </b-card>
      
      <!-- <div v-for="i in emptyCardCount" :key="`empty-${i}`" class="empty-card"></div> -->
    <div class="pagination">
      <div class="pagination-buttons">
      <button @click="goToPreviousPage" :disabled="currentPage === 1">이전</button>
      <span>{{ currentPage }} / {{ totalPages }}</span>
      <button @click="goToNextPage" :disabled="currentPage === totalPages">다음</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MyMovie',
  data() {
    return {
      currentPage: 1,
      perPage: 6,
    };
  },
  computed: {
    movies() {
      return this.$store.state.likedMovies;
    },
    displayedMovies() {
      const itemsPerRow = 3;
      const itemsPerPage = itemsPerRow * 2;
      const startIndex = (this.currentPage - 1) * itemsPerPage;
      const endIndex = startIndex + itemsPerPage;
      return this.movies.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.movies.length / 6);
    },
    // emptyCardCount() {
    //   const itemsPerRow = 3;
    //   const itemsPerPage = itemsPerRow * 2;
    //   return itemsPerPage - this.displayedMovies.length;
    // },
  },
  methods: {
    moveToMovie(movieId) {
      this.$router.push({ name: 'movie_detail', params: { movie_id: movieId } });
    },
    goToPreviousPage() {
      if (this.currentPage > 1) {
        this.currentPage--;
      }
    },
    goToNextPage() {
      if (this.currentPage < this.totalPages) {
        this.currentPage++;
      }
    },
  },
};
</script>

<style scoped>

.movie-card {
  display: inline-block;
  width: 120px; /* 원하는 너비로 조정 */
  height: 160px; /* 원하는 높이로 조정 */
  margin: 10px;
  cursor: pointer;
}

.movie-card > img {
  height: 100%;
}

.pagination-buttons {
  display: flex;
  align-items: center;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1rem;
}

.pagination button {
  font-size: 14px;
  padding: 0.5rem 1rem;
  margin: 0 0.3rem;
  background-color: #55b2d4;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.pagination button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination span {
  font-size: 14px;
}
</style>