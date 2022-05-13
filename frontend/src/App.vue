<template>
  <v-app id="app">
    <v-main>
      <router-view :key="$route.path"/>
    </v-main>

    <zd-modal v-bind="{ name: 'appModal '}" />

    <zd-alert v-bind="{ name: 'appAlert '}" />

    <zd-dialog v-bind="{ name: 'appDialog '}" />

    <zd-loading v-bind="{ name: 'appLoading' }" />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';

@Component
export default class App extends Vue {
  public created() {
  }
}
</script>
