'use client'

import { Button } from '@/components/button'
import { Container } from '@/components/container'
import { Navbar } from '@/components/navbar'
import { Heading } from '@/components/text'
import { useState } from 'react'
import { useRouter } from 'next/navigation'

export default function SetupDemoPage() {
  const [isSetup, setIsSetup] = useState(false)
  const router = useRouter()

  const setupDummyData = () => {
    // User data
    const userData = {
      name: 'Demo User',
      email: 'demo@example.com'
    }

    // Sample audit data with limitlesschiroatx.com and other realistic examples
    const sampleAudits = [
      {
        url: 'https://limitlesschiroatx.com',
        score: 73,
        issues: {
          critical: 4,
          warning: 7,
          info: 12
        },
        pages_scanned: 42,
        load_time: 2.3,
        recommendations: [
          'Optimize images - 15 images are over 1MB and slowing down page load',
          'Add missing meta descriptions to 8 key service pages',
          'Fix 3 broken internal links to appointment booking pages',
          'Implement structured data markup for local business schema',
          'Optimize mobile responsiveness on service detail pages',
          'Improve page titles - 6 pages have non-descriptive titles',
          'Add alt text to 12 images for better accessibility',
          'Optimize Core Web Vitals - LCP is 4.2s (should be under 2.5s)',
          'Fix duplicate meta descriptions on blog posts',
          'Add canonical tags to prevent duplicate content issues',
          'Optimize for local SEO keywords like "chiropractor Austin TX"',
          'Improve internal linking structure for better crawlability'
        ],
        date: new Date(Date.now() - 2 * 24 * 60 * 60 * 1000).toISOString(), // 2 days ago
        type: 'free'
      },
      {
        url: 'https://example-agency.com',
        score: 89,
        issues: {
          critical: 1,
          warning: 3,
          info: 8
        },
        pages_scanned: 156,
        load_time: 1.8,
        recommendations: [
          'Fix one critical redirect chain on the main service page',
          'Optimize 3 images for better compression',
          'Add structured data for service pages',
          'Improve meta description for blog category pages',
          'Update outdated content on 2 service pages',
          'Add internal links to improve page authority distribution',
          'Optimize contact form for better conversion',
          'Update copyright year in footer'
        ],
        date: new Date(Date.now() - 5 * 24 * 60 * 60 * 1000).toISOString(), // 5 days ago
        type: 'pro'
      },
      {
        url: 'https://client-website.com',
        score: 91,
        issues: {
          critical: 0,
          warning: 2,
          info: 5
        },
        pages_scanned: 78,
        load_time: 1.4,
        recommendations: [
          'Minor image optimization opportunities on 2 pages',
          'Add FAQ schema markup to improve rich snippets',
          'Update meta descriptions to include target keywords',
          'Optimize page titles for better click-through rates',
          'Add breadcrumb navigation for better user experience'
        ],
        date: new Date(Date.now() - 1 * 24 * 60 * 60 * 1000).toISOString(), // 1 day ago
        type: 'pro'
      },
      {
        url: 'https://startup-demo.com',
        score: 65,
        issues: {
          critical: 6,
          warning: 11,
          info: 15
        },
        pages_scanned: 23,
        load_time: 3.1,
        recommendations: [
          'Critical: Fix broken SSL certificate causing security warnings',
          'Critical: Resolve 404 errors on 5 important product pages',
          'Optimize page load speed - currently 3.1s average',
          'Add mobile viewport meta tag for proper mobile rendering',
          'Fix broken contact form submission',
          'Add Google Analytics and Search Console integration',
          'Optimize images - reduce file sizes by up to 70%',
          'Add meta descriptions to all pages',
          'Fix HTML validation errors (23 errors found)',
          'Implement proper heading hierarchy (H1, H2, H3)',
          'Add social media meta tags for better sharing',
          'Set up XML sitemap and submit to search engines'
        ],
        date: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000).toISOString(), // 1 week ago
        type: 'free'
      }
    ]

    // Save to localStorage
    localStorage.setItem('userName', userData.name)
    localStorage.setItem('userEmail', userData.email)
    localStorage.setItem('userAudits', JSON.stringify(sampleAudits))

    setIsSetup(true)
  }

  const goToDashboard = () => {
    router.push('/dashboard')
  }

  const goToAudit = () => {
    router.push('/audit')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white">
      <Navbar />
      
      <Container className="py-24">
        <div className="max-w-2xl mx-auto text-center">
          <Heading as="h1">Demo Setup</Heading>
          <p className="mt-6 text-xl text-slate-600">
            Set up your account with sample audit data to explore the full AUTO SEO experience.
          </p>

          {!isSetup ? (
            <div className="mt-12">
              <div className="bg-white rounded-3xl shadow-xl border border-slate-200 p-8 mb-8">
                <h2 className="text-2xl font-bold text-slate-900 mb-6">
                  What you&apos;ll get:
                </h2>
                
                <div className="space-y-4 text-left">
                  <div className="flex items-start gap-3">
                    <div className="bg-emerald-100 text-emerald-600 rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold mt-1">
                      ✓
                    </div>
                    <div>
                      <h3 className="font-semibold text-slate-900">Sample User Account</h3>
                      <p className="text-slate-600 text-sm">Demo User with realistic usage data</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start gap-3">
                    <div className="bg-emerald-100 text-emerald-600 rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold mt-1">
                      ✓
                    </div>
                    <div>
                      <h3 className="font-semibold text-slate-900">4 Sample Audits</h3>
                      <p className="text-slate-600 text-sm">Including limitlesschiroatx.com with realistic SEO issues</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start gap-3">
                    <div className="bg-emerald-100 text-emerald-600 rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold mt-1">
                      ✓
                    </div>
                    <div>
                      <h3 className="font-semibold text-slate-900">Mixed Plan Types</h3>
                      <p className="text-slate-600 text-sm">See both Free and Pro audit experiences</p>
                    </div>
                  </div>
                  
                  <div className="flex items-start gap-3">
                    <div className="bg-emerald-100 text-emerald-600 rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold mt-1">
                      ✓
                    </div>
                    <div>
                      <h3 className="font-semibold text-slate-900">Realistic Data</h3>
                      <p className="text-slate-600 text-sm">Professional SEO recommendations and scores</p>
                    </div>
                  </div>
                </div>
                
                <div className="mt-8 bg-slate-50 rounded-xl p-4">
                  <h3 className="font-semibold text-slate-900 mb-2">Featured Audit:</h3>
                  <div className="text-sm text-slate-600">
                    <p><strong>limitlesschiroatx.com</strong> - Score: 73/100</p>
                    <p>42 pages scanned, 23 issues found</p>
                    <p>Realistic chiropractic practice SEO audit with actionable recommendations</p>
                  </div>
                </div>
              </div>

              <Button 
                onClick={setupDummyData}
                className="bg-emerald-600 hover:bg-emerald-700 text-lg px-8 py-4"
              >
                Set Up Demo Account
              </Button>
              
              <p className="mt-4 text-sm text-slate-500">
                This will populate your browser with sample data for testing
              </p>
            </div>
          ) : (
            <div className="mt-12">
              <div className="bg-emerald-50 border border-emerald-200 rounded-3xl p-8 mb-8">
                <div className="text-4xl mb-4">🎉</div>
                <h2 className="text-2xl font-bold text-emerald-900 mb-4">
                  Demo Account Ready!
                </h2>
                <p className="text-emerald-800 mb-6">
                  Your account has been set up with sample audit data. You can now explore the full AUTO SEO experience.
                </p>
                
                <div className="grid md:grid-cols-2 gap-4">
                  <div className="bg-white rounded-xl p-4 text-center">
                    <h3 className="font-semibold text-slate-900 mb-2">View Dashboard</h3>
                    <p className="text-sm text-slate-600 mb-3">
                      See your audit history and account overview
                    </p>
                    <Button 
                      onClick={goToDashboard}
                      className="w-full bg-emerald-600 hover:bg-emerald-700"
                    >
                      Go to Dashboard
                    </Button>
                  </div>
                  
                  <div className="bg-white rounded-xl p-4 text-center">
                    <h3 className="font-semibold text-slate-900 mb-2">Try New Audit</h3>
                    <p className="text-sm text-slate-600 mb-3">
                      Run a fresh audit on any website
                    </p>
                    <Button 
                      onClick={goToAudit}
                      variant="secondary"
                      className="w-full border-emerald-300 text-emerald-700"
                    >
                      Start New Audit
                    </Button>
                  </div>
                </div>
              </div>
              
              <div className="bg-blue-50 rounded-2xl p-6">
                <h3 className="font-semibold text-blue-900 mb-2">💡 Pro Tip</h3>
                <p className="text-blue-800 text-sm">
                  The sample data includes both Free and Pro audit types. Notice how Pro audits show more detailed recommendations and unlimited page scanning.
                </p>
              </div>
            </div>
          )}
        </div>
      </Container>
    </div>
  )
} 