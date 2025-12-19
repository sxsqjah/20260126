import { defineStore } from 'pinia'

export type Locale = 'zh-CN' | 'ko-KR' | 'en-US'

export const useI18nStore = defineStore('i18n', {
  state: () => ({
    locale: 'zh-CN' as Locale
  }),
  
  actions: {
    setLocale(newLocale: Locale) {
      this.locale = newLocale
      localStorage.setItem('locale', newLocale)
    },
    
    initLocale() {
      const saved = localStorage.getItem('locale') as Locale | null
      if (saved && ['zh-CN', 'ko-KR', 'en-US'].includes(saved)) {
        this.locale = saved
      } else {
        // 根据浏览器语言自动选择
        const browserLang = navigator.language
        if (browserLang.startsWith('ko')) {
          this.locale = 'ko-KR'
        } else if (browserLang.startsWith('zh')) {
          this.locale = 'zh-CN'
        } else {
          this.locale = 'en-US'
        }
      }
    }
  }
})

