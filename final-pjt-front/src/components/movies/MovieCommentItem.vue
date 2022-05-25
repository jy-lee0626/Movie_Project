<template>
<li class="movie-comment-item">
  <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
  {{ comment.user.username }}
  </router-link>:
  <span v-if="!isEditing">{{ payload.content }}</span>

  <span v-if="isEditing">
    <input type="text" v-model="payload.content">
    <button @click="onUpdate">Update</button>
    <button @click="switchIsEditing">Cancel</button>
  </span>

  <span v-if="currentUser.username === comment.user.username && !isEditing">
    <button @click="switchIsEditing">Edit</button>
    <button @click="deleteComment(payload)">Edit</button>
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
        commentPk: this.comment.pk,
        content: this.comment.content
      },
    }
  },
  computed: {
    ...mapGetters(['currentUser'])
  },
  methods: {
    ...mapActions(['updateComment', 'deleteComment']),
    switchEditing() {
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

</style>