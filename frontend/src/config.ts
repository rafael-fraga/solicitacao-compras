import { IConfig } from '@zeedhi/core';

const config: IConfig = {
  endPoint: process.env.VUE_APP_END_POINT,
  metadataEndPoint: process.env.VUE_APP_METADATA_END_POINT,
  env: {
    productId: process.env.VUE_APP_PRODUCT_ID,
    authUrl: process.env.VUE_APP_AUTH_URL || process.env.VUE_APP_END_POINT,
  },
};

export default config;
