<template>
  <div class="home">
    <div class="box">
      <img src="https://raw.githubusercontent.com/dontk1llme/finalPJT/master/mp3/home.gif" alt="" :class="{ 'fade-out': popLogin }">
      <div class="loader animate__fade" :class="{ 'fade-out': popLogin }" @animationend="hideElements"></div>
      <LogIn class="login-pop animate__animated animate__fadeIn" v-show="!this.$store.state.username"/>
    </div>
    <SetProfile v-show="this.$store.state.token && !this.$store.state.userId"/>
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
    hideElements() {
      this.popLogin = true;
    },
    goToHome() {
      this.$router.push({ name: 'main' })
    }
  },
};
</script>

<style scoped>
.fade-out {
  animation-name: fadeOut;
  animation-duration: 0.5s;
  animation-fill-mode: forwards;
}

@keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}

.home {
  position: relative;
  justify-content: center;
  width: 100vw;
  height: 100vh;
  vertical-align: center;
  padding-top: 20px;
}

.box {
  display: inline-block;
  width: 80%;
  margin-top: 0px;
}

img {
  padding: 0;
  width: 100%;
}

.loader {
  position: absolute;
  width: 80%;
  height: 30px;
  background-color: rgba(255, 255, 255, 0.2);
}

.loader:before {
  content: "";
  position: absolute;
  background-color: #fff;
  top: 0px;
  left: 0;
  height: 30px;
  width: 0px;
  z-index: 0;
  opacity: 1;
  transform-origin: 100% 0%;
  animation: loader 5s ease-in-out forwards;
}

.loader:after {
  content: "LOADING ...";
  color: #48bde0;
  font-weight: 200;
  font-size: 20px;
  position: absolute;
  width: 100%;
  height: 30px;
  line-height: 30px;
  left: 0;
  top: 0;
}

@keyframes loader {
  0% {
    width: 0px;
  }
  70% {
    width: 100%;
    opacity: 1;
  }
  90% {
    opacity: 1;
    width: 100%;
  }
  100% {
    opacity: 1;
    width: 100%;
  }
}

.login-pop {
  animation-delay: 5s;
}
</style>
