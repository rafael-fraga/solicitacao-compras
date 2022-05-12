import Vue from 'vue';
import App from './App.vue';
import router from './router';
import { vuetify } from './plugins';
import './components';
import './registerServiceWorker';
import 'roboto-fontface/css/roboto/roboto-fontface.css';
import './styles/style.scss';

Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount('#app');
