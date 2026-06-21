<template>
  <footer id="footer" class="bg-black border-t border-white/10 pt-20 pb-10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
        <div class="col-span-1 md:col-span-2">
          <span class="text-2xl font-bold font-mono text-white tracking-tighter">
            CRYPTO<span class="text-brand-cyan">-K</span> QUANTS
          </span>
          <p class="mt-6 text-gray-500 text-sm max-w-sm leading-relaxed whitespace-pre-line">
            {{ $t('footer.description') }}
          </p>
        </div>
        <div>
          <h4 class="text-white font-bold mb-6">{{ $t('footer.products.title') }}</h4>
          <ul class="space-y-4 text-sm text-gray-500">
            <li>
              <a href="#" @click.prevent="scrollToLogin" class="hover:text-brand-cyan transition cursor-pointer">{{ $t('footer.products.subscription') }}</a>
            </li>
            <li>
              <a href="#" @click.prevent="scrollToLogin" class="hover:text-brand-cyan transition cursor-pointer">{{ $t('footer.products.api') }}</a>
            </li>
            <li>
              <a :href="currentWhitepaper.href" :download="currentWhitepaper.filename" class="hover:text-brand-cyan transition">{{ $t('footer.products.whitepaper') }}</a>
            </li>
            <li>
              <a href="#" @click.prevent="openBacktestModal" class="hover:text-brand-cyan transition cursor-pointer">{{ $t('footer.products.backtest') }}</a>
            </li>
          </ul>
        </div>
        <div>
          <h4 class="text-white font-bold mb-6">{{ $t('footer.support.title') }}</h4>
          <ul class="space-y-4 text-sm text-gray-500">
            <li>
              <a href="#" class="hover:text-brand-cyan transition">{{ $t('footer.support.help') }}</a>
            </li>
            <li>
              <a href="https://t.me/Crypto_Wealth888" target="_blank" rel="noopener noreferrer" class="hover:text-brand-cyan transition">{{ $t('footer.support.community') }}</a>
            </li>
            <li>
              <a id="footer-contact" :href="contactMailto" class="hover:text-brand-cyan transition">{{ $t('footer.support.contact') }}</a>
            </li>
            <li>
              <a href="#" class="hover:text-brand-cyan transition">{{ $t('footer.support.business') }}</a>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-white/10 pt-10">
        <div class="p-4 bg-red-900/10 border border-red-900/40 rounded text-xs text-red-100/80 mb-8 leading-relaxed">
          {{ $t('footer.risk') }}
        </div>
        <div class="flex flex-col md:flex-row justify-between items-center text-xs text-gray-600">
          <p>{{ $t('footer.copyright') }}</p>
          <div class="flex space-x-6 mt-4 md:mt-0">
            <router-link to="/privacy" class="hover:text-gray-400">{{ $t('footer.privacy') }}</router-link>
            <router-link to="/terms" class="hover:text-gray-400">{{ $t('footer.terms') }}</router-link>
          </div>
        </div>
      </div>
    </div>

    <Teleport to="body">
      <div
        v-if="showBacktestModal"
        class="fixed inset-0 z-[100] flex items-center justify-center bg-black/75 px-4 backdrop-blur-sm"
        @click.self="closeBacktestModal"
      >
        <div class="glass-card relative w-full max-w-md rounded-xl border border-brand-cyan/30 bg-brand-gray/90 p-8 text-center shadow-[0_0_40px_rgba(102,252,241,0.14)]">
          <button
            type="button"
            class="absolute right-4 top-4 flex h-8 w-8 items-center justify-center rounded border border-white/10 text-gray-400 transition hover:border-brand-cyan/40 hover:text-brand-cyan"
            aria-label="Close"
            @click="closeBacktestModal"
          >
            ×
          </button>
          <div class="mx-auto mb-5 h-px w-20 bg-brand-cyan/60 shadow-[0_0_16px_rgba(102,252,241,0.55)]"></div>
          <p class="text-base font-semibold leading-relaxed text-white">
            {{ $t('footer.products.backtestPending') }}
          </p>
        </div>
      </div>
    </Teleport>
  </footer>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { contactMailto } from '../config/contact'
import { getWhitepaperDownload } from '../config/whitepapers'
import { useI18nStore } from '../stores/i18n'

const showBacktestModal = ref(false)
const i18nStore = useI18nStore()
const currentWhitepaper = computed(() => getWhitepaperDownload(i18nStore.locale))

function openBacktestModal() {
  showBacktestModal.value = true
}

function closeBacktestModal() {
  showBacktestModal.value = false
}

function handleBacktestModalKeydown(event: KeyboardEvent) {
  if (event.key === 'Escape') {
    closeBacktestModal()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleBacktestModalKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleBacktestModalKeydown)
})

function scrollToLogin() {
  // 滚动到页面顶部（导航栏位置）
  window.scrollTo({ top: 0, behavior: 'smooth' })
  
  // 等待滚动完成后高亮登录按钮
  setTimeout(() => {
    // 查找导航栏中的登录按钮（通过类名查找）
    const loginButtons = document.querySelectorAll('a.font-mono.text-xs.font-bold.text-brand-cyan')
    if (loginButtons.length > 0) {
      const loginButton = loginButtons[loginButtons.length - 1] as HTMLElement
      // 添加高亮效果
      const originalStyle = loginButton.style.cssText
      loginButton.style.transition = 'all 0.3s'
      loginButton.style.transform = 'scale(1.1)'
      loginButton.style.boxShadow = '0 0 20px rgba(102, 252, 241, 0.5)'
      
      setTimeout(() => {
        loginButton.style.cssText = originalStyle
      }, 1500)
    }
  }, 500)
}
</script>

<style scoped>
</style>
