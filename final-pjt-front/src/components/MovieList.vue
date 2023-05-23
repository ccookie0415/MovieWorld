// 전부 둘러보기
<template>
  <div class="all-movies">
    <b-card
      v-for="movie in displayedMovies"
      :key="movie.id"
      :img-src="movie.poster_URL"
      img-alt="Image"
      img-top
      img-size
      tag="article"
      class="movie-card"
      @click="goToDetail(movie.id)"
    >
    </b-card>

    <div class="bottom-section">
      <SearchBar @search-movie="searchMovie" class="search-bar" />
      <div class="pagination">
        <button @click="goToPreviousPage" :disabled="currentPage === 1">이전</button>
        <span>{{ currentPage }} / {{ totalPages }}</span>
        <button @click="goToNextPage" :disabled="currentPage === totalPages">다음</button>
      </div>
    </div>
  </div>
</template>

<script>

import SearchBar from "@/components/SearchBar";

export default {
  name: 'MovieList',
  components: {
    SearchBar,
  },
  props: {
    movies: Array,
  },
  data() {
    return {
      currentPage: 1,
      perPage: 6,
    };
  },
  computed: {
    displayedMovies() {
      const startIndex = (this.currentPage - 1) * this.perPage;
      const endIndex = startIndex + this.perPage;
      return this.movies.slice(startIndex, endIndex);
    },
    totalPages() {
      return Math.ceil(this.movies.length / this.perPage);
    },
  },
  methods: {
    goToDetail(id) {
      this.$router.push({ name: 'movie_detail', params: { movie_id: id } })
        .then(() => window.scrollTo(0, 0));
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
    searchMovie(keyword) {
      this.$emit("search-movie", keyword); //여기추가햇음!
      const movies = this.movies.filter((movie) => {
        return movie.title.includes(keyword);
      });
      if (movies) {
        this.movieList = movies;
        this.searchYes = true;
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  // margin-top: 1rem;
}

.pagination button {
  font-size: 14px;
  padding: 0.5rem 1rem;
  margin: 0 0.3rem;
  background-color: #55b2d4;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  // z-index: 1;
}

.pagination button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.pagination span {
  font-size: 14px;
}


.bottom-section {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

// .movie-card {
//   display: inline-block;
//   width: 150px; /* 카드의 너비 조정 */
//   height: 200px; /* 카드의 높이 조정 */
//   margin: 10px;
//   cursor: pointer;
// }

// .movie-card>img {
//   height: 100%;
// }

.movie-card {
  display: inline-block;
  width: 120px; /* 원하는 너비로 조정 */
  height: 160px; /* 원하는 높이로 조정 */
  margin: 10px;
  cursor: pointer;
  // z-index: 2;
}

.card-body {
    flex: 1 1 auto;
    padding: 0px !important;
    color: var(--bs-card-color);
}

.movie-card > img {
  height: 100%;
}


</style>