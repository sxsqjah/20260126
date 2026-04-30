<template>
  <section id="features" class="py-24 bg-brand-gray/20 relative">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16 reveal">
        <h2 class="text-3xl md:text-4xl font-bold text-white">{{ $t('features.title') }}</h2>
        <p class="mt-3 text-brand-cyan font-mono text-sm tracking-widest">{{ $t('features.subtitle') }}</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Market Flow 多源资金洞察 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal group">
          <div class="feature-icon feature-icon--market" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="marketFlowIcon" x1="9" y1="10" x2="56" y2="55" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#66FCF1" />
                  <stop offset="0.48" stop-color="#37A6FF" />
                  <stop offset="1" stop-color="#A855F7" />
                </linearGradient>
              </defs>
              <path d="M10 45h44" stroke="url(#marketFlowIcon)" stroke-width="2.5" stroke-linecap="round" opacity="0.32" />
              <path d="M12 42C21 26 28 48 36 32C42 19 47 20 54 13" stroke="url(#marketFlowIcon)" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M47 13h7v7" stroke="#E9FFFD" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
              <rect x="12" y="36" width="7" height="10" rx="3.5" fill="#66FCF1" opacity="0.78" />
              <rect x="25" y="31" width="7" height="15" rx="3.5" fill="#37A6FF" opacity="0.78" />
              <rect x="38" y="25" width="7" height="21" rx="3.5" fill="#A855F7" opacity="0.72" />
              <circle cx="13" cy="42" r="3.5" fill="#E9FFFD" />
              <circle cx="36" cy="32" r="3.5" fill="#E9FFFD" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.kModel.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.kModel.description') }}
          </p>
          <div class="module-visual">
            <div class="flow-bars">
              <span style="height: 32%"></span>
              <span style="height: 68%"></span>
              <span style="height: 46%"></span>
              <span style="height: 78%"></span>
              <span style="height: 58%"></span>
              <span style="height: 88%"></span>
            </div>
          </div>
        </div>

        <!-- MTF Engine 多周期共振 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-100 group">
          <div class="feature-icon feature-icon--mtf" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="mtfEngineIcon" x1="14" y1="11" x2="52" y2="54" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#5EE7FF" />
                  <stop offset="0.5" stop-color="#3B82F6" />
                  <stop offset="1" stop-color="#C084FC" />
                </linearGradient>
              </defs>
              <circle cx="32" cy="32" r="23" stroke="url(#mtfEngineIcon)" stroke-width="2.5" opacity="0.35" />
              <circle cx="32" cy="32" r="15" stroke="url(#mtfEngineIcon)" stroke-width="2.5" opacity="0.62" />
              <circle cx="32" cy="32" r="7" fill="url(#mtfEngineIcon)" />
              <path d="M17 39c6-15 16-17 30-11" stroke="#E9FFFD" stroke-width="3.5" stroke-linecap="round" />
              <path d="M42 22l7 5-8 4" stroke="#E9FFFD" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />
              <circle cx="17" cy="39" r="3.5" fill="#66FCF1" />
              <circle cx="47" cy="28" r="3.5" fill="#C084FC" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.aiTrading.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.aiTrading.description') }}
          </p>
          <div class="module-visual">
            <div class="time-rings">
              <span>5M</span>
              <span>15M</span>
              <span>1H</span>
              <span>4H</span>
              <span>1D</span>
            </div>
          </div>
        </div>

        <!-- AI-Signal 智能评分 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-200 group">
          <div class="feature-icon feature-icon--ai" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="aiSignalIcon" x1="12" y1="10" x2="55" y2="53" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#66FCF1" />
                  <stop offset="0.45" stop-color="#8B5CF6" />
                  <stop offset="1" stop-color="#FF4FD8" />
                </linearGradient>
              </defs>
              <rect x="17" y="15" width="30" height="34" rx="9" fill="rgba(11, 18, 32, 0.74)" stroke="url(#aiSignalIcon)" stroke-width="3" />
              <path d="M25 39c4-10 10-13 19-9" stroke="#E9FFFD" stroke-width="3.2" stroke-linecap="round" />
              <path d="M32 33l6-8" stroke="url(#aiSignalIcon)" stroke-width="3.4" stroke-linecap="round" />
              <circle cx="24" cy="26" r="3.6" fill="#66FCF1" />
              <circle cx="32" cy="33" r="3.6" fill="#8B5CF6" />
              <circle cx="43" cy="29" r="3.6" fill="#FF4FD8" />
              <path d="M9 24h8M9 40h8M47 24h8M47 40h8M24 7v8M40 7v8M24 49v8M40 49v8" stroke="url(#aiSignalIcon)" stroke-width="3" stroke-linecap="round" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.riskControl.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.riskControl.description') }}
          </p>
          <div class="module-visual">
            <div class="score-meter">
              <div class="score-meter__label">
                <span>Signal Score</span>
                <strong class="text-brand-cyan">72%</strong>
              </div>
              <div class="score-bars">
                <span style="height: 42%"></span>
                <span style="height: 66%"></span>
                <span style="height: 84%"></span>
                <span style="height: 58%"></span>
                <span style="height: 72%"></span>
              </div>
            </div>
          </div>
        </div>

        <!-- Risk Gate 风控准入 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-300 group">
          <div class="feature-icon feature-icon--risk" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="riskGateIcon" x1="14" y1="8" x2="51" y2="55" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#7CFFB2" />
                  <stop offset="0.5" stop-color="#66FCF1" />
                  <stop offset="1" stop-color="#FF8B6E" />
                </linearGradient>
              </defs>
              <path d="M32 8l19 10v13c0 13-7.5 21-19 25C20.5 52 13 44 13 31V18L32 8z" fill="rgba(11, 18, 32, 0.7)" stroke="url(#riskGateIcon)" stroke-width="3" stroke-linejoin="round" />
              <path d="M23 33l6 6 13-15" stroke="#E9FFFD" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M15 48h34" stroke="url(#riskGateIcon)" stroke-width="3" stroke-linecap="round" opacity="0.56" />
              <circle cx="49" cy="18" r="4" fill="#FF8B6E" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.signalProcessing.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.signalProcessing.description') }}
          </p>
          <div class="module-visual">
            <div class="risk-tags">
              <span class="risk-tag risk-tag--pass">Passed</span>
              <span class="risk-tag risk-tag--block">Blocked</span>
              <span class="risk-tag">SL / RR</span>
            </div>
          </div>
        </div>

        <!-- Semi-Auto 执行闭环 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-400 group">
          <div class="feature-icon feature-icon--auto" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="semiAutoIcon" x1="11" y1="10" x2="54" y2="54" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#66FCF1" />
                  <stop offset="0.5" stop-color="#37A6FF" />
                  <stop offset="1" stop-color="#FACC15" />
                </linearGradient>
              </defs>
              <path d="M18 29a14 14 0 0123-10l4 4" stroke="url(#semiAutoIcon)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M46 16v9h-9" stroke="#E9FFFD" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M46 35a14 14 0 01-23 10l-4-4" stroke="url(#semiAutoIcon)" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
              <path d="M18 48v-9h9" stroke="#E9FFFD" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round" />
              <circle cx="20" cy="30" r="5" fill="#66FCF1" />
              <circle cx="32" cy="32" r="6" fill="rgba(11, 18, 32, 0.78)" stroke="#E9FFFD" stroke-width="3" />
              <circle cx="44" cy="34" r="5" fill="#FACC15" />
              <path d="M29 32l2 2 5-6" stroke="#66FCF1" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.shadowRun.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.shadowRun.description') }}
          </p>
          <div class="module-visual">
            <div class="execution-line">
              <span>Manual Confirm</span>
              <span>TP</span>
              <span>SL</span>
            </div>
          </div>
        </div>

        <!-- 多交易所支持 -->
        <div class="tech-module-card p-8 rounded-xl hover:border-brand-cyan/40 transition duration-500 reveal delay-500 group">
          <div class="feature-icon feature-icon--exchange" aria-hidden="true">
            <svg viewBox="0 0 64 64" fill="none">
              <defs>
                <linearGradient id="multiExchangeIcon" x1="12" y1="9" x2="54" y2="55" gradientUnits="userSpaceOnUse">
                  <stop stop-color="#5EE7FF" />
                  <stop offset="0.48" stop-color="#66FCF1" />
                  <stop offset="1" stop-color="#22C55E" />
                </linearGradient>
              </defs>
              <circle cx="32" cy="32" r="18" fill="rgba(11, 18, 32, 0.72)" stroke="url(#multiExchangeIcon)" stroke-width="3" />
              <path d="M14 32h36M32 14c5 5 8 11 8 18s-3 13-8 18M32 14c-5 5-8 11-8 18s3 13 8 18" stroke="#E9FFFD" stroke-width="2.4" stroke-linecap="round" opacity="0.78" />
              <circle cx="18" cy="18" r="5" fill="#5EE7FF" />
              <circle cx="49" cy="25" r="5" fill="#66FCF1" />
              <circle cx="42" cy="49" r="5" fill="#22C55E" />
              <path d="M22 19c8-4 15-3 23 4M46 30c1 7-1 12-6 17M38 50c-8 0-14-4-18-11" stroke="url(#multiExchangeIcon)" stroke-width="3" stroke-linecap="round" />
            </svg>
          </div>
          <h3 class="text-xl font-bold text-white mb-3">{{ $t('features.multiExchange.title') }}</h3>
          <p class="text-gray-400 text-sm leading-relaxed">
            {{ $t('features.multiExchange.description') }}
          </p>
        </div>
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
.reveal.delay-300 {
  transition-delay: 0.3s;
}
.reveal.delay-400 {
  transition-delay: 0.4s;
}
.reveal.delay-500 {
  transition-delay: 0.5s;
}

.feature-icon {
  --icon-a: 102, 252, 241;
  --icon-b: 59, 130, 246;
  position: relative;
  display: flex;
  width: 68px;
  height: 68px;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  overflow: hidden;
  border: 1px solid rgba(var(--icon-a), 0.34);
  border-radius: 18px;
  background:
    radial-gradient(circle at 28% 18%, rgba(255, 255, 255, 0.18), transparent 24%),
    linear-gradient(145deg, rgba(var(--icon-a), 0.24), rgba(var(--icon-b), 0.12) 56%, rgba(8, 14, 26, 0.9));
  box-shadow:
    inset 0 0 22px rgba(var(--icon-a), 0.09),
    0 0 26px rgba(var(--icon-a), 0.18),
    0 18px 34px rgba(0, 0, 0, 0.28);
  transition: transform 0.32s ease, border-color 0.32s ease, box-shadow 0.32s ease;
}

.feature-icon::before {
  content: "";
  position: absolute;
  inset: -42%;
  background: conic-gradient(
    from 180deg,
    transparent,
    rgba(var(--icon-a), 0.5),
    rgba(var(--icon-b), 0.36),
    transparent 62%
  );
  opacity: 0.42;
  transition: transform 0.7s ease, opacity 0.32s ease;
}

.feature-icon::after {
  content: "";
  position: absolute;
  inset: 1px;
  border-radius: 17px;
  background:
    linear-gradient(145deg, rgba(255, 255, 255, 0.08), transparent 34%),
    rgba(8, 14, 26, 0.62);
}

.feature-icon svg {
  position: relative;
  z-index: 1;
  width: 45px;
  height: 45px;
  filter: drop-shadow(0 0 12px rgba(var(--icon-a), 0.5));
}

.tech-module-card:hover .feature-icon {
  border-color: rgba(var(--icon-a), 0.72);
  box-shadow:
    inset 0 0 24px rgba(var(--icon-a), 0.13),
    0 0 34px rgba(var(--icon-a), 0.28),
    0 20px 42px rgba(0, 0, 0, 0.34);
  transform: translateY(-3px) scale(1.05);
}

.tech-module-card:hover .feature-icon::before {
  opacity: 0.76;
  transform: rotate(95deg);
}

.feature-icon--market {
  --icon-a: 102, 252, 241;
  --icon-b: 168, 85, 247;
}

.feature-icon--mtf {
  --icon-a: 94, 231, 255;
  --icon-b: 192, 132, 252;
}

.feature-icon--ai {
  --icon-a: 102, 252, 241;
  --icon-b: 255, 79, 216;
}

.feature-icon--risk {
  --icon-a: 124, 255, 178;
  --icon-b: 255, 139, 110;
}

.feature-icon--auto {
  --icon-a: 102, 252, 241;
  --icon-b: 250, 204, 21;
}

.feature-icon--exchange {
  --icon-a: 94, 231, 255;
  --icon-b: 34, 197, 94;
}

@media (prefers-reduced-motion: reduce) {
  .feature-icon,
  .feature-icon::before {
    transition: none;
  }
}

@media (max-width: 767px) {
  #features {
    padding-top: 4.25rem;
    padding-bottom: 4.25rem;
  }

  #features .text-center.mb-16 {
    margin-bottom: 2.2rem;
  }

  #features h2 {
    font-size: 2rem;
    line-height: 1.2;
  }

  #features .grid {
    gap: 1rem;
  }

  .tech-module-card {
    padding: 1.2rem !important;
    border-radius: 18px;
  }

  .feature-icon {
    width: 56px;
    height: 56px;
    margin-bottom: 1rem;
    border-radius: 16px;
  }

  .feature-icon::after {
    border-radius: 15px;
  }

  .feature-icon svg {
    width: 37px;
    height: 37px;
  }

  .tech-module-card h3 {
    margin-bottom: 0.65rem;
    font-size: 1.22rem;
    line-height: 1.35;
  }

  .tech-module-card p {
    font-size: 0.88rem;
    line-height: 1.65;
  }

  .module-visual {
    min-height: 42px;
    margin-top: 1rem;
    padding-top: 0.85rem;
  }

  .flow-bars,
  .score-bars {
    height: 36px;
  }

  .time-rings,
  .risk-tags,
  .execution-line {
    gap: 0.4rem;
  }

  .time-rings {
    flex-wrap: wrap;
  }

  .time-rings span,
  .risk-tag {
    padding: 0.42rem 0.55rem;
    font-size: 0.62rem;
  }

  .execution-line {
    align-items: flex-start;
    font-size: 0.68rem;
  }
}
</style>
