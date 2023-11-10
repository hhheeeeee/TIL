<template>
  
  <div class="container1">
    <img class="backgroundimg" src="@/assets/background.gif" alt="">
    <h1 class="title">Your Video App</h1>
  </div>
  
</template>

<script setup>

</script>

<style scoped>
.container1 {
  margin: 0px 0px;
  padding: 0px 0px;
  width: 100%;
  position: relative;

} 
.backgroundimg {
  width:100%;
  height:100%;
  object-fit: cover;
}

.title {
  position: absolute;
  top: 40%;
  left: 30%;
  color: white;
}
</style>