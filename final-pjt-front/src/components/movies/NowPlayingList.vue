<template>
  <div>
    <div class="row_css">
      <div class="header_css">
        <h3 class="title_css mt-5">현재 상영작</h3>
        <div class="progress-bar_css mt-5"></div>
      </div>
      <div class="container_css mt-3">
        <button class="handle left-handle">
          <div class="text">&#8249;</div>
        </button>
        <div class="slider">
          <img class="img__item" v-for="nowplay in nowplaying.slice(0, 20)" :key="nowplay.id" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${nowplay.poster_path}`" alt="포스터 없음">
        </div>
        <button class="handle right-handle">
          <div class="text">&#8250;</div>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import '../../assets/js/home.js'
// import js from 'vuex'
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
*, *::after, *::before {
  box-sizing: border-box;
}

:root {
  --handle-size: 3rem;
  --img-gap: .25rem;
}

body {
  margin: 0;
}

.container_css {
  display: flex;
  justify-content: center;
  overflow: hidden;
}

.slider {
  --items-per-screen: 9;
  --slider-index: 0;
  display: flex;
  flex-grow: 1;
  margin: 0 var(--img-gap);
  transform: translateX(calc(var(--slider-index) * -100%));
  transition: transform 250ms ease-in-out;
}

.slider > img {
  flex: 0 0 calc(100% / var(--items-per-screen));
  max-width: calc(1000% / var(--items-per-screen));
  aspect-ratio: 2 / 3;
  padding: var(--img-gap);
  border-radius: 1rem;
}

.handle {
  border: none;
  border-radius: 1rem;
  flex-grow: 0;
  flex-shrink: 0;
  background-color: rgba(255, 255, 255, .25);
  z-index: 10;
  margin: var(--img-gap) 0;
  width: var(--handle-size);
  cursor: pointer;
  font-size: 5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  line-height: 0;
  transition: background-color 150ms ease-in-out;
}

.left-handle {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}

.right-handle {
  border-top-right-radius: 0;
  border-bottom-right-radius: 0;
}

.handle:hover,
.handle:focus {
  background-color: rgba(255, 255, 255, .5);
}

.text {
  transition: transform 150ms ease-in-out;
}

.handle:hover .text,
.handle:focus .text {
  transform: scale(1.2);
}

.header_css {
  display: flex;
  justify-content: space-between;
  padding: .5rem calc(var(--img-gap) * 2 + var(--handle-size));
  align-items: center;
}

.title_css {
  font-size: 2rem;
  margin: 0;
}

.progress-bar_css {
  display: flex;
  gap: .25rem;
}

.progress-item {
  flex: 0 0 1.5rem;
  min-width: 1.5rem;
  height: .5rem;
  background-color: rgba(255, 255, 255, .5);
}

.progress-item.active {
  background-color: rgba(255, 255, 255, .9);
}

.img__item {
  padding: 0 2px;
  transition: 250ms all;
}

.img__item:hover {
  margin: 0 40px;
  transform: scale(1.2);
}

@media (max-width: 1000px) {
  .slider {
    --items-per-screen: 3;
  }
}

@media (max-width: 500px) {
  .slider {
    --items-per-screen: 2;
  }
}

body {
  background-color: rgba(250,227,217,1);
  color: white;
}
</style>