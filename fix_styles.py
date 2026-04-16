with open('styles.css', 'r') as f:
    css = f.read()

# Fix for outcome-stat gradient override
css += """

/* Override outcome-stat for light mode */
.outcomes-section .outcome-stat {
    background: none;
    -webkit-text-fill-color: var(--primary);
    color: var(--primary);
}

/* Fix .square-module background */
.light-card.square-module {
    background: #fff;
    border: 1px solid #e1e4e8 !important;
}
.light-card.square-module:hover {
    background: #fff !important;
    border-color: rgba(45, 123, 191, 0.5) !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
}
.light-card.square-module .card-text p {
    color: var(--text-body) !important;
}

/* Specificity overrides for markis-grid text */
.markis-grid .card-text h3 { color: var(--text-dark) !important; }
.markis-grid .light-card:hover .card-text h3 { color: var(--primary) !important; }
.markis-grid .card-icon-wrapper svg { color: var(--primary) !important; opacity: 1 !important; }

/* Override .dashboard-widget glow */
.dashboard-widget.light-panel {
    background: #fff !important;
    border: 1px solid #e1e4e8 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05) !important;
}
.dashboard-widget.light-panel .glow-orb { display: none; }
.dashboard-widget.light-panel .widget-header { border-bottom-color: #e1e4e8; color: var(--text-dark); }
.dashboard-widget.light-panel .metric-label { color: var(--text-body); }
.dashboard-widget.light-panel .metric-box { background: var(--bg-light); border-color: #e1e4e8; }
.dashboard-widget.light-panel .metric-value { color: var(--text-dark); }
.dashboard-widget.light-panel .metric-value.text-blue { color: var(--primary) !important; }
.dashboard-widget.light-panel .metric-value.text-positive { color: #10B981 !important; }
"""

with open('styles.css', 'w') as f:
    f.write(css)

