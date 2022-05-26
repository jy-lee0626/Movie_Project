<template>
  <div>
    <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">인기 영화</h3>
        <div class="progress-bar_css mt-5 pt-5"></div>
      </div>
      <div class="container_css">
        <button class="handle left-handle" style="{z-index: 100;}">
          <div class="text_css_l">&#8249;</div>
        </button>
        <div class="slider">

          <router-link class="img__item" tag="img" v-for="popul in popular" :key="popul.id" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${popul.poster_path}`" alt="포스터 없음" :to="{ name: 'moviedetail', params: { movieNum: popul.movie_num } }"  ></router-link>
          
          <!-- <span v-for="popul in popular" :key="popul.id">
            <span v-if="popul.poster_path">
              <router-link class="img__item" :to="{ name: 'moviedetail', params: { movieNum: popul.movie_num } }" tag="img" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${popul.poster_path}`" alt="포스터 없음"></router-link>
            </span>
          </span> -->
        </div>
        <button class="handle right-handle" style="{position:relative; z-index: 100;}">
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
  name: 'PopularList',
  computed: {
    ...mapGetters(['popular'])
  },
  methods: {
    ...mapActions(['fetchPopular'])
  },
  created() {
    this.fetchPopular()
  }
}
</script>

<style>

</style>