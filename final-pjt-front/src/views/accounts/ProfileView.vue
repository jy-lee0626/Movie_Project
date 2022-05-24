<template>
  <div>
    <h1>{{ profile.username }}님의 프로필</h1>

    <h2>작성한 글</h2>
    <!-- <ul>
      <li v-for="article in profile.articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul> -->

    <h2>좋아요 한 글</h2>
    <!-- <ul>
      <li v-for="article in profile.like_articles" :key="article.pk">
        <router-link :to="{ name: 'article', params: { articlePk: article.pk } }">
          {{ article.title }}
        </router-link>
      </li>
    </ul> -->
    <h2>유저 추천</h2>
    {{ recommendUser }}
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
