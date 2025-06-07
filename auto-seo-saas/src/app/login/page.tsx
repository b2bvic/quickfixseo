'use client'

import { Button } from '@/components/button'
import { Container } from '@/components/container'
import { Footer } from '@/components/footer'
import { GradientBackground } from '@/components/gradient'
import { Link } from '@/components/link'
import { Navbar } from '@/components/navbar'
import { Heading } from '@/components/text'
import { EyeIcon, EyeSlashIcon } from '@heroicons/react/24/outline'
import { useState } from 'react'

function BenefitsSidebar() {
  return (
    <div className="hidden lg:flex lg:flex-col lg:justify-center lg:px-12 lg:py-24 bg-gradient-to-br from-emerald-600 to-teal-700">
      <div className="text-white">
        <div className="mb-8">
          <h1 className="text-4xl font-bold mb-4">
            Your next client is waiting for this audit
          </h1>
          <p className="text-xl text-emerald-100">
            Join 2,800+ agencies who save 39.75 hours per audit. Get professional, client-ready reports in minutes, not days.
          </p>
        </div>
        
        <div className="space-y-6">
          <div className="flex items-start gap-4">
            <div className="bg-white/20 rounded-full p-2 mt-1">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            </div>
            <div>
              <h3 className="font-semibold text-lg mb-2">
                Save 39.75 hours per audit
              </h3>
              <p className="text-emerald-100 text-sm">
                What takes 40 hours manually takes 15 minutes with AUTO SEO. That&apos;s enough time to close 3 more deals.
              </p>
            </div>
          </div>
          
          <div className="flex items-start gap-4">
            <div className="bg-white/20 rounded-full p-2 mt-1">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            </div>
            <div>
              <h3 className="font-semibold text-lg mb-2">
                Professional reports that close deals
              </h3>
              <p className="text-emerald-100 text-sm">
                Beautiful, client-ready reports with executive summaries and action plans. Your clients will be impressed.
              </p>
            </div>
          </div>
          
          <div className="flex items-start gap-4">
            <div className="bg-white/20 rounded-full p-2 mt-1">
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            </div>
            <div>
              <h3 className="font-semibold text-lg mb-2">
                Scale without hiring anyone
              </h3>
              <p className="text-emerald-100 text-sm">
                Handle 10x more clients with the same team. Each audit pays for itself in time saved.
              </p>
            </div>
          </div>
        </div>
        
        <div className="mt-8 pt-8 border-t border-white/20">
          <div className="grid grid-cols-3 gap-4 text-center">
            <div>
              <div className="text-2xl font-bold">2,800+</div>
              <div className="text-xs text-emerald-200">Happy agencies</div>
            </div>
            <div>
              <div className="text-2xl font-bold">15M+</div>
              <div className="text-xs text-emerald-200">Pages audited</div>
            </div>
            <div>
              <div className="text-2xl font-bold">$5,943</div>
              <div className="text-xs text-emerald-200">Saved per audit</div>
            </div>
          </div>
        </div>
        
        <div className="mt-8 bg-white/10 rounded-xl p-6">
          <h3 className="font-semibold mb-3">
            What you get immediately:
          </h3>
          <div className="grid grid-cols-2 gap-2 text-sm text-emerald-100">
            <div>• 25 pages free forever</div>
            <div>• Professional reports</div>
            <div>• 7-day Pro trial</div>
            <div>• Expert support</div>
            <div>• No credit card needed</div>
            <div>• Cancel anytime</div>
          </div>
        </div>
      </div>
    </div>
  )
}

function LoginForm() {
  const [showPassword, setShowPassword] = useState(false)
  
  return (
    <div className="flex min-h-screen">
      <BenefitsSidebar />
      
      <div className="flex-1 flex flex-col justify-center px-6 py-12 lg:px-16 bg-gradient-to-br from-slate-50 to-white">
        <div className="mx-auto w-full max-w-md">
          {/* Mobile header - only shown on small screens */}
          <div className="lg:hidden mb-8 text-center">
            <h1 className="text-3xl font-bold text-slate-900 mb-4">
              Transform your SEO workflow
            </h1>
            <p className="text-slate-600">
              Save 39.75 hours per audit with professional reports in minutes
            </p>
            
            <div className="mt-6 grid grid-cols-3 gap-4 text-center">
              <div className="bg-emerald-50 rounded-lg p-3">
                <div className="text-lg font-bold text-emerald-600">2,800+</div>
                <div className="text-xs text-slate-600">Agencies</div>
              </div>
              <div className="bg-slate-100 rounded-lg p-3">
                <div className="text-lg font-bold text-slate-600">15M+</div>
                <div className="text-xs text-slate-600">Pages</div>
              </div>
              <div className="bg-emerald-50 rounded-lg p-3">
                <div className="text-lg font-bold text-emerald-600">$5,943</div>
                <div className="text-xs text-slate-600">Saved</div>
              </div>
            </div>
          </div>
          
          <div className="bg-white rounded-3xl shadow-xl border border-slate-200 p-8">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-bold text-slate-900">
                Start your free trial
              </h2>
              <p className="mt-2 text-slate-600">
                Transform your workflow in the next 5 minutes
              </p>
            </div>
            
            <form className="space-y-6">
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-slate-700 mb-2">
                  Work email address
                </label>
                <input
                  id="email"
                  name="email"
                  type="email"
                  autoComplete="email"
                  required
                  className="w-full px-4 py-3 border border-slate-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-colors"
                  placeholder="you@agency.com"
                />
              </div>
              
              <div>
                <label htmlFor="password" className="block text-sm font-medium text-slate-700 mb-2">
                  Password
                </label>
                <div className="relative">
                  <input
                    id="password"
                    name="password"
                    type={showPassword ? 'text' : 'password'}
                    autoComplete="new-password"
                    required
                    className="w-full px-4 py-3 pr-12 border border-slate-300 rounded-xl focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-colors"
                    placeholder="Create a secure password"
                  />
                  <button
                    type="button"
                    className="absolute inset-y-0 right-0 pr-3 flex items-center"
                    onClick={() => setShowPassword(!showPassword)}
                  >
                    {showPassword ? (
                      <EyeSlashIcon className="h-5 w-5 text-slate-400" />
                    ) : (
                      <EyeIcon className="h-5 w-5 text-slate-400" />
                    )}
                  </button>
                </div>
              </div>
              
              <Button type="submit" className="w-full text-lg py-3 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-700 hover:to-teal-700">
                Start Free 7-Day Trial
              </Button>
            </form>
            
            <div className="mt-6 text-center">
              <Link href="/pricing" className="text-sm text-emerald-600 hover:text-emerald-500">
                View pricing options
              </Link>
            </div>
            
            <div className="mt-6 pt-6 border-t border-slate-100">
              <p className="text-center text-sm text-slate-600 mb-4">
                Already have an account?
              </p>
              
              <Button 
                href="/dashboard" 
                variant="secondary" 
                className="w-full text-sm py-2 border-slate-300 hover:border-slate-400"
              >
                Go to dashboard
              </Button>
            </div>
          </div>
          
          <div className="mt-8">
            <div className="bg-emerald-50 border border-emerald-200 rounded-3xl p-6">
              <h3 className="font-semibold text-emerald-900 mb-3 text-center">
                🎯 What you get immediately
              </h3>
              <div className="space-y-2 text-sm text-emerald-800">
                <div className="flex items-center gap-2">
                  <svg className="w-4 h-4 text-emerald-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  <span>25 pages free forever (no credit card)</span>
                </div>
                <div className="flex items-center gap-2">
                  <svg className="w-4 h-4 text-emerald-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  <span>7-day trial of Professional features</span>
                </div>
                <div className="flex items-center gap-2">
                  <svg className="w-4 h-4 text-emerald-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  <span>Complete audit in 15 minutes</span>
                </div>
                <div className="flex items-center gap-2">
                  <svg className="w-4 h-4 text-emerald-600" fill="currentColor" viewBox="0 0 20 20">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  <span>Professional reports that impress clients</span>
                </div>
              </div>
            </div>
          </div>
          
          {/* Risk reversal section */}
          <div className="mt-6 text-center">
            <div className="bg-slate-50 rounded-xl p-4">
              <div className="flex items-center justify-center gap-2 text-sm text-slate-600">
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20">
                  <path fillRule="evenodd" d="M2.166 4.999A11.954 11.954 0 0010 1.944 11.954 11.954 0 0017.834 5c.11.65.166 1.32.166 2.001 0 5.225-3.34 9.67-8 11.317C5.34 16.67 2 12.225 2 7c0-.682.057-1.35.166-2.001zm11.541 3.708a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
                </svg>
                <span>30-day money-back guarantee • Cancel anytime • Keep all reports</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default function LoginPage() {
  return (
    <main className="min-h-screen">
      <LoginForm />
    </main>
  )
}
