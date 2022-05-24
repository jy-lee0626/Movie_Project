<template>
  <div>
    <p>{{ movieDetail }}</p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieDetail',
  data() {
    return {
      movieNum: this.$route.params.movieNum
    }
  },
  computed: {
    ...mapGetters(['movieDetail'])
  },
  methods: {
    ...mapActions(['fetchMovieDetail'])
  },
  created() {
    this.fetchMovieDetail(this.movieNum)
  },
}
</script>

<style>

</style>