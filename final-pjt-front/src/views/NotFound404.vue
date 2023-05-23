<template>
  <div>
    <h1>404 NOT FOUND</h1>
    <h3>다시 이용해 주세요.</h3>
    <p> 로그인을 했다면? </p>
    <button @click="logOut" class="update-info"><span style="display: block;">로그아웃</span></button>
    <p> 로그인을 안 했다면? </p>
    <button @click="goTo" class="update-info"><span style="display: block;">메인 가기</span></button>
  </div>
</template>

<script>
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'NotFound404',
  components: {
    UpdateUserInfo,
  },
  computed: {
    user(){
      return this.$store.state.user
    },
    userId() {
      return this.$store.state.userId;
    },
  },
  methods: {
    logOut() {
      this.$store.commit("LOGOUT");
      window.localStorage.clear();
      this.$router.push({ name: "home" });

      this.popAva = false;},
    goTo(){
      // const path = `/${this.userId}/main/myhome`;
      const path = '/';
      this.$router.push(path).catch(err => {
        if (err.name !== "NavigationDuplicated") {
          throw err;
        }
      });
      console.log('갓음')
      // location.reload();
      setTimeout(()=>{ // 받아오는건 정상이니까 조금 느리게 받아와서 새고하는 기분
        this.$router.go(0)
        }, 5)
      
      console.log('새고')
    }
  },
  created() {
    this.$store.dispatch('FirstFollow', this.$route.params.userId)
  }
}
</script>

<style>

</style>