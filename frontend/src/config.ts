import { IConfig } from '@zeedhi/core';

const config: IConfig = {
  endPoint: process.env.VUE_APP_END_POINT,
  metadataEndPoint: process.env.VUE_APP_METADATA_END_POINT,
};

export default config;
