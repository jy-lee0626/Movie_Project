<template>
  <div>
    <h1>Signup</h1>

    <account-error-list v-if="authError"></account-error-list>

    <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">아이디: </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
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
        <label for="firstname">이름:</label>
        <input v-model="credentials.first_name" type="text" id="first_name" required />
      </div>
      
      <div class="form-check form-check-inline">
        <input v-model="credentials.gender" class="form-check-input" type="radio" name="Male" id="Male" value="Male">
        <label class="form-check-label" for="Male">남자</label>
      </div>
      <div class="form-check form-check-inline">
        <input v-model="credentials.gender" class="form-check-input" type="radio" name="Female" id="Female" value="Female">
        <label class="form-check-label" for="Female">여자</label>
      </div>
      
      <!-- <div class="input-group mb-3">
        <input type="file" class="form-control" id="profile">
        <label class="input-group-text" for="profile">Upload</label>
      </div> -->
      <div>
        <button>가입하기</button>
      </div>
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
