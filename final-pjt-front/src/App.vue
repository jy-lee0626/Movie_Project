<template>
  <div id="app">
    <nav-bar></nav-bar>
    <br/>
    <router-view :key="$route.fullPath"></router-view>
      <!-- <button
        type="button"
        class="btn btn-danger btn-floating btn-lg"
        id="btn-back-to-top"
        >
        <i class="fas fa-arrow-up"></i>
      </button> -->
    <foo-ter></foo-ter>
  </div>
</template>

<script>
  // import './assets/js/up.js'
  import NavBar from '@/components/NavBar.vue'
  import FooTer from '@/components/FooTer.vue'

  import { mapActions } from 'vuex'

  export default {
    name: 'App',
    components: { NavBar, FooTer},
    methods: {
      ...mapActions(['fetchCurrentUser'])
    },
    created() {
      this.fetchCurrentUser()
    }
  }
</script>


<style>
/* html, body {    margin: 0;    height: 100%;    overflow: hidden;} */
#app {
  /* font-family: Avenir, Helvetica, Arial, sans-serif; */
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
}

/* #wrapper{
  height: auto;
  min-height: 100%;
  padding-bottom: 20rem;
} */

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.profile_image {
  border-radius: 50%;
}
</style>
