<template>
  <div>
    <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">TV Show</h3>
        <div class="progress-bar_css mt-5 pt-5"></div>
      </div>
      <div class="container_css">
        <button class="handle left-handle">
          <div class="text_css_l">&#8249;</div>
        </button>
        <div class="slider">
          <router-link class="img__item" tag="img" v-for="tv in tvshow.results" :key="tv.id" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${tv.poster_path}`" alt="포스터 없음" :to="{ name: 'moviedetail', params: { movieNum: tv.id } }"></router-link>
        </div>
        <button class="handle right-handle">
          <div class="text_css_r">&#8250;</div>
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
  name: 'TvshowList',
  computed: {
    ...mapGetters(['tvshow'])
  },
  methods: {
    ...mapActions(['fetchTvshow'])
  },
  created() {
    this.fetchTvshow()
  },
}
</script>

<style>

</style>