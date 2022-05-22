<template>
  <div>
    <div>TestVue</div>
    <now-playing-list></now-playing-list>
  </div>
</template>

<script>
import NowPlayingList from '@/components/movies/NowPlayingList.vue'
export default {
  name: "TestView",
  components: {
    NowPlayingList,
  }
}
</script>

<style>

</style>