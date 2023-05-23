<template>
  <div>
    <UserInfo/>

  </div>
</template>



<script>
import UserInfo from '@/components/UserInfo'

export default {
  name: 'ProfileView',
  components: {
    UserInfo,
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
    this.$store.dispatch('getProfile', this.$route.params.userId)
  },
}
</script>

<style lang="scss" scoped>



.storage {
  position: relative;
  display: flex;
  bottom: 100px;
  width: 70%;
  margin-top: 15%;
  margin-left: 15%;
  // margin-right: 15%;
  padding-bottom: 10vh;
  background-color: rgb(221, 221, 221);
  border: none;
  box-shadow: 1px 1px 1px 1px rgb(196, 196, 196);
  /* height: 80%; */
}

/* i태그 */
svg {
  text-decoration: none;
  color: black;
  text-shadow: 2px 2px gray;
}

span {
  font-size: 1.5vw;
  padding-left: 1.5vw;
  padding-right: 1.5vw;
  color: black;
}


</style>