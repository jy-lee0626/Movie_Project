<template>
  <div>
    <h3>Community</h3>
    <ReviewForm :review="review" action="create" />
  </div>
</template>

<script>
  import ReviewForm from '@/components/community/ReviewForm.vue'
  export default {
    name: 'CreateReview',
    components: { ReviewForm },
    data() {
      return {
        review: {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style>

</style>
