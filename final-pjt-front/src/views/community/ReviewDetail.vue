<template>
  <div>
    <h1>{{ review.title }}</h1>
    <p>
      {{ review.content }}
    </p>
    
    <div v-if="isAuthor">
      <router-link :to="{ name: 'EditReview', params: { reviewNum } }">
        <button>Edit</button>
      </router-link>
      <button @click="deleteReview(reviewNum)">Delete</button>
    </div>
    
    <div>
      Likeit:
      <button
        @click="likeReview(reviewNum)"
      >{{ likeCount }}</button>
    </div>

    <hr />
    
    <CommentList :comments="review.comment_set"/>

  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'
  import CommentList from '@/components/community/CommentList.vue'



  export default {
    name: 'ReviewDetail',
    components: { CommentList },
    data() {
      return {
        reviewNum: this.$route.params.reviewNum,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'review']),
      likeCount() {
        return this.review.like_users?.length
      }
    },
    methods: {
      ...mapActions([
        'fetchReviewDetail',
        'likeReview',
        'deleteReview',
      ])
    },
    created() {
      this.fetchReviewDetail(this.reviewNum)
    },
  }
</script>

<style></style>
