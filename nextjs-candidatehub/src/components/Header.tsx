"use client";

import Image from "next/image";
import Link from "next/link";

export default function Header() {
  return (
    <header className="site-header glass-panel">
      <div className="container header-container">
        <div className="logo">
          <Image src="/Logo.png" alt="CandidateHub Logo" width={32} height={32} className="logo-img" />
          <span>CandidateHub</span>
        </div>
        <nav className="main-nav" id="mainNav">
          <Link href="/markis">Markis AI</Link>
          <Link href="/platform">Platform</Link>
          <Link href="/pricing">Pricing</Link>
          <Link href="/about">About</Link>
          <Link href="/insights">Insights</Link>
          <Link href="/contact">Contact</Link>
        </nav>
        <div className="header-actions">
          <Link href="/trial" className="btn btn-secondary nav-btn-trial" style={{ marginRight: '0.5rem', background: '#fff', color: 'var(--primary)', border: '1px solid var(--primary)' }}>
            Start Free Trial
          </Link>
          <Link href="/demo" className="btn btn-primary">Book a Demo</Link>
        </div>
        <button className="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle Navigation" style={{ display: 'none' }}>
          <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" strokeWidth="2" fill="none">
            <path d="M3 12h18M3 6h18M3 18h18" />
          </svg>
        </button>
      </div>
    </header>
  );
}
