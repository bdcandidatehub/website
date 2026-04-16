import re

# 1. Update index.html
with open('index.html', 'r') as f:
    html_content = f.read()

header_pattern = re.compile(r'<!-- Header / Navigation -->.*?</header>', re.DOTALL)
new_header = """<!-- Header / Navigation -->
    <header class="site-header glass-panel">
        <div class="container header-container">
            <div class="logo">
                <img src="logo.png" alt="CandidateHub Logo" class="logo-img">
            </div>
            <nav class="main-nav" id="mainNav">
                <a href="#problem">The Problem</a>
                <a href="#markis">Markis AI</a>
                <a href="#how-it-works">Platform</a>
                <a href="#outcomes">Outcomes</a>
            </nav>
            <div class="header-actions">
                <a href="/trial" class="btn btn-secondary nav-btn-trial" style="margin-right: 0.5rem; background: #fff; color: var(--primary); border: 1px solid var(--primary);">Start Free Trial</a>
                <a href="/demo" class="btn btn-primary">Book a Demo</a>
            </div>
            <button class="mobile-menu-btn" id="mobileMenuBtn" aria-label="Toggle Navigation" style="display: none;">
                <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none"><path d="M3 12h18M3 6h18M3 18h18"/></svg>
            </button>
        </div>
    </header>"""

html_content = header_pattern.sub(new_header, html_content)


body_pattern = re.compile(r'<!-- Section 2: Meet Markis -->.*</body>', re.DOTALL)
new_body = """<!-- Section 1: The Problem -->
    <section id="problem" class="section section-light problem-section">
        <div class="container text-center text-dark" style="max-width: 780px;">
            <h2 class="section-title text-dark">Your ATS tracks candidates. It doesn't convert them.</h2>
            <p class="section-subtitle text-body section-body-copy" style="max-width: 100%;">
                Candidates apply and hear nothing. Silver medalists disappear into the database. Recruiters spend their time chasing instead of engaging — not because they don't care, but because the tools they have were built for record-keeping, not relationships.
            </p>
            
            <div class="problem-stats row">
                <div class="stat-col column fade-in-up">
                    <div class="stat-number">60%</div>
                    <div class="stat-label">of candidates never hear back after applying</div>
                </div>
                <div class="stat-col column fade-in-up">
                    <div class="stat-number">4 in 5</div>
                    <div class="stat-label">silver medalists are never re-engaged</div>
                </div>
                <div class="stat-col column fade-in-up">
                    <div class="stat-number">#1</div>
                    <div class="stat-label">reason for recruiter burnout is manual follow-up</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 2: Meet Markis -->
    <section id="markis" class="section section-offwhite markis-section">
        <div class="container text-dark">
            <div class="section-header text-center">
                <span class="eyebrow">Meet Markis</span>
                <h2 class="section-title text-dark">The engagement layer your ATS was never designed to provide.</h2>
                <p class="section-subtitle text-body">
                    Markis is the intelligence layer inside CandidateHub. It watches signals, recommends actions, drafts communications, and keeps talent workflows moving — without adding more work to your plate.
                </p>
                <div class="rule-box fade-in-up">
                    <p><em>Markis recommends. You decide. Every action requires human approval.</em></p>
                </div>
            </div>
            
            <div class="markis-grid">
                <!-- Row 1 -->
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Talent Intelligence Strategist</h3>
                            <p class="text-body">Analyzes talent pools, market trends, and organizational needs to optimize strategy.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 00-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0020 4.77 5.07 5.07 0 0019.91 1S18.73.65 16 2.48a13.38 13.38 0 00-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 005 4.77a5.44 5.44 0 00-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 009 18.13V22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Journey Architect</h3>
                            <p class="text-body">Designs automated, multi-channel candidate and employee journeys to drive engagement.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><circle cx="12" cy="12" r="10" stroke="currentColor" stroke-width="2"/><path d="M12 6v6l4 2" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Recruiting Coordinator</h3>
                            <p class="text-body">Handles scheduling, follow-ups, initial screenings, and routine candidate communications.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Employee Retention Advisor</h3>
                            <p class="text-body">Identifies flight risks and prompts timely interventions to keep your top talent.</p>
                        </div>
                    </div>
                </div>
                <!-- Row 2 -->
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M18 20V10M12 20V4M6 20v-6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="18" cy="10" r="2" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="4" r="2" stroke="currentColor" stroke-width="2"/><circle cx="6" cy="14" r="2" stroke="currentColor" stroke-width="2"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Workforce Planning Analyst</h3>
                            <p class="text-body">Forecasts staffing needs across locations based on historical data and seasonality.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2M9 7a4 4 0 100-8 4 4 0 000 8zM23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Candidate Engagement Specialist</h3>
                            <p class="text-body">Nurtures declined or passive candidates with relevant updates and career opportunities.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M12 15l-3 3m0 0l-3-3m3 3V11M12 9l3-3m0 0l3 3m-3-3v8" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Internal Mobility Advisor</h3>
                            <p class="text-body">Matches existing employees to new roles, fostering long-term career growth internally.</p>
                        </div>
                    </div>
                </div>
                <div class="light-card square-module">
                    <div class="card-content">
                        <div class="card-icon-circle">
                            <svg viewBox="0 0 24 24" fill="none" class="icon"><path d="M22 11.08V12a10 10 0 11-5.93-9.14M22 4L12 14.01l-3-3" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
                        </div>
                        <div class="card-text text-dark">
                            <h3>Hiring Operations Manager</h3>
                            <p class="text-body">Oversees the end-to-end recruitment process, ensuring compliance and efficiency.</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Section 3: Stack diagram -->
    <section id="how-it-works" class="section section-light stack-section">
        <div class="container text-dark">
            <div class="section-header text-center">
                <h2 class="section-title text-dark">Built to sit on top of your existing ATS.</h2>
                <p class="section-subtitle text-body">
                    You don't need to rip and replace anything. CandidateHub adds the engagement and intelligence layer your current stack is missing.
                </p>
            </div>
            
            <div class="stack-diagram fade-in-up">
                <div class="tier tier-1">
                    <div class="tier-pill grey-pill">ATS</div>
                    <span class="tier-label">System of record</span>
                </div>
                <div class="tier-arrow">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="tier tier-2">
                    <div class="tier-pill blue-pill font-bold">CandidateHub</div>
                    <span class="tier-label">System of engagement</span>
                </div>
                <div class="tier-arrow">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                </div>
                <div class="tier tier-3">
                    <div class="tier-pill dark-blue-pill">Markis</div>
                    <span class="tier-label">System of intelligence</span>
                </div>
            </div>
            <div class="stack-note text-center">
                <p>Works with Workday, Greenhouse, ADP, iCIMS, BambooHR and more.</p>
            </div>
        </div>
    </section>

    <!-- Section 4: Built for mid-market -->
    <section class="section section-offwhite midmarket-section">
        <div class="container text-dark">
            <div class="split-layout">
                <div class="split-content fade-in-up">
                    <h2 class="section-title text-dark">Built for teams doing the work of ten.</h2>
                    <p class="section-subtitle text-left text-body">
                        If your recruiting team is small, your hiring volume is high, and your locations keep multiplying — CandidateHub was built for exactly that.
                    </p>
                    <div class="recognition-list">
                        <div class="rec-item">
                            <span class="rec-problem">24 locations, one HR Director.</span>
                            <span class="rec-solution">CandidateHub gives you enterprise-grade visibility without enterprise complexity.</span>
                        </div>
                        <div class="rec-item">
                            <span class="rec-problem">Seasonal hiring spikes.</span>
                            <span class="rec-solution">Markis helps you build talent pools before you need them, not after.</span>
                        </div>
                        <div class="rec-item">
                            <span class="rec-problem">Sky-high turnover.</span>
                            <span class="rec-solution">Identify flight risks early and automate the interventions that actually retain people.</span>
                        </div>
                    </div>
                </div>
                <div class="split-visual fade-in-up">
                    <div class="dashboard-widget light-panel relative">
                        <div class="widget-header">
                            <h4>Operations Command</h4>
                        </div>
                        <div class="widget-metrics">
                            <div class="metric-box box-light">
                                <span class="metric-label">Active Locations</span>
                                <span class="metric-value text-blue">24</span>
                            </div>
                            <div class="metric-box box-light">
                                <span class="metric-label">Seasonal Shift</span>
                                <span class="metric-value text-positive">Ready</span>
                            </div>
                            <div class="metric-box full-width box-light">
                                <span class="metric-label">Turnover Risk Alert</span>
                                <div class="risk-bar box-light-bar">
                                    <div class="risk-level" style="width: 15%;"></div>
                                </div>
                                <span class="metric-sub">Reduced by 40% this quarter</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="icp-note text-center fade-in-up">
                <p>Manufacturing &middot; Distribution &middot; Retail &middot; Healthcare-adjacent &middot; Multi-entity orgs</p>
            </div>
        </div>
    </section>

    <!-- Section 5: Consent Differentiator -->
    <section class="section section-dark-trust consent-section">
        <div class="container text-center text-white">
            <h2 class="section-title text-white">We don't scrape. We don't spam.</h2>
            <p class="section-subtitle text-white mw-700 mx-auto opacity-90" style="margin-left:auto; margin-right:auto;">
                Every candidate interaction on CandidateHub is opt-in, intentional, and compliant. In a world of data harvesting and automated blasting, consent-based engagement isn't just an ethical choice — it's a competitive advantage.
            </p>
            <div class="trust-pills row justify-center fade-in-up">
                <div class="trust-pill">No data scraping</div>
                <div class="trust-pill">Consent-first outreach</div>
                <div class="trust-pill">Compliance built in</div>
            </div>
        </div>
    </section>

    <!-- Section 6: Outcomes -->
    <section id="outcomes" class="section section-light outcomes-section">
        <div class="container text-dark">
            <div class="section-header text-center">
                <h2 class="section-title text-dark">What teams see after switching.</h2>
            </div>
            <div class="outcomes-grid">
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">85%</div>
                    <h4>Reduction in Manual Work</h4>
                    <p class="text-body">Automate scheduling, follow-ups, and repetitive tasks with Markis.</p>
                </div>
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">3x</div>
                    <h4>Higher Response Rates</h4>
                    <p class="text-body">Engage candidates through personalized, multi-channel journeys.</p>
                </div>
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">40%</div>
                    <h4>Lower Turnover Risk</h4>
                    <p class="text-body">Identify flight risks before they leave with proactive interventions.</p>
                </div>
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">+60%</div>
                    <h4>Internal Mobility</h4>
                    <p class="text-body">Seamlessly deploy existing talent to new roles and locations.</p>
                </div>
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">2x</div>
                    <h4>Faster Time-to-Fill</h4>
                    <p class="text-body">Gain real-time insights and reduce friction in your hiring pipeline.</p>
                </div>
                <div class="outcome-card light-panel text-center fade-in-up">
                    <div class="outcome-stat text-blue">2x</div>
                    <h4>Better Retention</h4>
                    <p class="text-body">Keep your critical frontline and operations talent engaged longer.</p>
                </div>
            </div>
            <div class="disclaimer-note text-center fade-in-up">
                <p>Based on early customer feedback.</p>
            </div>
        </div>
    </section>

    <!-- Section 7: Social proof -->
    <section class="section section-offwhite social-proof-section">
        <div class="container text-dark text-center">
            <h2 class="section-title text-dark mb-4">Trusted by growing teams</h2>
            <div class="logo-bar row justify-center fade-in-up">
                <div class="logo-placeholder"></div>
                <div class="logo-placeholder"></div>
                <div class="logo-placeholder"></div>
                <div class="logo-placeholder"></div>
                <div class="logo-placeholder"></div>
                <div class="logo-placeholder"></div>
            </div>
        </div>
    </section>

    <!-- Section 8: Final CTA -->
    <section class="section section-brand final-cta-section">
        <div class="container text-center text-white">
            <h2 class="section-title text-white" style="margin-bottom: 2rem;">Hiring is broken in the middle. We fix that.</h2>
            <p class="section-subtitle text-white mw-700 mx-auto opacity-90" style="margin-left:auto; margin-right:auto;">
                See CandidateHub and Markis in action — or start your free trial and have it running alongside your ATS today.
            </p>
            <div class="cta-actions row justify-center fade-in-up" style="gap: 1rem; margin-top: 2.5rem;">
                <a href="/demo" class="btn btn-primary btn-large">Book a Demo</a>
                <a href="/trial" class="btn btn-secondary-white btn-large">Start Free Trial</a>
            </div>
            <div class="trust-line fade-in-up" style="margin-top: 2rem; opacity: 0.8; font-size: 0.9rem;">
                <p>No credit card required &middot; Works with your existing ATS &middot; Setup in under a day</p>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="site-footer light-footer">
        <div class="container text-dark">
            <div class="footer-content">
                <div class="footer-brand">
                    <div class="logo">
                        <img src="logo.png" alt="CandidateHub Logo" class="logo-img" style="height: 24px; width: auto; filter: invert(0.8) brightness(0.2);">
                        <span class="text-dark">CandidateHub</span>
                    </div>
                    <p class="text-body" style="margin-top:1rem;">The engagement layer your ATS was never designed to provide.</p>
                </div>
                <div class="footer-links">
                    <div class="link-group">
                        <h4 class="text-dark">Platform</h4>
                        <a href="#markis" class="text-body">Markis AI</a>
                        <a href="#features" class="text-body">Features</a>
                        <a href="#integrations" class="text-body">Integrations</a>
                        <a href="#pricing" class="text-body">Pricing</a>
                    </div>
                    <div class="link-group">
                        <h4 class="text-dark">Company</h4>
                        <a href="#about" class="text-body">About</a>
                        <a href="#careers" class="text-body">Careers</a>
                        <a href="#contact" class="text-body">Contact</a>
                    </div>
                    <div class="link-group">
                        <h4 class="text-dark">Resources</h4>
                        <a href="#blog" class="text-body">Blog</a>
                        <a href="#help" class="text-body">Help Center</a>
                    </div>
                    <div class="link-group">
                        <h4 class="text-dark">Legal</h4>
                        <a href="#privacy" class="text-body">Privacy</a>
                        <a href="#terms" class="text-body">Terms</a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom text-body">
                &copy; 2026 CandidateHub. All rights reserved.
            </div>
        </div>
    </footer>
    <script src="main.js"></script>
</body>
</html>
"""

html_content = body_pattern.sub(new_body, html_content)
with open('index.html', 'w') as f:
    f.write(html_content)


# 2. Update styles.css
with open('styles.css', 'r') as f:
    css_content = f.read()

new_css_vars = """
    --text-dark: #0D1117;
    --text-body: #4A5568;
    --bg-light: #F8F9FB; /* Light / near-white */
    --bg-offwhite: #EFF2F6;
    --brand-blue: #2D7BBF;
    --brand-dark-blue: #0A1929;
"""
css_content = css_content.replace("--transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);", "--transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);\n" + new_css_vars)

appended_css = """

/* --- New Section Styles --- */
.section-light { background: var(--bg-light); color: var(--text-dark); }
.section-offwhite { background: var(--bg-offwhite); color: var(--text-dark); }
.section-dark-trust { background: var(--brand-dark-blue); color: #fff; }
.section-brand { background: var(--brand-blue); color: #fff; }

.text-dark { color: var(--text-dark) !important; }
.text-body { color: var(--text-body) !important; }
.text-white { color: #fff !important; }
.text-blue { color: var(--primary) !important; }

.row { display: flex; flex-wrap: wrap; }
.column { flex: 1; min-width: 250px; }
.justify-center { justify-content: center; }

.btn-secondary-white {
    background: #fff;
    color: var(--primary);
    border: 2px solid var(--primary);
}
.btn-secondary-white:hover {
    background: var(--bg-offwhite);
    transform: translateY(-2px);
}

/* Header & Mobile nav */
#mainNav.mobile-active {
    display: flex !important;
    flex-direction: column;
    position: absolute;
    top: 80px;
    left: 0;
    width: 100%;
    background: rgba(4, 8, 18, 0.95);
    padding: 1rem;
    padding-bottom: 2rem;
    gap: 1.5rem;
    border-bottom: 1px solid var(--border-glass);
}
.mobile-menu-btn {
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
}
@media (min-width: 769px) {
    .mobile-menu-btn { display: none !important; }
    #mainNav { display: flex !important; }
}
@media (max-width: 768px) {
    .header-actions { display: none; }
    .mobile-menu-btn { display: block !important; }
    #mainNav { display: none; }
}

/* The Problem */
.problem-stats { margin-top: 4rem; gap: 2rem; }
.stat-col { padding: 1.5rem; }
.stat-number { font-size: 3rem; font-weight: 700; color: var(--primary); margin-bottom: 0.5rem; line-height: 1; }
.stat-label { font-size: 1rem; color: var(--text-body); }

/* Markis */
.eyebrow { font-variant: small-caps; color: var(--primary); font-weight: 600; letter-spacing: 1px; font-size: 0.9rem; display: block; margin-bottom: 0.5rem; }
.rule-box { margin-top: 1.5rem; opacity: 0.8; font-size: 0.95rem; }
.light-card {
    background: #fff;
    border: 1px solid #e1e4e8;
    border-radius: 12px;
    padding: 1.5rem;
    transition: var(--transition);
    height: 100%;
    display: flex;
    flex-direction: column;
}
.light-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    border-color: rgba(45, 123, 191, 0.3);
}
.card-icon-circle {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: var(--secondary);
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1.5rem;
}
.card-icon-circle svg { width: 24px; height: 24px; color: var(--primary); }
.card-text h3 { font-size: 1.1rem; color: var(--text-dark); margin-bottom: 0.5rem; font-weight: 600; }
.card-text p { font-size: 0.9rem; margin-top: 0 !important; max-height: unset !important; opacity: 1 !important; }

/* Stack Diagram */
.stack-diagram { display: flex; align-items: center; justify-content: center; gap: 1rem; margin: 4rem 0 2rem; flex-wrap: wrap; }
.tier { display: flex; flex-direction: column; align-items: center; gap: 0.75rem; }
.tier-pill { padding: 1rem 2.5rem; border-radius: 50px; font-weight: 500; font-size: 1.1rem; }
.grey-pill { background: #e1e4e8; color: var(--text-body); }
.blue-pill { background: var(--secondary); color: var(--primary); font-size: 1.25rem !important; padding: 1.25rem 3rem; }
.dark-blue-pill { background: var(--brand-dark-blue); color: #fff; }
.tier-label { font-size: 0.85rem; color: var(--text-body); font-weight: 500; }
.arrow { color: #cbd5e1; width: 32px; height: 32px; }
.stack-note p { font-size: 0.9rem; color: var(--text-body); }
.font-bold { font-weight: 700; }

/* Mid-Market */
.recognition-list { display: flex; flex-direction: column; gap: 1.5rem; margin-top: 2rem; }
.rec-item { font-size: 1.05rem; line-height: 1.5; }
.rec-problem { font-weight: 700; color: var(--text-dark); margin-right: 0.5rem; }
.rec-solution { color: var(--text-body); }
.light-panel { background: #fff; border-radius: 16px; border: 1px solid #e1e4e8; box-shadow: 0 10px 30px rgba(0,0,0,0.05); padding: 2rem; }
.box-light { background: var(--bg-light); border: 1px solid #e1e4e8; border-radius: 12px; padding: 1.5rem; }
.box-light .metric-label { color: var(--text-body); }
.box-light-bar { background: #e1e4e8; }
.icp-note { margin-top: 4rem; font-size: 0.85rem; color: var(--text-body); font-weight: 500; }

/* Consent Options */
.trust-pills { gap: 1.5rem; margin-top: 4rem; }
.trust-pill {
    padding: 0.75rem 1.5rem;
    border-radius: 50px;
    background: transparent;
    border: 1px solid rgba(255,255,255,0.2);
    color: #fff;
    font-weight: 500;
}

/* Outcomes */
.disclaimer-note { margin-top: 3rem; font-size: 0.85rem; color: var(--text-body); font-style: italic; }

/* Social Proof */
.logo-bar { gap: 3rem; align-items: center; margin-top: 3rem; flex-wrap: wrap; }
.logo-placeholder { background: #cbd5e1; width: 120px; height: 40px; border-radius: 4px; opacity: 0.5; }

/* Footer */
.light-footer { background: var(--bg-light); border-top: 1px solid #e1e4e8; }
.light-footer .link-group a:hover { color: var(--primary); }

@media (max-width: 768px) {
    .stack-diagram { flex-direction: column; }
    .arrow { transform: rotate(90deg); }
    .problem-stats.row { flex-direction: column; gap: 1rem; }
}
"""

with open('styles.css', 'a') as f:
    f.write(appended_css)


# 3. Update main.js
with open('main.js', 'r') as f:
    js_content = f.read()

# Add new selectors for animations
js_content = js_content.replace("'.square-module, .outcome-card, .testimonial-card, .split-content, .dashboard-widget, .timeline-node'", "'.square-module, .outcome-card, .testimonial-card, .split-content, .dashboard-widget, .timeline-node, .fade-in-up, .light-card'")

# Add mobile menu toggle
mobile_menu_js = """
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mainNav = document.getElementById('mainNav');
    if(mobileMenuBtn && mainNav) {
        mobileMenuBtn.addEventListener('click', () => {
            mainNav.classList.toggle('mobile-active');
        });
    }
"""

js_content = js_content.replace("});", mobile_menu_js + "\n});")

with open('main.js', 'w') as f:
    f.write(js_content)

