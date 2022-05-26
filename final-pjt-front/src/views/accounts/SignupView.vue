<template>
  <div>
    <account-error-list v-if="authError"></account-error-list>

    <div class="background_login">
        <div class="shape_login"></div>
        <div class="shape_login"></div>
    </div>
    <form class="form_login" @submit.prevent="signup(credentials)">
      <h3>Signup Here</h3>
      <div>
        <input  class="input_login" placeholder="Username" v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <input class="input_login" placeholder="Password" v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <input class="input_login" placeholder="Confirm Password" v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <input class="input_login" placeholder="Firstname" v-model="credentials.first_name" type="text" id="first_name" required />
      </div>

      <div class="form-check form-check-inline mt-4">
        <input v-model="credentials.gender" class="form-check-input" type="radio" name="Male" id="Male" value="Male">
        <label class="form-check-label" for="Male">Male</label>
      </div>
      <div class="form-check form-check-inline">
        <input v-model="credentials.gender" class="form-check-input" type="radio" name="Female" id="Female" value="Female">
        <label class="form-check-label" for="Female">Female</label>
      </div>


        <button class="button_login" style="margin-top: 2rem;">Sign up</button>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/accounts/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
          first_name: '',
          gender: '',
          profile: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style></style>