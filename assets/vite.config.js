import { defineConfig } from 'vite';
import { path } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: './src/main.js',
        frames: './src/frames.js'
        // secondary: './src/secondary.js'
      },
      output: {
        entryFileNames: '[name].js',
        chunkFileNames: '[name].js',
        assetFileNames: '[name][extname]'
      }
    },
    outDir: '../cmsmc/static',
    assetsDir: '',
    minify: true,
    sourcemap: false
  }
})
