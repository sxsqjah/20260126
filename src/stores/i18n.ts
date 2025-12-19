import { defineStore } from 'pinia'

export type Locale = 'zh-CN' | 'ko-KR' | 'en-US' | 'ja-JP'

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
      if (saved && ['zh-CN', 'ko-KR', 'en-US', 'ja-JP'].includes(saved)) {
        this.locale = saved
      } else {
        // 根据系统默认语言自动选择
        const browserLang = navigator.language || navigator.languages?.[0] || 'en-US'
        const langCode = browserLang.toLowerCase()
        
        // 更精确的语言匹配
        if (langCode.startsWith('ko') || langCode.includes('korean')) {
          this.locale = 'ko-KR'
        } else if (langCode.startsWith('zh-cn') || langCode === 'zh' || langCode.includes('chinese')) {
          this.locale = 'zh-CN'
        } else if (langCode.startsWith('zh-tw') || langCode.startsWith('zh-hk')) {
          // 繁体中文也默认使用简体中文
          this.locale = 'zh-CN'
        } else if (langCode.startsWith('ja') || langCode.includes('japanese')) {
          this.locale = 'ja-JP'
        } else if (langCode.startsWith('en') || langCode.includes('english')) {
          this.locale = 'en-US'
        } else {
          // 默认使用英文
          this.locale = 'en-US'
        }
        
        // 保存自动检测的语言到 localStorage
        localStorage.setItem('locale', this.locale)
      }
    }
  }
})

