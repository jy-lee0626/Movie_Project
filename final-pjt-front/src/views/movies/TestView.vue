<template>
  <div>
    <div>TestVue</div>
    <now-playing-list></now-playing-list>
    <up-coming></up-coming>
  </div>
</template>

<script>
import NowPlayingList from '@/components/movies/NowPlayingList.vue'
import UpComing from '@/components/movies/UpComing.vue'

export default {
  name: "TestView",
  components: {
    NowPlayingList,
    UpComing,
  }
}
</script>

<style>

</style>