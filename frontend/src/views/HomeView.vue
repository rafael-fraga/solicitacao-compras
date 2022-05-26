<template>
<div>
  <Estoque class="card"/>
  <InputPedido />
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  import Estoque from '../components/Estoque/GridEstoque.vue'

  export default Vue.extend({
    name: 'MainPage',

    components: {
      Estoque,
    },
  })
</script>
<style scoped>
.card {
  padding: 20px 50px 20px 50px;
}
</style>