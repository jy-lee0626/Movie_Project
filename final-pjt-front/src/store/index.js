import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'


const SERVER_URL = 'http://127.0.0.1:8000/'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  getters: {
  },
  mutations: {
    LOGIN(state) {
      state.isLogin = true
    },
    LOGOUT(state) {
      state.isLogin = false
    },
  },
  actions: {
    login({commit}, credentials) {
      axios({
        method: 'POST',
        url: `${SERVER_URL}accounts/api-token-auth/`,
        data: credentials,
      })
      .then(res => {
        localStorage.setItem('jwt', res.data.token)
        commit('LOGIN')
        router.push({name: 'Home'})
      })
      .catch(err => console.log(err))
    },
    logout({commit}) {
      localStorage.removeItem('jwt')
      commit('LOGOUT')
      router.push({ name: 'Login' })
    },
  },
  modules: {
  }
})
