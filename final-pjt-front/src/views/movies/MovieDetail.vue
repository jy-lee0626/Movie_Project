<template>
  <div>
    <!-- <div class="container">
      <div class="row detail_box">
        <img class="detail_img col-6 col-lg-12" :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movieDetail.poster_path}`" alt="..." style="max-width: 300px; max-height: 450px;">
        <div class="detail_text col-6 col-lg-12">
          <h1>{{ movieDetail.title }}</h1>
          <p>개봉일: {{ movieDetail.release_date }}</p>
          <div>
          <p>overview: {{ movieDetail.overview | maxlength(300, '...') }}</p>
          </div>
          <p>평점: {{ movieDetail.vote_average }}</p>
          <p>{{ movieDetail.genres }}</p>
        <div>
          Likeit: {{ likeCount }} 
          <br>
          <button @click="likeMovie(movieNum)">좋아요</button>
          {{ likecount }}
        </div>
      </div>
      </div>
    </div>
    <div>
      <p>코멘트</p>
      <p>vue파일 만들어야됨</p>
    </div> -->
    <!-- ---- -->
    <div class="movie-detail-card">
      <div class="movie-detail-toolbar">
        <!-- <v-btn
          icon
          dark
          @click="dialog = false">
          <v-icon>mdi-close</v-icon>
        </v-btn> -->
        <!-- <img id="logo-image" src="@/assets/images/logo.png"/> -->
      </div>
      <div class="movie-detail-body">
        <div class="movie-detail-poster">
          <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movieDetail.poster_path}`" alt="포스터 없음">
        </div>
        <div class="movie-detail-info">
          <!-- info header -->
          <div class="movie-detail-upper">
            <div class="movie-detail-info-header">
              <div class="movie-detail-info-header-left">
                <div class="movie-detail-title">
                  {{ movieDetail.title }}
                </div>
                <div
                class="movie-release-date">
                  개봉  : {{ movieDetail.release_date }}
                </div>
                <div>
                  {{ movieDetail.genres }}
                </div>
              </div>
              <div class="movie-detail-info-header-right">
                <div class="movie-vote">
                  {{ movieDetail.vote_average }}
                </div>
                <img id="movie-star" src="@/assets/images/star.png">
              </div>
            </div>
            <!-- info overview -->
            <div class="movie-detail-overview-header">
              줄거리
            </div>
            <hr>
            <div class="movie-detail-overview-body">
              {{ movieDetail.overview | maxlength(430, '...') }}
            </div>
          </div>
          <div class="movie-detail-lower">
            <!-- youtube -->
            <div class="movie-youtube-area">
              관련 영상
              <hr>
              <YoutubeList :title="movieDetail.title"/>
              {{ youtubeVideos }}
            </div>
          </div>
        </div>
      </div>
    </div>
  <!-- --- -->
    <movie-comment-form></movie-comment-form>
    <movie-comment-item></movie-comment-item>
    <movie-comment-list></movie-comment-list>
  </div>
</template>

<script>
import MovieCommentForm from '@/components/movies/MovieCommentForm.vue'
import MovieCommentItem from '@/components/movies/MovieCommentItem.vue'
import MovieCommentList from '@/components/movies/MovieCommentList.vue'
import YoutubeList from '@/components/movies/YoutubeList'

import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'MovieDetail',
  components: {
    MovieCommentForm,
    MovieCommentItem,
    MovieCommentList,
    YoutubeList,
  },
  data() {
    return {
      movieNum: this.$route.params.movieNum,
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
    }
  },
  props: {
    movieDetail: {
      type: Object,
      required: true
    },
  },
  filters: {
  maxlength: function (text, stop, clamp) {
    return text.slice(0, stop) + (stop < text.length ? clamp || '...' : '')
    }
  },
  computed: {
    ...mapGetters(['movieDetail', 'youtubeVideos']),
    likeCount() {
      return this.movieDetail.like_count
    },
  },
  methods: {
    ...mapActions(['fetchMovieDetail', 'likeMovie'])
  },
  created() {
    this.fetchMovieDetail(this.movieNum)
  },
}
</script>

<style>
/* .detail_box {
  align-items: center;
  justify-content: center;
}
.detail_img {
  margin: 3rem;
}
.detail_text {
  text-align: start;
  width: 30rem;
}
.detail_text > h1 {
  margin-top: 1rem;
} */

/* --- */
.movie-detail-card {
  font-family: 'Noto Sans KR', sans-serif;
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  padding: 2rem;
  min-height: 100%;
  height: auto;
}

/* .movie-detail-toolbar {
  height: 56px;
} */

.movie-detail-body {
  display: flex;
  flex-flow: row wrap;
  margin: 1rem;
  justify-content: center;
}

.movie-detail-info {
  display: flex;
  flex-flow: column wrap;
  justify-content: space-between;
  margin: 1rem 0 0 4rem;
  width: 60%;
}

.movie-detail-info-header {
  display: flex;
  flex-flow: row nowrap;
  justify-content: space-between;
  height: 70px;
}
.movie-detail-poster > img {
  width: 390px;
}

.movie-detail-title {
  font-size: 40px;
}

.movie-detail-info-header-right {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
}

.movie-vote {
  font-size: 30px;
}

#movie-star {
  height: 50%;
  margin-left: 1rem;
}

.movie-detail-overview-header {
  margin-top: 5rem;
  font-size: 27px;
}

.movie-detail-overview-body {
  font-size: 17px;
  text-align: start;
}

</style>