<template>
  <section :class="compact ? 'hero-pipeline' : 'web3-section py-24'">
    <div :class="compact ? 'w-full' : 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8'">
      <div class="mx-auto max-w-3xl text-center reveal" :class="{ 'hero-pipeline__header': compact }">
        <p class="font-mono text-sm tracking-[0.35em] text-brand-cyan">{{ $t('web3.pipeline.eyebrow') }}</p>
        <h2 :class="compact ? 'mt-3 text-2xl font-bold text-white md:text-3xl' : 'mt-4 text-3xl font-bold text-white md:text-4xl'">{{ $t('web3.pipeline.title') }}</h2>
        <p class="mt-3 text-xl font-semibold text-brand-cyan">{{ $t('web3.pipeline.subtitle') }}</p>
        <p :class="compact ? 'mt-4 text-sm leading-7 text-gray-400' : 'mt-6 text-base leading-8 text-gray-400'">
          {{ $t('web3.pipeline.description') }}
        </p>
      </div>

      <div v-if="compact" class="pipeline-mobile-summary reveal delay-100">
        <div v-for="(step, index) in mobileSteps" :key="step.key" class="pipeline-mobile-chip">
          <span>{{ String(index + 1).padStart(2, '0') }}</span>
          <strong>{{ $t(`web3.pipeline.steps.${step.key}.title`) }}</strong>
        </div>
      </div>

      <div class="pipeline reveal delay-100" :class="compact ? 'pipeline--compact mt-8' : 'mt-14'">
        <div v-for="(step, index) in steps" :key="step.key" class="pipeline-step" :style="{ '--step-delay': `${index * 0.24}s` }">
          <div class="pipeline-step__index">{{ String(index + 1).padStart(2, '0') }}</div>
          <div>
            <h3 class="break-words text-sm font-semibold leading-snug text-white">{{ $t(`web3.pipeline.steps.${step.key}.title`) }}</h3>
            <p v-if="$t(`web3.pipeline.steps.${step.key}.subtitle`)" class="mt-1 text-xs text-gray-500">{{ $t(`web3.pipeline.steps.${step.key}.subtitle`) }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import { useRevealAnimation } from '../../composables/useRevealAnimation'

defineProps<{
  compact?: boolean
}>()

const steps = [
  { key: 'market' },
  { key: 'feature' },
  { key: 'scoring' },
  { key: 'risk' },
  { key: 'approval' },
  { key: 'execution' },
  { key: 'shadow' },
]

const mobileSteps = [
  { key: 'market' },
  { key: 'scoring' },
  { key: 'risk' },
  { key: 'execution' },
]

useRevealAnimation()
</script>
