<template>
  <div>
    <ul class="review_list p-0">
      <li v-for="review in reviewlist" :key="review.pk" 
      class="review-lisat-item" style="position: relative;">
        <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }"
        style="text-decoration: none; 
        color: white; 
        font-weight: bold; 
        margin-right: 1rem;">
          {{ review.title }} 
        </router-link>

        <span 
        style="position: absolute; bottom: 1rem; right: 5rem">
          {{ review.created_at | formatDate }}
        </span>
        <hr>
      </li>
    </ul> 
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import moment from 'moment'

export default {
  name: "ReviewList",
  computed: {
    ...mapGetters(['reviewlist']),
  },
  filters: {
    formatDate (value) {
      console.log(value)
      if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
      }
    },
  },
  methods: {
    ...mapActions(['fetchReviews',])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>
.review-lisat-item {
  list-style-type: none;
  font-size: 1.5rem;
}
</style>