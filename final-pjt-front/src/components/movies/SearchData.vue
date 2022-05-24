<template>
  <div>
    {{ searchdata }}
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: "SearchData",
  computed: {
    ...mapGetters(['searchdata'])
  }
}
</script>

<style>

</style>