import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath, URL } from 'node:url'
import path from 'node:path'

const apkDownloadHeaders = () => ({
  name: 'apk-download-headers',
  configureServer(server) {
    server.middlewares.use((req, res, next) => {
      if (!req.url) {
        return next()
      }

      const pathname = req.url.split('?')[0]
      if (!pathname.startsWith('/downloads/')) {
        return next()
      }

      const filename = path.posix.basename(pathname)
      if (filename.endsWith('.apk')) {
        res.setHeader('Content-Type', 'application/vnd.android.package-archive')
        res.setHeader('Content-Disposition', `attachment; filename="${filename}"`)
      } else if (filename.endsWith('.ipa')) {
        res.setHeader('Content-Type', 'application/octet-stream')
        res.setHeader('Content-Disposition', `attachment; filename="${filename}"`)
      }

      return next()
    })
  },
  configurePreviewServer(server) {
    server.middlewares.use((req, res, next) => {
      if (!req.url) {
        return next()
      }

      const pathname = req.url.split('?')[0]
      if (!pathname.startsWith('/downloads/')) {
        return next()
      }

      const filename = path.posix.basename(pathname)
      if (filename.endsWith('.apk')) {
        res.setHeader('Content-Type', 'application/vnd.android.package-archive')
        res.setHeader('Content-Disposition', `attachment; filename="${filename}"`)
      } else if (filename.endsWith('.ipa')) {
        res.setHeader('Content-Type', 'application/octet-stream')
        res.setHeader('Content-Disposition', `attachment; filename="${filename}"`)
      }

      return next()
    })
  },
})

export default defineConfig({
  plugins: [apkDownloadHeaders(), vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    port: 5175,
    strictPort: true,
    open: true
  }
})
