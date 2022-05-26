<template>
  <div>
    <div>
      <table class="table" style="color: white;">
        <thead>
          <tr>
            <th scope="col">글쓴이</th>
            <th scope="col">제목</th>
            <th scope="col" class="w-25">등록 시간</th>
          </tr>
        </thead>
        <tbody >
          
          <tr v-for="review in reviewlist" :key="review.id" style="position: relative;">
            <th scope="row" style="font-weight: normal;">{{review.user.first_name}}</th>
            <td style="font-weight: normal;">
              <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }" style="text-decoration: none; color: white;">
                {{ review.title }} 
              </router-link></td>
            <td  style="font-size: 0.8rem;">{{review.created_at|formatDate}}</td>
            
          </tr>
        </tbody>
      </table>

    </div>
    <!-- <ul class="review_list p-0">
      <li v-for="review in reviewlist" :key="review.pk" 
      class="review-lisat-item" style="position: relative;">
        <router-link :to="{ name: 'ReviewDetail', params: { reviewNum: review.id } }"
        style="text-decoration: none; 
        color: white; 
        font-weight: bold; 
        margin-right: 1rem;">
          {{ review.id }} 
        </router-link>

        <span 
        style="position: absolute; bottom: 1rem; right: 5rem">
          {{ review.created_at | formatDate }}
        </span>
        <hr>
      </li>
    </ul>  -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'
import moment from 'moment'

export default {
  name: "ReviewList",
  computed: {
    ...mapGetters(['reviewlist']),
  },
  filters: {
    formatDate (value) {
      console.log(value)
      if (value) {
        return moment(String(value)).format('MM/DD/YYYY hh:mm')
      }
    },
  },
  methods: {
    ...mapActions(['fetchReviews',])
  },
  created() {
    this.fetchReviews()
  }
}
</script>

<style>
.review-lisat-item {
  list-style-type: none;
  font-size: 1.5rem;
}
</style>