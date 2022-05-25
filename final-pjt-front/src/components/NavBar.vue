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
          <!-- <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'nowplaying' }">현재 상영작</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">인기 영화</a>
          </li> -->
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'test' }">TEST</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" :to="{ name: 'ReviewsView' }">COMMUNITY</router-link>
          </li>
        </ul>
        <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="isLoggedIn">
          <form class="form-inline active-purple search_form" @submit.prevent="search(searchdata)">
            <input class="form-control form-control-sm search_input_form mt-2" type="search" role="link" v-model="searchdata" placeholder="Search" aria-label="Search">
            <button class="search_button"><i class="fas search_icon fa-search"></i></button>
          </form>
          <li class="nav-item mr-2 user_css">
            <router-link class="nav-link text-white" :to="{ name: 'profile', params: { username } }">
              <img :src="`${currentUser.profile_image}`" alt="" class="profile_image"  style="width: 30px;">
              {{ currentUser.first_name }}님</router-link>
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
  import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'NavBar',
    data() {
      return {
        searchdata: '',
      }
    },
    computed: {
      ...mapGetters(['isLoggedIn', 'currentUser']),
      username() {
        return this.currentUser.username ? this.currentUser.username : 'guest'
      },
    },
    methods: {
      ...mapActions(['search'])
    }
  }
</script>

<style>
.active-purple {
  width: 20rem;
  margin: 0 1rem 0 0;
}
.active-purple-2 input[type=text]:focus:not([readonly]) {
  border-bottom: 1px solid #ce93d8;
  box-shadow: 0 1px 0 0 #ce93d8;
}
.active-purple input[type=text] {
  border-bottom: 1px solid #ce93d8;
  box-shadow: 0 1px 0 0 #ce93d8;
}
.active-cyan-2 input[type=text]:focus:not([readonly]) {
  border-bottom: 1px solid #4dd0e1;
  box-shadow: 0 1px 0 0 #4dd0e1;
}
.active-cyan input[type=text] {
  border-bottom: 1px solid #4dd0e1;
  box-shadow: 0 1px 0 0 #4dd0e1;
}
.active-cyan .fa, .active-cyan-2 .fa {
  color: #4dd0e1;
}
.active-purple .fa, .active-purple-2 .fa {
  color: #ce93d8;
}
.search_icon {
  color: white;
  margin: 0.8rem 0.5rem 0 0;
}
.search_button {
  background-color: black;
}
.search_form {
  margin-right: 0.5rem;
  display: flex;
  height: 20px;
}
.search_input_form {
  margin-right: 0.5rem;
}
</style>