<template>
  <form @submit.prevent="onSubmit">
    <label for="comment">comment: </label>
    <input type="text" id="commentlist" v-model="content" required
    style="margin-right: 2rem; margin-left: 1rem;" placeholder="댓글을 남겨주세요">
    <button id="commentlistbtn" type="button" class="btn btn-info">댓글</button>
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
#commentlist::placeholder {
  color: grey;
}
#commentlistbtn {
  padding: 5px 5px;
}
</style>