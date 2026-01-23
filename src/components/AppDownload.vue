<template>
  <section id="download" class="py-24 bg-brand-gray/20 relative overflow-hidden">
    <div class="absolute top-10 right-0 w-[500px] h-[500px] bg-brand-cyan/5 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-0 left-0 w-[600px] h-[600px] bg-blue-900/10 rounded-full blur-[140px] pointer-events-none"></div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
      <div class="text-center mb-16 reveal">
        <h2 class="text-3xl md:text-4xl font-bold text-white">{{ $t('download.title') }}</h2>
        <p class="mt-3 text-brand-cyan font-mono text-sm tracking-widest">{{ $t('download.subtitle') }}</p>
        <p class="mt-4 text-gray-400 max-w-2xl mx-auto">{{ $t('download.description') }}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div
          v-for="(item, index) in downloadItems"
          :key="item.key"
          class="glass-card p-8 rounded-2xl border border-white/10 hover:border-brand-cyan/40 transition duration-500 reveal"
          :class="index === 1 ? 'delay-100' : ''"
        >
          <div class="flex items-start justify-between">
            <div>
              <h3 class="text-xl font-bold text-white">{{ $t(`download.${item.key}.title`) }}</h3>
              <p class="text-sm text-gray-400 mt-2">{{ $t(`download.${item.key}.meta`) }}</p>
            </div>
            <span class="text-xs font-mono text-brand-cyan border border-brand-cyan/40 px-2 py-1 rounded">
              {{ $t(`download.${item.key}.badge`) }}
            </span>
          </div>
          <div class="mt-6 flex flex-wrap items-center gap-3">
            <a
              :href="item.url"
              :download="item.filename"
              class="btn-primary px-6 py-3 rounded-lg font-bold text-sm"
            >
              {{ $t(`download.${item.key}.cta`) }}
            </a>
            <span class="text-xs text-gray-500 font-mono">
              {{ item.filename }}
            </span>
          </div>
          <p class="text-xs text-gray-500 mt-4">
            {{ $t(`download.${item.key}.note`) }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { appDownloads } from '../config/appDownloads'
import { useRevealAnimation } from '../composables/useRevealAnimation'

const downloadItems = [
  { key: 'android', ...appDownloads.android },
  { key: 'ios', ...appDownloads.ios },
]

useRevealAnimation()
</script>

<style scoped>
.reveal.delay-100 {
  transition-delay: 0.1s;
}
</style>
