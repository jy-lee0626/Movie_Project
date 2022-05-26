import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import movies from './modules/movies'
import community from './modules/community'
import nowplayingmovie from '@/assets/js/home'
// import upup from '@/assets/js/up'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, movies, community, nowplayingmovie},
})
