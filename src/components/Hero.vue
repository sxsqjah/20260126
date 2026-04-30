<template>
  <header class="hero-shell relative pt-32 pb-20 lg:pt-44 lg:pb-28 overflow-hidden flex items-center justify-center min-h-screen">
    <HeroBlockchainNetwork />

    <div class="hero-content relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center reveal active">
      <div class="hero-badge inline-block mb-6 px-4 py-1 rounded-full border border-brand-cyan/30 bg-brand-cyan/5">
        <span class="text-brand-cyan font-mono text-xs tracking-widest uppercase">
          {{ $t('hero.badge') }}
        </span>
      </div>

      <h1 class="hero-title text-5xl md:text-7xl font-bold text-white mb-6 tracking-tight leading-tight">
        {{ $t('hero.title') }} <br/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan via-blue-200 to-white text-glow">
          {{ $t('hero.titleHighlight') }}
        </span>
      </h1>

      <p class="hero-subtitle mt-6 max-w-3xl mx-auto text-lg md:text-xl text-brand-light leading-relaxed">
        {{ $t('hero.subtitle') }}<br/>
        <span class="text-brand-cyan/80">{{ $t('hero.subtitleHighlight') }}</span>
      </p>

      <DecisionPipeline compact />

      <div class="hero-stats mt-12 grid grid-cols-2 md:grid-cols-4 gap-8 border-t border-white/5 pt-8">
        <div class="hero-stat reveal delay-100">
          <div class="hero-stat__value text-3xl font-mono font-bold text-white">24/7</div>
          <div class="hero-stat__label text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.latency') }}</div>
        </div>
        <div class="hero-stat reveal delay-200">
          <div class="hero-stat__value text-3xl font-mono font-bold text-white">AI</div>
          <div class="hero-stat__label text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.uptime') }}</div>
        </div>
        <div class="hero-stat reveal delay-300">
          <div class="hero-stat__value text-3xl font-mono font-bold text-brand-cyan">Risk Gate</div>
          <div class="hero-stat__label text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.model') }}</div>
        </div>
        <div class="hero-stat reveal delay-400">
          <div class="hero-stat__value text-3xl font-mono font-bold text-white">On-chain</div>
          <div class="hero-stat__label text-xs text-gray-500 uppercase tracking-wide mt-1">{{ $t('hero.stats.monitor') }}</div>
        </div>
      </div>
    </div>

  </header>
</template>

<script setup lang="ts">
import { useRevealAnimation } from '../composables/useRevealAnimation'
import HeroBlockchainNetwork from './web3/HeroBlockchainNetwork.vue'
import DecisionPipeline from './web3/DecisionPipeline.vue'

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
