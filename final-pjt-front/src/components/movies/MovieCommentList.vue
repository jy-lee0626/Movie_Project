<template>
  <div class="movie-comment-list">
    <h2>CommentList</h2>
    <div>
      <movie-comment-item
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk"
      :moviedetail="moviedetail">
      </movie-comment-item>
    </div>
    <movie-comment-form :moviedetail="moviedetail"></movie-comment-form>
  </div>
</template>

<script>
import MovieCommentItem from '@/components/movies/MovieCommentItem.vue'
import MovieCommentForm from '@/components/movies/MovieCommentForm.vue'

export default {
  name: "MovieCommentList",
  components: { MovieCommentItem, MovieCommentForm },
  props: { comments: Array, moviedetail: Object },
}
</script>

<style>

</style>