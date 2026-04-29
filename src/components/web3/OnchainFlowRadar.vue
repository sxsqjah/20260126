<template>
  <section class="web3-section py-24">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
        <div class="reveal">
          <p class="font-mono text-sm tracking-[0.35em] text-brand-cyan">{{ $t('web3.onchain.eyebrow') }}</p>
          <h2 class="mt-4 text-3xl font-bold text-white md:text-4xl">{{ $t('web3.onchain.title') }}</h2>
          <p class="mt-2 text-xl font-semibold text-brand-cyan">{{ $t('web3.onchain.subtitle') }}</p>
          <p class="mt-6 max-w-xl text-base leading-8 text-gray-400">
            {{ $t('web3.onchain.description') }}
          </p>
          <div class="radar-shell mt-10">
            <div class="radar-sweep"></div>
            <div class="radar-dot radar-dot--one"></div>
            <div class="radar-dot radar-dot--two"></div>
            <div class="radar-dot radar-dot--three"></div>
          </div>
        </div>

        <div class="grid gap-4 sm:grid-cols-2 reveal delay-100">
          <article v-for="item in flowCards" :key="item.key" class="flow-card">
            <div class="flex items-center justify-between gap-4">
              <p class="text-sm font-semibold text-white">{{ $t(`web3.onchain.cards.${item.key}.label`) }}</p>
              <span :class="['flow-card__status', item.tone]">{{ $t(`web3.onchain.cards.${item.key}.value`) }}</span>
            </div>
            <p class="mt-2 text-xs text-gray-500">{{ $t(`web3.onchain.cards.${item.key}.caption`) }}</p>
            <div class="mt-5 flex h-10 items-end gap-1.5">
              <span
                v-for="height in item.bars"
                :key="`${item.key}-${height}`"
                class="flow-card__bar"
                :style="{ height: `${height}%` }"
              ></span>
            </div>
          </article>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRevealAnimation } from '../../composables/useRevealAnimation'

const flowCards = [
  { key: 'whale', tone: 'tone-cyan', bars: [36, 58, 46, 72, 64, 84] },
  { key: 'netflow', tone: 'tone-blue', bars: [72, 64, 48, 42, 36, 28] },
  { key: 'stablecoin', tone: 'tone-cyan', bars: [24, 34, 52, 61, 76, 82] },
  { key: 'liquidation', tone: 'tone-warn', bars: [44, 56, 62, 58, 48, 52] },
  { key: 'oi', tone: 'tone-purple', bars: [32, 40, 53, 66, 74, 88] },
  { key: 'funding', tone: 'tone-blue', bars: [54, 48, 50, 56, 52, 60] },
]

useRevealAnimation()
</script>
