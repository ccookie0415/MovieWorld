import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainView from '../views/MainView.vue'
import DetailView from '../views/DetailView.vue'
import ReviewView from '../views/ReviewView.vue'
import NotFound404 from '../views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  //수정을해보아요..~
  {
    // path: '/main',
    path: '/:userId/main',
    name: 'main',
    component: MainView,
    redirect: '/:userId/main/myhome', //첫화면
    children:[
      {
        path: 'zzim',
        name: 'movie_zzim_list',
        component: () => import('../views/MyZzimView.vue')
      },
      {
        path: 'movies',
        name: 'movie_list',
        component: () => import('../views/MyLookAroundView.vue')
        // component: () => import('../views/ReadView.vue')
      },
      {
        path: 'guest',
        name: 'guest_book',
        component: () => import('../views/MyGuestBookView.vue')
      },
      {
        path: 'myhome',
        name: 'my_home',
        component: () => import('../views/MyHomeView.vue')
      },
      {
        path: 'rec',
        name: 'movie_recommend_list',
        component: () => import('../views/MyRecommendView.vue')
      },
      {
        path: 'review',
        name: 'my_review',
        component: () => import('../views/MyReviewView.vue')
      },
      {
        path: 'movies/:movie_id',
        name: 'movie_detail',
        component: DetailView,
      },
      {
        path: 'reviews/:review_id',
        name: 'review_detail',
        component: ReviewView,
      },
    ]
  },
  

  //--------------------------------

  // {
  //   path: '/:userId',
  //   name: 'NotFound404',
  //   component: NotFound404,
  // },
  {
    path: '/not-found-404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/not-found-404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
