<template>
  <div>
    <div>Home</div>
    <div 
    v-for="nowplay in nowplaying" :key="nowplay.id"
      class="flex flex-shrink-0 justify-center items-center w-1/2 max-w-sm mx-auto my-8"
    >
      <div
        :style="{
          backgroundImage: `url(https://www.themoviedb.org/t/p/w300_and_h450_bestv2${nowplay.poster_path})`
        }"
        class="bg-gray-300 h-64 w-full rounded-lg shadow-md bg-cover bg-center"
      ></div>
    </div>
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
  created() {
    this.fetchNowplaying()
  },
}
</script>