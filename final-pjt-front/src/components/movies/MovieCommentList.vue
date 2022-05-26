<template>
  <div class="movie-comment-list">
    <hr>
    <movie-comment-form :moviedetail="moviedetail"></movie-comment-form>
    <div class="d-flex justify-content-center">
      <ul class="comment_list">
        <movie-comment-item
        v-for="comment in comments"
        :comment="comment"
        :key="comment.pk"
        :moviedetail="moviedetail">
        </movie-comment-item>
      </ul>
    </div>
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
.comment_list {
  /* display: inline; */
  justify-content: space-between;
  align-items: center;
  height: 4rem;
  width: 50rem;
}
</style>