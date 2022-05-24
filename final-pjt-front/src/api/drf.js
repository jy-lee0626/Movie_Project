const HOST = 'http://localhost:8000/api/v1/'

const ACCOUNTS = 'accounts/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const MOVIES = 'movies/'
const BASE_URL = 'https://api.themoviedb.org/3/'
const KEY = '?api_key=03f03c44041dd5b89d9605ef7395f631&language=ko-KR&page=1'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
    recommendUser: username => HOST + ACCOUNTS + 'profile/' + username + '/user_match/',
  },
  articles: {
    articles: () => HOST + ARTICLES,
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
  movies: {
    movies: () => HOST + MOVIES,
    search: (searchdata) => HOST + MOVIES + 'search/' + `${searchdata}`, 
  },
  nowplaying: {
    nowplaying: () => HOST + MOVIES + 'nowplaying/',
  },
  upcoming: {
    upcoming: () => BASE_URL + 'movie/upcoming' + KEY
  },
  popular: {
    popular: () => BASE_URL + 'movie/popular' + KEY
  },
  tvshow: {
    tvshow: () => BASE_URL + 'tv/popular' + KEY
  },
  moviedetail: {
    moviedetail: (movieNum) => HOST + MOVIES + `${movieNum}/`,
  }
}
