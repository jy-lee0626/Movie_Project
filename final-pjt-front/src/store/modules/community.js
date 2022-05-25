// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  state: {
    reviewlist: [],
    
  },

  getters: {
    reviewlist: state => state.reviewlist,
    
  },

  mutations: {
    SET_REVIEWLIST: (state, reviewlist) => state.reviewlist = reviewlist,
    // SET_UPCOMING: (state, upcoming) => state.upcoming = upcoming,
    
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
    }
  }
}