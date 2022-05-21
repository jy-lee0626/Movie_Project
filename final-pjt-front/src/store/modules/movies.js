import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'

export default {
  state: {
    movies: [],
    movie: {},
    nowplaying: [],
  },

  getters: {
    movies: state => state.movies,
    movie: state => state.movie,
    nowplaying: state => state.nowplaying,
    isAuthor: (state, getters) => {
      return state.movie.user?.username === getters.currentUser.username
    },
    isMovie: state => !_.isEmpty(state.movie),
    isnowplaying: state => !_.isEmpty(state.nowplaying),
  },

  mutations: {
    SET_MOVIES: (state, movies) => state.movies = movies,
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
  },

  actions: {
    fetchMovies({ commit, getters }) {
      axios({
        url: drf.movies.movies(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_MOVIES', res.data))
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
  }
}