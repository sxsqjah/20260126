import { onMounted, onUnmounted } from 'vue'

export function useRevealAnimation() {
  let observer: IntersectionObserver | null = null

  const initObserver = () => {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.1
    }

    observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active')
          observer?.unobserve(entry.target)
        }
      })
    }, observerOptions)

    // 观察所有带有 .reveal 类的元素
    document.querySelectorAll('.reveal').forEach(el => {
      observer?.observe(el)
    })
  }

  onMounted(() => {
    initObserver()
  })

  onUnmounted(() => {
    if (observer) {
      observer.disconnect()
    }
  })
}

