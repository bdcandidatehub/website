"use client";

import Image from "next/image";
import Link from "next/link";

export default function Footer() {
  return (
    <footer className="site-footer light-footer">
      <div className="container text-dark">
        <div className="footer-content">
          <div className="footer-brand">
            <div className="logo">
              <Image src="/Logo.png" alt="CandidateHub Logo" width={24} height={24} className="logo-img" style={{ filter: 'invert(0.8) brightness(0.2)' }} />
              <span className="text-dark">CandidateHub</span>
            </div>
            <p className="text-body" style={{ marginTop: '1rem' }}>The engagement layer your ATS was never designed to provide.</p>
          </div>
          <div className="footer-links">
            <div className="link-group">
              <h4 className="text-dark">Platform</h4>
              <Link href="/markis" className="text-body">Markis AI</Link>
              <Link href="/platform" className="text-body">Platform</Link>
              <Link href="#integrations" className="text-body">Integrations</Link>
              <Link href="/pricing" className="text-body">Pricing</Link>
            </div>
            <div className="link-group">
              <h4 className="text-dark">Company</h4>
              <Link href="/about" className="text-body">About</Link>
              <Link href="#careers" className="text-body">Careers</Link>
              <Link href="/contact" className="text-body">Contact</Link>
            </div>
            <div className="link-group">
              <h4 className="text-dark">Resources</h4>
              <Link href="/insights" className="text-body">Insights</Link>
              <Link href="#help" className="text-body">Help Center</Link>
            </div>
            <div className="link-group">
              <h4 className="text-dark">Legal</h4>
              <Link href="#privacy" className="text-body">Privacy</Link>
              <Link href="#terms" className="text-body">Terms</Link>
            </div>
          </div>
        </div>
        <div className="footer-bottom text-body">
          &copy; 2026 CandidateHub. All rights reserved.
        </div>
      </div>
    </footer>
  );
}
