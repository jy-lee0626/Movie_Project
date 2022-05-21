import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    nowplaying: [],
  },

  getters: {
    nowplaying: state => state.nowplaying,
    isnowplaying: state => !_.isEmpty(state.nowplaying),
  },

  mutations: {
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
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
  }
}