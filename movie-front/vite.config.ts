import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import nodePolyfills from "rollup-plugin-polyfill-node";
import rollupNodePolyFill from "rollup-plugin-node-polyfills";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    esbuildOptions: {
      // Node.js global to browser globalThis
      define: {
        global: "globalThis", //<-- AWS SDK
      },
    },
  },
  build: {
    outDir: "./build",
    chunkSizeWarningLimit: 2048,
    assetsInlineLimit: 2048, // 2kb
    rollupOptions: {
      plugins: [
        // Enable rollup polyfills plugin
        // used during production bundling
        nodePolyfills(),
      ],
    },
  },
  resolve: {
    alias: [
      {
        find: "events",
        replacement: "rollup-plugin-node-polyfills/polyfills/events",
      },
    ],
  },
  server: {
    cors: true,
    proxy: {
      "/api": {
        target: "https://localhost:9200",
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});
