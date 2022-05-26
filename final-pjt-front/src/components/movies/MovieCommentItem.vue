<template>

<div class="movie-comment-item d-flex justify-content-between my-5" style="margin-left: 3rem; height: auto;">
  <router-link 
  :to="{ name: 'profile', params: { username: comment.user.username } }"
  style="text-decoration: none; color: white; font-weight: bold; margin-right: 1rem;" class="d-block">
    <div style="width: 10rem">
      <img :src="`http://localhost:8000${comment.user.profile_image}`" alt="" class="profile_image"  style="width: 30px; margin-bottom: 0.4rem; margin-right: 0.2rem;">
      {{ comment.user.first_name }}
   </div>
  </router-link>
  <div v-if="!isEditing" class="mx-3 w-50" style="font-weight: initial;">{{ payload.content }}</div>
  <div v-if="currentUser.username === comment.user.username && !isEditing">
    <button @click="switchIsEditing" type="button" class="btn btn-info btn-sm " style="margin-right: 1rem;">Edit</button>
    <button @click="deleteComment(payload)" class="btn btn-danger btn-sm">Delete</button>
  </div>
  <div v-if="!isEditing" class="mx-3" id="comment_rank">
    <span v-show="payload.rank === 1" class="icon" style="color: yellow;">★</span>
    <span v-show="payload.rank === 2" class="icon" style="color: yellow;">★★</span>
    <span v-show="payload.rank === 3" class="icon" style="color: yellow;">★★★</span>
    <span v-show="payload.rank === 4" class="icon" style="color: yellow;">★★★★</span>
    <span v-show="payload.rank === 5" class="icon" style="color: yellow;">★★★★★</span>
  </div>
  <span v-if="isEditing" class="d-flex align-items-start">
    <!-- <input type="number" v-model="payload.rank"> -->
    <input type="text" v-model="payload.content" 
      style="margin-right: 3rem; margin-left: 3rem;">
    <form class="rating edit_form_rank">
        <label>
          <input type="radio" name="stars" value="1" v-model="payload.rank"/>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="2" v-model="payload.rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="3" v-model="payload.rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>   
        </label>
        <label>
          <input type="radio" name="stars" value="4" v-model="payload.rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="5" v-model="payload.rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
      </form>
    
    <button @click="onUpdate" type="button" class="btn btn-success mx-3">Update</button>
    <!-- <button @click="switchIsEditing">Cancel</button> -->
  </span>
</div>
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
  /* height: 100%; */
}
#comment_rank {
  border: 0.1rem;
  text-emphasis-color: yellow;
  /* border-block-style: solid;
  border-block-color: white; */
}

</style>