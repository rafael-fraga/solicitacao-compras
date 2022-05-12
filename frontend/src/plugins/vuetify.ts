import { Vuetify } from '@zeedhi/vuetify';
import '@mdi/font/css/materialdesignicons.css';
import { initTheme } from '@zeedhi/common';
import theme from '../theme';

export default new Vuetify({
  icons: {
    iconfont: 'mdi',
  },
  theme: initTheme(theme),
});
