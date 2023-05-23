<template>
  <div class="all-movies">
    <b-card
      v-for="review in displayedreviews"
      :key="review.id"
      :img-src="`http://127.0.0.1:8000${review?.img}`"
      img-alt="Image"
      img-top
      img-size
      class="review-card"
      @click="moveToReview(review.id)"
    >
    </b-card>
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
  name: 'MyReview',

  data() {
    return {
      currentPage: 1,
      perPage: 6,
    };
  },

  computed: {
    reviews() {
      return this.$store.state.myReviews;
    },

    displayedreviews() {
      const itemsPerRow = 3;
      const itemsPerPage = itemsPerRow * 2;
      const startIndex = (this.currentPage - 1) * itemsPerPage;
      const endIndex = startIndex + itemsPerPage;
      return this.reviews.slice(startIndex, endIndex);
    },

    totalPages() {
      return Math.ceil(this.reviews.length / 6);
    },
  },

  methods: {
    moveToReview(reviewId) {
      this.$router.push({ name: 'review_detail', params: { review_id: reviewId } });
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

.review-card {
  display: inline-block;
  width: 120px; /* 원하는 너비로 조정 */
  height: 160px; /* 원하는 높이로 조정 */
  margin: 10px;
  cursor: pointer;
}

.review-card > img {
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

