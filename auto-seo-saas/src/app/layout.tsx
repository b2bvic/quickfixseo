import '@/styles/tailwind.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: {
    template: '%s - QuickFixSEO',
    default: 'QuickFixSEO - Professional SEO Audits in Minutes',
  },
      description: 'Get professional SEO audits in minutes, not weeks. QuickFixSEO finds everything wrong with your website and tells you exactly how to fix it. Built by Scale With Search, trusted by 2,800+ agencies worldwide.',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <head>
        <link
          rel="stylesheet"
          href="https://api.fontshare.com/css?f%5B%5D=switzer@400,500,600,700&amp;display=swap"
        />
        <link
          rel="alternate"
          type="application/rss+xml"
          title="The Radiant Blog"
          href="/blog/feed.xml"
        />
      </head>
      <body className="text-gray-950 antialiased">{children}</body>
    </html>
  )
}
