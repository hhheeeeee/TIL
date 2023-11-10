<template>
    <div class="container">
      <div class="back" @click="goback"> 🡸 뒤로가기</div>
      <h1>나중에 볼 동영상</h1>
      <div class="laterresult">
        <div v-if="laterVideos.length > 0">
          <div v-for="video in laterVideos">
            <div class="videocard">
              <img class='thumbnail' :src="video.items[0].snippet.thumbnails.default.url" alt="" @click="goDetail(video)">
              <div class="videotitle">{{ video.items[0].snippet.title }}</div>
              <div>
              </div><button type="button" class="btn btn-danger" @click="remove(video)">목록에서 삭제</button>
            </div>
          </div>
        </div>
        <div v-else>
          <h1>텅~~~</h1>
        </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const laterVideos = ref(null)
laterVideos.value = JSON.parse(localStorage.getItem('later')) || []

const goback = function () {
  router.push(`/`)
}

const goDetail = function (video) {
  router.push(`/${video.items[0].id}`)
}

const remove = (video) => {
  const tmpVideo = laterVideos.value.findIndex((item) => item.items[0].id === video.items[0].id)
  laterVideos.value.splice(tmpVideo, 1)
  localStorage.setItem('later', JSON.stringify(laterVideos.value))
}


// const removeCart = (product) => {
//   // localStoage 에서 삭제
//   // 현재 cartItems.value 에서 삭제
//   // 1. 현재 localStorage 에 저장된 데이터를 가져오기
//   // 이 코드는 valid 하기 위해 한 단계 더 작성했다고 생각하시면 됩니다.
//   // const existingCart = JSON.parse(localStorage.getItem('cart'))

//   // 2. 삭제할 아이템 index 검색
//   const itemIdx = laterVideos.value.findIndex((item) => item.id === product.id)

//   // 3. 데이터 삭제
//   laterVideos.value.splice(itemIdx, 1)

//   // 4. 삭제된 데이터를 기준으로 데이터를 반영
//   localStorage.setItem('cart', JSON.stringify(laterVideos.value))
// }

</script>

<style lang="scss" scoped>

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

.laterresult {
  display: flex;
  flex-wrap: wrap;
  margin: 30px;
}
.videocard {
  width: 300px;
  height: 350px;
  border: 1px solid black;
  margin: 20px;
  border-radius: 5px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  
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

button{
  width: 170px;
  margin: auto;
}

</style>