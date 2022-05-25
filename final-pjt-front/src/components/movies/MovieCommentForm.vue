<template>
  <div>
    <form @submit.prevent="onSubmit" class="movie-comment-form">
      <label for="comment">comment: </label>
      <input type="text" id="comment" v-model="content" required>
      <button>CommentForm</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: "MovieCommentForm",
  data() {
    return {
      content: ''
    }
  }, 
  computed: {
    ...mapGetters(['movieDetail'])
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ moviePk: this.movieDetail.pk, content: this.content, })
      this.content = ''
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid black;
  margin: 1rem;
  padding: 1rem;
}
</style>