<template>
  <div>
    <div class="container">
      <div class="row">
        <div v-if="issearch" class="col">
          <span class="search__span" v-for="data in searchdata" :key="data.id">
            <span v-if="data.poster_path">
              <router-link class="search__item p-3" :to="{ name: 'moviedetail', params: { movieNum: data.id } }" tag="img" :src="`https://www.themoviedb.org/t/p/w220_and_h330_bestv2${data.poster_path}`" alt="포스터 없음"></router-link>
            </span>
          </span>
        </div>
      </div>
    </div>
    <div v-if="!issearch">
      <h2 class="mt-5">검색결과가 없습니다.</h2>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: "SearchData",
  computed: {
    ...mapGetters(['searchdata', 'issearch'])
  }
}
</script>

<style>
.search__item {
  width: 14rem;
  margin: 1.3rem 0;
  transition: 100ms all;
}

.search__item:hover {
  margin: 20px;
  cursor: pointer;
  transition-delay: 0.4s;
  transform: scale(1.2);
}
</style>