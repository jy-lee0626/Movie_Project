// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    reviewlist: [],
    reviewdetail: {},
  },

  getters: {
    reviewlist: state => state.reviewlist,
    reviewDetail: state => state.reviewdetail,
  },

  mutations: {
    SET_REVIEWLIST: (state, reviewlist) => state.reviewlist = reviewlist,
    SET_REVIEWDETAIL: (state, reviewdetail) => state.reviewdetail = reviewdetail
  },

  actions: {
    fetchReviews({ commit, getters }) {
      axios({
        url: drf.community.reviews(),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEWLIST', res.data))
        .catch(err => console.error(err.response))
    },
    fetchReviewDetail({ commit, getters }, reviewNum) {
      axios({
        url: drf.community.reviewDetail(reviewNum),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_REVIEWDETAIL', res.data))
      .catch(err => console.error(err.response))
    },
  }
}