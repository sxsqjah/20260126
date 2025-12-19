<template>
  <div class="min-h-screen bg-brand-dark">
    <Navigation />
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 pt-32 pb-20">
      <div class="glass-card p-8 md:p-12 rounded-xl">
        <h1 class="text-4xl font-bold text-white mb-4">{{ $t('terms.title') }}</h1>
        <p class="text-gray-400 text-sm mb-8">{{ $t('terms.lastUpdated') }}</p>
        
        <div class="prose prose-invert max-w-none">
          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section1.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section1.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section2.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section2.content') }}</p>
            <ul class="list-disc list-inside text-gray-300 space-y-2 ml-4">
              <li>{{ $t('terms.section2.item1') }}</li>
              <li>{{ $t('terms.section2.item2') }}</li>
              <li>{{ $t('terms.section2.item3') }}</li>
              <li>{{ $t('terms.section2.item4') }}</li>
            </ul>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section3.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section3.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section4.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section4.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section5.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section5.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section6.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section6.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section7.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section7.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section8.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section8.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section9.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section9.content') }}</p>
          </section>

          <section class="mb-8">
            <h2 class="text-2xl font-bold text-white mb-4">{{ $t('terms.section10.title') }}</h2>
            <p class="text-gray-300 leading-relaxed mb-4">{{ $t('terms.section10.content') }}</p>
          </section>
        </div>

        <div class="mt-12 pt-8 border-t border-white/10">
          <router-link
            to="/"
            class="text-brand-cyan hover:text-white transition duration-300"
          >
            ← {{ $t('terms.backToHome') }}
          </router-link>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup lang="ts">
import Navigation from '../components/Navigation.vue'
import Footer from '../components/Footer.vue'
</script>

<style scoped>
</style>

