<template>
  <li class="youtube-list-item">
    <v-dialog
      v-model="dialog"
      hide-overlay
      width="1000px"
    >
    <template v-slot:activator="{ on, attrs }">
      <img
        :src="imgSrc" alt="thumbnail"
        v-bind="attrs"
        v-on="on">
    </template>
      <div class="youtube-dialog-card">
        <div class="youtube-container">
          <iframe :src="videoURL" frameborder="0"></iframe>
        </div>
      </div>
    </v-dialog>
  </li>
</template>

<script>
export default {
  name: 'YoutubeListItem',
  data() {
    return {
      dialog: false
    }
  },
  props: {
    video: {
      type: Object,
      required: true
    }
  },
  computed: {
    imgSrc() {
      return this.video.snippet.thumbnails.high.url
    },
    videoURL: function () {
      const { videoId } = this.video.id
      return `https://www.youtube.com/embed/${videoId}`
    },
  }
}
</script>

<style>

</style>
