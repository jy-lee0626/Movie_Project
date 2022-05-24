<template>
  <div>
    <search-data></search-data>
  </div>
</template>

<script>
import SearchData from '@/components/movies/SearchData.vue'

import { mapGetters } from 'vuex'

export default {
  name: "SearchDataView",
  components: { SearchData },
  computed: {
    ...mapGetters(['searchdata'])
  }
}
</script>

<style>

</style>