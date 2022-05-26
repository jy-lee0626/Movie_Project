<template>
  <div class="review-form-card w-75">
    <div class="container">
      <form @submit.prevent="onSubmit">
        <div class="d-flex ">
          <div class="form-group container-fluid">
            <input v-model="newReview.title" type="text" class="form-control bg-transparent text-white" id="title" :maxlength="50" placeholder="제목을 입력하세요">
          </div>
          <div class="align-items-center m-auto">
            <button class="btn btn-primary align-self-center">{{ action }}</button>
          </div>

        </div>
        <hr>
        <div class="form-group">
          <textarea type="textarea" v-model="newReview.content" class="form-control bg-transparent text-white" id="content" placeholder="내용을 입력하세요"></textarea>
        </div>
        
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

  export default {
    name: 'ReviewForm',
    props: {
      review: Object,
      action: String,
    },
    data() {
      return {
        newReview: {
          title: this.review.title,
          content: this.review.content,
        }
      }
    },

    methods: {
      ...mapActions(['createReview', 'updateReview']),
      onSubmit() {
        if (this.action === 'create') {
          this.createReview(this.newReview)
        } else if (this.action === 'update') {
          const payload = {
            reviewNum: this.review.id,
            ...this.newReview,
          }
          this.updateReview(payload)
        }
      },
    },
  }
</script>

<style scoped>

  .review-form-card {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    padding: 2rem;
    width: 80%;
    min-height: 100%;
    margin: auto;
    height: auto;
  }

  #content {
    height: 35rem;
  }

  input {
    border: none;
    font-size: 2rem;
  }

  textarea {
    border: none;
  }
</style>
