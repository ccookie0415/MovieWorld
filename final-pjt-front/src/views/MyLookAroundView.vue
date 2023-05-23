<template>
  <div>
    <div class="header news__header">
      <span>Look Around</span>
      <span>둘러보기</span>
    </div>

    <div>
      <MovieList
        :movies="movieList"
        @search-movie="searchMovie"
      />
      <!-- <SearchBar @search-movie="searchMovie" class="search-bar" /> -->
    </div>
  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar";
import MovieList from "@/components/MovieList";


const toggle = document.querySelectorAll('button')


export default {
  name: "MyLookAroundView",
  components: {
    SearchBar,
    MovieList,
  },
  data() {
    return {
      selected: "A",
      searchYes: false,
      movieList: [],
    };
  },
  computed: {
    movies() {
      return this.$store.state.movies;
    },
  },
  methods: {
    toggleChange() {
      const toggle = document.querySelector('.slider-toggle')
      toggle.classList.toggle('left')
      toggle.classList.toggle('right')
      if(toggle.classList.contains('left') === true) {
        this.selected = 'A'
      } else {
        this.selected = 'B'
      }
      this.sortMovies();
    },
    sortMovies() {
      if (this.selected === "A") {
        if (!this.searchYes) {
          this.movieList = this.movies;
        }
        this.movieList.sort((a, b) => {
          return b.popularity - a.popularity;
        });
      } else {
        if (!this.searchYes) {
          this.movieList = this.movies;
        }
        this.movieList.sort((a, b) => {
          return b.release_date.localeCompare(a.release_date);
        });
      }
    },
    searchMovie(keyword) {
      const movies = this.movies.filter((movie) => {
        return movie.title.includes(keyword);
      });
      if (movies) {
        this.movieList = movies;
        this.searchYes = true;
      }
    },
  },
  created() {
    this.sortMovies();
  },
};


</script>

<style lang="scss" scoped>

header {
  top: 0;
  left: 0;
  right: 0;
  padding: 1rem;
}

.search-bar {
  margin-bottom: 3px;

}

// 여기서부터 펌
// .slider-toggle {
//     position: absolute;
//     top:50px; left:70vw; right: 0;
//     height: 32px;
//     margin-top: -16px;
//     line-height: 32px;
//     z-index: 999 !important;
// }

.slider-toggle {
    position: absolute;
    top: 50px;
    left: 70vw;
    right: 0;
    height: 32px;
    width: 60px; /* 변경된 width 값 */
    margin-top: 60px;
    line-height: 32px;
    font-size : 0.5em;
    z-index: 999 !important;
}

.label{
  position: absolute;
  font-size: 14px;
  font-weight: bold;
  color: darkgray;
  transition: color .3s;
}
.label:first-of-type { right:50%; margin-right:50px }
.label:last-of-type { left:50%; margin-left:50px; }
.slider-toggle.left .label:first-of-type,
.slider-toggle.right .label:last-of-type {
    color: #333;
}

.slider {
    position: absolute;
    display: inline-block;
    background: gray;
    left: 50%;
    width:80px; height:32px;
    margin-left: -40px;
    border-radius: 4px;
    cursor: pointer;
    box-shadow:
        0 1px 0 rgba(255,255,255,.5),
        inset 0 4px 0 rgba(0,0,0,.2);
}

.toggle {
  position: absolute;
  top:-4px; left:4px;
  background: #55b2d4;
  width: 32px;
  height: 32px;
  border-radius: 4px;
  transition: left .3s;
  box-shadow: 
      0 1px 0 rgba(0,0,0,.4), 
      inset 0 1px 0 rgba(0,0,0,.05), 
      inset 0 -4px 0 #55b2d4, 
      inset 0 -5px 0 rgba(255,255,255,.4);
}
.slider-toggle.right .toggle { left:44px; }

.grip {
  position: absolute;
  top:50%; left:8px; right:8px;
  margin-top: -3px;
  height: 2px;
  background: rgba(255,255,255,.9);
}
.grip::before {
  content: '';
  position: absolute;
  top:-4px; left:0;
  width:100%; height:100%;
  background: inherit;
}
.grip::after {
  content: '';
  position: absolute;
  top:4px; left:0;
  width:100%; height:100%;
  background: inherit;
}


button {
  display: inline-block;
  font-size: 15px;
  width: 45px;
  height: 40px;
  margin-right: 3px;
  box-shadow: 1px 1px #908581;
  border: 1px solid rgb(204, 204, 204);
  border-radius: 100px;
  background-color: #E6E6E6;
}

.select-on { 
  background-color: #F0E2D7;
  font-weight: bold;
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