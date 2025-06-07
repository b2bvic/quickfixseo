'use client'

import { Button } from '@/components/button'
import { Container } from '@/components/container'
import { Navbar } from '@/components/navbar'
import { Heading, Subheading } from '@/components/text'
import { useState } from 'react'
import { ChevronRightIcon } from '@heroicons/react/16/solid'
import { 
  GlobeAltIcon, 
  CheckCircleIcon, 
  ExclamationTriangleIcon,
  ClockIcon,
  ArrowPathIcon
} from '@heroicons/react/24/outline'

interface AuditFormData {
  url: string
  email: string
  name: string
}

interface AuditResult {
  url: string
  score: number
  issues: {
    critical: number
    warning: number
    info: number
  }
  pages_scanned: number
  load_time: number
  recommendations: string[]
}

export default function AuditPage() {
  const [step, setStep] = useState<'form' | 'processing' | 'results'>('form')
  const [formData, setFormData] = useState<AuditFormData>({
    url: '',
    email: '',
    name: ''
  })
  const [auditResult, setAuditResult] = useState<AuditResult | null>(null)
  const [isProcessing, setIsProcessing] = useState(false)

  const handleFormSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setStep('processing')
    setIsProcessing(true)

    // Simulate audit processing
    setTimeout(() => {
      // Mock audit results
      const mockResult: AuditResult = {
        url: formData.url,
        score: Math.floor(Math.random() * 40) + 60, // Score between 60-100
        issues: {
          critical: Math.floor(Math.random() * 5) + 1,
          warning: Math.floor(Math.random() * 8) + 3,
          info: Math.floor(Math.random() * 10) + 5
        },
        pages_scanned: Math.floor(Math.random() * 50) + 25,
        load_time: Math.random() * 2 + 1,
        recommendations: [
          'Optimize image compression to improve load times',
          'Add missing meta descriptions to 12 pages',
          'Fix broken internal links',
          'Implement structured data markup',
          'Optimize mobile responsiveness'
        ]
      }
      
      setAuditResult(mockResult)
      setIsProcessing(false)
      setStep('results')
      
      // Save to localStorage for dashboard
      const savedAudits = JSON.parse(localStorage.getItem('userAudits') || '[]')
      savedAudits.push({
        ...mockResult,
        date: new Date().toISOString(),
        type: 'free'
      })
      localStorage.setItem('userAudits', JSON.stringify(savedAudits))
      localStorage.setItem('userEmail', formData.email)
      localStorage.setItem('userName', formData.name)
    }, 3000)
  }

  const AuditForm = () => (
    <Container className="py-24">
      <div className="max-w-2xl mx-auto">
        <div className="text-center mb-12">
          <Heading as="h1">Get Your Free SEO Audit</Heading>
          <p className="mt-6 text-xl text-slate-600">
                         Discover what&apos;s holding your website back from ranking higher. 
            Get a comprehensive audit in under 15 minutes.
          </p>
        </div>

        <div className="bg-white rounded-3xl shadow-xl border border-slate-200 p-8">
          <form onSubmit={handleFormSubmit} className="space-y-6">
            <div>
              <label htmlFor="url" className="block text-sm font-medium text-slate-700 mb-2">
                Website URL
              </label>
              <div className="relative">
                <GlobeAltIcon className="absolute left-3 top-1/2 transform -translate-y-1/2 h-5 w-5 text-slate-400" />
                <input
                  id="url"
                  name="url"
                  type="url"
                  required
                  value={formData.url}
                  onChange={(e) => setFormData({...formData, url: e.target.value})}
                  className="w-full pl-10 pr-4 py-3 border border-slate-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
                  placeholder="https://yourwebsite.com"
                />
              </div>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label htmlFor="name" className="block text-sm font-medium text-slate-700 mb-2">
                  Your Name
                </label>
                <input
                  id="name"
                  name="name"
                  type="text"
                  required
                  value={formData.name}
                  onChange={(e) => setFormData({...formData, name: e.target.value})}
                  className="w-full px-4 py-3 border border-slate-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
                  placeholder="John Doe"
                />
              </div>
              
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-2">
                  Email Address
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  required
                  value={formData.email}
                  onChange={(e) => setFormData({...formData, email: e.target.value})}
                  className="w-full px-4 py-3 border border-slate-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500"
                  placeholder="john@company.com"
                />
              </div>
            </div>
            
            <Button type="submit" className="w-full text-lg py-4 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700">
              Start Free Audit
            </Button>
          </form>
          
          <div className="mt-6 text-center">
            <p className="text-sm text-slate-500">
              ✓ No credit card required &nbsp;&nbsp; ✓ Results in 15 minutes &nbsp;&nbsp; ✓ 100% free
            </p>
          </div>
        </div>

        {/* Upgrade Options */}
        <div className="mt-16 grid md:grid-cols-2 gap-6">
          <div className="bg-slate-50 rounded-2xl p-6 border border-slate-200">
            <h3 className="text-lg font-semibold text-slate-900 mb-3">Free Audit Includes:</h3>
            <ul className="space-y-2 text-sm text-slate-600">
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-500" />
                Basic SEO health check
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-500" />
                Up to 25 pages scanned
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-500" />
                Top 5 critical issues
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-500" />
                Basic recommendations
              </li>
            </ul>
          </div>
          
          <div className="bg-gradient-to-br from-emerald-50 to-teal-50 rounded-2xl p-6 border border-emerald-200">
            <h3 className="text-lg font-semibold text-emerald-900 mb-3">Upgrade to Pro:</h3>
            <ul className="space-y-2 text-sm text-emerald-700 mb-4">
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-600" />
                Unlimited pages scanned
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-600" />
                Detailed technical analysis
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-600" />
                Client-ready PDF reports
              </li>
              <li className="flex items-center gap-2">
                <CheckCircleIcon className="h-4 w-4 text-emerald-600" />
                Priority support
              </li>
            </ul>
            <Button href="/pricing" variant="secondary" className="w-full text-emerald-700 border-emerald-300">
              View Pro Plans
            </Button>
          </div>
        </div>
      </div>
    </Container>
  )

  const ProcessingView = () => (
    <Container className="py-24">
      <div className="max-w-2xl mx-auto text-center">
        <div className="mb-8">
          <ArrowPathIcon className="h-16 w-16 text-emerald-600 mx-auto animate-spin" />
        </div>
        
        <Heading as="h1" className="mb-6">Analyzing Your Website</Heading>
        <p className="text-xl text-slate-600 mb-12">
          Our AI is scanning {formData.url} for SEO issues and opportunities. 
          This usually takes 30-60 seconds.
        </p>
        
        <div className="bg-white rounded-2xl p-8 shadow-lg border">
          <div className="space-y-4">
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-600">Crawling pages...</span>
              <CheckCircleIcon className="h-5 w-5 text-emerald-500" />
            </div>
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-600">Analyzing technical SEO...</span>
              <ArrowPathIcon className="h-5 w-5 text-emerald-500 animate-spin" />
            </div>
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-400">Checking content quality...</span>
              <ClockIcon className="h-5 w-5 text-slate-300" />
            </div>
            <div className="flex items-center justify-between text-sm">
              <span className="text-slate-400">Generating recommendations...</span>
              <ClockIcon className="h-5 w-5 text-slate-300" />
            </div>
          </div>
        </div>
      </div>
    </Container>
  )

  const ResultsView = () => {
    if (!auditResult) return null

    const getScoreColor = (score: number) => {
      if (score >= 80) return 'text-emerald-600 bg-emerald-100'
      if (score >= 60) return 'text-yellow-600 bg-yellow-100'
      return 'text-red-600 bg-red-100'
    }

    return (
      <Container className="py-24">
        <div className="max-w-4xl mx-auto">
          <div className="text-center mb-12">
            <Heading as="h1">Your SEO Audit Results</Heading>
            <p className="mt-4 text-xl text-slate-600">
              Analysis complete for {auditResult.url}
            </p>
          </div>

          {/* Overall Score */}
          <div className="bg-white rounded-3xl shadow-xl border p-8 mb-8">
            <div className="flex items-center justify-between mb-6">
              <div>
                <h2 className="text-2xl font-bold text-slate-900">Overall SEO Score</h2>
                <p className="text-slate-600">Based on {auditResult.pages_scanned} pages analyzed</p>
              </div>
              <div className={`text-4xl font-bold px-6 py-3 rounded-2xl ${getScoreColor(auditResult.score)}`}>
                {auditResult.score}
              </div>
            </div>
            
            <div className="grid grid-cols-3 gap-6 text-center">
              <div className="bg-red-50 rounded-xl p-4">
                <div className="text-2xl font-bold text-red-600">{auditResult.issues.critical}</div>
                <div className="text-sm text-red-700">Critical Issues</div>
              </div>
              <div className="bg-yellow-50 rounded-xl p-4">
                <div className="text-2xl font-bold text-yellow-600">{auditResult.issues.warning}</div>
                <div className="text-sm text-yellow-700">Warnings</div>
              </div>
              <div className="bg-blue-50 rounded-xl p-4">
                <div className="text-2xl font-bold text-blue-600">{auditResult.issues.info}</div>
                <div className="text-sm text-blue-700">Improvements</div>
              </div>
            </div>
          </div>

          {/* Quick Stats */}
          <div className="grid md:grid-cols-3 gap-6 mb-8">
            <div className="bg-white rounded-2xl shadow-lg p-6 border">
              <h3 className="font-semibold text-slate-900 mb-2">Pages Scanned</h3>
              <div className="text-3xl font-bold text-emerald-600">{auditResult.pages_scanned}</div>
            </div>
            <div className="bg-white rounded-2xl shadow-lg p-6 border">
              <h3 className="font-semibold text-slate-900 mb-2">Load Time</h3>
              <div className="text-3xl font-bold text-blue-600">{auditResult.load_time.toFixed(1)}s</div>
            </div>
            <div className="bg-white rounded-2xl shadow-lg p-6 border">
              <h3 className="font-semibold text-slate-900 mb-2">Issues Found</h3>
              <div className="text-3xl font-bold text-red-600">
                {auditResult.issues.critical + auditResult.issues.warning}
              </div>
            </div>
          </div>

          {/* Top Recommendations */}
          <div className="bg-white rounded-3xl shadow-xl border p-8 mb-8">
            <h2 className="text-2xl font-bold text-slate-900 mb-6">Top Recommendations</h2>
            <div className="space-y-4">
              {auditResult.recommendations.slice(0, 3).map((rec, index) => (
                <div key={index} className="flex items-start gap-3 p-4 bg-slate-50 rounded-xl">
                  <div className="bg-emerald-100 text-emerald-600 rounded-full w-6 h-6 flex items-center justify-center text-sm font-bold">
                    {index + 1}
                  </div>
                  <div className="flex-1">
                    <p className="text-slate-700">{rec}</p>
                  </div>
                </div>
              ))}
            </div>
            
            <div className="mt-6 p-4 bg-emerald-50 rounded-xl border border-emerald-200">
              <p className="text-emerald-800 text-center font-medium">
                🎯 Want the full detailed report with all {auditResult.recommendations.length} recommendations? 
              </p>
              <div className="flex justify-center mt-3">
                <Button href="/pricing" className="bg-emerald-600 hover:bg-emerald-700">
                  Upgrade to see all insights
                </Button>
              </div>
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Button href="/dashboard" className="bg-emerald-600 hover:bg-emerald-700">
              View in Dashboard
            </Button>
            <Button href="/audit" variant="secondary" className="border-slate-300">
              Run Another Audit
            </Button>
            <Button href="/pricing" variant="secondary" className="border-emerald-300 text-emerald-700">
              Upgrade for More Features
            </Button>
          </div>
        </div>
      </Container>
    )
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white">
      <Navbar />
      {step === 'form' && <AuditForm />}
      {step === 'processing' && <ProcessingView />}
      {step === 'results' && <ResultsView />}
    </div>
  )
} 