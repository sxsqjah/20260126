<template>
  <div class="min-h-screen web3-page-bg">
    <Navigation />
    <Hero />
    <Features />
    <OnchainFlowRadar />
    <QuantCommandCenter />
    <Pricing />
    <AppDownload />
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Navigation from '../components/Navigation.vue'
import Hero from '../components/Hero.vue'
import Features from '../components/Features.vue'
import OnchainFlowRadar from '../components/web3/OnchainFlowRadar.vue'
import QuantCommandCenter from '../components/web3/QuantCommandCenter.vue'
import Pricing from '../components/Pricing.vue'
import AppDownload from '../components/AppDownload.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
</style>
