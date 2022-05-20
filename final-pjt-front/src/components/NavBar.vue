<template>
  <nav class="navbar navbar-expand-lg sticky-top navbar-dark" style="background-color: #a29bfe;">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Navbar</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">현재 상영작</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">인기 영화</a>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="isLoggedIn">
          <b-avatar v-b-toggle.sidebar-footer :src="profile.profileurl" class="mr-3"></b-avatar>
          <li class="nav-item mr-2" style="line-height: 0; margin-top: 8%;">
            <span class="text-white mb-0">{{user}} 님 환영합니다.</span>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" @click.native="logout" to="#">Logout</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-else>
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