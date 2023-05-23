<template>
  <div>
    <div class="header news__header">
      <span>Movie UserRecommend</span>
      <span>영화 추천</span>
    </div>

    <div>
      <UserRecommend/>
      <hr>
      <NewKindRecommend />
    </div>
  </div>
</template>

<script>

import UserRecommend from "@/components/UserRecommend";
import NewKindRecommend from "@/components/NewKindRecommend";


export default {
    name: 'MyRecommendView',
    components:{
      UserRecommend,
      NewKindRecommend,
    },

    created(){
      this.$store.dispatch("getUserInfo");
      this.$store.dispatch("getMyGenreMovie");
      this.$store.dispatch("getNewKindGenreMovie");
    },
};
</script>

<style>

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
