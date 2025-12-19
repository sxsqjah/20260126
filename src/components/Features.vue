<template>
  <section id="features" class="py-24 bg-brand-gray/20 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16 reveal">
        <h2 class="text-3xl md:text-4xl font-bold text-white">{{ $t('features.title') }}</h2>
        <p class="mt-3 text-brand-cyan font-mono text-sm tracking-widest">{{ $t('features.subtitle') }}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- K-Model 共振引擎 -->
        <div class="glass-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal group">
          <div class="w-14 h-14 bg-brand-cyan/10 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-7 h-7 text-brand-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.kModel.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.kModel.description') }}
          </p>
        </div>

        <!-- DL-Signal 深度学习 -->
        <div class="glass-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-100 group">
          <div class="w-14 h-14 bg-brand-cyan/10 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-7 h-7 text-brand-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.aiTrading.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.aiTrading.description') }}
          </p>
        </div>

        <!-- Risk Budgeting 风控 -->
        <div class="glass-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-200 group">
          <div class="w-14 h-14 bg-brand-cyan/10 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-7 h-7 text-brand-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.riskControl.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.riskControl.description') }}
          </p>
        </div>

        <!-- 信号处理引擎 -->
        <div class="glass-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-300 group">
          <div class="w-14 h-14 bg-brand-cyan/10 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-7 h-7 text-brand-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.signalProcessing.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.signalProcessing.description') }}
          </p>
        </div>

        <!-- 多交易所支持 -->
        <div class="glass-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-400 group">
          <div class="w-14 h-14 bg-brand-cyan/10 rounded-lg flex items-center justify-center mb-6 group-hover:scale-110 transition-transform duration-300">
            <svg class="w-7 h-7 text-brand-cyan" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"></path>
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.multiExchange.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.multiExchange.description') }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRevealAnimation } from '../composables/useRevealAnimation'

useRevealAnimation()
</script>

<style scoped>
.reveal.delay-100 {
  transition-delay: 0.1s;
}
.reveal.delay-200 {
  transition-delay: 0.2s;
}
.reveal.delay-300 {
  transition-delay: 0.3s;
}
.reveal.delay-400 {
  transition-delay: 0.4s;
}
</style>

