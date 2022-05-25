<template>
  <div>
    <h2>reviewList</h2>
    {{reviewlist}}
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