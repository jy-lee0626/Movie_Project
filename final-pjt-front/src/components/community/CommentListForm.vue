<template>
  <form @submit.prevent="onSubmit">
    <label for="comment">comment: </label>
    <input type="text" id="comment" v-model="content" required>
    <button>댓글 달기</button>
  </form>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: 'CommentListForm',
  data() {
    return {
      content: ''
    }
  },
  computed: {
    ...mapGetters(['review']),
  },
  methods: {
    ...mapActions(['createReviewComment']),
    onSubmit() {
      this.createReviewComment({ reviewNum: this.review.id, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>

</style>