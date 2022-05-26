<template>
  <div class="profile-card w-75">
    <div class="user-information d-flex  justify-content-between">
      <div class="m-3">
        <img :src="`${profile.profile_image}`" class="profile_image" alt="profile_image" style="width: 200px; ">
      </div>
      <div class="w-50 container container d-flex justify-content-center align-items-center">
        <div class="h-50">
          <h1>{{ profile.first_name }}
            <br>
          </h1>
          <p>
            {{profile.username}}
          </p>

        </div>

      </div>

    </div>
    <h2>작성한 글</h2>
    <hr>
      <p v-if="!profile.review_set.length">

        작성한 글이 없습니다.
      </div>
      <div v-else>
        <table class="table" style="color: white;">
          <thead>
            <tr>
              <th scope="col">제목</th>
              <th scope="col" class="w-25">등록 시간</th>
            </tr>
          </thead>
          <tbody >
            
            <tr v-for="review in profile.review_set" :key="review.id" style="position: relative;">
              <td style="font-weight: normal;">
                <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }" style="text-decoration: none; color: white;">
                  {{ review.title }} 
                </router-link></td>
              <td  style="font-size: 0.8rem;">{{review.created_at|formatDate}}</td>
              
            </tr>
          </tbody>
        </table>
      </div>
    <hr>
    <h2>좋아요 한 영화</h2>
      <p v-if="!profile.like_movies.length">
        <br>
        재미있게 본 영화를 추천해주세요
        
      </p>
      <div class="container d-flex" v-else>
        <div class="row" >
          <span class="m-1 col" v-for="movie in profile.like_movies" :key="movie.movie_num">
            <router-link class="text-decoration-none text-white" :to="{ name: 'moviedetail', params: { movieNum: movie.movie_num } }">
              <img :src="`https://www.themoviedb.org/t/p/w300_and_h450_bestv2${movie.poster_path}`" alt="poster" style="width: 120px; ">
              <br>
              {{movie.title}}
            </router-link>
          </span>
        </div>
      </div>
    <hr>
    <div v-if="currentUser.username === profile.username">
      <h2>유저 추천</h2>
      <br>
        <div>
          <router-link :to="{ name: 'profile', params: { username: recommendUser.username } }">
            <img link :src="`${recommendUser.profile_image}`" alt="profile_image" class="profile_image" style="width: 100px;">
          </router-link>
          <p>
            {{ recommendUser.first_name}}
          </p>
        </div>
      </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
import moment from 'moment'

export default {
  name: 'ProfileView',
  data() {
    return {

    }
  },
  filters: {
    formatDate (value) {
      console.log(value)
      if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
      }
    },
  },
  computed: {
    ...mapGetters(['profile', 'recommendUser', 'currentUser']),
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchRecommendUser']),

  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.fetchRecommendUser(payload)
  },
}
</script>

<style scoped>

  .profile-card {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    padding: 2rem;
    width: 80%;
    max-width: 1000px;
    min-height: 100%;
    margin: auto;
    height: auto;
  }
</style>