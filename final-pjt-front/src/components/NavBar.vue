<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark" style="background-color: black;">
    <div class="container-fluid">
      <router-link class="navbar-brand" style="color: pink;" :to="{ name: 'MovieListView' }">Navbar</router-link>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item active">
            <router-link class="nav-link" :to="{ name: 'MovieListView' }">Home</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'nowplaying' }">현재 상영작</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">인기 영화</a>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'test' }">TEST</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="isLoggedIn">
          <li class="nav-item mr-2 user_css">
            <router-link class="nav-link text-white" :to="{ name: 'profile', params: { username } }">{{ currentUser.username }}님</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'logout' }">Logout</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="!isLoggedIn">
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'login' }">Login</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'signup' }">SignUp</router-link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
  }
</script>

<style>

</style>