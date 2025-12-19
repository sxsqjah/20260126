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
              <a href="/Crypto-K_Quants_Whitepaper_v1.3.pdf" download="Crypto-K_Quants_Whitepaper_v1.3.pdf" class="hover:text-brand-cyan transition">{{ $t('footer.products.whitepaper') }}</a>
            </li>
            <li>
              <a href="#" @click.prevent="scrollToLogin" class="hover:text-brand-cyan transition cursor-pointer">{{ $t('footer.products.backtest') }}</a>
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
              <a href="#" class="hover:text-brand-cyan transition">{{ $t('footer.support.community') }}</a>
            </li>
            <li>
              <a href="#" class="hover:text-brand-cyan transition">{{ $t('footer.support.contact') }}</a>
            </li>
            <li>
              <a href="#" class="hover:text-brand-cyan transition">{{ $t('footer.support.business') }}</a>
            </li>
          </ul>
        </div>
      </div>
      
      <div class="border-t border-white/10 pt-10">
        <div class="p-4 bg-red-900/10 border border-red-900/30 rounded text-xs text-red-200/60 mb-8 leading-relaxed">
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
  </footer>
</template>

<script setup lang="ts">
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

