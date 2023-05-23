<template>
  <div>
    <div class="header news__header">
      <span>My Movie</span>
      <span>내가 찜한 영화</span>
    </div>

    <MyMovie/>
  </div>
</template>

<script>
import MyMovie from '@/components/MyMovie'

export default {
  name: 'MyZzimView',
  components: {
    MyMovie,
  },
  data() {
    return {
      updataAva: false,
    }
  },
  methods: {
    updateInfo() {
      this.updataAva = true
    }
  },
  created() {
    this.$store.dispatch('userLikedMovie', this.$route.params.userId)

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