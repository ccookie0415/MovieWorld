<template>
  <div>
    <div class="header news__header">
      <span>My Review</span>
      <span>나의 리뷰</span>
    </div>

    <MyReview/>
  </div>
</template>

<script>
import MyReview from '@/components/MyReview'

export default {
  name: 'MyReviewView',
  components: {
    MyReview,
  },
  data() {
    return {
      updataAva: false,
    }
  },
  methods: {
    getUserReviews() {
      this.$store.dispatch('getUserReviews', this.$store.state.username)
    },
    updateInfo() {
      this.updataAva = true
    }
  },
  created() {
    this.$store.dispatch('MyReviews', this.$route.params.userId)

  },
}
</script>

<style lang="scss" scoped>
.my-movie-wrapper {
  padding: 20px;
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
</style>