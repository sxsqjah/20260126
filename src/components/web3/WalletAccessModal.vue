<template>
  <Teleport to="body">
    <div v-if="open" class="wallet-modal" role="dialog" aria-modal="true" aria-labelledby="wallet-access-title">
      <button class="wallet-modal__backdrop" type="button" aria-label="Close modal" @click="$emit('close')"></button>
      <div class="wallet-modal__panel">
        <div class="flex items-start justify-between gap-6">
          <div>
            <p class="font-mono text-xs uppercase tracking-[0.3em] text-brand-cyan">{{ $t('web3.wallet.eyebrow') }}</p>
            <h2 id="wallet-access-title" class="mt-3 text-2xl font-bold text-white">{{ $t('web3.wallet.title') }}</h2>
          </div>
          <button class="wallet-modal__close" type="button" aria-label="Close modal" @click="$emit('close')">
            <span></span>
            <span></span>
          </button>
        </div>
        <p class="mt-6 text-sm leading-7 text-gray-300">
          {{ $t('web3.wallet.description') }}
        </p>
        <div class="mt-6 grid gap-3 text-xs text-gray-400 sm:grid-cols-3">
          <div class="wallet-modal__note">{{ $t('web3.wallet.notes.wallet') }}</div>
          <div class="wallet-modal__note">{{ $t('web3.wallet.notes.transfer') }}</div>
          <div class="wallet-modal__note">{{ $t('web3.wallet.notes.execution') }}</div>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
defineProps<{
  open: boolean
}>()

defineEmits<{
  close: []
}>()
</script>

<style scoped>
.wallet-modal {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: grid;
  place-items: center;
  padding: 20px;
}

.wallet-modal__backdrop {
  position: absolute;
  inset: 0;
  background: rgba(3, 8, 14, 0.76);
  backdrop-filter: blur(10px);
}

.wallet-modal__panel {
  position: relative;
  width: min(560px, 100%);
  border: 1px solid rgba(102, 252, 241, 0.28);
  border-radius: 16px;
  background: linear-gradient(145deg, rgba(11, 18, 28, 0.96), rgba(20, 28, 46, 0.9));
  box-shadow: 0 0 60px rgba(102, 252, 241, 0.16);
  padding: 28px;
}

.wallet-modal__close {
  position: relative;
  width: 36px;
  height: 36px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 999px;
}

.wallet-modal__close span {
  position: absolute;
  left: 10px;
  top: 17px;
  width: 14px;
  height: 2px;
  background: rgba(255, 255, 255, 0.72);
}

.wallet-modal__close span:first-child {
  transform: rotate(45deg);
}

.wallet-modal__close span:last-child {
  transform: rotate(-45deg);
}

.wallet-modal__note {
  border: 1px solid rgba(102, 252, 241, 0.16);
  border-radius: 10px;
  background: rgba(102, 252, 241, 0.04);
  padding: 10px;
  text-align: center;
}
</style>
