<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{ name: 'CreateReview'}">
      리뷰 작성
    </router-link>
    <ReviewList />
  </div>
</template>

<script>
import ReviewList from '@/components/community/ReviewList'

export default {
  name: "ReviewsView",
  components: {
    ReviewList
  }
}
</script>

<style>

</style>