<template>
  <section class="py-24 relative overflow-hidden">
    <div class="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(102,252,241,0.08),transparent_36%)]"></div>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="grid gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
        <div class="reveal">
          <p class="font-mono text-sm tracking-[0.35em] text-brand-cyan">{{ $t('web3.command.eyebrow') }}</p>
          <h2 class="mt-4 text-3xl font-bold text-white md:text-4xl">{{ $t('web3.command.title') }}</h2>
          <p class="mt-3 text-xl font-semibold text-brand-cyan">{{ $t('web3.command.subtitle') }}</p>
          <p class="mt-6 max-w-xl text-base leading-8 text-gray-400">
            {{ $t('web3.command.description') }}
          </p>
        </div>

        <div class="command-panel reveal delay-100">
          <div class="command-panel__scan"></div>
          <div class="grid gap-4 md:grid-cols-2">
            <div v-for="metric in metrics" :key="metric.key" class="command-metric">
              <span>{{ $t(`web3.command.metrics.${metric.key}.label`) }}</span>
              <strong :class="metric.tone">{{ $t(`web3.command.metrics.${metric.key}.value`) }}</strong>
            </div>
          </div>

          <div class="mt-8 grid gap-6 lg:grid-cols-[1fr_0.8fr]">
            <div class="terminal-chart">
              <svg viewBox="0 0 420 160" fill="none" role="img" aria-label="Simulated market chart">
                <path class="terminal-chart__grid" d="M0 40H420M0 80H420M0 120H420M84 0V160M168 0V160M252 0V160M336 0V160" />
                <path class="terminal-chart__line" d="M8 112C46 94 58 116 93 86C126 58 143 76 176 66C212 54 220 28 260 46C294 61 308 99 343 76C374 56 389 42 412 50" />
                <path class="terminal-chart__risk" d="M42 128H128M286 32H378" />
              </svg>
            </div>
            <div class="space-y-3">
              <div class="hud-pill">{{ $t('web3.command.pills.signal') }} <strong>72%</strong></div>
              <div class="hud-pill">{{ $t('web3.command.pills.risk') }} <strong>{{ $t('web3.command.pills.passed') }}</strong></div>
              <div class="hud-pill">{{ $t('web3.command.pills.execution') }} <strong>{{ $t('web3.command.pills.manual') }}</strong></div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRevealAnimation } from '../../composables/useRevealAnimation'

const metrics = [
  { key: 'btc', tone: 'tone-cyan' },
  { key: 'eth', tone: 'tone-blue' },
  { key: 'risk', tone: 'tone-cyan' },
  { key: 'volatility', tone: 'tone-blue' },
  { key: 'liquidity', tone: 'tone-cyan' },
  { key: 'model', tone: 'tone-purple' },
  { key: 'execution', tone: 'tone-blue' },
  { key: 'shadow', tone: 'tone-cyan' },
]

useRevealAnimation()
</script>
