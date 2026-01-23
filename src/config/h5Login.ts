const h5LoginPort = 5173

export function getH5LoginUrl(): string {
  if (typeof window === 'undefined') {
    return `http://localhost:${h5LoginPort}`
  }

  const host = window.location.hostname || 'localhost'
  return `http://${host}:${h5LoginPort}`
}
