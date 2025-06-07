'use client'

import { useEffect } from 'react'
import { useRouter } from 'next/navigation'

export default function GetStartedRedirect() {
  const router = useRouter()

  useEffect(() => {
    // Redirect to the audit page
    router.replace('/audit')
  }, [router])

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-white flex items-center justify-center">
      <div className="text-center">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-emerald-600 mx-auto mb-4"></div>
        <p className="text-slate-600">Redirecting to audit page...</p>
      </div>
    </div>
  )
} 