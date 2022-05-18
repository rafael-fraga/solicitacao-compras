<template>
  <router-link :to="instance.to">
    <v-img
      :src="instance.src"
      class="logo"
    ></v-img>
  </router-link>
</template>

<script lang="ts" src="./ImgLink.ts"></script>
<style scoped>
.logo {
  width: 100px;
}
</style>
