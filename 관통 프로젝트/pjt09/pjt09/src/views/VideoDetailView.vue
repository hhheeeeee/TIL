<script setup>
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'

const API_KEY = import.meta.env.VITE_MYAPIKEY;
const router = useRouter()
const route = useRoute()
const video = ref('')
const videoId = route.params.videoId
const videoInfoURL= `https://youtube.googleapis.com/youtube/v3/videos?key=${API_KEY}&part=snippet%2CcontentDetails%2Cstatistics&id=${videoId}`
const videoURL = `http://www.youtube.com/embed/${videoId}`

axios.get(videoInfoURL)
  .then((response) => {
    video.value = response.data
  }).catch((error) => {
    console.error(error)
  })

// const localStorage = JSON.parse(localStorage.getItem('later'))

const addlater = function (video) {
  const existingLater = JSON.parse(localStorage.getItem('later')) || []
  const isDuplicate = existingLater.length > 0 && existingLater.find((item) => item.id === video.id)
    // 중복이 아니라면 추가
    if(!isDuplicate) {
      return false
  } else {
    return true }
}


const addlater1 = function(video) {
  const existingLater = JSON.parse(localStorage.getItem('later')) || []
  const isDuplicate = existingLater.length > 0 && existingLater.find((item) => item.id === video.id)
  // 중복이 아니라면 추가
  if(isDuplicate) {
    alert('나중에 볼 비디오에 추가합니당~')
    existingLater.push(video)
  } else {
    alert('이미 나중에 볼 영상으로 저장한 비디오 입니다!!!!')
  }

  // 수정된 카트 데이터를 localStorage 에 저장
  localStorage.setItem('later', JSON.stringify(existingLater))
  router.push('/later')
}


const goback = function () {
  router.push(`/`)
}

</script>

<template>
  <div class="container">
      <div class="back" @click="goback"> 🡸 뒤로가기</div>
      <div v-if="video">
        <div class="videodetail">
          <h1>{{ video.items[0].snippet.title }}</h1>
          <p class="publishedAt">업로드 날짜 : {{ video.items[0].snippet.publishedAt }}</p>
          <iframe class ="playvideo" type="text/html" width="640" height="360"
                  :src="videoURL"
                  frameborder="0"></iframe>
          <p class="description">{{ video.items[0].snippet.description }}</p>
          <div v-if="addlater(video) == true">
            <button type="button" class="btn btn-primary" @click="addlater1(video)">동영상 저장</button>
          </div>
          <div v-else>
            <button type="button" class="btn btn-primary" @click="addlater1(video)">이미 저장된 비디오</button>
          </div>
        </div>
      </div>
  </div>
</template>


<style scoped>
.container {
    width: 80%;
    /* border: 1px solid black; */
}

.back {
  margin: 20px 0px;
}

.publishedAt {
  color: grey;
}

.description{
  margin-top: 30px;
}
</style>