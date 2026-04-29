<template>
  <div class="blockchain-network" aria-hidden="true">
    <canvas ref="canvasRef" class="network-canvas"></canvas>
    <div class="network-grid"></div>
    <div class="engine-ring">
      <div class="engine-ring__core"></div>
      <div class="engine-ring__orbit engine-ring__orbit--outer"></div>
      <div class="engine-ring__orbit engine-ring__orbit--inner"></div>
    </div>
    <div class="hash-stream hash-stream--left">
      <span v-for="hash in leftHashes" :key="hash">{{ hash }}</span>
    </div>
    <div class="hash-stream hash-stream--right">
      <span v-for="hash in rightHashes" :key="hash">{{ hash }}</span>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue'

type NodePoint = {
  x: number
  y: number
  vx: number
  vy: number
  radius: number
}

const canvasRef = ref<HTMLCanvasElement | null>(null)
const leftHashes = ['0xA91F', 'zk-482', 'OI+12', 'liq:37', 'hash:8E']
const rightHashes = ['flow:in', '0x72C4', 'fund:+', 'risk:ok', 'AI:72']

let animationFrame = 0
let nodes: NodePoint[] = []
let reducedMotion = false
let cleanupResize: (() => void) | null = null

function createNodes(width: number, height: number) {
  const isMobile = width < 768
  const count = isMobile ? 26 : 54
  nodes = Array.from({ length: count }, () => ({
    x: Math.random() * width,
    y: Math.random() * height,
    vx: (Math.random() - 0.5) * 0.18,
    vy: (Math.random() - 0.5) * 0.18,
    radius: Math.random() * 1.4 + 0.8,
  }))
}

function resizeCanvas(canvas: HTMLCanvasElement) {
  const { width, height } = canvas.getBoundingClientRect()
  const ratio = Math.min(window.devicePixelRatio || 1, 2)
  canvas.width = Math.max(1, Math.floor(width * ratio))
  canvas.height = Math.max(1, Math.floor(height * ratio))
  const context = canvas.getContext('2d')
  context?.setTransform(ratio, 0, 0, ratio, 0, 0)
  createNodes(width, height)
}

function drawNetwork(canvas: HTMLCanvasElement) {
  const context = canvas.getContext('2d')
  if (!context) {
    return
  }

  const { width, height } = canvas.getBoundingClientRect()
  context.clearRect(0, 0, width, height)

  const maxDistance = width < 768 ? 120 : 165
  for (let i = 0; i < nodes.length; i += 1) {
    const node = nodes[i]
    if (!reducedMotion) {
      node.x += node.vx
      node.y += node.vy
      if (node.x < 0 || node.x > width) node.vx *= -1
      if (node.y < 0 || node.y > height) node.vy *= -1
    }

    for (let j = i + 1; j < nodes.length; j += 1) {
      const other = nodes[j]
      const distance = Math.hypot(node.x - other.x, node.y - other.y)
      if (distance < maxDistance) {
        const opacity = (1 - distance / maxDistance) * 0.22
        context.strokeStyle = `rgba(102, 252, 241, ${opacity})`
        context.lineWidth = 1
        context.beginPath()
        context.moveTo(node.x, node.y)
        context.lineTo(other.x, other.y)
        context.stroke()
      }
    }

    context.fillStyle = 'rgba(102, 252, 241, 0.72)'
    context.shadowColor = 'rgba(102, 252, 241, 0.85)'
    context.shadowBlur = 8
    context.beginPath()
    context.arc(node.x, node.y, node.radius, 0, Math.PI * 2)
    context.fill()
    context.shadowBlur = 0
  }

  if (!reducedMotion) {
    animationFrame = requestAnimationFrame(() => drawNetwork(canvas))
  }
}

onMounted(() => {
  const canvas = canvasRef.value
  if (!canvas) {
    return
  }

  reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches
  resizeCanvas(canvas)
  drawNetwork(canvas)

  const handleResize = () => {
    resizeCanvas(canvas)
    if (reducedMotion) {
      drawNetwork(canvas)
    }
  }
  window.addEventListener('resize', handleResize)
  cleanupResize = () => window.removeEventListener('resize', handleResize)
})

onBeforeUnmount(() => {
  cancelAnimationFrame(animationFrame)
  cleanupResize?.()
})
</script>

<style scoped>
.blockchain-network {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  background:
    radial-gradient(circle at 50% 38%, rgba(102, 252, 241, 0.14), transparent 26%),
    linear-gradient(180deg, rgba(8, 18, 28, 0.28), rgba(11, 12, 16, 0.94));
}

.network-canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  opacity: 0.82;
}

.network-grid {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(102, 252, 241, 0.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(102, 252, 241, 0.08) 1px, transparent 1px);
  background-size: 52px 52px;
  mask-image: linear-gradient(to bottom, rgba(0, 0, 0, 0.95), transparent 84%);
}

.engine-ring {
  position: absolute;
  left: 50%;
  top: 44%;
  width: min(44vw, 520px);
  aspect-ratio: 1;
  transform: translate(-50%, -50%);
  opacity: 0.8;
}

.engine-ring__core,
.engine-ring__orbit {
  position: absolute;
  inset: 18%;
  border-radius: 999px;
  border: 1px solid rgba(102, 252, 241, 0.28);
  box-shadow: inset 0 0 36px rgba(102, 252, 241, 0.08), 0 0 36px rgba(102, 252, 241, 0.12);
}

.engine-ring__core {
  inset: 30%;
  background: radial-gradient(circle, rgba(102, 252, 241, 0.18), rgba(69, 162, 158, 0.04) 58%, transparent 68%);
}

.engine-ring__orbit--outer {
  animation: spinRing 18s linear infinite;
  border-top-color: rgba(157, 120, 255, 0.6);
}

.engine-ring__orbit--inner {
  inset: 25%;
  animation: spinRing 12s linear infinite reverse;
  border-right-color: rgba(102, 252, 241, 0.72);
}

.hash-stream {
  position: absolute;
  top: 24%;
  display: grid;
  gap: 12px;
  color: rgba(102, 252, 241, 0.38);
  font-family: 'JetBrains Mono', monospace;
  font-size: 12px;
  letter-spacing: 0.08em;
}

.hash-stream--left {
  left: 6%;
}

.hash-stream--right {
  right: 6%;
  top: 32%;
}

.hash-stream span {
  animation: hashPulse 4s ease-in-out infinite;
}

.hash-stream span:nth-child(2n) {
  color: rgba(166, 120, 255, 0.34);
  animation-delay: 1.2s;
}

@keyframes spinRing {
  to {
    transform: rotate(360deg);
  }
}

@keyframes hashPulse {
  0%, 100% {
    opacity: 0.22;
    transform: translateY(0);
  }
  50% {
    opacity: 0.82;
    transform: translateY(-6px);
  }
}

@media (max-width: 767px), (prefers-reduced-motion: reduce) {
  .engine-ring {
    width: 86vw;
    opacity: 0.45;
  }

  .hash-stream {
    display: none;
  }

  .engine-ring__orbit,
  .hash-stream span {
    animation: none;
  }
}
</style>
