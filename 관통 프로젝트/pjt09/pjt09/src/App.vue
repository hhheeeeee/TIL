<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">      
      <nav class="nav">
        <div class="index">
          <div class="mytitle">MyTube</div>
          <!-- <img alt="movie logo" class="logo" src="@/assets/movieicon.png" width="50" height="50" /> -->
          <div><RouterLink to="/">Home</RouterLink></div>
          <div><RouterLink to="/search">Search</RouterLink></div>
          <div><RouterLink to="/Later">Later</RouterLink></div>

        </div>
      </nav>
    </div>
    <RouterView />
  </header>
</template>

<style scoped>

header {
  margin: 0px 0px;
  padding: 0px 0px;
}
.wrapper{
  margin: 0px 0px;
}

.nav {
  width: 100%;
  height: 60px;
  background-color: darkslategrey;
  padding: 0px 20px;
}

.index {
  width: 35%;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: space-around;
}


.navigation {
  display: flex;
}


a {
  text-decoration:none; 
  color: darkgrey
}

.mytitle {
  color: white;
  font-weight: bold;
}
</style>
