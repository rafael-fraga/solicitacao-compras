<template>
  <v-app id="app">
    <component v-if="$route.name !== 'login'" :is="menu.component" v-bind="menu"></component>
    <component v-if="$route.name !== 'login'" :is="header.component" v-bind="header"></component>

    <v-main>
      <router-view :key="$route.path"/>
    </v-main>

    <!-- Modal -->
    <zd-modal v-bind="{ name: 'appModal '}" />

    <!-- Alert -->
    <zd-alert v-bind="{ name: 'appAlert '}" />

    <!-- Dialog -->
    <zd-dialog v-bind="{ name: 'appDialog '}" />

    <!-- Loading -->
    <zd-loading v-bind="{ name: 'appLoading' }" />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import Component from 'vue-class-component';
import { IMenu, IHeader } from '@zeedhi/common';

@Component
export default class App extends Vue {
  public menu!: IMenu;

  public header!: IHeader;

  public created() {
    this.menu = {
      component: 'ZdMenu',
      name: 'main-menu',
      cssClass: 'main-menu',
      app: true,
      clipped: true,
      floating: true,
      mini: false,
      miniWidth: 58,
      mobileBreakpoint: 800,
      closeToMini: true,
      isLocal: true,
      isVisible: true,
      itemsUrl: 'menu',
    };

    this.header = {
      component: 'ZdHeader',
      name: 'main-header',
      app: true,
      color: 'white',
      cssClass: 'main-header',
      height: 64,
      leftSlot: [
        {
          name: 'menu-button',
          component: 'ZdMenuButton',
          menuName: 'main-menu',
          small: true,
          keyMap: {
            'ctrl+m': {
              event: '{{AppController.toggleMenu}}',
            },
          },
        },
        {
          name: 'headerImage',
          component: 'ImgLink',
          src: '/img/logo.svg',
          to: '/',
        },
      ],
      rightSlot: [
        {
          name: 'logout-button',
          component: 'ZdButton',
          icon: true,
          to: '/login',
          iconName: 'mdi-logout',
        },
      ],
    };
  }
}
</script>
