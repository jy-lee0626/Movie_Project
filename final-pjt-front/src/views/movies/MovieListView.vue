<template>
  <div>
    <div>MovieListView</div>
    <ul>
      <li v-for="(nowplay, idx) in nowplaying" :key="idx">
        {{ nowplay }}
        <span>hi</span>
      </li>
    </ul>
    <div v-if="!isnowplaying">영화 없어</div>
    <span>hi</span>
    <a href="http://127.0.0.1:8000/api/v1/movies/nowplaying/">dd</a>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieListView',
  computed: {
    ...mapGetters(['nowplaying', 'isnowplaying'])
  },
  methods: {
    ...mapActions(['fetchNowplaying'])
  },
  create() {
    this.fetchNowplaying()
  },
}
</script>

<style>

</style>