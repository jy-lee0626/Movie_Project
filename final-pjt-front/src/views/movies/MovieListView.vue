<template>
  <div>
    <div>HOME</div>
    <div class="container">
      <div class="row">
        <div class="col-3 my-3" v-for="nowplay in nowplaying" :key="nowplay.id">
          <div class="card" style="width: 18rem;">
            <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${nowplay.poster_path}`" class="card-img-top" alt="...">
            <div class="card-body">
              <a href="#" class="btn btn-primary">Detail</a>
            </div>
          </div>
        </div>
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
  created() {
    this.fetchNowplaying()
  },
}
</script>

<style>

</style>