// import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'
import router from '@/router'
import _ from 'lodash'

export default {
  state: {
    reviewlist: [],
    review: {}
  },

  getters: {
    reviewlist: state => state.reviewlist,
    review: state => state.review,
    isReview: state => !_.isEmpty(state.review),
    isAuthor: (state, getters) => {
      return state.review.user?.username === getters.currentUser.username
    }
  },

  mutations: {
    SET_REVIEWLIST: (state, reviewlist) => state.reviewlist = reviewlist,
    SET_REVIEW: (state, review) => state.review = review,
    SET_REVIEW_COMMENTS: (state, comments) => (state.review.comment_set = comments),
  },

  actions: {
    fetchReviews({ commit, getters }, ) {
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
      .then(res => commit('SET_REVIEW', res.data))
      .catch(err => console.error(err.response))
    },

    createReview({ commit, getters }, review) {
      axios({
        url: drf.community.reviews(),
        method: 'post',
        data: review,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'ReviewDetail',
            params: { reviewNum: getters.review.id }
          })
        })
    },

    updateReview({ commit, getters }, { reviewNum, title, content}) {

      axios({
        url: drf.community.reviewDetail(reviewNum),
        method: 'put',
        data: { title, content },
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW', res.data)
          router.push({
            name: 'ReviewDetail',
            params: { reviewNum: getters.review.id }
          })
        })
    },

    deleteReview({ commit, getters }, reviewNum) {      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.community.reviewDetail(reviewNum),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_REVIEW', {})
            router.push({ name: 'ReviewsView' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeReview({ commit, getters }, reviewNum) {
      axios({
        url: drf.community.likeReview(reviewNum),
        method: 'post',
        headers: getters.authHeader,
      })
        .then(res => commit('SET_REVIEW', res.data))
        .catch(err => console.error(err.response))
    },

		createReviewComment({ commit, getters }, { reviewNum, content }) {
      const comment = { content }

      axios({
        url: drf.community.comments(reviewNum),
        method: 'post',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
          console.log(this.review)
        })
        .catch(err => console.error(err.response))
    },

    updateReviewComment({ commit, getters }, { reviewPk, commentPk, content }) {
      const comment = { content }

      axios({
        url: drf.community.commentDetail(reviewPk, commentPk),
        method: 'put',
        data: comment,
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_REVIEW_COMMENTS', res.data)
        })
        .catch(err => console.error(err.response))
    },

    deleteReviewComment({ commit, getters }, { reviewPk, commentPk }) {
        if (confirm('정말 삭제하시겠습니까?')) {
          axios({
            url: drf.community.commentDetail(reviewPk, commentPk),
            method: 'delete',
            data: {},
            headers: getters.authHeader,
          })
            .then(res => {
              commit('SET_REVIEW_COMMENTS', res.data)
            })
            .catch(err => console.error(err.response))
        }
      },
    
  }
}