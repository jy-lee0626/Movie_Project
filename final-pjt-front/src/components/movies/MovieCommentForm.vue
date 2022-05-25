<template>
  <div>
    <form class="d-flex justify-content-center align-items-end" @submit.prevent="onSubmit">
      <!-- <label for="comment">comment: </label> -->
      <input class="comment_input" type="text" id="comment" placeholder="댓글을 남겨주세요" v-model="content" required>
      <!-- <input type="number" step="0.5" v-model="rank"> -->
      <form class="rating">
        <label>
          <input type="radio" name="stars" value="1" v-model="rank"/>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="2" v-model="rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="3" v-model="rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>   
        </label>
        <label>
          <input type="radio" name="stars" value="4" v-model="rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
        <label>
          <input type="radio" name="stars" value="5" v-model="rank"/>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
          <span class="icon">★</span>
        </label>
      </form>
      <button class="button_comment">댓글</button>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'
export default {
  name: "MovieCommentForm",
  data() {
    return {
      content: '',
      rank: 0
    }
  }, 
  props: {
    moviedetail: Object 
  },
  computed: {
    ...mapGetters(['movieDetail'])
  },
  methods: {
    ...mapActions(['createMovieComment']),
    onSubmit() {
      this.createMovieComment({ movieNum: this.moviedetail.movie_num, content: this.content, rank: this.rank })
      this.content = ''
      this.rank = 0
    }
  }
}
</script>

<style>
.comment-list-form {
  border: 1px solid white;
  margin: 1rem;
  padding: 1rem;
}
.comment_input {
  width: 380px;
  margin: 0 1rem 0 0;
  padding: 8px;
  outline: 0;
}
.comment_input::placeholder {
  font-weight: bold;
  color: grey;
  opacity: 1;
}
/* --- 버튼 css */
.button_comment {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  
  background: var(--button-bg-color);
  color: var(--button-color);
  
  margin: 0;
  padding: 0.5rem 1rem;
  
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 1rem;
  font-weight: 400;
  text-align: center;
  text-decoration: none;
  
  border: none;
  border-radius: 4px;
  
  display: inline-block;
  width: auto;
  
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  
  cursor: pointer;
  
  transition: 0.5s;
  --button-bg-color: #28a745;
  --button-hover-bg-color: #218838;
}
.button_comment:active,
.button_comment:hover,
.button_comment:focus {
  background: var(--button-hover-bg-color);
  outline: 0;
}


/* ---별 css */
.rating {
  display: inline-block;
  position: relative;
  height: 50px;
  line-height: 50px;
  font-size: 30px;
  margin: 0 1rem 0 0;
}

.rating label {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  cursor: pointer;
}

.rating label:last-child {
  position: static;
}

.rating label:nth-child(1) {
  z-index: 5;
}

.rating label:nth-child(2) {
  z-index: 4;
}

.rating label:nth-child(3) {
  z-index: 3;
}

.rating label:nth-child(4) {
  z-index: 2;
}

.rating label:nth-child(5) {
  z-index: 1;
}

.rating label input {
  position: absolute;
  top: 0;
  left: 0;
  opacity: 0;
}

.rating label .icon {
  float: left;
  color: transparent;
}

.rating label:last-child .icon {
  color: white;
}

.rating:not(:hover) label input:checked ~ .icon,
.rating:hover label:hover input ~ .icon {
  color: yellow;
}

.rating label input:focus:not(:checked) ~ .icon:last-child {
  color: #000;
  text-shadow: 0 0 5px #09f;
}
</style>