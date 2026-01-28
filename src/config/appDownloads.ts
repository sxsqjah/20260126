import { buildApiUrl } from './api'

export const appDownloads = {
  android: {
    url: buildApiUrl('/system/app-download'),
    filename: 'ckq-app-android.apk',
  },
  ios: {
    url: 'https://home.ckqpro.com/#/',
    filename: 'ckq-app-ios.ipa',
  },
}
