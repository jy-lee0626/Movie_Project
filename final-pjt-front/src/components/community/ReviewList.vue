<template>
  <div>
    <h2>reviewList</h2>
    <ul>
      <li v-for="review in reviewlist" :key="review.pk">
        <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }">
          제목: {{ review.title }} 
          <br>
          내용: {{ review.content }}
        </router-link>
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
  methods: {
    ...mapActions(['fetchReviews',])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>

</style>