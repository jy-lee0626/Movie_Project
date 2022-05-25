import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '../store'

import MovieListView from '@/views/movies/MovieListView.vue' //Home
import NowPlayingListView from '@/views/movies/NowPlayingListView.vue'

import TestView from '@/views/movies/TestView.vue'
import MovieDetail from '@/views/movies/MovieDetail.vue'
import SearchDataView from '@/views/movies/SearchDataView.vue'

import ReviewsView from '@/views/community/ReviewsView.vue'
import ReviewDetail from '@/views/community/ReviewDetail.vue'
import CreateReview from '@/views/community/CreateReview.vue'
import EditReview from '@/views/community/EditReview.vue'

import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import SignupView from '@/views/accounts/SignupView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'
import NotFound404 from '../views/accounts/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/logout',
    name: 'logout',
    component: LogoutView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/profile/:username',
    name: 'profile',
    component: ProfileView
  },
  {
    path: '/',  // Home
    name: 'MovieListView',
    component: MovieListView
  },
  {
    path: '/nowplaying',
    name: 'nowplaying',
    component: NowPlayingListView
  },
  {
    path: '/test',
    name: 'test',
    component: TestView
  },
  {
    path: '/movie/detail/:movieNum',
    name: 'moviedetail',
    component: MovieDetail
  },
  {
    path: '/movies/search/:searchdata',
    name: 'SearchDataView',
    component: SearchDataView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404'
  },
  {
    path: '/community/',
    name: 'ReviewsView',
    component: ReviewsView
  },
  {
    path: '/community/:reviewNum',
    name: 'ReviewDetail',
    component: ReviewDetail
  },
  {
    path: '/community/:reviewNum/edit',
    name: 'EditReview',
    component: EditReview
  },
  {
    path: '/community/create',
    name: 'CreateReview',
    component: CreateReview
  },
  
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  store.commit('SET_AUTH_ERROR', null)

  const { isLoggedIn } = store.getters

  const noAuthPages = ['login', 'signup']

  const isAuthRequired = !noAuthPages.includes(to.name)

  if (isAuthRequired && !isLoggedIn) {
    alert('로그인이 필요합니다!')
    next({ name: 'login' })
  } else {
    next()
  }
})

export default router
