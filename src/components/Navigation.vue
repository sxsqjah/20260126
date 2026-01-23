<template>
  <nav class="fixed w-full z-50 bg-brand-dark/90 backdrop-blur-md border-b border-white/5">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-20">
        <div class="flex-shrink-0 cursor-pointer" @click="scrollToTop">
          <span class="text-2xl font-bold font-mono text-white tracking-tighter hover:text-brand-cyan transition duration-300">
            CRYPTO<span class="text-brand-cyan">-K</span> QUANTS
          </span>
        </div>
        
        <div class="hidden md:flex items-center space-x-6">
          <div class="ml-10 flex items-baseline space-x-8">
            <a @click="navigateToSection('features')" class="text-sm font-medium hover:text-brand-cyan transition duration-300 cursor-pointer">
              {{ $t('nav.features') }}
            </a>
            <a @click="navigateToSection('pricing')" class="text-sm font-medium hover:text-brand-cyan transition duration-300 cursor-pointer">
              {{ $t('nav.pricing') }}
            </a>
            <a @click="navigateToSection('footer')" class="text-sm font-medium hover:text-brand-cyan transition duration-300 cursor-pointer">
              {{ $t('nav.contact') }}
            </a>
          </div>
          
          <!-- 语言切换器 - 地球图标按钮 -->
          <div class="relative border-l border-white/10 pl-6">
            <button
              @click="toggleLanguageMenu"
              class="flex items-center gap-2 px-3 py-2 rounded-md text-gray-400 hover:text-white hover:bg-white/10 focus:outline-none transition duration-300"
              :class="{ 'text-brand-cyan': languageMenuOpen }"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span class="text-sm font-medium">{{ currentLanguageName }}</span>
            </button>
            
            <!-- 语言下拉菜单 -->
            <div
              v-show="languageMenuOpen"
              class="absolute right-0 mt-2 w-48 bg-brand-gray border border-white/10 rounded-lg shadow-lg z-50"
            >
              <div class="py-1">
                <button
                  v-for="lang in languages"
                  :key="lang.code"
                  @click="changeLanguage(lang.code)"
                  :class="[
                    'w-full text-left px-4 py-2 text-sm transition duration-300',
                    currentLocale === lang.code
                      ? 'bg-brand-cyan/20 text-brand-cyan'
                      : 'text-gray-300 hover:bg-white/5 hover:text-white'
                  ]"
                >
                  <span class="font-medium">{{ lang.label }}</span>
                  <span class="ml-2 text-xs text-gray-500">{{ lang.name }}</span>
                </button>
              </div>
            </div>
          </div>
          
          <div class="flex items-center gap-3">
            <a @click="navigateToSection('download')" class="font-mono text-xs font-bold text-white border border-white/30 px-4 py-2 rounded hover:bg-white/10 hover:border-white/50 transition duration-300 cursor-pointer">
              {{ $t('nav.appDownload') }}
            </a>
            <a :href="loginUrl" class="font-mono text-xs font-bold text-brand-cyan border border-brand-cyan/50 px-4 py-2 rounded hover:bg-brand-cyan hover:text-brand-dark transition duration-300">
              {{ $t('nav.login') }}
            </a>
          </div>
        </div>

        <div class="flex items-center space-x-4 md:hidden">
          <!-- 移动端语言切换 - 地球图标按钮 -->
          <div class="relative">
            <button
              @click="toggleLanguageMenu"
              class="flex items-center gap-2 px-2 py-2 rounded-md text-gray-400 hover:text-white hover:bg-white/10 focus:outline-none transition duration-300"
              :class="{ 'text-brand-cyan': languageMenuOpen }"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span class="text-xs font-medium hidden sm:inline">{{ currentLanguageName }}</span>
            </button>
            
            <!-- 移动端语言下拉菜单 -->
            <div
              v-show="languageMenuOpen"
              class="absolute right-0 mt-2 w-48 bg-brand-gray border border-white/10 rounded-lg shadow-lg z-50"
            >
              <div class="py-1">
                <button
                  v-for="lang in languages"
                  :key="lang.code"
                  @click="changeLanguage(lang.code)"
                  :class="[
                    'w-full text-left px-4 py-2 text-sm transition duration-300',
                    currentLocale === lang.code
                      ? 'bg-brand-cyan/20 text-brand-cyan'
                      : 'text-gray-300 hover:bg-white/5 hover:text-white'
                  ]"
                >
                  <span class="font-medium">{{ lang.label }}</span>
                  <span class="ml-2 text-xs text-gray-500">{{ lang.name }}</span>
                </button>
              </div>
            </div>
          </div>
          
          <button
            type="button"
            @click="toggleMenu"
            class="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-white/10 focus:outline-none"
          >
            <svg class="h-6 w-6" stroke="currentColor" fill="none" viewBox="0 0 24 24">
              <path
                v-if="!mobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- 移动端菜单 -->
    <div
      v-show="mobileMenuOpen"
      class="md:hidden bg-brand-dark border-b border-white/10 mobile-menu"
    >
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <a
          @click="navigateToSection('features'); toggleMenu()"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan cursor-pointer"
        >
          {{ $t('nav.features') }}
        </a>
        <a
          @click="navigateToSection('pricing'); toggleMenu()"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan cursor-pointer"
        >
          {{ $t('nav.pricing') }}
        </a>
        <a
          @click="navigateToSection('footer'); toggleMenu()"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan cursor-pointer"
        >
          {{ $t('nav.contact') }}
        </a>
        <a
          @click="navigateToSection('download'); toggleMenu()"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan"
        >
          {{ $t('nav.appDownload') }}
        </a>
        <a
          :href="loginUrl"
          class="block px-3 py-2 rounded-md text-base font-medium text-brand-cyan"
        >
          {{ $t('nav.login') }}
        </a>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useI18n } from 'vue-i18n'
import { useRouter, useRoute } from 'vue-router'
import { useI18nStore, type Locale } from '../stores/i18n'
import { getH5LoginUrl } from '../config/h5Login'

const { locale } = useI18n()
const i18nStore = useI18nStore()
const router = useRouter()
const route = useRoute()

const mobileMenuOpen = ref(false)
const languageMenuOpen = ref(false)
const loginUrl = getH5LoginUrl()

const languages = [
  { code: 'zh-CN' as Locale, label: '中', name: '中文' },
  { code: 'zh-TW' as Locale, label: '繁', name: '繁體中文' },
  { code: 'ko-KR' as Locale, label: '한', name: '한국어' },
  { code: 'en-US' as Locale, label: 'EN', name: 'English' },
  { code: 'ja-JP' as Locale, label: '日', name: '日本語' }
]

const currentLocale = computed(() => i18nStore.locale)

const currentLanguageName = computed(() => {
  const current = languages.find(lang => lang.code === currentLocale.value)
  return current ? current.name : '中文'
})

function changeLanguage(lang: Locale) {
  i18nStore.setLocale(lang)
  languageMenuOpen.value = false
}

function toggleLanguageMenu() {
  languageMenuOpen.value = !languageMenuOpen.value
}

function toggleMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value
  languageMenuOpen.value = false
}

// 点击外部关闭语言菜单
function handleClickOutside(event: MouseEvent) {
  const target = event.target as HTMLElement
  if (!target.closest('.relative')) {
    languageMenuOpen.value = false
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.addEventListener('click', handleClickOutside)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('click', handleClickOutside)
  }
})

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}

function navigateToSection(section: string) {
  // 如果当前不在首页，先跳转到首页
  if (route.path !== '/') {
    router.push('/').then(() => {
      // 等待页面加载后滚动到指定区域
      setTimeout(() => {
        const element = document.getElementById(section)
        if (element) {
          element.scrollIntoView({ behavior: 'smooth', block: 'start' })
        }
      }, 100)
    })
  } else {
    // 如果已经在首页，直接滚动
    const element = document.getElementById(section)
    if (element) {
      element.scrollIntoView({ behavior: 'smooth', block: 'start' })
    }
  }
}
</script>

<style scoped>
</style>
