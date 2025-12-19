<template>
  <header class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 overflow-hidden flex items-center justify-center min-h-[90vh]">
    <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0 pointer-events-none">
      <div class="absolute top-[-10%] right-[-5%] w-[500px] h-[500px] bg-brand-cyan/10 rounded-full blur-[100px] animate-float"></div>
      <div class="absolute bottom-[-10%] left-[-10%] w-[600px] h-[600px] bg-blue-900/10 rounded-full blur-[120px]"></div>
    </div>
    
    <div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal active">
      <div class="inline-block mb-6 px-4 py-1 rounded-full border border-brand-cyan/30 bg-brand-cyan/5">
        <span class="text-brand-cyan font-mono text-xs tracking-widest uppercase">
          {{ $t('hero.badge') }}
        </span>
      </div>
      
      <h1 class="text-5xl md:text-7xl font-bold text-white mb-6 tracking-tight leading-tight">
        Trade like a <br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-white text-glow">
          Korean Quant.
        </span>
      </h1>
      
      <p class="mt-6 max-w-2xl mx-auto text-lg md:text-xl text-brand-light leading-relaxed">
        {{ $t('hero.subtitle') }}<br/>
        <span class="text-brand-cyan/80">{{ $t('hero.subtitleHighlight') }}</span>
      </p>
      
      <div class="mt-12 flex flex-col sm:flex-row justify-center gap-4">
        <a
          href="#pricing"
          class="btn-primary px-8 py-4 rounded font-bold text-lg shadow-lg shadow-brand-cyan/20"
        >
          {{ $t('hero.ctaPrimary') }}
        </a>
        <a
          href="#"
          class="group border border-white/20 text-white px-8 py-4 rounded font-bold text-lg hover:bg-white/5 transition flex items-center justify-center gap-2"
        >
          <svg class="w-5 h-5 text-brand-cyan group-hover:translate-y-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
          </svg>
          {{ $t('hero.ctaSecondary') }}
        </a>
      </div>
      
      <div class="mt-20 grid grid-cols-2 md:grid-cols-4 gap-8 border-t border-white/5 pt-10">
        <div class="reveal delay-100">
          <div class="text-3xl font-mono font-bold text-white">~15ms</div>
          <div class="text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.latency') }}</div>
        </div>
        <div class="reveal delay-200">
          <div class="text-3xl font-mono font-bold text-white">99.9%</div>
          <div class="text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.uptime') }}</div>
        </div>
        <div class="reveal delay-300">
          <div class="text-3xl font-mono font-bold text-brand-cyan">K-Model</div>
          <div class="text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.model') }}</div>
        </div>
        <div class="reveal delay-400">
          <div class="text-3xl font-mono font-bold text-white">24/7</div>
          <div class="text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.monitor') }}</div>
        </div>
      </div>
    </div>
  </header>
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

