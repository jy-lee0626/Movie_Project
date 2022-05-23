import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    nowplaying: [],
    upcoming: [],
  },

  getters: {
    nowplaying: state => state.nowplaying,
    isnowplaying: state => !_.isEmpty(state.nowplaying),
    upcoming: state => state.upcoming
  },

  mutations: {
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
    SET_UPCOMING: (state, upcoming) => state.upcoming = upcoming,
  },

  actions: {
    fetchNowplaying({ commit, getters }) {
      axios({
        url: drf.nowplaying.nowplaying(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_NOWPLAYING', res.data))
        .catch(err => console.error(err.response))
    },
    fetchUpcoming({ commit }) {
      axios({
        url: drf.upcoming.upcoming(),
        method: 'get',
      })
        .then(res => commit('SET_UPCOMING', res.data))
        .catch(err => console.error(err.response))
    },
  }
}