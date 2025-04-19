const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");


module.exports = {
  mode: 'none',
  entry: {
    main: './js/index.js',
    framed: './js/framed.js',
    now: './js/now.js',
    council: './js/council.js'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, '../static/js')
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              importLoaders: 1
            }
          }
        ]
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '../css/[name].css',
    }),
  ],

};
