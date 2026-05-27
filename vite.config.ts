import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig(({ mode }) => ({
  plugins: [react()],
  base:
    mode === 'hr'
      ? '/vite-vtb-himari-profile/hr/'
      : '/vite-vtb-himari-profile/',
}))
