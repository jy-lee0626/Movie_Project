<template>
  <div class="container">
    <div class="slider">
      <img v-for="nowplay in nowplaying" :key="nowplay.id" :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${nowplay.poster_path}`" alt="포스터 없음">
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'NowPlayingList',
  computed: {
    ...mapGetters(['nowplaying'])
  },
  methods: {
    ...mapActions(['fetchNowplaying'])
  },
  created() {
    this.fetchNowplaying()
  },
}
</script>

<style>
  @import '../../assets/styles/nowplay.css';
</style>