import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
  base: "/build/",

  plugins: [tailwindcss()],

  build: {
    rollupOptions: {
      input: "./src/js/main.js",
      output: {
        entryFileNames: "js/bundle.js",
        assetFileNames: (assetInfo) => {
          if (assetInfo.name.endsWith(".css")) {
            return "css/bundle.css";
          }
          return "assets/[name][extname]";
        },
      },
    },

    outDir: "static/build",
  },
});
