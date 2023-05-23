<template>
  <div class="home">
    <div class="box">
      <LogIn class="animate__animated animate__fadeIn" v-show="!this.$store.state.username"/>
    </div>
    <SetProfile v-show="this.$store.state.token && !this.$store.state.userId"/>
    <!-- <SetProfile /> -->
  </div>
</template>


<script>
import LogIn from "@/components/LogIn";
import SetProfile from "@/components/SetProfile";
import _ from 'lodash'

export default {
  name: "HomeView",
  components: {
    LogIn,
    SetProfile,
  },
  data() {
    return {
      popLogin: false,
    };
  },
  computed: {
    famousLine() {
      return _.sample(famousLines)
    }
  },
  methods: {
    popDiv() {
      this.popLogin = true;
    },
    goToHome() {
      this.$router.push({ name : 'main'})
    }
  },
};
</script>



<style scoped>
@import url(https://fonts.googleapis.com/css?family=Lato:300);
@import url('https://webfontworld.github.io/Rebecca/Rebecca.css');

h5 {
  font-family: 'Rebecca';
  color: #58504e;
  text-shadow: 1px 1px  #F0E2D7;
}

.home {
  position: relative;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  vertical-align: center;
  padding-top: 20px;
}

/* .box {
  display: inline-block;
  position: relative;
  margin-top: 60px;
  height: 90vh;
  width: 800px;
} */
.box {
  display: inline-block;
  /* position: absolute; */
  /* justify-content: center; */
  width: 80%;
  margin-top: 0px;
}

img {
  padding: 0;
  width: 80%;
}

.home > div > h1 {
  font-size: 8vw;
  z-index: 3;
  position: absolute;
  display: inline-block;
  font-family: Harmond;
  margin: 0;
  /* background-color: black; */
  width: 10vw;
}

.movie {
  top: 12vh;
  left: 21vw;
  color: #E6C628;
  text-shadow: 3px 3px #764E03;
  animation-name: fadeOut;
  animation-duration: 2.5s;
  animation-delay: 2s;
  animation-fill-mode: forwards;
}

.memory {
  top: 21vh;
  left: 30vw;
  color: #764E03;
  text-shadow: 3px 3px #E6C628;
  animation-name: fadeOut;
  animation-duration: 2.5s;
  animation-delay: 2s;
  animation-fill-mode: forwards;
}

.m1 {
  top: 12vh;
  left: 21vw;
  color: #E6C628;
  text-shadow: 3px 3px #764E03;
  /* transform: translate(30vw, 2vh); */
  animation-name: example;
  animation-duration: 2.5s;
  animation-delay: 2s;
  animation-fill-mode: forwards;
}

@keyframes example {
  0%   {left:21vw; top:12vh; font-size: 8vw}
  100% {left:35vw; top:13vh;  font-size: 11vw}
}

.m2 {
  top: 21vh;
  left: 47vw;
  color: #764E03;
  text-shadow: 3px 3px #E6C628;
  animation-name: example2;
  animation-duration: 2.5s;
  animation-delay: 2s;
  animation-fill-mode: forwards;
}

@keyframes example2 {
  0%   {left:47vw; top:21vh; font-size: 8vw}
  100% {left:49vw; top:12.7vh; font-size: 11vw}
}


.loader{
  position: absolute;
  width: 64%;
  height: 30px;
  left: 18%;
  background-color: rgba(255,255,255,0.2);
}

.loader:before{
  content: "";
  position: absolute;
  background-color: #fff;
  top: 0px;
  left: 0;
  height: 30px;
  width: 0px;
  z-index: 0;
  opacity: 1;
  -webkit-transform-origin:  100% 0%;
      transform-origin:  100% 0% ;
  -webkit-animation: loader 10s ease-in-out forwards;
      animation: loader 10s ease-in-out forwards;
}

.loader:after{
  content: "LOADING ...";
  color: #fff;
  font-family:  Lato,"Helvetica Neue" ;
  font-weight: 200;
  font-size: 20px;
  position: absolute;
  width: 100%;
  height: 30px;
  line-height: 30px;
  left: 0;
  top: 0;
}

@-webkit-keyframes loader{
    0%{width: 0px;}
    70%{width: 100%; opacity: 1;}
    90%{opacity: 1; width: 100%;}
    100%{opacity: 1;width: 100%;}
}

@keyframes loader{
    0%{width: 0px;}
    70%{width: 100%; opacity: 1;}
    90%{opacity: 1; width: 100%;}
    100%{opacity: 1;width: 100%;}
}


@keyframes ball {
  0% {
    top: 0px;
  }
  95% {
    width: 100px;
  }
  to {
    top: 300px;
    width: 115px;
    /* height:90px */
  }
}

/* .login-pop {
  animation-delay: 6.7s;
} */

.move {
  font-size: 3vw;
  z-index: 3;
  position: absolute;
  margin: 0;
  top: 25%;
  width: 16%;
  left: 42%;
  background: rgba(255, 255, 255, 0.3);
  border-radius: 100%;
  text-align: center;
}

.signup-div {
  display: inline-block;
  width: 550px;
  height: 500px;
  position: absolute;
  /* object-fit: contain; */
  top: 100px;
  left: 200px;
  padding-top: 40px;
  padding-left: 60px;
  padding-right: 60px;
  border: 1px solid gray;
  box-shadow: 5px 5px 10px 3px rgb(136, 136, 136);
  z-index: 999;
  background-color: rgb(218, 210, 210);
}
.signup-div > h2 {
  margin-bottom: 20px;
}

.signup-input { 
  display: inline-block;
  position: relative;
  width: 430px;
  display: flex;
  justify-content: space-between;
  margin-top: 5px;
}


.signup-input > input {
  width: 300px;
  height: 33px;
  border: 1px solid gray;
  border-radius: 8px;
}

.input-btn {
  margin-top: 20px;
  margin-bottom: 20px;
}

</style>