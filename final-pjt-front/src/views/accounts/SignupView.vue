<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input  v-model="credentials.userid" type="text" id="userid" required/>
      </div>
      <div>
        <label for="password1">비밀번호: </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">비밀번호 확인:</label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <label for="username">이름: </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          userid: '',
          password1: '',
          password2: '',
          username: '',
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
