<template>
  <div id="app" class="scroll-container">

      <router-view></router-view>
      
    <a href="#app" class="moveToTop"><font-awesome-icon icon="fa-solid fa-chevron-up" /></a>
    <footer>
      <p>by hyejin, yeseul</p>
    </footer>
  </div>
</template>

<script>


export default {
  data() {
    return {
    };
  },
  methods: {
  },
  created() {
    this.$store.dispatch("getMovies");
    this.$store.dispatch("getReviews");
  },
};

</script>

<style lang="scss">
@import url("https://use.fontawesome.com/releases/v5.13.0/css/all.css");

@font-face {
  font-family: "Harmond";
  src: local("Harmond"), url(./fonts/Harmond-ExtBdItaExp.otf) format("truetype");
}
@import url("https://fonts.googleapis.com/css2?family=Hahmlet:wght@200;300&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600&display=swap");

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
  font-family: "Hahmlet", serif;
  font-family: "Cinzel", serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: rgb(212, 201, 201);
  background-image: url('./assets/back.PNG');
  color: black;
  width: 100vw;
  height: 100vh;
}
// #app::before {
//   content: '';
//   background-image: url('https://www.cinecasero.uy/img/noise-full.png');
//   opacity: 0.03;
//   position: fixed;
//   z-index:-1 !important;
//   top:0;
//   left:0;
//   right:0;
//   bottom:0;
// }

div {
  margin: 0;
  // padding-top: 5px;
  font-family: "Hahmlet", serif;
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
body, html {
  cursor: url(assets/dotori.png)  20 30, auto;
}

// .link:hover { cursor : url(cursor.png) 20 30, url(cursor2.png) 20 30, auto; }
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
  font-family: Harmond;
  // font-family: 'Rebecca';
  display: inline-block;
  width: 100%;
  text-align: center;
}

// p, span, h1, h2, h3, h4, h5 {
//   white-space: normal; 
//   word-break: keep-all;
// }
</style>
