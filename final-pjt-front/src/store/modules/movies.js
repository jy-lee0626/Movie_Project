import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'
import router from '@/router'

export default {
  state: {
    nowplaying: [],
    upcoming: [],
    popular: [],
    tvshow: [],
    moviedetail: {},
    searchdata: [],
  },

  getters: {
    nowplaying: state => state.nowplaying,
    isnowplaying: state => !_.isEmpty(state.nowplaying),
    upcoming: state => state.upcoming,
    popular: state => state.popular,
    tvshow: state => state.tvshow,
    movieDetail: state => state.moviedetail,
    searchdata: state => state.searchdata,
  },

  mutations: {
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
    SET_UPCOMING: (state, upcoming) => state.upcoming = upcoming,
    SET_POPULAR: (state, popular) => state.popular = popular,
    SET_TVSHOW: (state, tvshow) => state.tvshow = tvshow,
    SET_MOVIEDETAIL: (state, moviedetail) => state.moviedetail = moviedetail,
    SET_SEARCHDATA: (state, searchdata) => state.searchdata = searchdata,
  },

  actions: {
    search( { commit, getters }, searchdata) {
      console.log(searchdata)
      axios({
        url: drf.movies.search(searchdata),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SEARCHDATA', res.data)
          router.push({ name: 'SearchData' })
        })
        .catch(err => console.error(err.response))
    },
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
    fetchMovieDetail({ commit, getters }, movieNum) {
      axios({
        url: drf.moviedetail.moviedetail(movieNum),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_MOVIEDETAIL', res.data))
      .catch(err => console.error(err.response))
    }
  }
}