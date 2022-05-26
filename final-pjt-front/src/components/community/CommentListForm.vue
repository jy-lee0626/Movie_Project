<template>
  <div class="container my-4">
    <div class="px-4 d-flex justify-content-between">
      <div class="mx-4 w-25 d-flex align-items-center">
        <img :src="`${currentUser.profile_image}`" class="profile_image img-fluid " alt="profile_image" style="width: 3rem; height: 3rem;">
        <div class="align-self-center m-auto">
          {{currentUser.first_name}}
        </div>
      </div>
      <div class="container-fluid">
        <form @submit.prevent="onSubmit" class="form-group d-flex">


          <input class="d-block w-75 m-2" type="text" id="comment" v-model="content" required>

          <button class="d-block btn btn-primary m-2">등록</button>


        </form>
      </div>
    </div>

  </div>
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
    ...mapGetters(['review', 'currentUser']),
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

</style>