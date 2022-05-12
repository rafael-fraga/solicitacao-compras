module.exports = {
  filenameHashing: true,
  productionSourceMap: process.env.VUE_APP_DEBUG_SOURCEMAP === 'TRUE' ? true : false,
  assetsDir: './assets',
  publicPath: process.env.VUE_APP_PUBLIC_PATH,
  chainWebpack: (config) => {
    config.resolve.symlinks(false);
    /*remove hash from images*/
    config.module
      .rule('images')
      .test(/\.(png|jpe?g|gif)(\?.*)?$/)
      .use('url-loader')
      .loader('url-loader')
      .options({
        name : 'assets/img/[name].[ext]'
      });
  },
  runtimeCompiler: true,
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
          exclude: /node_modules/,
          options: {
            plugins: [
              ['@babel/plugin-proposal-decorators', { legacy: true }],
              '@babel/plugin-proposal-class-properties',
            ]
          }
        },
      ]
    },
    optimization: {
      splitChunks: {
        chunks: 'all',
        maxAsyncRequests: 5,
        maxInitialRequests: Infinity,
        minSize: 20000,
        name: true,
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name(module) {
              let packageName = module.context.match(
                /[\\/]node_modules[\\/](.*?)([\\/]|$)/
              );
              if (packageName[1] === '@zeedhi') {
                packageName = module.context.match(
                  /[\\/]node_modules[\\/](.*?)[\\/](.*?)([\\/]|$)/
                );
                return `npm.${packageName[1].replace('@', '')}.${
                  packageName[2]
                }`;
              } else {
                return `npm.${packageName[1].replace('@', '')}`;
              }
            },
          },
          styles: {
            test: /\.css$/,
            name: 'styles',
            chunks: 'all',
            enforce: true,
          },
        },
      },
    },
  },
};
