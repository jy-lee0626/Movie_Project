<template>
  <div>
    <img :src="`${profile.profile_image}`" class="profile_image" alt="profile_image" style="width: 300px; ">
    <h1>{{ profile.first_name }}
      <br>
      <small>
        {{profile.username}}
      </small>
    </h1>
    <h2>작성한 글</h2>
      <p v-if="!profile.review_set.length">
        작성한 글이 없습니다.
      </p>
      <p v-else>
        <ul>
          <li v-for="review in profile.review_set" :key="review.id">
            <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }">
              {{ review.title }}
            </router-link>
          </li>
        </ul> 
      </p>
    <hr>
    <h2>좋아요 한 영화</h2>
      <p v-if="!profile.like_movies.length">
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

export default {
  name: 'ProfileView',
  data() {
    return {

    }
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
