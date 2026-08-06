import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";
import fs from "fs";

export default defineConfig({
  base: "/build/",

  plugins: [
    tailwindcss(),

    {
      name: "copy-pwa-files",

      closeBundle() {
        fs.cpSync("src/pwa", "static/build/pwa", { recursive: true });

        fs.cpSync("src/assets/icons", "static/build/assets/icons", {
          recursive: true,
        });
      },
    },
  ],

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
