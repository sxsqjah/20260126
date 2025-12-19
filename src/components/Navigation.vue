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
            <a href="#features" class="text-sm font-medium hover:text-brand-cyan transition duration-300">
              {{ $t('nav.features') }}
            </a>
            <a href="#pricing" class="text-sm font-medium hover:text-brand-cyan transition duration-300">
              {{ $t('nav.pricing') }}
            </a>
            <a href="#footer" class="text-sm font-medium hover:text-brand-cyan transition duration-300">
              {{ $t('nav.contact') }}
            </a>
          </div>
          
          <!-- 语言切换器 -->
          <div class="flex items-center space-x-2 border-l border-white/10 pl-6">
            <button
              v-for="lang in languages"
              :key="lang.code"
              @click="changeLanguage(lang.code)"
              :class="[
                'px-3 py-1 text-xs font-mono rounded transition duration-300',
                currentLocale === lang.code
                  ? 'bg-brand-cyan text-brand-dark'
                  : 'text-brand-light hover:text-brand-cyan hover:bg-white/5'
              ]"
            >
              {{ lang.label }}
            </button>
          </div>
          
          <a href="#" class="font-mono text-xs font-bold text-brand-cyan border border-brand-cyan/50 px-4 py-2 rounded hover:bg-brand-cyan hover:text-brand-dark transition duration-300">
            {{ $t('nav.login') }}
          </a>
        </div>

        <div class="flex items-center space-x-4 md:hidden">
          <!-- 移动端语言切换 -->
          <div class="flex items-center space-x-1">
            <button
              v-for="lang in languages"
              :key="lang.code"
              @click="changeLanguage(lang.code)"
              :class="[
                'px-2 py-1 text-xs font-mono rounded',
                currentLocale === lang.code
                  ? 'bg-brand-cyan text-brand-dark'
                  : 'text-brand-light'
              ]"
            >
              {{ lang.label }}
            </button>
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
          href="#features"
          @click="toggleMenu"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan"
        >
          {{ $t('nav.features') }}
        </a>
        <a
          href="#pricing"
          @click="toggleMenu"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan"
        >
          {{ $t('nav.pricing') }}
        </a>
        <a
          href="#footer"
          @click="toggleMenu"
          class="block px-3 py-2 rounded-md text-base font-medium text-white hover:bg-white/5 hover:text-brand-cyan"
        >
          {{ $t('nav.contact') }}
        </a>
        <a
          href="#"
          class="block px-3 py-2 rounded-md text-base font-medium text-brand-cyan"
        >
          {{ $t('nav.login') }}
        </a>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { useI18nStore, type Locale } from '../stores/i18n'

const { locale } = useI18n()
const i18nStore = useI18nStore()

const mobileMenuOpen = ref(false)

const languages = [
  { code: 'zh-CN' as Locale, label: '中' },
  { code: 'ko-KR' as Locale, label: '한' },
  { code: 'en-US' as Locale, label: 'EN' }
]

const currentLocale = computed(() => i18nStore.locale)

function changeLanguage(lang: Locale) {
  i18nStore.setLocale(lang)
}

function toggleMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: 'smooth' })
}
</script>

<style scoped>
</style>

