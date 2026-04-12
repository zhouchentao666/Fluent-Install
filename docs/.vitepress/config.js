import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'FluentInstall 流畅入库',
  description: '免费开源的 Steam 入库工具，基于 cai-install 后端改编，采用 Fluent Design 设计',

  base: '/Fluent-Install/',

  head: [
    ['link', { rel: 'icon', href: '/icon.ico' }],
    ['link', { rel: 'shortcut icon', href: '/icon.ico' }]
  ],

  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-CN',
      themeConfig: {
        nav: [
          { text: '首页', link: '/' },
          { text: '入门指南', link: '/guide/getting-started' },
          { text: '常见问题', link: '/faq/' },
          {
            text: '关于',
            items: [
              { text: '关于项目', link: '/about' },
              { text: '鸣谢', link: '/thanks' },
              { text: '捐赠', link: '/donate' }
            ]
          },
          {
            text: '社区与交流',
            items: [
              { text: 'GitHub Issue', link: 'https://github.com/zhouchentao666/Fluent-Install/issues' },
              { text: 'Q群', link: 'https://qm.qq.com/q/gtTLap5Jw4' },
              { text: 'TG群', link: 'https://t.me/+vTrqXKpRJE9kNmVl' }
            ]
          }
        ],
        sidebar: [
          {
            text: '指南',
            items: [
              { text: '入门指南', link: '/guide/getting-started' }
            ]
          },
          {
            text: '常见问题',
            items: [
              { text: 'FAQ', link: '/faq/' }
            ]
          },
          {
            text: '关于',
            items: [
              { text: '关于项目', link: '/about' },
              { text: '鸣谢', link: '/thanks' },
              { text: '捐赠', link: '/donate' }
            ]
          }
        ],
        footer: {
          message: 'FluentInstall 流畅入库 - 免费开源的 Steam 入库工具',
          copyright: 'Copyright © 2024-present'
        },
        socialLinks: [
          { icon: 'github', link: 'https://github.com/zhouchentao666/Fluent-Install' }
        ]
      }
    },
    'zh-tw': {
      label: '繁體中文',
      lang: 'zh-TW',
      themeConfig: {
        nav: [
          { text: '首頁', link: '/zh-tw/' },
          { text: '入門指南', link: '/zh-tw/guide/getting-started' },
          { text: '常見問題', link: '/zh-tw/faq/' },
          {
            text: '關於',
            items: [
              { text: '關於專案', link: '/zh-tw/about' },
              { text: '鳴謝', link: '/zh-tw/thanks' },
              { text: '捐贈', link: '/zh-tw/donate' }
            ]
          },
          {
            text: '社群與交流',
            items: [
              { text: 'GitHub Issue', link: 'https://github.com/zhouchentao666/Fluent-Install/issues' },
              { text: 'QQ群', link: 'https://qm.qq.com/q/gtTLap5Jw4' },
              { text: 'TG群', link: 'https://t.me/+vTrqXKpRJE9kNmVl' }
            ]
          }
        ],
        sidebar: [
          {
            text: '指南',
            items: [
              { text: '入門指南', link: '/zh-tw/guide/getting-started' }
            ]
          },
          {
            text: '常見問題',
            items: [
              { text: 'FAQ', link: '/zh-tw/faq/' }
            ]
          },
          {
            text: '關於',
            items: [
              { text: '關於專案', link: '/zh-tw/about' },
              { text: '鳴謝', link: '/zh-tw/thanks' },
              { text: '捐贈', link: '/zh-tw/donate' }
            ]
          }
        ],
        footer: {
          message: 'FluentInstall 流暢入庫 - 免費開源的 Steam 入庫工具',
          copyright: 'Copyright © 2024-present'
        },
        socialLinks: [
          { icon: 'github', link: 'https://github.com/zhouchentao666/Fluent-Install' }
        ]
      }
    },
    'en': {
      label: 'English',
      lang: 'en-US',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: 'Quick Start', link: '/en/guide/getting-started' },
          { text: 'FAQ', link: '/en/faq/' },
          {
            text: 'About',
            items: [
              { text: 'About Project', link: '/en/about' },
              { text: 'Credits', link: '/en/thanks' },
              { text: 'Donate', link: '/en/donate' }
            ]
          },
          {
            text: 'Community',
            items: [
              { text: 'GitHub Issue', link: 'https://github.com/zhouchentao666/Fluent-Install/issues' },
              { text: 'QQ Group', link: 'https://qm.qq.com/q/gtTLap5Jw4' },
              { text: 'Telegram', link: 'https://t.me/+vTrqXKpRJE9kNmVl' }
            ]
          }
        ],
        sidebar: [
          {
            text: 'Guide',
            items: [
              { text: 'Quick Start', link: '/en/guide/getting-started' }
            ]
          },
          {
            text: 'FAQ',
            items: [
              { text: 'FAQ', link: '/en/faq/' }
            ]
          },
          {
            text: 'About',
            items: [
              { text: 'About Project', link: '/en/about' },
              { text: 'Credits', link: '/en/thanks' },
              { text: 'Donate', link: '/en/donate' }
            ]
          }
        ],
        footer: {
          message: 'FluentInstall - Free & Open Source Steam Library Tool',
          copyright: 'Copyright © 2024-present'
        },
        socialLinks: [
          { icon: 'github', link: 'https://github.com/zhouchentao666/Fluent-Install' }
        ]
      }
    }
  },

  themeConfig: {
    logo: '/icon.ico',
    search: {
      provider: 'local'
    }
  }
})

