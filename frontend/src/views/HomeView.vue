<template>
  <GridView />
</template>

<script lang="ts">
  import Vue from 'vue'
  import GridView from '../components/GridView.vue'
  // import EstoqueView from '../components/EstoqueView.vue'

  export default Vue.extend({
    name: 'MainPage',

    components: {
      GridView,
      // EstoqueView,
    },
  })
</script>
