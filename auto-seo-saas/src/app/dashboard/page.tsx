'use client'

import { Button } from '@/components/button'
import { DashboardNavbar } from '@/components/dashboard-navbar'
import { useState, useEffect } from 'react'
import { 
  ChartBarIcon,
  ClockIcon,
  DocumentArrowDownIcon,
  ExclamationTriangleIcon,
  PlusIcon,
  StarIcon,
  EyeIcon,
  ChevronDownIcon,
  ChevronUpIcon,
  GlobeAltIcon,
  BugAntIcon,
  ShieldCheckIcon,
  DocumentTextIcon,
  CogIcon,
  ChartPieIcon,
  ServerIcon,
  LinkIcon,
  PhotoIcon,
  MagnifyingGlassIcon,
  DevicePhoneMobileIcon,
  LockClosedIcon,
  HomeIcon,
  DocumentChartBarIcon,
  UsersIcon,
  ChevronRightIcon
} from '@heroicons/react/24/outline'

interface SavedAudit {
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
  date: string
  type: 'free' | 'pro' | 'enterprise'
}

interface UserData {
  name: string
  email: string
  subscription: 'free' | 'pro' | 'enterprise'
  audits_remaining: number
  total_audits: number
}

const sidebarNavigation = [
  { name: 'Dashboard', href: '/dashboard', icon: HomeIcon, current: true },
  { name: 'Reports', href: '/dashboard', icon: DocumentChartBarIcon, current: false },
]

const organizationSections = [
  { name: 'Overview', id: 'overview', icon: ChartBarIcon, premium: false },
  { name: 'Technical SEO', id: 'technical', icon: CogIcon, premium: false },
  { name: 'Performance', id: 'performance', icon: ChartPieIcon, premium: true },
  { name: 'Content Analysis', id: 'content', icon: DocumentTextIcon, premium: false },
  { name: 'Security', id: 'security', icon: LockClosedIcon, premium: true },
  { name: 'Mobile', id: 'mobile', icon: DevicePhoneMobileIcon, premium: true },
  { name: 'Images', id: 'images', icon: PhotoIcon, premium: false },
  { name: 'Links', id: 'links', icon: LinkIcon, premium: true },
  { name: 'Vulnerabilities', id: 'vulnerabilities', icon: BugAntIcon, premium: true },
]

const reportTabs = [
  { name: 'Overview', id: 'overview', premium: false },
  { name: 'Technical Issues', id: 'technical', premium: false },
  { name: 'Performance', id: 'performance', premium: true },
  { name: 'Content', id: 'content', premium: false },
  { name: 'Recommendations', id: 'recommendations', premium: false },
  { name: 'Export', id: 'export', premium: true },
]

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export default function DashboardPage() {
  const [userData, setUserData] = useState<UserData | null>(null)
  const [audits, setAudits] = useState<SavedAudit[]>([])
  const [loading, setLoading] = useState(true)
  const [activeTab, setActiveTab] = useState('overview')
  const [selectedWebsite, setSelectedWebsite] = useState<SavedAudit | null>(null)
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)

  useEffect(() => {
    // Load user data from localStorage
    const savedAudits = JSON.parse(localStorage.getItem('userAudits') || '[]')
    const userEmail = localStorage.getItem('userEmail') || 'demo@example.com'
    const userName = localStorage.getItem('userName') || 'Demo User'
    
    setAudits(savedAudits)
    setSelectedWebsite(savedAudits[0] || null)
    setUserData({
      name: userName,
      email: userEmail,
      subscription: 'free', // Can be 'free', 'pro', or 'enterprise'
      audits_remaining: Math.max(0, 3 - savedAudits.length),
      total_audits: savedAudits.length
    })
    setLoading(false)
  }, [])

  const formatDate = (dateStr: string) => {
    return new Date(dateStr).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    })
  }

  const getScoreColor = (score: number) => {
    if (score >= 80) return 'text-emerald-600 bg-emerald-100'
    if (score >= 60) return 'text-yellow-600 bg-yellow-100'
    return 'text-red-600 bg-red-100'
  }

  const isPremiumFeature = (tabId: string) => {
    const tab = reportTabs.find(t => t.id === tabId)
    return tab?.premium && userData?.subscription === 'free'
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-50">
        <DashboardNavbar />
        <div className="flex items-center justify-center h-96">
          <div className="text-xl text-slate-600">Loading dashboard...</div>
        </div>
      </div>
    )
  }

  if (!userData || audits.length === 0) {
    return (
      <div className="min-h-screen bg-slate-50">
        <DashboardNavbar />
        <div className="flex items-center justify-center h-96">
          <div className="max-w-2xl mx-auto text-center">
            <h1 className="text-4xl font-medium tracking-tighter text-gray-950">Welcome to AUTO SEO</h1>
            <p className="mt-6 text-xl text-slate-600 mb-8">
              Run your first audit to access your dashboard.
            </p>
            <Button href="/audit" className="bg-emerald-600 hover:bg-emerald-700">
              Start Your First Audit
            </Button>
          </div>
        </div>
      </div>
    )
  }

  const PremiumLock = ({ children, feature }: { children: React.ReactNode, feature: string }) => (
    <div className="relative">
      <div className="filter blur-sm pointer-events-none">
        {children}
      </div>
      <div className="absolute inset-0 flex items-center justify-center bg-white/80 backdrop-blur-sm rounded-lg">
        <div className="text-center p-6">
          <LockClosedIcon className="h-12 w-12 text-slate-400 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-slate-900 mb-2">Unlock {feature}</h3>
          <p className="text-sm text-slate-600 mb-4">
            Upgrade to Pro to access advanced {feature.toLowerCase()} analysis
          </p>
          <Button href="/pricing" className="bg-emerald-600 hover:bg-emerald-700">
            Upgrade to Pro
          </Button>
        </div>
      </div>
    </div>
  )

  const OverviewTab = () => (
    <div className="space-y-6">
      <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <ChartBarIcon className="h-8 w-8 text-emerald-600" />
            </div>
            <div className="ml-5 w-0 flex-1">
              <dl>
                <dt className="text-sm font-medium text-slate-500 truncate">Overall Score</dt>
                <dd className="text-2xl font-bold text-slate-900">{selectedWebsite?.score || 0}</dd>
              </dl>
            </div>
          </div>
        </div>
        
        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <ExclamationTriangleIcon className="h-8 w-8 text-red-600" />
            </div>
            <div className="ml-5 w-0 flex-1">
              <dl>
                <dt className="text-sm font-medium text-slate-500 truncate">Critical Issues</dt>
                <dd className="text-2xl font-bold text-slate-900">{selectedWebsite?.issues.critical || 0}</dd>
              </dl>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <GlobeAltIcon className="h-8 w-8 text-blue-600" />
            </div>
            <div className="ml-5 w-0 flex-1">
              <dl>
                <dt className="text-sm font-medium text-slate-500 truncate">Pages Scanned</dt>
                <dd className="text-2xl font-bold text-slate-900">
                  {userData?.subscription === 'free' ? Math.min(selectedWebsite?.pages_scanned || 0, 25) : selectedWebsite?.pages_scanned || 0}
                  {userData?.subscription === 'free' && (selectedWebsite?.pages_scanned || 0) > 25 && (
                    <span className="text-sm text-slate-500 ml-1">/25 free limit</span>
                  )}
                </dd>
              </dl>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow p-6">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <ClockIcon className="h-8 w-8 text-purple-600" />
            </div>
            <div className="ml-5 w-0 flex-1">
              <dl>
                <dt className="text-sm font-medium text-slate-500 truncate">Load Time</dt>
                <dd className="text-2xl font-bold text-slate-900">{selectedWebsite?.load_time.toFixed(1)}s</dd>
              </dl>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-white rounded-lg shadow">
        <div className="p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Issue Distribution</h3>
          <div className="grid grid-cols-3 gap-4">
            <div className="text-center p-4 bg-red-50 rounded-lg">
              <div className="text-3xl font-bold text-red-600">{selectedWebsite?.issues.critical || 0}</div>
              <div className="text-sm text-red-700">Critical</div>
              <div className="text-xs text-red-600 mt-1">Requires immediate attention</div>
            </div>
            <div className="text-center p-4 bg-yellow-50 rounded-lg">
              <div className="text-3xl font-bold text-yellow-600">{selectedWebsite?.issues.warning || 0}</div>
              <div className="text-sm text-yellow-700">Warnings</div>
              <div className="text-xs text-yellow-600 mt-1">Should be addressed soon</div>
            </div>
            <div className="text-center p-4 bg-blue-50 rounded-lg">
              <div className="text-3xl font-bold text-blue-600">{selectedWebsite?.issues.info || 0}</div>
              <div className="text-sm text-blue-700">Improvements</div>
              <div className="text-xs text-blue-600 mt-1">Optimization opportunities</div>
            </div>
          </div>
        </div>
      </div>
      
      {userData?.subscription === 'free' && (
        <div className="bg-gradient-to-r from-emerald-500 to-teal-600 rounded-lg shadow p-6 text-white">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-lg font-medium mb-2">🚀 Unlock the Full Power of AUTO SEO</h3>
              <p className="text-emerald-100">
                Get unlimited pages, advanced analytics, PDF reports, and priority support.
              </p>
            </div>
            <Button href="/pricing" className="bg-white text-emerald-600 hover:bg-emerald-50">
              Upgrade Now
            </Button>
          </div>
        </div>
      )}
    </div>
  )

  const TechnicalTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Technical SEO Issues</h3>
        <div className="space-y-4">
          {selectedWebsite?.recommendations.slice(0, userData?.subscription === 'free' ? 5 : undefined).map((rec, index) => (
            <div key={index} className="flex items-start gap-3 p-4 border border-slate-200 rounded-lg">
              <div className={`rounded-full w-8 h-8 flex items-center justify-center text-sm font-bold ${
                index < 3 ? 'bg-red-100 text-red-600' :
                index < 6 ? 'bg-yellow-100 text-yellow-600' :
                'bg-blue-100 text-blue-600'
              }`}>
                {index + 1}
              </div>
              <div className="flex-1">
                <p className="text-sm font-medium text-slate-900">{rec}</p>
                <p className="text-xs text-slate-500 mt-1">
                  {index < 3 ? 'Critical Priority' : index < 6 ? 'Medium Priority' : 'Low Priority'}
                </p>
              </div>
              {userData?.subscription !== 'free' ? (
                <Button variant="secondary" className="text-xs">
                  Fix Guide
                </Button>
              ) : (
                <div className="text-xs text-slate-400 px-3 py-1 border border-slate-200 rounded">
                  Pro Feature
                </div>
              )}
            </div>
          ))}
          
          {userData?.subscription === 'free' && selectedWebsite && selectedWebsite.recommendations.length > 5 && (
            <div className="p-4 bg-emerald-50 rounded-lg border border-emerald-200 text-center">
              <p className="text-emerald-800 font-medium">
                {selectedWebsite.recommendations.length - 5} more issues found
              </p>
              <p className="text-emerald-700 text-sm mt-1">
                Upgrade to Pro to see all technical issues and get detailed fix guides
              </p>
              <Button href="/pricing" className="mt-3 bg-emerald-600 hover:bg-emerald-700">
                Upgrade to See All Issues
              </Button>
            </div>
          )}
        </div>
      </div>
    </div>
  )

  const PerformanceTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-medium text-slate-900 mb-4">Core Web Vitals</h3>
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">Largest Contentful Paint</span>
                <span className="text-sm font-medium text-red-600">4.2s</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">First Input Delay</span>
                <span className="text-sm font-medium text-green-600">89ms</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">Cumulative Layout Shift</span>
                <span className="text-sm font-medium text-yellow-600">0.15</span>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow p-6">
            <h3 className="text-lg font-medium text-slate-900 mb-4">Page Speed Insights</h3>
            <div className="space-y-4">
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">Mobile Score</span>
                <span className="text-sm font-medium text-yellow-600">67</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">Desktop Score</span>
                <span className="text-sm font-medium text-green-600">84</span>
              </div>
              <div className="flex justify-between items-center">
                <span className="text-sm text-slate-600">Time to Interactive</span>
                <span className="text-sm font-medium text-red-600">5.1s</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    )

    return isPremiumFeature('performance') ? (
      <PremiumLock feature="Performance Analytics">
        {content}
      </PremiumLock>
    ) : content
  }

  const ContentTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Content Analysis</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">
              {userData?.subscription === 'free' ? '5+' : '23'}
            </div>
            <div className="text-sm text-slate-600">Missing Meta Descriptions</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">
              {userData?.subscription === 'free' ? '3+' : '8'}
            </div>
            <div className="text-sm text-slate-600">Duplicate Titles</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">
              {userData?.subscription === 'free' ? '25+' : '156'}
            </div>
            <div className="text-sm text-slate-600">Images Without Alt Text</div>
          </div>
        </div>

        {userData?.subscription === 'free' && (
          <div className="mt-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
            <p className="text-blue-800 text-center">
              📊 Upgrade to Pro to see complete content analysis with detailed page-by-page breakdowns
            </p>
          </div>
        )}
      </div>
    </div>
  )

  const RecommendationsTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Action Plan</h3>
        <div className="space-y-4">
          {selectedWebsite?.recommendations.slice(0, userData?.subscription === 'free' ? 3 : undefined).map((rec, index) => (
            <div key={index} className="flex items-start gap-3 p-4 border-l-4 border-emerald-500 bg-emerald-50">
              <div className="flex-1">
                <p className="text-sm font-medium text-slate-900">{rec}</p>
                {userData?.subscription !== 'free' && (
                  <div className="mt-2 flex items-center gap-4 text-xs text-slate-500">
                    <span>Impact: High</span>
                    <span>Effort: Medium</span>
                    <span>Est. Time: 2-4 hours</span>
                  </div>
                )}
              </div>
              {userData?.subscription !== 'free' ? (
                <Button variant="secondary" className="text-xs">
                  View Guide
                </Button>
              ) : (
                <div className="text-xs text-slate-400 px-3 py-1 border border-slate-200 rounded">
                  Pro Details
                </div>
              )}
            </div>
          ))}
          
          {userData?.subscription === 'free' && (
            <div className="p-6 bg-gradient-to-r from-emerald-50 to-teal-50 rounded-lg border border-emerald-200">
              <h4 className="font-semibold text-emerald-900 mb-2">🎯 Get Your Complete Action Plan</h4>
              <p className="text-emerald-800 text-sm mb-4">
                Unlock detailed implementation guides, priority rankings, and time estimates for all recommendations.
              </p>
              <Button href="/pricing" className="bg-emerald-600 hover:bg-emerald-700">
                Upgrade for Full Action Plan
              </Button>
            </div>
          )}
        </div>
      </div>
    </div>
  )

  const ExportTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Export Options</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="border border-slate-200 rounded-lg p-6 text-center">
              <DocumentArrowDownIcon className="h-12 w-12 text-slate-400 mx-auto mb-4" />
              <h4 className="text-lg font-medium text-slate-900 mb-2">Executive Summary</h4>
              <p className="text-sm text-slate-600 mb-4">High-level overview for stakeholders</p>
              <Button className="w-full">Download PDF</Button>
            </div>
            <div className="border border-slate-200 rounded-lg p-6 text-center">
              <DocumentTextIcon className="h-12 w-12 text-slate-400 mx-auto mb-4" />
              <h4 className="text-lg font-medium text-slate-900 mb-2">Technical Report</h4>
              <p className="text-sm text-slate-600 mb-4">Detailed technical analysis</p>
              <Button className="w-full">Download PDF</Button>
            </div>
          </div>
        </div>
      </div>
    )

    return isPremiumFeature('export') ? (
      <PremiumLock feature="PDF Export">
        {content}
      </PremiumLock>
    ) : content
  }

  const SecurityTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Security Analysis</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-red-600">2</div>
              <div className="text-sm text-slate-600">SSL Issues</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-yellow-600">1</div>
              <div className="text-sm text-slate-600">Mixed Content</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-green-600">0</div>
              <div className="text-sm text-slate-600">Malware Detected</div>
            </div>
          </div>
        </div>
      </div>
    )

    return userData?.subscription === 'free' ? (
      <PremiumLock feature="Security Analysis">
        {content}
      </PremiumLock>
    ) : content
  }

  const MobileTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Mobile Optimization</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-yellow-600">67</div>
              <div className="text-sm text-slate-600">Mobile Score</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-green-600">Yes</div>
              <div className="text-sm text-slate-600">Mobile Friendly</div>
            </div>
          </div>
        </div>
      </div>
    )

    return userData?.subscription === 'free' ? (
      <PremiumLock feature="Mobile Analysis">
        {content}
      </PremiumLock>
    ) : content
  }

  const ImagesTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Image Optimization</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">
              {userData?.subscription === 'free' ? '25+' : '156'}
            </div>
            <div className="text-sm text-slate-600">Images Found</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-red-600">
              {userData?.subscription === 'free' ? '10+' : '47'}
            </div>
            <div className="text-sm text-slate-600">Missing Alt Text</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-yellow-600">
              {userData?.subscription === 'free' ? '15+' : '89'}
            </div>
            <div className="text-sm text-slate-600">Unoptimized Size</div>
          </div>
        </div>
      </div>
    </div>
  )

  const LinksTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Link Analysis</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-green-600">234</div>
              <div className="text-sm text-slate-600">Internal Links</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-blue-600">67</div>
              <div className="text-sm text-slate-600">External Links</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-red-600">3</div>
              <div className="text-sm text-slate-600">Broken Links</div>
            </div>
          </div>
        </div>
      </div>
    )

    return userData?.subscription === 'free' ? (
      <PremiumLock feature="Link Analysis">
        {content}
      </PremiumLock>
    ) : content
  }

  const VulnerabilitiesTab = () => {
    const content = (
      <div className="space-y-6">
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-medium text-slate-900 mb-4">Security Vulnerabilities</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-red-600">1</div>
              <div className="text-sm text-slate-600">High Risk</div>
            </div>
            <div className="text-center p-4 border border-slate-200 rounded-lg">
              <div className="text-2xl font-bold text-yellow-600">3</div>
              <div className="text-sm text-slate-600">Medium Risk</div>
            </div>
          </div>
        </div>
      </div>
    )

    return userData?.subscription === 'free' ? (
      <PremiumLock feature="Vulnerability Scanning">
        {content}
      </PremiumLock>
    ) : content
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <DashboardNavbar />
      
      <div className="flex">
        {/* Sidebar */}
        <div className={`${sidebarCollapsed ? 'w-16' : 'w-64'} bg-white shadow-sm border-r border-slate-200 transition-all duration-300`}>
          <div className="p-6">
            <div className="flex items-center justify-between mb-6">
              {!sidebarCollapsed && (
                <h2 className="text-lg font-semibold text-slate-900">SEO Dashboard</h2>
              )}
              <Button 
                onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
                variant="secondary" 
                className="p-2"
              >
                <ChevronRightIcon className={`h-4 w-4 transition-transform ${sidebarCollapsed ? '' : 'rotate-180'}`} />
              </Button>
            </div>
            
            <nav className="space-y-1">
              {sidebarNavigation.map((item) => {
                const Icon = item.icon
                return (
                  <a
                    key={item.name}
                    href={item.href}
                    className={classNames(
                      item.current
                        ? 'bg-emerald-50 border-emerald-500 text-emerald-700'
                        : 'border-transparent text-slate-600 hover:text-slate-700 hover:bg-slate-50',
                      'group flex items-center pl-2 py-2 text-sm font-medium border-l-4'
                    )}
                  >
                    <Icon className="mr-3 h-5 w-5" />
                    {!sidebarCollapsed && item.name}
                  </a>
                )
              })}
            </nav>
            
            {!sidebarCollapsed && (
              <div className="mt-8">
                <h3 className="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-3">
                  Analysis
                </h3>
                <nav className="space-y-1">
                  {organizationSections.map((item) => {
                    const Icon = item.icon
                    const isLocked = item.premium && userData?.subscription === 'free'
                    return (
                      <button
                        key={item.id}
                        onClick={() => !isLocked && setActiveTab(item.id)}
                        className={classNames(
                          'group flex items-center pl-2 py-2 text-sm font-medium rounded-md w-full text-left',
                          activeTab === item.id
                            ? 'bg-emerald-50 text-emerald-700'
                            : isLocked 
                            ? 'text-slate-400 cursor-not-allowed' 
                            : 'text-slate-600 hover:text-slate-700 hover:bg-slate-50'
                        )}
                        disabled={isLocked}
                      >
                        <Icon className="mr-3 h-4 w-4" />
                        <span className="flex-1">{item.name}</span>
                        {isLocked && <LockClosedIcon className="h-3 w-3 text-slate-400" />}
                      </button>
                    )
                  })}
                </nav>
              </div>
            )}
          </div>
        </div>
        
        {/* Main Content */}
        <div className="flex-1">
          <div className="p-6">
            {/* Website Selector */}
            <div className="mb-6">
              <div className="bg-white rounded-lg shadow p-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-4">
                    <h1 className="text-2xl font-bold text-slate-900">SEO Dashboard</h1>
                    <select 
                      className="border border-slate-300 rounded-md px-3 py-2 text-sm"
                      value={selectedWebsite?.url || ''}
                      onChange={(e) => {
                        const website = audits.find(a => a.url === e.target.value)
                        setSelectedWebsite(website || null)
                      }}
                    >
                      {audits.map((audit, index) => (
                        <option key={index} value={audit.url}>
                          {audit.url} (Score: {audit.score})
                        </option>
                      ))}
                    </select>
                  </div>
                  <div className="flex items-center gap-3">
                    <Button href="/audit" variant="secondary">
                      <PlusIcon className="h-4 w-4 mr-2" />
                      New Audit
                    </Button>
                    {userData?.subscription !== 'free' ? (
                      <Button>
                        <DocumentArrowDownIcon className="h-4 w-4 mr-2" />
                        Export Report
                      </Button>
                    ) : (
                      <Button href="/pricing" className="bg-gradient-to-r from-emerald-600 to-teal-600">
                        <StarIcon className="h-4 w-4 mr-2" />
                        Upgrade to Export
                      </Button>
                    )}
                  </div>
                </div>
              </div>
            </div>

            {/* Tabs */}
            <div className="mb-6">
              <div className="border-b border-slate-200">
                <nav className="-mb-px flex space-x-8">
                  {reportTabs.map((tab) => {
                    const isLocked = tab.premium && userData?.subscription === 'free'
                    return (
                      <button
                        key={tab.id}
                        onClick={() => !isLocked && setActiveTab(tab.id)}
                        className={classNames(
                          activeTab === tab.id
                            ? 'border-emerald-500 text-emerald-600'
                            : isLocked
                            ? 'border-transparent text-slate-400 cursor-not-allowed'
                            : 'border-transparent text-slate-500 hover:text-slate-700 hover:border-slate-300',
                          'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm flex items-center gap-2'
                        )}
                        disabled={isLocked}
                      >
                        {tab.name}
                        {isLocked && <LockClosedIcon className="h-3 w-3" />}
                      </button>
                    )
                  })}
                </nav>
              </div>
            </div>

            {/* Tab Content */}
            <div>
              {activeTab === 'overview' && <OverviewTab />}
              {activeTab === 'technical' && <TechnicalTab />}
              {activeTab === 'performance' && <PerformanceTab />}
              {activeTab === 'content' && <ContentTab />}
              {activeTab === 'recommendations' && <RecommendationsTab />}
              {activeTab === 'export' && <ExportTab />}
              {activeTab === 'security' && <SecurityTab />}
              {activeTab === 'mobile' && <MobileTab />}
              {activeTab === 'images' && <ImagesTab />}
              {activeTab === 'links' && <LinksTab />}
              {activeTab === 'vulnerabilities' && <VulnerabilitiesTab />}
            </div>
          </div>
        </div>
      </div>
    </div>
  )
} 