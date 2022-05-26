<template>
  <div class="d-flex justify-content-center">
    <div style="width: 80%">
      <h1 style="margin-bottom: 3rem;">Movie Review</h1>
      <div class="d-flex justify-content-end">
        <router-link :to="{ name: 'CreateReview'}" 
        class="btn btn-success" style="margin-right: 3rem;">
          리뷰 작성
        </router-link>
      </div>
      <hr>
      <div class="d-flex justify-content-center mt-3">
        <h4 style="margin-left: 31.5rem; margin-right: 8.5rem; font-weight: bold;">제목</h4>
        <h4 style="padding-left: 20rem; font-weight: bold;">작성일</h4>
      </div>
      <hr>
      <ReviewList />
    </div>
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