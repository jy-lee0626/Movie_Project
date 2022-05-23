import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    nowplaying: [],
    upcoming: [],
    popular: [],
    tvshow: [],
  },

  getters: {
    nowplaying: state => state.nowplaying,
    isnowplaying: state => !_.isEmpty(state.nowplaying),
    upcoming: state => state.upcoming,
    popular: state => state.popular,
    tvshow: state => state.tvshow
  },

  mutations: {
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
    SET_UPCOMING: (state, upcoming) => state.upcoming = upcoming,
    SET_POPULAR: (state, popular) => state.popular = popular,
    SET_TVSHOW: (state, tvshow) => state.tvshow = tvshow,
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
    fetchPopular({ commit }) {
      axios({
        url: drf.popular.popular(),
        method: 'get',
      })
        .then(res => commit('SET_POPULAR', res.data))
        .catch(err => console.error(err.response))
    },
    fetchTvshow({ commit }) {
      axios({
        url: drf.tvshow.tvshow(),
        method: 'get',
      })
        .then(res => commit('SET_TVSHOW', res.data))
        .catch(err => console.error(err.response))
    },
  }
}