<template>
  <div class="movie-comment-list">
    <h2>CommentList</h2>
    <ul>
      <movie-comment-item
      v-for="comment in comments"
      :comment="comment"
      :key="comment.pk">
      </movie-comment-item>
    </ul>
    <movie-comment-form></movie-comment-form>
  </div>
</template>

<script>
import MovieCommentItem from '@/components/movies/MovieCommentItem.vue'
import MovieCommentForm from '@/components/movies/MovieCommentForm.vue'

export default {
  name: "MovieCommentList",
  components: { MovieCommentItem, MovieCommentForm },
  props: { comments: Array },
}
</script>

<style>

</style>