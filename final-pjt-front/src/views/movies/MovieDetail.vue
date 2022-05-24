<template>
<div>
  <div class="d-flex">
    <!-- <p>{{ movieDetail }}</p> -->
    <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movieDetail.poster_path}`" class="card-img-top d-flex" alt="..." style="max-width: 300px; max-height: 450px;">
    <div>
      <h2>title: {{ movieDetail.title }}</h2>
      <p>release_date: {{ movieDetail.release_date }}</p>
      <div>
      <p>overview: {{ movieDetail.overview }}</p>
      </div>
      <p>vote_count: {{ movieDetail.vote_count }}</p>
      <p>vote_average: {{ movieDetail.vote_average }}</p>
      <p>popularity: {{ movieDetail.popularity }}</p>
      <p>genres: {{ movieDetail.genres }}</p>
      <p>like_count: {{ movieDetail.like_count }}</p>
      <p>movie_like: {{ movieDetail.movie_like }}</p>
      <input type="submit" value="좋아요">
      <div>
        <!-- 여기에 좋아요 버튼 만들어야됨 -->
      </div>
    </div>
  </div>
  <div>
    <p>코멘트</p>
    <p>vue파일 만들어야됨</p>
  </div>
</div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieDetail',
  data() {
    return {
      movieNum: this.$route.params.movieNum
    }
  },
  computed: {
    ...mapGetters(['movieDetail'])
  },
  methods: {
    ...mapActions(['fetchMovieDetail'])
  },
  created() {
    this.fetchMovieDetail(this.movieNum)
  },
}
</script>

<style>

</style>