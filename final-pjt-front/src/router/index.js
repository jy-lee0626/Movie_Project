import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/UserSignup'
import Login from '@/views/accounts/UserLogin'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
