<template>
  <div>
    <form @submit.prevent="onSubmit" class="movie-comment-form">
      <label for="comment">comment: </label>
      <input type="text" id="comment" v-model="content" required>
      <input type="number" step="0.5" v-model="rank">
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
      content: '',
      rank: 0
    }
  }, 
  props: {
    moviedetail: Object 
  },
  computed: {
    ...mapGetters(['movieDetail'])
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ movieNum: this.moviedetail.movie_num, content: this.content, rank: this.rank })
      this.content = ''
      this.rank = 0
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