<template>
  <div>
    <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">인기 영화</h3>
        <div class="progress-bar_css mt-5"></div>
      </div>
      <div class="container_css mt-3">
        <button class="handle left-handle">
          <div class="text">&#8249;</div>
        </button>
        <div class="slider">
          <img class="img__item" v-for="popular in popular.results" :key="popular.id" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${popular.poster_path}`" alt="포스터 없음">
        </div>
        <button class="handle right-handle">
          <div class="text">&#8250;</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import '../../assets/js/home.js'
// import js from 'vuex'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'PopularList',
  computed: {
    ...mapGetters(['popular'])
  },
  methods: {
    ...mapActions(['fetchPopular'])
  },
  created() {
    this.fetchPopular()
  },
}
</script>

<style>

</style>