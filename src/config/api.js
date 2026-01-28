// 官网 API 地址配置（可按需修改）

// 开发环境 API 地址
const DEV_API_URL = 'http://154.193.243.23:8080'

// 生产环境 API 地址（请按实际域名修改）
const PROD_API_URL = 'https://home.ckqpro.com/api'

// 是否使用开发环境
const USE_DEV = false

export function getApiBaseUrl() {
  const runtime = typeof window !== 'undefined' ? window.__CKQ_API_BASE_URL : ''
  const runtimeValue = typeof runtime === 'string' ? runtime.trim() : ''
  const base = runtimeValue || (USE_DEV ? DEV_API_URL : PROD_API_URL)
  if (!base) return ''
  return base.endsWith('/') ? base.slice(0, -1) : base
}

export function buildApiUrl(path) {
  const base = getApiBaseUrl()
  if (!base) return path
  if (!path) return base
  if (path.startsWith('/')) return `${base}${path}`
  return `${base}/${path}`
}

export const API_BASE_URL = getApiBaseUrl()
