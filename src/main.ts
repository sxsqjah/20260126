import { createApp } from 'vue'
import { createI18n } from 'vue-i18n'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'
import { useI18nStore } from './stores/i18n'

import './assets/main.css'

// 导入翻译文件
import zhCN from './locales/zh-CN.json'
import koKR from './locales/ko-KR.json'
import enUS from './locales/en-US.json'
import jaJP from './locales/ja-JP.json'

const pinia = createPinia()

// 初始化 i18n store
const i18nStore = useI18nStore(pinia)
i18nStore.initLocale()

// 配置 i18n
const i18n = createI18n({
  legacy: false,
  locale: i18nStore.locale,
  fallbackLocale: 'en-US',
  messages: {
    'zh-CN': zhCN,
    'ko-KR': koKR,
    'en-US': enUS,
    'ja-JP': jaJP
  }
})

const app = createApp(App)

app.use(pinia)
app.use(router)
app.use(i18n)

app.mount('#app')

