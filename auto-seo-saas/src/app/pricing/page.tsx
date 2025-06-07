import { Container } from '@/components/container'
import { Navbar } from '@/components/navbar'
import { Footer } from '@/components/footer'
import { Heading } from '@/components/text'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Pricing - Get Professional SEO Audits in Minutes',
  description:
    'Stop spending weeks on manual SEO audits. Get professional, client-ready reports in 12 minutes. Plans start at $19/month. No setup fees, cancel anytime.',
}

export default function Pricing() {
  return (
    <main className="overflow-hidden">
      <div className="absolute inset-0 bg-gradient-to-br from-emerald-50 via-white to-slate-50"></div>
      <Container className="relative">
        <Navbar />
      </Container>
      <Container className="relative mt-16 py-16">
        <div className="text-center">
          <Heading as="h1" className="max-w-4xl mx-auto">
            Pricing - Coming Soon
          </Heading>
          <p className="mt-6 text-xl text-slate-600">
            We&apos;re working on our pricing page. Please check back soon!
          </p>
        </div>
      </Container>
      <Footer />
    </main>
  )
}
