'use client'

import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Menu,
  MenuButton,
  MenuItem,
  MenuItems,
} from '@headlessui/react'
import { Bars3Icon, BellIcon, ChevronDownIcon } from '@heroicons/react/24/outline'
import { PlusIcon, ChartBarIcon, CogIcon, StarIcon } from '@heroicons/react/20/solid'
import { Link } from './link'
import { Logo } from './logo'
import { Button } from './button'
import { useState, useEffect } from 'react'

interface UserData {
  name: string
  email: string
  subscription: 'free' | 'pro' | 'enterprise'
  audits_remaining: number
}

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: ChartBarIcon, current: true },
  { name: 'New Audit', href: '/audit', icon: PlusIcon, current: false },
  { name: 'Pricing', href: '/pricing', icon: StarIcon, current: false },
]

function classNames(...classes: string[]) {
  return classes.filter(Boolean).join(' ')
}

export function DashboardNavbar() {
  const [userData, setUserData] = useState<UserData | null>(null)

  useEffect(() => {
    // Load user data from localStorage
    const savedAudits = JSON.parse(localStorage.getItem('userAudits') || '[]')
    const userEmail = localStorage.getItem('userEmail') || 'demo@example.com'
    const userName = localStorage.getItem('userName') || 'Demo User'
    
    setUserData({
      name: userName,
      email: userEmail,
      subscription: 'free',
      audits_remaining: Math.max(0, 3 - savedAudits.length),
    })
  }, [])

  return (
    <Disclosure as="nav" className="bg-white shadow-sm border-b border-slate-200">
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div className="flex h-16 justify-between">
          <div className="flex">
            <div className="flex flex-shrink-0 items-center">
              <Link href="/dashboard">
                <Logo className="h-8 w-auto" />
              </Link>
            </div>
            <div className="hidden sm:-my-px sm:ml-10 sm:flex sm:space-x-8">
              {navigation.map((item) => {
                const Icon = item.icon
                return (
                  <Link
                    key={item.name}
                    href={item.href}
                    className={classNames(
                      item.current
                        ? 'border-emerald-500 text-slate-900'
                        : 'border-transparent text-slate-500 hover:border-slate-300 hover:text-slate-700',
                      'inline-flex items-center border-b-2 px-1 pt-1 text-sm font-medium'
                    )}
                    aria-current={item.current ? 'page' : undefined}
                  >
                    <Icon className="mr-2 h-4 w-4" />
                    {item.name}
                  </Link>
                )
              })}
            </div>
          </div>
          
          <div className="hidden sm:ml-6 sm:flex sm:items-center sm:space-x-4">
            {/* Audit Credits Display */}
            {userData?.subscription === 'free' && (
              <div className="flex items-center gap-2 px-3 py-1 bg-slate-50 rounded-full">
                <span className="text-sm text-slate-600">
                  {userData.audits_remaining} free audits left
                </span>
                {userData.audits_remaining <= 1 && (
                  <Button href="/pricing" className="text-xs px-2 py-1 bg-emerald-600 hover:bg-emerald-700">
                    Upgrade
                  </Button>
                )}
              </div>
            )}

            {/* New Audit Button */}
            <Button href="/audit" className="bg-emerald-600 hover:bg-emerald-700">
              <PlusIcon className="mr-2 h-4 w-4" />
              New Audit
            </Button>

            {/* Profile dropdown */}
            <Menu as="div" className="relative ml-3">
              <div>
                <MenuButton className="relative flex items-center rounded-full bg-white p-1 text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2">
                  <span className="sr-only">Open user menu</span>
                  <div className="flex items-center gap-2">
                    <div className="h-8 w-8 rounded-full bg-emerald-100 flex items-center justify-center">
                      <span className="text-sm font-medium text-emerald-600">
                        {userData?.name.charAt(0).toUpperCase() || 'U'}
                      </span>
                    </div>
                    <div className="hidden md:block text-left">
                      <div className="text-sm font-medium text-slate-900">{userData?.name}</div>
                      <div className="text-xs text-slate-500 capitalize">{userData?.subscription} Plan</div>
                    </div>
                    <ChevronDownIcon className="h-4 w-4 text-slate-400" />
                  </div>
                </MenuButton>
              </div>
              <MenuItems className="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
                <MenuItem>
                  <div className="px-4 py-2 border-b border-slate-200">
                    <div className="text-sm font-medium text-slate-900">{userData?.name}</div>
                    <div className="text-sm text-slate-500">{userData?.email}</div>
                  </div>
                </MenuItem>
                <MenuItem>
                  <Link
                    href="/dashboard"
                    className="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50"
                  >
                    Dashboard
                  </Link>
                </MenuItem>
                <MenuItem>
                  <Link
                    href="/pricing"
                    className="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50"
                  >
                    {userData?.subscription === 'free' ? 'Upgrade Plan' : 'Billing'}
                  </Link>
                </MenuItem>
                <MenuItem>
                  <Link
                    href="/dashboard"
                    className="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50"
                  >
                    Settings
                  </Link>
                </MenuItem>
                <MenuItem>
                  <Link
                    href="/"
                    className="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50"
                  >
                    Sign out
                  </Link>
                </MenuItem>
              </MenuItems>
            </Menu>
          </div>

          {/* Mobile menu button */}
          <div className="-mr-2 flex items-center sm:hidden">
            <DisclosureButton className="relative inline-flex items-center justify-center rounded-md bg-white p-2 text-slate-400 hover:bg-slate-100 hover:text-slate-500 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2">
              <span className="sr-only">Open main menu</span>
              <Bars3Icon className="block h-6 w-6" aria-hidden="true" />
            </DisclosureButton>
          </div>
        </div>
      </div>

      {/* Mobile menu */}
      <DisclosurePanel className="sm:hidden">
        <div className="space-y-1 pb-3 pt-2">
          {navigation.map((item) => {
            const Icon = item.icon
            return (
              <DisclosureButton
                key={item.name}
                as={Link}
                href={item.href}
                className={classNames(
                  item.current
                    ? 'border-emerald-500 bg-emerald-50 text-emerald-700'
                    : 'border-transparent text-slate-600 hover:border-slate-300 hover:bg-slate-50 hover:text-slate-800',
                  'block border-l-4 py-2 pl-3 pr-4 text-base font-medium'
                )}
                aria-current={item.current ? 'page' : undefined}
              >
                <div className="flex items-center">
                  <Icon className="mr-3 h-5 w-5" />
                  {item.name}
                </div>
              </DisclosureButton>
            )
          })}
        </div>
        
        <div className="border-t border-slate-200 pb-3 pt-4">
          <div className="flex items-center px-4">
            <div className="flex-shrink-0">
              <div className="h-10 w-10 rounded-full bg-emerald-100 flex items-center justify-center">
                <span className="text-sm font-medium text-emerald-600">
                  {userData?.name.charAt(0).toUpperCase() || 'U'}
                </span>
              </div>
            </div>
            <div className="ml-3">
              <div className="text-base font-medium text-slate-800">{userData?.name}</div>
              <div className="text-sm font-medium text-slate-500">{userData?.email}</div>
            </div>
          </div>
          
          {userData?.subscription === 'free' && (
            <div className="mt-3 px-4">
              <div className="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                <span className="text-sm text-slate-600">
                  {userData.audits_remaining} free audits left
                </span>
                <Button href="/pricing" className="text-xs px-3 py-1 bg-emerald-600 hover:bg-emerald-700">
                  Upgrade
                </Button>
              </div>
            </div>
          )}
          
          <div className="mt-3 space-y-1">
            <DisclosureButton
              as={Link}
              href="/audit"
              className="block px-4 py-2 text-base font-medium text-slate-500 hover:bg-slate-100 hover:text-slate-800"
            >
              <div className="flex items-center">
                <PlusIcon className="mr-3 h-5 w-5" />
                New Audit
              </div>
            </DisclosureButton>
            <DisclosureButton
              as={Link}
              href="/pricing"
              className="block px-4 py-2 text-base font-medium text-slate-500 hover:bg-slate-100 hover:text-slate-800"
            >
              {userData?.subscription === 'free' ? 'Upgrade Plan' : 'Billing'}
            </DisclosureButton>
            <DisclosureButton
              as={Link}
              href="/dashboard"
              className="block px-4 py-2 text-base font-medium text-slate-500 hover:bg-slate-100 hover:text-slate-800"
            >
              Settings
            </DisclosureButton>
            <DisclosureButton
              as={Link}
              href="/"
              className="block px-4 py-2 text-base font-medium text-slate-500 hover:bg-slate-100 hover:text-slate-800"
            >
              Sign out
            </DisclosureButton>
          </div>
        </div>
      </DisclosurePanel>
    </Disclosure>
  )
} 