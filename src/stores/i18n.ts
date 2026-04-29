import { defineStore } from 'pinia'

const supportedLocales = ['zh-CN', 'zh-TW', 'ko-KR', 'en-US', 'ja-JP'] as const
export type Locale = typeof supportedLocales[number]

const geoIpUrl = 'https://ipwho.is/?fields=country_code'
const localeStorageKey = 'locale'
const localePreferenceSourceKey = 'localePreferenceSource'
const manualPreferenceSource = 'manual'

function mapCountryToLocale(countryCode: string | null): Locale {
  switch (countryCode?.toUpperCase()) {
    case 'CN':
      return 'zh-CN'
    case 'TW':
    case 'HK':
      return 'zh-TW'
    case 'KR':
      return 'ko-KR'
    case 'JP':
      return 'ja-JP'
    default:
      return 'en-US'
  }
}

function isSupportedLocale(value: string | null): value is Locale {
  return supportedLocales.includes(value as Locale)
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
      localStorage.setItem(localeStorageKey, newLocale)
      localStorage.setItem(localePreferenceSourceKey, manualPreferenceSource)
    },
    
    async initLocale() {
      const saved = localStorage.getItem(localeStorageKey)
      const preferenceSource = localStorage.getItem(localePreferenceSourceKey)

      if (isSupportedLocale(saved) && preferenceSource === manualPreferenceSource) {
        this.locale = saved
        return
      }

      const countryCode = await fetchCountryCode()
      this.locale = mapCountryToLocale(countryCode)

      if (saved && !isSupportedLocale(saved)) {
        localStorage.removeItem(localeStorageKey)
      }
    }
  }
})
