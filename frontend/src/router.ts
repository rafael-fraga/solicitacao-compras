import Vue from 'vue';
import Router from 'vue-router';
import { components } from '@zeedhi/vuetify';

const { ZdFramePage } = components;

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: ZdFramePage,
      props: () => ({
        path: 'home',
        local: true,
      }),
    },
    {
      path: '*',
      component: ZdFramePage,
      props: {
        path: 'notfound',
        local: true,
      },
    },
  ],
});

export default router;
