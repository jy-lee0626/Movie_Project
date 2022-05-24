<template>
  <div>
    <span>search</span>
    <!-- <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">현재 상영작</h3>
        <div class="progress-bar_css mt-5 pt-5"></div>
      </div>
      <div class="container_css">
        <button class="handle left-handle">
          <div class="text_css">&#8249;</div>
        </button>
        <div class="slider">
          <router-link class="img__item" v-for="data in serachdata.slice(0, 20)" :key="data.id" :to="{ name: 'moviedetail', params: { movieNum: data.movie_num } }" tag="img" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${data.poster_path}`" alt="포스터 없음"></router-link>
        </div>
        <button class="handle right-handle">
          <div class="text_css">&#8250;</div>
        </button>
      </div>
    </div> -->
    <div v-for="data in searchdata" :key="data.id">
      {{ data.title }}
      <img :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${data.poster_path}`" alt="포스터 없음">
    </div>
    <h2 v-if="!searchdata" class="mt-5">검색결과가 없습니다.</h2>
    {{ searchdata }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: "SearchData",
  computed: {
    ...mapGetters(['searchdata'])
  }
}
</script>

<style>

</style>