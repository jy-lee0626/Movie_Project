<template>
  <div >
    <CommentListForm/>
    <hr>
    <div>
      <CommentListItem
        v-for="comment in comments" 
        :comment="comment" 
        :key="comment.pk"
      />        
    </div>

  </div>
</template>

<script>
import CommentListItem from '@/components/community/CommentListItem.vue'
import CommentListForm from '@/components/community/CommentListForm.vue'
// import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'CommentList',
  components: { CommentListForm, CommentListItem },
  props: { comments: Array },
}
</script>

<style>
</style>