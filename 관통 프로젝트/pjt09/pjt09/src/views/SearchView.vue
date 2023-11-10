<template>
  <div class="container">
    <div class="back" @click="gohome"> 🡸 뒤로가기</div>
    <div class="searcharea">
      <h1>비디오 검색</h1>
      <div class="input-group mb-3">
        <input type="text" class="form-control"
                          @input="onInput" :value="inputKeyword"
                          placeholder="검색어로 입력해주세요" aria-label="Recipient's username" aria-describedby="basic-addon2">
        <div class="input-group-append">
          <button class="btn btn-success" type="button" @click="clicksearchbutton">찾기</button>
        </div>
      </div>
    </div>
    <div class="searchresult">
      <div v-for="video in videos">
        <div class="videocard" @click="goDetail(video)">
          <img class='thumbnail' :src="video.snippet.thumbnails.default.url" alt="">
          <div class="videotitle">{{ video.snippet.title }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
// 사용자 입력값 받을 부분
const inputKeyword = ref('')

// 검색한 영상들이 담길 리스트
const videos = ref([])


// Youtube API KEY
const API_KEY = import.meta.env.VITE_MYAPIKEY;

// 최대 검색 갯수
const maxSearch = ref(25)


// 양뱡향바인드를 통해 입력값 받기
const onInput = function (event) {
  inputKeyword.value = event.currentTarget.value
}

const clicksearchbutton = function(event){
  
  // 검색결과 API
  const youtubeURL = `https://youtube.googleapis.com/youtube/v3/search?part=snippet&maxResults=${maxSearch.value}&q=${inputKeyword.value}&key=${API_KEY}&type=video`
  
  axios.get(youtubeURL)
  .then((response) => {
    videos.value = response.data.items
  }).catch((error) => {
    console.log(error)
  })
  
} 

const gohome = function () {
  router.push(`/`)
}

const goDetail = function (video) {
  router.push(`/${video.id.videoId}`)
}

</script>

<style scoped>
.container {
  width: 90%;
  /* border: 1px solid black; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  margin: auto;
}

.back {
  margin: 10px;
}

.searchresult {
  display: flex;
  flex-wrap: wrap;
  margin: 30px;
}
.videocard {
  width: 300px;
  height: 300px;
  border: 1px solid black;
  margin: 20px;
  border-radius: 5px;
  
}

.thumbnail{
  width: 300px;
  height: 200px;
  object-fit: fill;
  border-radius: 5px 5px 0px 0px;

}

.videotitle{
  margin-top: 10px;
  text-align: center;
}

</style>
