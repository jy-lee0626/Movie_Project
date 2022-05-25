<template>
  <div>
    <ul class="youtube-list">
      <YoutubeListItem
        v-for="(video, idx) in youtubeVideos"
        :key="idx"
        :video="video"
      />
    </ul>
  </div>
  
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'YoutubeList',
  computed: {
    ...mapState([
      'youtubeVideos'
    ])
  },
  // created() {
  //   this.$store.dispatch('searchYoutube', this.title)
  // },
}
</script>

<style>

</style>
