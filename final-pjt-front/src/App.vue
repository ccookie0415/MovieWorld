<template>
  <div id="app" class="scroll-container">

      <router-view></router-view>
      
    <a href="#app" class="moveToTop"><font-awesome-icon icon="fa-solid fa-chevron-up" /></a>
    <footer>
      <p> * ☆ ｡･ﾟ*.｡ by Hyejin, Yeseul ｡.*ﾟ･｡ ☆ *</p>
    </footer>
  </div>
</template>

<script>
export default {
  data() {
    return {};
  },
  methods: {},
  created() {
    this.$store.dispatch("getMovies");
    this.$store.dispatch("getReviews");
  },
};
</script>

<style lang="scss">
@import url("https://use.fontawesome.com/releases/v5.13.0/css/all.css");

@import url("https://cdn.jsdelivr.net/npm/galmuri/dist/galmuri.css");

html {
  scroll-behavior: smooth;
  background-color: rgb(212, 201, 201);
  -ms-overflow-style: none;
}

html::-webkit-scrollbar {
  display: none;
}

#app {
  margin: 0;
  font-family: "Galmuri11", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(212, 201, 201);
  background-image: url('./assets/back.PNG');
  color: black;
  width: 100vw;
  height: 100vh;
}

div {
  margin: 0;
  font-family: "Galmuri11", sans-serif;
}

p {
  margin: 0;
}

.moveToTop {
  position: fixed;
  bottom: 50px;
  right: 15px;
  color: darkgray;
  font-size: 30px;
}

.moveToTop :hover {
  color: black;
}

.is-pulled {
  margin-left: 180px;
  transition: 0.5s;
  height: 100vh;
}

.is-back {
  margin-left: 0;
  transition: 0.5s;
  transition-delay: 0.17s;
}

.animate__fadeInLeft {
  animation-delay: 0.2s;
  animation-duration: 10s;
}

body,
html {
  cursor: url(assets/dotori.png) 20 30, auto;
}

footer {
  display: inline-block;
  width: 100%;
  height: 35px;
  display: flex;
  position: fixed;
  bottom: 0;
  justify-content: center;
  background-color: #55b2d4;
  padding-top: 5px;
  z-index: 999 !important;
}

footer > p {
  font-family: "Galmuri11", sans-serif;
  display: inline-block;
  width: 100%;
  text-align: center;
}

// p, span, h1, h2, h3, h4, h5 {
//   white-space: normal;
//   word-break: keep-all;

</style>