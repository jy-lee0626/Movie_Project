<template>
  <div class="review-list-card w-75">
    <h3>Community</h3>
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
.review-list-card {
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  min-height: 100%;
  margin: auto;
  height: auto;
}
</style>