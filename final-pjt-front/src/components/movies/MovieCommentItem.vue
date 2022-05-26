<template>

<li class="movie-comment-item d-flex justify-content-start">
  <router-link 
  :to="{ name: 'profile', params: { username: comment.user.username } }"
  style="text-decoration: none; color: white; font-weight: bold; margin-right: 1rem;">
  {{ comment.user.first_name }}
  </router-link>:
  <span v-if="!isEditing" class="mx-3" style="font-weight: initial;">{{ payload.content }}</span>
  <span v-if="!isEditing" class="mx-3" id="comment_rank">{{ payload.rank }} 점</span>

  <span v-if="isEditing">
    <p>test</p>
    <input type="number" v-model="payload.rank">
    <input type="text" v-model="payload.content">
    <button @click="onUpdate">Update</button>
    <!-- <button @click="switchIsEditing">Cancel</button> -->
  </span>
  <span v-if="currentUser.username === comment.user.username && !isEditing">
    <button type="button" class="btn btn-info" style="margin-right: 1rem;" @click="switchIsEditing">Edit</button>
    <button @click="deleteComment(payload)" class="btn btn-danger">Delete</button>
  </span>
</li>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  name: "MovieCommentItem",
  props: { comment: Object, moviedetail: Object  },
  data() {
    return {
      isEditing: false,
      payload: {
        movieNum: this.moviedetail.movie_num,
        commentPk: this.comment.id,
        content: this.comment.content,
        rank: this.comment.rank,
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchIsEditing() {
      this.isEditing = !this.isEditing
    },
    onUpdate() {
      this.updateComment(this.payload)
      this.isEditing = false
    }
  },
}
</script>

<style>
.movie-comment-item {
  list-style-type: none;
  font-size: 1.5rem;
  height: 100%;
  width: 50rem;
}
#comment_rank {
  border: 0.1rem;
  text-emphasis-color: yellow;
  /* border-block-style: solid;
  border-block-color: white; */
}

</style>