<template>
  <router-view />
</template>

<script setup lang="ts">
import { watch } from 'vue'
import { useI18n } from 'vue-i18n'
import { useI18nStore } from './stores/i18n'

const { locale } = useI18n()
const i18nStore = useI18nStore()

// 同步 store 和 i18n 的 locale
watch(() => i18nStore.locale, (newLocale) => {
  locale.value = newLocale
}, { immediate: true })
</script>

<style scoped>
</style>

