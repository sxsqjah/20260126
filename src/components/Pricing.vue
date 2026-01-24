<template>
  <section id="pricing" class="py-24 relative overflow-hidden">
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-brand-cyan/5 rounded-full blur-[120px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16 reveal">
        <h2 class="text-3xl md:text-4xl font-bold text-white">{{ $t('pricing.title') }}</h2>
        <p class="mt-4 text-gray-400">{{ $t('pricing.subtitle') }}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-8 items-start">
        <!-- Basic Plan -->
        <div class="glass-card p-8 rounded-2xl border-t-4 border-gray-600 reveal">
          <h3 class="text-lg font-medium text-gray-400">{{ $t('pricing.basic.name') }}</h3>
          <div class="my-6 flex items-baseline">
            <span class="text-5xl font-bold text-white tracking-tight">{{ $t('pricing.basic.price') }}</span>
            <span class="text-lg text-gray-500 ml-2">{{ $t('pricing.basic.period') }}</span>
          </div>
          <p class="text-sm text-gray-400 mb-8 border-b border-white/10 pb-8">
            {{ $t('pricing.basic.description') }}
          </p>
          <ul class="space-y-4 mb-8 text-sm text-gray-300">
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.basic.features.strategy') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.basic.features.position') }}
            </li>
            <li class="flex items-center text-gray-500">
              <span class="mr-3">●</span>
              {{ $t('pricing.basic.features.delay') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.basic.features.notification') }}
            </li>
          </ul>
          <a
            href="#"
            class="block w-full py-3 border border-white/20 text-center rounded-lg hover:bg-white/5 hover:text-white transition text-sm font-bold"
          >
            {{ $t('pricing.basic.cta') }}
          </a>
        </div>

        <!-- Advanced Plan -->
        <div class="glass-card p-8 rounded-2xl border-t-4 border-brand-cyan relative transform md:-translate-y-6 shadow-2xl shadow-brand-cyan/10 reveal delay-100">
          <div class="absolute top-0 right-0 bg-brand-cyan text-brand-dark text-xs font-bold px-3 py-1 rounded-bl-lg">
            {{ $t('pricing.advanced.badge') }}
          </div>
          <h3 class="text-lg font-medium text-white">{{ $t('pricing.advanced.name') }}</h3>
          <div class="my-6 flex items-baseline">
            <span class="text-5xl font-bold text-brand-cyan tracking-tight">{{ $t('pricing.advanced.price') }}</span>
            <span class="text-lg text-gray-400 ml-2">{{ $t('pricing.advanced.period') }}</span>
          </div>
          <p class="text-sm text-gray-300 mb-8 border-b border-white/10 pb-8">
            {{ $t('pricing.advanced.description') }}
          </p>
          <ul class="space-y-4 mb-8 text-sm text-white font-medium">
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.advanced.features.strategies') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.advanced.features.resonance') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.advanced.features.api') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.advanced.features.risk') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.advanced.features.report') }}
            </li>
          </ul>
          <a
            href="https://home.ckqpro.com/#/pages/auth/register"
            class="block w-full py-4 bg-brand-cyan text-brand-dark font-bold text-center rounded-lg hover:bg-brand-cyanDim hover:shadow-[0_0_20px_rgba(102,252,241,0.4)] transition"
          >
            {{ $t('pricing.advanced.cta') }}
          </a>
        </div>

        <!-- Pro Quant Plan -->
        <div class="glass-card p-8 rounded-2xl border-t-4 border-purple-500 reveal delay-200">
          <h3 class="text-lg font-medium text-purple-400">{{ $t('pricing.pro.name') }}</h3>
          <div class="my-6 flex items-baseline">
            <span class="text-5xl font-bold text-white tracking-tight">{{ $t('pricing.pro.price') }}</span>
            <span class="text-lg text-gray-500 ml-2">{{ $t('pricing.pro.period') }}</span>
          </div>
          <p class="text-sm text-gray-400 mb-8 border-b border-white/10 pb-8">
            {{ $t('pricing.pro.description') }}
          </p>
          <ul class="space-y-4 mb-8 text-sm text-gray-300">
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.pro.features.all') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.pro.features.priority') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.pro.features.revenue') }}
            </li>
            <li class="flex items-center">
              <span class="text-brand-cyan mr-3">✓</span>
              {{ $t('pricing.pro.features.custom') }}
            </li>
          </ul>
          <a
            href="#footer-contact"
            class="block w-full py-3 border border-purple-500/50 text-purple-400 text-center rounded-lg hover:bg-purple-500/10 transition text-sm font-bold"
          >
            {{ $t('pricing.pro.cta') }}
          </a>
        </div>
      </div>
      
      <div class="mt-16 glass-card p-10 rounded-xl flex flex-col md:flex-row items-center justify-between reveal">
        <div>
          <h3 class="text-xl font-bold text-white">{{ $t('pricing.enterprise.title') }}</h3>
          <p class="text-gray-400 mt-2">{{ $t('pricing.enterprise.description') }}</p>
        </div>
        <a
          href="#"
          class="mt-6 md:mt-0 text-brand-cyan border-b border-brand-cyan pb-1 hover:text-white hover:border-white transition font-mono"
        >
          {{ $t('pricing.enterprise.cta') }}
        </a>
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
</style>
