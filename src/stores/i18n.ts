import { defineStore } from 'pinia'

const supportedLocales = ['zh-CN', 'zh-TW', 'ko-KR', 'en-US', 'ja-JP'] as const
export type Locale = typeof supportedLocales[number]

const geoIpUrl = 'https://ipwho.is/?fields=country_code'

function mapCountryToLocale(countryCode: string | null): Locale {
  switch (countryCode) {
    case 'CN':
      return 'zh-CN'
    case 'TW':
      return 'zh-TW'
    case 'KR':
      return 'ko-KR'
    case 'JP':
      return 'ja-JP'
    case 'US':
      return 'en-US'
    default:
      return 'en-US'
  }
}

async function fetchCountryCode(): Promise<string | null> {
  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), 2500)

  try {
    const response = await fetch(geoIpUrl, { signal: controller.signal })
    if (!response.ok) {
      return null
    }
    const data = await response.json()
    if (typeof data.country_code === 'string') {
      return data.country_code.toUpperCase()
    }
    return null
  } catch {
    return null
  } finally {
    clearTimeout(timeoutId)
  }
}

export const useI18nStore = defineStore('i18n', {
  state: () => ({
    locale: 'zh-CN' as Locale
  }),
  
  actions: {
    setLocale(newLocale: Locale) {
      this.locale = newLocale
      localStorage.setItem('locale', newLocale)
    },
    
    async initLocale() {
      const saved = localStorage.getItem('locale') as Locale | null
      if (saved && supportedLocales.includes(saved)) {
        this.locale = saved
      } else {
        const countryCode = await fetchCountryCode()
        this.locale = mapCountryToLocale(countryCode)
        localStorage.setItem('locale', this.locale)
      }
    }
  }
})
