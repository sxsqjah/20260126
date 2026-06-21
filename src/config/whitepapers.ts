import type { Locale } from '../stores/i18n'

type WhitepaperDownload = {
  href: string
  filename: string
}

const whitepaperDownloads: Record<Locale, WhitepaperDownload> = {
  'zh-CN': {
    href: '/whitepapers/Crypto-K_Quants_Whitepaper_v1.3_zh-CN.pdf',
    filename: 'Crypto-K_Quants_Whitepaper_v1.3_zh-CN.pdf',
  },
  'zh-TW': {
    href: '/whitepapers/Crypto-K_Quants_Whitepaper_v1.3_zh-TW.pdf',
    filename: 'Crypto-K_Quants_Whitepaper_v1.3_zh-TW.pdf',
  },
  'ko-KR': {
    href: '/whitepapers/Crypto-K_Quants_Whitepaper_v1.3_ko-KR.pdf',
    filename: 'Crypto-K_Quants_Whitepaper_v1.3_ko-KR.pdf',
  },
  'en-US': {
    href: '/whitepapers/Crypto-K_Quants_Whitepaper_v1.3_en-US.pdf',
    filename: 'Crypto-K_Quants_Whitepaper_v1.3_en-US.pdf',
  },
  'ja-JP': {
    href: '/whitepapers/Crypto-K_Quants_Whitepaper_v1.3_ja-JP.pdf',
    filename: 'Crypto-K_Quants_Whitepaper_v1.3_ja-JP.pdf',
  },
}

export function getWhitepaperDownload(locale: Locale): WhitepaperDownload {
  return whitepaperDownloads[locale]
}
