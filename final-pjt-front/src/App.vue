<template>
  <div id="app">
<nav class="navbar navbar-expand-lg navbar-dark" style="background-color: #a29bfe;">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">인기영화</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">현재 상영작</a>
        </li>
      </ul>
      <ul class="navbar-nav ml-auto mt-2 mt-lg-0" v-if="login">
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
          <router-link class="nav-link" :to="{ name: 'Login' }">Login</router-link>
        </li>
        <li class="nav-item">
          <router-link class="nav-link" :to="{ name: 'Signup' }">SignUp</router-link>
        </li>
      </ul>
    </div>
  </div>
</nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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
</style>
