<template>
  <div>
    <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">개봉 예정</h3>
        <div class="progress-bar_css mt-5 pt-5"></div>
      </div>
      <div class="container_css">
        <button class="handle left-handle">
          <div class="text_css_l">&#8249;</div>
        </button>
        <div class="slider">
          <router-link class="img__item" v-for="coming in upcoming.results" :key="coming.id" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${coming.poster_path}`" alt="포스터 없음" tag="img" :to="{ name: 'moviedetail', params: { movieNum: coming.id } }"></router-link>
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
  name: 'UpComing',
  computed: {
    ...mapGetters(['upcoming'])
  },
  methods: {
    ...mapActions(['fetchUpcoming'])
  },
  created() {
    this.fetchUpcoming()
  },
}
</script>

<style>

</style>