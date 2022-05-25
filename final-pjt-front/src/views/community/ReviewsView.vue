<template>
  <div>
    <h1>Articles</h1>
    <ReviewList />
    <router-link :to="{ name: 'CreateReview'}">
      새 리뷰 작성
    </router-link>
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