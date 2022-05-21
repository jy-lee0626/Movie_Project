<template>
  <div>
    <div>MovieListView</div>
    <button @click="fetchNowplaying">눌러</button>
    <div v-for="nowplay in nowplaying" :key="nowplay.id" class="card" style="width: 18rem;">
      <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${nowplay.poster_path}`" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title"> {{ nowplay.title }}</h5>
        <a href="#" class="btn btn-primary">Detail</a>
      </div>
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
  beforeCreate() {
    this.fetchNowplaying()
  },
}
</script>

<style>

</style>