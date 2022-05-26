<template>
<li class="movie-comment-item">
  <router-link :to="{ name: 'profile', params: { username: comment.user.username } }">
  {{ comment.user.username }}
  </router-link>:
  <span  v-if="!isEditing">comment: {{ payload.content }}</span>
  <span  v-if="!isEditing">rank: {{ payload.rank }}</span>

  <span v-if="isEditing">
    <input type="text" v-model="payload.content">
    <button @click="onUpdate">Update</button>
    <button @click="switchIsEditing">Cancel</button>
  </span>
  <!-- <div>{{ currentUser }}</div> -->
  <span v-if="currentUser.username === comment.user.username && !isEditing">
    <button @click="switchIsEditing">Edit</button>
    <button @click="deleteComment(payload)">Delete</button>
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