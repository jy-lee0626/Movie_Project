import axios from 'axios'
import drf from '@/api/drf'
// import router from '@/router'

import _ from 'lodash'
import router from '@/router'

const YOUTUBE_URL = 'https://www.googleapis.com/youtube/v3/search'
const YOUTUBE_KEY = 'AIzaSyB61ki4KeefQptF3Atc9TF1JyOiK4CQ_Ms'

export default {
  state: {
    nowplaying: [],
    upcoming: [],
    popular: [],
    tvshow: [],
    moviedetail: {},
    searchdata: [],
    youtubeVideos: [],
  },

  getters: {
    nowplaying: state => state.nowplaying,
    isnowplaying: state => !_.isEmpty(state.nowplaying),
    upcoming: state => state.upcoming,
    popular: state => state.popular,
    tvshow: state => state.tvshow,
    movieDetail: state => state.moviedetail,
    searchdata: state => state.searchdata,
    issearch: state => !_.isEmpty(state.searchdata),
    youtubeVideos: state => state.youtubeVideos,
  },

  mutations: {
    SET_NOWPLAYING: (state, nowplaying) => state.nowplaying = nowplaying,
    SET_UPCOMING: (state, upcoming) => state.upcoming = upcoming,
    SET_POPULAR: (state, popular) => state.popular = popular,
    SET_TVSHOW: (state, tvshow) => state.tvshow = tvshow,
    SET_MOVIEDETAIL: (state, moviedetail) => state.moviedetail = moviedetail,
    SET_SEARCHDATA: (state, searchdata) => state.searchdata = searchdata,
    SET_MOVIE_COMMENTS: (state, createmoviecomment) => (state.moviedetail.createmoviecomment = createmoviecomment),
    SEARCH_YOUTUBE: function (state, res) {
      state.youtubeVideos = res.data.items
    },
  },

  actions: {
    search( { commit, getters }, searchdata) {
      axios({
        url: drf.movies.search(),
        method: 'post',
        data: {searchdata: searchdata},
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_SEARCHDATA', res.data)
          router.push({
            name: 'SearchDataView',
            params: { searchdata: searchdata }
          })
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
    fetchPopular({ commit, getters }) {
      axios({
        url: drf.popular.popular(),
        method: 'get',
        headers: getters.authHeader,
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
    },
    likeMovie({ commit, getters }, movieNum) {
      axios({
        url: drf.likemovie.likemovie(movieNum),
        method: 'post',
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIEDETAIL', res.data)
      })
      .catch(err => console.error(err.response))
    },
    createMovieComment({ commit, getters }, { moviePk, content }) {
      const comment = { content }

      axios({
        url: drf.moviedetail.createmoviecomment(moviePk),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIE_COMMENTS', res.data)
      })
      .catch(err => console.error(err.response))
    },
    updateComment({ commit, getters }, {moviePk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.moviedetail.moviecommentdetail(moviePk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
      .then(res => {
        commit('SET_MOVIE_COMMENTS', res.data)
      })
      .catch(err => console.error(err.response))
    },

    deleteComment({ commit, getters }, { moviePk, commentPk }) {
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.moviedetail.moviecommentdetail(moviePk, commentPk),
          method: 'delete',
          data: {},
          headers: getters.authHeader,
        })
        .then(res => {
          commit('SET_MOVIE_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
      }
    },
    searchYoutube: function ({ commit }, searchText) {
      const params = {
        q: searchText+'movie',
        key: YOUTUBE_KEY,
        part: 'snippet',
        type: 'video'
      }
      axios({
        method: 'get',
        url: YOUTUBE_URL,
        params,
      })
      .then(res => {
        commit('SEARCH_YOUTUBE', res)
        console.log(res.data)
      })
      .catch(err => console.log(err))
    },
  }
}