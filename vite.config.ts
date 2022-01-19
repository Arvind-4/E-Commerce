import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';

export default defineConfig({
  plugins: [solidPlugin()],
  root: './src',
  build: {
    target: 'esnext',
    manifest: true,
    polyfillDynamicImport: false,
    minify: true,
    outDir: '../dist', 
  },
});
