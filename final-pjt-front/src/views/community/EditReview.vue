<template>
  <div>
    <ReviewForm v-if="isReview" :review="review" action="update"/>

  </div>

</template>

<script>
import ReviewForm from '@/components/community/ReviewForm.vue'

import { mapGetters, mapActions } from 'vuex'
  export default {
    name: 'EditReview',
    components: { ReviewForm },
    computed: {
      ...mapGetters(['review', 'isReview',])
    },
    methods: {
      ...mapActions(['fetchReviewDetail'])
    },
    created() {
      this.fetchReviewDetail(this.$route.params.reviewNum)
    },
  }
</script>

<style>

</style>