import Vue from 'vue'
import VueCookies from 'vue-cookies'

import App from './App.vue'
import router from './router'
import store from './store'

import './assets/js/home.js'


Vue.config.productionTip = false

Vue.use(VueCookies)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
