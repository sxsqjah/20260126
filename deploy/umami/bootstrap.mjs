import { readFile } from 'node:fs/promises'

const envText = await readFile(new URL('.env', import.meta.url), 'utf8')
const config = Object.fromEntries(
  envText
    .split(/\r?\n/)
    .filter((line) => line && !line.startsWith('#'))
    .map((line) => {
      const separator = line.indexOf('=')
      return [line.slice(0, separator), line.slice(separator + 1)]
    }),
)

const baseUrl = `http://127.0.0.1:${config.UMAMI_PORT || '3000'}`

async function request(path, options = {}) {
  const response = await fetch(`${baseUrl}${path}`, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  })

  const body = await response.json().catch(() => null)
  if (!response.ok) {
    throw new Error(`${options.method || 'GET'} ${path} failed (${response.status}): ${JSON.stringify(body)}`)
  }

  return body
}

async function login(password) {
  return request('/api/auth/login', {
    method: 'POST',
    body: JSON.stringify({ username: 'admin', password }),
  })
}

let auth
let passwordChanged = false

try {
  auth = await login(config.UMAMI_ADMIN_PASSWORD)
} catch {
  auth = await login('umami')
  await request(`/api/users/${auth.user.id}`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${auth.token}` },
    body: JSON.stringify({ password: config.UMAMI_ADMIN_PASSWORD }),
  })
  passwordChanged = true
  auth = await login(config.UMAMI_ADMIN_PASSWORD)
}

const websites = await request('/api/websites?pageSize=100', {
  headers: { Authorization: `Bearer ${auth.token}` },
})

const websiteList = Array.isArray(websites) ? websites : websites.data || []
let website = websiteList.find((item) => item.domain === 'ckqpro.com')

if (!website) {
  website = await request('/api/websites', {
    method: 'POST',
    headers: { Authorization: `Bearer ${auth.token}` },
    body: JSON.stringify({ name: 'Crypto-K Quants', domain: 'ckqpro.com' }),
  })
}

console.log(`ADMIN_PASSWORD_CHANGED=${passwordChanged}`)
console.log(`UMAMI_WEBSITE_ID=${website.id}`)

const endAt = Date.now() + 60_000
const startAt = endAt - 60 * 60 * 1000
const stats = await request(
  `/api/websites/${website.id}/stats?startAt=${startAt}&endAt=${endAt}`,
  { headers: { Authorization: `Bearer ${auth.token}` } },
)

console.log(`LAST_HOUR_PAGEVIEWS=${stats.pageviews}`)
console.log(`LAST_HOUR_VISITORS=${stats.visitors}`)
