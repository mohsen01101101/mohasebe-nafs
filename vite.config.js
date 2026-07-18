import { defineConfig } from "vite";


export default defineConfig({
    build: {
        rollupOptions: {
            input: "./src/js/main.js",
            output: {
                entryFileNames: "bundle.js",
            },
        },
        outDir: "static/js",
        emptyOutDir: false,
    },
});
