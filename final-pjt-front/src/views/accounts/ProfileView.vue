<template>
  <div>
    <img :src="`${profile.profile_image}`" alt="" style="width: 300px; border-radius: 50% ">
    <h1>{{ profile.first_name }}님의 프로필</h1>

    <h2>작성한 글</h2>
      <p v-if="profile.review_set">
        작성한 글이 없습니다. 
      </p>
      <p v-else>
        <ul>
          <li v-for="article in profile.articles" :key="article.pk">
            <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
              {{ article.title }}
            </router-link>
          </li>

        </ul>
      </p>
    <hr>
    <p>{{profile}}</p>
    <h2>좋아요 한 영화</h2>
      <p v-if="profile.like_movies">
        <ul>
          <li v-for="movie in profile.like_movies" :key="movie.movie_num">
            <router-link :to="{ name: 'moviedetail', params: { movieNum: movie.movie_num } }">
              {{ movie }}
            </router-link>
          </li>
        </ul>
      </p>
      <p v-else>
        재미있게 본 영화를 추천해주세요
      </p>
    <h2>유저 추천</h2>
      <p>
        {{ recommendUser.first_name}}
      </p>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile', 'recommendUser'])
  },
  methods: {
    ...mapActions(['fetchProfile', 'fetchRecommendUser'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
    this.fetchRecommendUser(payload)
  },
}
</script>
