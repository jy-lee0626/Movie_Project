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
        style="position: absolute; bottom: 1rem; right: 2rem">
          {{ review.created_at | maxlength(19) }}
        </span>
        <hr>
      </li>
    </ul> 
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: "ReviewList",
  computed: {
    ...mapGetters(['reviewlist']),
  },
  filters: {
  maxlength: function (value, size) {
  if (!value) return '';
  value = value.toString();

  if (value.length <= size) {
    return value;
  }
  return value.substr(0, size);
  }},
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