<template>
  <div>
    <popular-list></popular-list>
    <now-playing-list></now-playing-list>
    <tvshow-list></tvshow-list>
    <up-coming></up-coming>
  </div>
</template>

<script>

import NowPlayingList from '@/components/movies/NowPlayingList.vue'
import UpComing from '@/components/movies/UpComing.vue'
import PopularList from '@/components/movies/PopularList.vue'
import TvshowList from '@/components/movies/TvshowList.vue'

export default {
  name: 'MovieListView',
  components: {
    NowPlayingList,
    UpComing,
    PopularList,
    TvshowList,
  },
}
</script>

<style>

</style>