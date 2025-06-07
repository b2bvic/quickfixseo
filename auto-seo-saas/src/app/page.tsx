import { BentoCard } from '@/components/bento-card'
import { Button } from '@/components/button'
import { Container } from '@/components/container'
import { Footer } from '@/components/footer'
import { Gradient } from '@/components/gradient'
import { Keyboard } from '@/components/keyboard'
import { Link } from '@/components/link'
import { LinkedAvatars } from '@/components/linked-avatars'
import { LogoCloud } from '@/components/logo-cloud'
import { LogoCluster } from '@/components/logo-cluster'
import { LogoTimeline } from '@/components/logo-timeline'
import { Map } from '@/components/map'
import { Navbar } from '@/components/navbar'
import { Screenshot } from '@/components/screenshot'
import { Testimonials } from '@/components/testimonials'
import { Heading, Subheading } from '@/components/text'
import { ChevronRightIcon } from '@heroicons/react/16/solid'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  description:
    'Get professional SEO audits in minutes, not weeks. AUTO SEO finds everything wrong with your website and tells you exactly how to fix it. Trusted by 2,800+ agencies worldwide.',
}

function Hero() {
  return (
    <div className="relative">
      <div className="absolute inset-0 bg-gradient-to-br from-emerald-50 via-white to-slate-50"></div>
      <Container className="relative">
        <Navbar
          banner={
            <Link
              href="/audit"
              className="flex items-center gap-1 rounded-full bg-emerald-100 px-3 py-0.5 text-sm/6 font-medium text-emerald-800 hover:bg-emerald-200 transition-colors"
            >
                              ⚡ Start your free audit now
              <ChevronRightIcon className="size-4" />
            </Link>
          }
        />
        <div className="pt-16 pb-24 sm:pt-24 sm:pb-32 md:pt-32 md:pb-48">
          <h1 className="font-display text-6xl/[0.9] font-medium tracking-tight text-balance text-slate-900 sm:text-8xl/[0.8] md:text-9xl/[0.8]">
            Your next client is waiting for this audit.
          </h1>
          <p className="mt-8 max-w-2xl text-xl/7 font-medium text-slate-600 sm:text-2xl/8">
            Stop spending weeks building SEO reports manually. AUTO SEO delivers comprehensive audits in 12 minutes, finds issues other tools miss, and creates client-ready presentations that close deals.
          </p>
          <div className="mt-12 flex flex-col gap-x-6 gap-y-4 sm:flex-row">
            <Button href="/audit" className="text-lg px-8 py-4 bg-emerald-600 hover:bg-emerald-700">Start free audit</Button>
                          <Button variant="secondary" href="/pricing" className="text-lg px-8 py-4 text-slate-700 border-slate-300 hover:border-slate-400">
                View pricing
              </Button>
          </div>
          <p className="mt-6 text-sm text-slate-500">
            ✓ No signup required for your first audit &nbsp;&nbsp; ✓ Results in under 15 minutes &nbsp;&nbsp; ✓ Client-ready report included
          </p>
        </div>
      </Container>
    </div>
  )
}

function TrustIndicators() {
  return (
    <Container className="py-16">
      <p className="text-center text-sm font-medium text-slate-500 mb-8">
        Trusted by agencies and consultants worldwide
      </p>
      <LogoCloud />
      <div className="mt-12 flex justify-center gap-8 text-sm text-slate-500">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 bg-emerald-500 rounded-full"></div>
          <span>2,800+ satisfied customers</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 bg-slate-400 rounded-full"></div>
          <span>15 million pages audited</span>
        </div>
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 bg-emerald-500 rounded-full"></div>
          <span>4.9/5 star rating</span>
        </div>
      </div>
    </Container>
  )
}

function ProblemSection() {
  return (
    <div className="bg-slate-50 py-24">
      <Container>
        <div className="max-w-4xl mx-auto text-center">
          <Heading as="h2" className="text-slate-900">
            Your biggest competitor just launched their new website
          </Heading>
          <p className="mt-6 text-xl text-slate-600 leading-relaxed">
            While you&apos;re still gathering screenshots and checking meta tags manually, they&apos;re already ranking for your keywords. Every day you delay is revenue walking out the door.
          </p>
          
          <div className="mt-16 grid md:grid-cols-3 gap-8">
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
              <div className="text-4xl mb-4">😩</div>
              <h3 className="text-lg font-semibold text-slate-900 mb-3">Clients getting impatient</h3>
              <p className="text-slate-600">Three weeks for an audit feels like three months to clients who need results yesterday. They want answers, not excuses.</p>
            </div>
            
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
              <div className="text-4xl mb-4">💸</div>
              <h3 className="text-lg font-semibold text-slate-900 mb-3">Money left on the table</h3>
              <p className="text-slate-600">Each hour you spend on manual audits is an hour not spent closing new deals. That&apos;s $200/hour in lost opportunity.</p>
            </div>
            
            <div className="bg-white p-8 rounded-2xl shadow-sm border border-slate-200">
              <div className="text-4xl mb-4">😤</div>
              <h3 className="text-lg font-semibold text-slate-900 mb-3">Competitors moving faster</h3>
              <p className="text-slate-600">While you&apos;re checking canonicals one by one, smart agencies are delivering professional audits in minutes.</p>
            </div>
          </div>
        </div>
      </Container>
    </div>
  )
}

function SolutionSection() {
  return (
    <div className="bg-gradient-to-b from-white to-emerald-50 py-24">
      <Container>
        <div className="text-center mb-16">
          <Heading as="h2" className="text-slate-900">
            What if you could impress clients in 12 minutes instead of 12 days?
          </Heading>
          <p className="mt-6 text-xl text-slate-600 max-w-3xl mx-auto">
            AUTO SEO scans your entire website faster than you can make coffee, finds problems other tools miss, and creates beautiful reports that make clients say &ldquo;wow.&rdquo;
          </p>
        </div>
        
        <div className="mt-16 mx-auto max-w-4xl">
          <div className="bg-gradient-to-br from-emerald-500 to-teal-600 rounded-3xl shadow-2xl p-8 text-white">
            <div className="bg-white/10 rounded-2xl p-6 backdrop-blur-sm">
              <div className="flex items-center gap-4 mb-6">
                <div className="w-12 h-12 bg-emerald-300 rounded-full flex items-center justify-center">
                  <span className="text-emerald-800 font-bold text-xl">✓</span>
                </div>
                <div>
                  <h3 className="text-xl font-bold">Audit Complete</h3>
                  <p className="text-emerald-100">Perfect timing for your client call</p>
                </div>
              </div>
              <div className="grid grid-cols-3 gap-4 text-center">
                <div className="bg-white/10 rounded-xl p-4">
                  <div className="text-2xl font-bold">847</div>
                  <div className="text-sm text-emerald-200">Pages Scanned</div>
                </div>
                <div className="bg-white/10 rounded-xl p-4">
                  <div className="text-2xl font-bold">23</div>
                  <div className="text-sm text-emerald-200">Issues Found</div>
                </div>
                <div className="bg-white/10 rounded-xl p-4">
                  <div className="text-2xl font-bold">A+</div>
                  <div className="text-sm text-emerald-200">Overall Score</div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <div className="mt-16 grid md:grid-cols-3 gap-8">
          <div className="text-center">
            <div className="bg-emerald-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">⚡</span>
            </div>
            <h3 className="text-xl font-semibold mb-3">Win more clients</h3>
            <p className="text-slate-600">Professional reports in minutes create trust instantly. Clients see you as the expert who gets things done.</p>
          </div>
          
          <div className="text-center">
            <div className="bg-slate-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">💰</span>
            </div>
            <h3 className="text-xl font-semibold mb-3">Triple your capacity</h3>
            <p className="text-slate-600">Handle 3x more clients without hiring anyone. Each audit takes 12 minutes instead of 12 hours.</p>
          </div>
          
          <div className="text-center">
            <div className="bg-emerald-100 w-16 h-16 rounded-full flex items-center justify-center mx-auto mb-4">
              <span className="text-2xl">🎯</span>
            </div>
            <h3 className="text-xl font-semibold mb-3">Never miss anything</h3>
            <p className="text-slate-600">Comprehensive analysis catches issues you&apos;d spend hours hunting for manually. Your clients get better results.</p>
          </div>
        </div>
      </Container>
    </div>
  )
}

function BentoSection() {
  return (
    <Container className="py-24">
      <Subheading className="text-center">Everything you need</Subheading>
      <Heading as="h3" className="mt-2 max-w-4xl text-center mx-auto">
        Professional audits that close deals and keep clients happy
      </Heading>

      <div className="mt-10 grid grid-cols-1 gap-4 sm:mt-16 lg:grid-cols-6 lg:grid-rows-2">
        <BentoCard
          eyebrow="Speed"
          title="Results while your coffee is still hot"
          description="Complete website audits in 12 minutes, not 12 hours. Scan hundreds of pages simultaneously while you focus on strategy, not spreadsheets."
          graphic={
            <div className="h-80 bg-gradient-to-br from-emerald-400 via-teal-500 to-emerald-600 rounded-2xl flex flex-col items-center justify-center text-white">
              <div className="text-6xl font-bold mb-2">12</div>
              <div className="text-xl font-medium">MINUTES</div>
            </div>
          }
          fade={['bottom']}
          className="max-lg:rounded-t-4xl lg:col-span-3 lg:rounded-tl-4xl"
        />
        <BentoCard
          eyebrow="Completeness"
          title="Find what others miss"
          description="Comprehensive scans check everything from meta tags to Core Web Vitals. Never wonder if you missed something important again."
          graphic={
            <div className="absolute inset-0 bg-gradient-to-br from-slate-600 to-slate-800 flex items-center justify-center">
              <div className="grid grid-cols-3 gap-4 text-white text-center">
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Technical</div>
                </div>
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Content</div>
                </div>
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Speed</div>
                </div>
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Mobile</div>
                </div>
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Security</div>
                </div>
                <div>
                  <div className="text-2xl mb-1">✓</div>
                  <div className="text-xs">Schema</div>
                </div>
              </div>
            </div>
          }
          fade={['bottom']}
          className="lg:col-span-3 lg:rounded-tr-4xl"
        />
        <BentoCard
          eyebrow="Professional presentation"
          title="Reports that close deals"
          description="Beautiful, client-ready reports with executive summaries, action plans, and ROI projections. Your clients will think you hired a team of consultants."
          graphic={
            <div className="flex size-full pt-10 pl-10">
              <div className="bg-white rounded-xl shadow-2xl p-6 w-full border">
                <div className="flex items-center gap-3 mb-4">
                  <div className="w-8 h-8 bg-emerald-100 rounded-full flex items-center justify-center">
                    <span className="text-emerald-600 font-bold text-sm">A+</span>
                  </div>
                  <div>
                    <div className="h-3 bg-slate-800 rounded w-24 mb-1"></div>
                    <div className="h-2 bg-slate-400 rounded w-16"></div>
                  </div>
                </div>
                <div className="space-y-2">
                  <div className="h-2 bg-emerald-200 rounded w-full"></div>
                  <div className="h-2 bg-yellow-200 rounded w-3/4"></div>
                  <div className="h-2 bg-red-200 rounded w-1/2"></div>
                </div>
              </div>
            </div>
          }
          className="lg:col-span-2 lg:rounded-bl-4xl"
        />
        <BentoCard
          eyebrow="Scale"
          title="Handle any size website"
          description="From 50-page local sites to 50,000-page enterprise platforms. No limits on Professional plans."
          graphic={
            <div className="flex items-center justify-center h-full text-6xl font-bold text-slate-400">
              ∞
            </div>
          }
          className="lg:col-span-2"
        />
        <BentoCard
          eyebrow="Insights"
          title="Smart recommendations that work"
          description="Don&apos;t just find problems—get actionable solutions. Every issue comes with clear fix instructions and priority rankings."
          graphic={
            <div className="h-80 bg-gradient-to-t from-emerald-400 via-teal-500 to-slate-600 rounded-2xl flex items-center justify-center">
              <div className="text-white text-4xl">💡</div>
            </div>
          }
          className="max-lg:rounded-b-4xl lg:col-span-2 lg:rounded-br-4xl"
        />
      </div>
    </Container>
  )
}

function ROISection() {
  return (
    <div className="bg-slate-900 py-24">
      <Container>
        <div className="text-center mb-16">
          <Subheading dark>The numbers don&apos;t lie</Subheading>
          <Heading as="h3" dark className="mt-2 text-white">
            Your first audit pays for AUTO SEO for the next 25 years
          </Heading>
        </div>

        <div className="grid md:grid-cols-2 gap-12 items-center">
          <div>
            <div className="bg-red-900/20 border border-red-800 rounded-2xl p-8 mb-8">
              <h4 className="text-xl font-semibold text-red-400 mb-4">❌ The old way</h4>
              <div className="space-y-3 text-red-300">
                <div className="flex justify-between">
                  <span>Hours per audit:</span>
                  <span className="font-bold">40 hours</span>
                </div>
                <div className="flex justify-between">
                  <span>Your billable rate:</span>
                  <span className="font-bold">$150/hour</span>
                </div>
                <div className="flex justify-between">
                  <span>Opportunity cost:</span>
                  <span className="font-bold">$6,000</span>
                </div>
                <div className="flex justify-between">
                  <span>Client satisfaction:</span>
                  <span className="font-bold">Stressed 😰</span>
                </div>
              </div>
            </div>
          </div>
          
          <div>
            <div className="bg-emerald-900/20 border border-emerald-800 rounded-2xl p-8">
              <h4 className="text-xl font-semibold text-emerald-400 mb-4">✅ The AUTO SEO way</h4>
              <div className="space-y-3 text-emerald-300">
                <div className="flex justify-between">
                  <span>Hours per audit:</span>
                  <span className="font-bold">0.2 hours</span>
                </div>
                <div className="flex justify-between">
                  <span>AUTO SEO cost:</span>
                  <span className="font-bold">$19/month</span>
                </div>
                <div className="flex justify-between">
                  <span>Time saved:</span>
                  <span className="font-bold">39.8 hours</span>
                </div>
                <div className="flex justify-between">
                  <span>Value created:</span>
                  <span className="font-bold text-2xl">$5,970</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div className="mt-16 text-center">
          <div className="bg-gradient-to-r from-emerald-600 to-teal-600 rounded-3xl p-8 max-w-2xl mx-auto">
            <h4 className="text-2xl font-bold text-white mb-4">
              Complete just ONE audit and save enough to pay for 25 years of service
            </h4>
            <p className="text-emerald-100 mb-6">
              That&apos;s not a typo. The time you save on your first audit literally pays for AUTO SEO for the next quarter-century.
            </p>
            <Button href="/audit" className="bg-white text-emerald-600 hover:bg-emerald-50">
              Start saving time today
            </Button>
          </div>
        </div>
      </Container>
    </div>
  )
}

function EnterpriseSection() {
  return (
    <div className="mx-2 mt-2 rounded-4xl bg-slate-900 py-32">
      <Container>
        <Subheading dark>Built for professionals</Subheading>
        <Heading as="h3" dark className="mt-2 max-w-3xl text-white">
          Everything you need to dominate your market
        </Heading>

        <div className="mt-10 grid grid-cols-1 gap-4 sm:mt-16 lg:grid-cols-6 lg:grid-rows-2">
          <BentoCard
            dark
            eyebrow="Performance"
            title="Lightning-fast results"
            description="While competitors crawl 1 page at a time, AUTO SEO analyzes 20 pages simultaneously. Get results 20x faster than anyone else."
            graphic={
              <div className="h-80 bg-gradient-to-br from-emerald-600 to-teal-600 rounded-2xl flex items-center justify-center">
                <div className="text-white text-6xl">⚡</div>
              </div>
            }
            fade={['top']}
            className="max-lg:rounded-t-4xl lg:col-span-4 lg:rounded-tl-4xl"
          />
          <BentoCard
            dark
            eyebrow="Pricing"
            title="Honest, transparent pricing"
            description="No hidden fees, no surprise charges. What you see is what you pay. Cancel anytime with 30-day money-back guarantee."
            graphic={
              <div className="flex flex-col gap-2 p-4">
                <div className="bg-emerald-600 text-white p-3 rounded-lg text-center">
                  <div className="font-bold">$19</div>
                  <div className="text-xs">per month</div>
                </div>
                <div className="bg-teal-600 text-white p-3 rounded-lg text-center">
                  <div className="font-bold">$199</div>
                  <div className="text-xs">per year</div>
                </div>
                <div className="bg-slate-600 text-white p-3 rounded-lg text-center">
                  <div className="font-bold">$999</div>
                  <div className="text-xs">lifetime</div>
                </div>
              </div>
            }
            className="z-10 overflow-visible lg:col-span-2 lg:rounded-tr-4xl"
          />
          <BentoCard
            dark
            eyebrow="Support"
            title="Expert help when you need it"
            description="Email support for Professional plans, priority support and video calls for Enterprise. Real SEO experts, not chatbots."
            graphic={<LinkedAvatars />}
            className="lg:col-span-2 lg:rounded-bl-4xl"
          />
          <BentoCard
            dark
            eyebrow="Integration"
            title="Fits your workflow perfectly"
            description="API access for Enterprise customers. White-label reports with your branding. Build it into your existing tools and processes."
            graphic={
              <div className="h-80 bg-gradient-to-br from-slate-700 to-slate-800 rounded-2xl flex items-center justify-center">
                <div className="text-white text-4xl">🔌</div>
              </div>
            }
            fade={['top']}
            className="max-lg:rounded-b-4xl lg:col-span-4 lg:rounded-br-4xl"
          />
        </div>
      </Container>
    </div>
  )
}

function FinalCTA() {
  return (
    <div className="bg-gradient-to-r from-emerald-600 to-teal-600 py-24">
      <Container>
        <div className="text-center">
          <h2 className="text-5xl font-bold text-white mb-6">
            Your next client is waiting for this audit
          </h2>
          <p className="text-xl text-emerald-100 mb-8 max-w-3xl mx-auto">
            Join 2,800+ agencies and consultants who&apos;ve already transformed their workflow. 
            Start your free audit today—no signup required.
          </p>
          
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center mb-8">
            <Button href="/audit" className="bg-white text-emerald-600 hover:bg-emerald-50 text-lg px-8 py-4">
              Start free audit
            </Button>
            <Button href="/pricing" variant="secondary" className="border-white text-white hover:bg-white hover:text-emerald-600 text-lg px-8 py-4">
              View pricing
            </Button>
          </div>
          
          <div className="flex justify-center gap-8 text-emerald-100 text-sm">
            <span>✓ No signup required</span>
            <span>✓ Results in 15 minutes</span>
            <span>✓ Client-ready report</span>
          </div>
        </div>
      </Container>
    </div>
  )
}

export default function Home() {
  return (
    <div className="overflow-hidden">
      <Hero />
      <TrustIndicators />
      <ProblemSection />
      <SolutionSection />
      <main>
        <div className="bg-gradient-to-b from-emerald-50/50 to-white py-16">
          <BentoSection />
        </div>
        <ROISection />
        <EnterpriseSection />
        <div className="bg-slate-50 py-32">
          <Container>
            <Testimonials />
          </Container>
        </div>
        <FinalCTA />
      </main>
      <Footer />
    </div>
  )
}
