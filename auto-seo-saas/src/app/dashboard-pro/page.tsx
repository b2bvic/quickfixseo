'use client'

import { Button } from '@/components/button'
import { DashboardNavbar } from '@/components/dashboard-navbar'
import { Heading } from '@/components/text'
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
  LockClosedIcon
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
  { name: 'Overview', href: '#overview', icon: ChartBarIcon, current: true },
  { name: 'Websites', href: '#websites', icon: GlobeAltIcon, current: false },
]

const organizationSections = [
  { name: 'Technical SEO', href: '#technical', icon: CogIcon, current: false },
  { name: 'Performance', href: '#performance', icon: ChartPieIcon, current: false },
  { name: 'Content Analysis', href: '#content', icon: DocumentTextIcon, current: false },
  { name: 'Security', href: '#security', icon: LockClosedIcon, current: false },
  { name: 'Mobile', href: '#mobile', icon: DevicePhoneMobileIcon, current: false },
  { name: 'Images', href: '#images', icon: PhotoIcon, current: false },
  { name: 'Links', href: '#links', icon: LinkIcon, current: false },
  { name: 'Vulnerabilities', href: '#vulnerabilities', icon: BugAntIcon, current: false },
]

const reportTabs = [
  { name: 'Overview', id: 'overview' },
  { name: 'Technical Issues', id: 'technical' },
  { name: 'Performance', id: 'performance' },
  { name: 'Content', id: 'content' },
  { name: 'Recommendations', id: 'recommendations' },
  { name: 'Export', id: 'export' },
]

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export default function DashboardProPage() {
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
      subscription: 'enterprise',
      audits_remaining: 0,
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
                <dd className="text-2xl font-bold text-slate-900">{selectedWebsite?.pages_scanned || 0}</dd>
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
    </div>
  )

  const TechnicalTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Technical SEO Issues</h3>
        <div className="space-y-4">
          {selectedWebsite?.recommendations.slice(0, 8).map((rec, index) => (
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
              <Button variant="secondary" className="text-xs">
                Fix Now
              </Button>
            </div>
          ))}
        </div>
      </div>
    </div>
  )

  const PerformanceTab = () => (
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

  const ContentTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Content Analysis</h3>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">23</div>
            <div className="text-sm text-slate-600">Missing Meta Descriptions</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">8</div>
            <div className="text-sm text-slate-600">Duplicate Titles</div>
          </div>
          <div className="text-center p-4 border border-slate-200 rounded-lg">
            <div className="text-2xl font-bold text-slate-900">156</div>
            <div className="text-sm text-slate-600">Images Without Alt Text</div>
          </div>
        </div>
      </div>
    </div>
  )

  const RecommendationsTab = () => (
    <div className="space-y-6">
      <div className="bg-white rounded-lg shadow p-6">
        <h3 className="text-lg font-medium text-slate-900 mb-4">Action Plan</h3>
        <div className="space-y-4">
          {selectedWebsite?.recommendations.map((rec, index) => (
            <div key={index} className="flex items-start gap-3 p-4 border-l-4 border-emerald-500 bg-emerald-50">
              <div className="flex-1">
                <p className="text-sm font-medium text-slate-900">{rec}</p>
                <div className="mt-2 flex items-center gap-4 text-xs text-slate-500">
                  <span>Impact: High</span>
                  <span>Effort: Medium</span>
                  <span>Est. Time: 2-4 hours</span>
                </div>
              </div>
              <Button variant="secondary" className="text-xs">
                View Details
              </Button>
            </div>
          ))}
        </div>
      </div>
    </div>
  )

  const ExportTab = () => (
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

  return (
    <div className="min-h-screen bg-slate-50">
      <DashboardNavbar />
      
      <div className="flex">
        {/* Sidebar */}
        <div className={`${sidebarCollapsed ? 'w-16' : 'w-64'} bg-white shadow-sm border-r border-slate-200 transition-all duration-300`}>
          <div className="p-6">
            <div className="flex items-center justify-between mb-6">
              {!sidebarCollapsed && (
                <h2 className="text-lg font-semibold text-slate-900">Multi-Site SEO</h2>
              )}
              <Button 
                onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
                variant="secondary"
                className="p-2"
              >
                <ChevronDownIcon className={`h-4 w-4 transition-transform ${sidebarCollapsed ? 'rotate-90' : '-rotate-90'}`} />
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
                    return (
                      <a
                        key={item.name}
                        href={item.href}
                        className="group flex items-center pl-2 py-2 text-sm font-medium text-slate-600 hover:text-slate-700 hover:bg-slate-50"
                      >
                        <Icon className="mr-3 h-4 w-4" />
                        {item.name}
                      </a>
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
                    <Button>
                      <DocumentArrowDownIcon className="h-4 w-4 mr-2" />
                      Export Report
                    </Button>
                  </div>
                </div>
              </div>
            </div>

            {/* Tabs */}
            <div className="mb-6">
              <div className="border-b border-slate-200">
                <nav className="-mb-px flex space-x-8">
                  {reportTabs.map((tab) => (
                    <button
                      key={tab.id}
                      onClick={() => setActiveTab(tab.id)}
                      className={classNames(
                        activeTab === tab.id
                          ? 'border-emerald-500 text-emerald-600'
                          : 'border-transparent text-slate-500 hover:text-slate-700 hover:border-slate-300',
                        'whitespace-nowrap py-2 px-1 border-b-2 font-medium text-sm'
                      )}
                    >
                      {tab.name}
                    </button>
                  ))}
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
            </div>
          </div>
        </div>
      </div>
    </div>
  )
} 