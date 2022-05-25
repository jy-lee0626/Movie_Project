<template>
  <div>
    {{reviewDetail}}
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'ReviewDetail',
  data() {
    return {
      reviewNum: this.$route.params.reviewNum,
    } 
  },
  computed: {
    ...mapGetters(['reviewDetail', ]),
  },
  methods: {
    ...mapActions(['fetchReviewDetail', 'likeReview'])
  },
  created() {
    this.fetchReviewDetail(this.reviewNum)
  },
}
</script>

<style>

</style>