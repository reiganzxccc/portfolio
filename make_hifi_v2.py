import base64
import os

def get_b64(path, mime):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

avatar_b64 = get_b64(r"c:\Users\NITRO\PROFE7\assets\profile_photo.jpg", "image/jpeg")
project_b64 = get_b64(r"c:\Users\NITRO\PROFE7\assets\govsupply_connect.png", "image/png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>HI-FI Wireframe Architecture - Jeron Opjer Portfolio Website</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * {{
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }}
  body {{
    background: #07090e;
    background-image: 
      linear-gradient(rgba(255,255,255,0.025) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.025) 1px, transparent 1px);
    background-size: 24px 24px;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #e2e8f0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 24px 20px 40px;
    min-height: 100vh;
  }}

  .canvas-wrapper {{
    position: relative;
    width: 1040px;
    max-width: 1040px;
  }}

  .browser-mockup {{
    background: #0b111c;
    border-radius: 16px;
    border: 1px solid #1e293b;
    box-shadow: 0 25px 60px -15px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.05);
    overflow: visible;
    position: relative;
  }}

  /* Top Browser Bar */
  .browser-header {{
    background: #080d15;
    padding: 10px 18px;
    border-top-left-radius: 16px;
    border-top-right-radius: 16px;
    border-bottom: 1px solid #1e293b;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .window-dots {{
    display: flex;
    gap: 7px;
  }}
  .dot {{
    width: 11px;
    height: 11px;
    border-radius: 50%;
  }}
  .dot.red {{ background: #ef4444; }}
  .dot.yellow {{ background: #f59e0b; }}
  .dot.green {{ background: #10b981; }}

  .url-bar {{
    background: #0f1724;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 4px 18px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: #94a3b8;
    letter-spacing: 0.5px;
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .url-bar .secure {{ color: #10b981; font-weight: 600; }}
  .url-bar .site-link {{ color: #cbd5e1; }}
  .url-bar .theme-tag {{ color: #38bdf8; font-weight: 600; }}

  .version-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #64748b;
  }}

  /* Academic Top Bar (from index.html) */
  .academic-topbar-mock {{
    background: rgba(15, 23, 42, 0.7);
    border-bottom: 1px solid #1e293b;
    padding: 7px 18px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 11px;
  }}
  .uni-badge-mock {{
    background: rgba(79, 123, 245, 0.15);
    color: #60a5fa;
    border: 1px solid #2563eb;
    padding: 2px 7px;
    border-radius: 4px;
    font-weight: 700;
    font-size: 9px;
    margin-right: 8px;
  }}
  .theme-btn-group {{
    display: flex;
    gap: 4px;
  }}
  .mock-theme-btn {{
    background: #111a28;
    border: 1px solid #1e293b;
    color: #94a3b8;
    padding: 2.5px 8px;
    border-radius: 4px;
    font-size: 9px;
    font-weight: 600;
  }}
  .mock-theme-btn.active {{
    background: #2563eb;
    border-color: #3b82f6;
    color: #ffffff;
  }}

  /* Main Two-Column Layout */
  .wireframe-grid {{
    display: grid;
    grid-template-columns: 260px 1fr;
    gap: 14px;
    padding: 16px;
  }}

  /* Numbered Annotations Badge */
  .badge-pin {{
    position: absolute;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #2563eb;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 2px #0b111c, 0 2px 8px rgba(37, 99, 235, 0.7);
    z-index: 50;
  }}
  .pin-1 {{ top: 220px; left: -11px; }}
  .pin-2 {{ top: 85px; right: -11px; }}
  .pin-3 {{ top: 280px; right: -11px; }}
  .pin-4 {{ top: 470px; right: -11px; }}
  .pin-5 {{ top: 730px; right: -11px; }}
  .pin-6 {{ top: 960px; right: -11px; }}
  .pin-7 {{ bottom: 80px; right: -11px; }}

  /* Generic Card Styles */
  .wf-card {{
    background: #0e1524;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 14px;
    position: relative;
  }}

  /* ================= LEFT SIDEBAR ================= */
  .sidebar-col {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  .profile-box {{
    background: #0e1524;
    border: 1px solid #2563eb;
    border-radius: 10px;
    padding: 16px 12px;
    text-align: center;
  }}
  .avatar-wrap {{
    position: relative;
    width: 82px;
    height: 82px;
    margin: 0 auto 10px;
  }}
  .avatar-img {{
    width: 100%;
    height: 100%;
    border-radius: 50%;
    object-fit: cover;
    border: 2.5px solid #38bdf8;
    box-shadow: 0 0 16px rgba(56, 189, 248, 0.35);
  }}
  .verified-icon {{
    position: absolute;
    bottom: 2px;
    right: 2px;
    background: #0284c7;
    color: #fff;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    border: 2px solid #0e1524;
  }}
  .profile-name {{
    font-size: 14px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 2px;
  }}
  .profile-role-pill {{
    display: inline-block;
    font-size: 9px;
    font-weight: 700;
    color: #60a5fa;
    background: rgba(79, 123, 245, 0.14);
    border: 1px solid #2563eb;
    padding: 2px 9px;
    border-radius: 12px;
    margin-bottom: 4px;
  }}
  .profile-meta {{
    font-size: 8px;
    color: #94a3b8;
    margin-bottom: 10px;
  }}
  .social-pills {{
    display: flex;
    justify-content: center;
    gap: 6px;
  }}
  .soc-pill {{
    background: #162032;
    border: 1px solid #26354f;
    color: #94a3b8;
    font-size: 9px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
  }}

  /* Nav Stack */
  .nav-stack {{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }}
  .nav-item {{
    background: #101827;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 11px;
    color: #94a3b8;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 600;
  }}
  .nav-item.active-blue {{
    border: 1.5px solid #4f7bf5;
    color: #ffffff;
    background: rgba(79, 123, 245, 0.22);
    box-shadow: 0 0 16px rgba(79, 123, 245, 0.4), inset 0 0 8px rgba(79, 123, 245, 0.15);
    font-weight: 700;
  }}

  /* Real Sidebar Contact Brief (from index.html) */
  .sidebar-contact-card {{
    background: #09101c;
    border: 1px solid #1e293b;
    border-radius: 8px;
    padding: 10px;
  }}
  .brief-title {{
    font-size: 8px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 7px;
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
  }}
  .brief-list {{
    display: flex;
    flex-direction: column;
    gap: 5px;
    font-size: 8px;
    color: #cbd5e1;
    font-family: 'JetBrains Mono', monospace;
  }}
  .brief-item {{
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .brief-icon {{
    color: #38bdf8;
    font-size: 9px;
  }}

  /* ================= RIGHT MAIN COLUMN ================= */
  .main-col {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  /* SECTION 2: Hero Section (Actual Content from index.html) */
  .hero-card {{
    background: #0e1524;
    border: 1px solid #2563eb;
    border-radius: 10px;
    padding: 16px 18px;
    position: relative;
  }}
  .hero-badge-pill {{
    display: inline-block;
    border: 1px solid #2563eb;
    background: rgba(79, 123, 245, 0.12);
    color: #60a5fa;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 12px;
    margin-bottom: 8px;
  }}
  .hero-title {{
    font-size: 18px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.3px;
    line-height: 1.25;
    margin-bottom: 6px;
  }}
  .hero-title span {{
    color: #60a5fa;
  }}
  .hero-desc {{
    font-size: 10px;
    color: #94a3b8;
    line-height: 1.45;
    margin-bottom: 12px;
    max-width: 680px;
  }}
  .hero-actions-row {{
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 12px;
  }}
  .btn-primary-blue {{
    background: #2563eb;
    border: 1px solid #3b82f6;
    color: #ffffff;
    font-size: 10.5px;
    font-weight: 700;
    padding: 7px 15px;
    border-radius: 6px;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.4);
  }}
  .btn-secondary-dark {{
    background: #111a28;
    border: 1px solid #1e293b;
    color: #cbd5e1;
    font-size: 10.5px;
    font-weight: 600;
    padding: 7px 14px;
    border-radius: 6px;
  }}
  .hero-stats-strip {{
    display: flex;
    gap: 16px;
    border-top: 1px solid #1e293b;
    padding-top: 9px;
  }}
  .stat-block {{
    display: flex;
    align-items: baseline;
    gap: 6px;
    font-size: 9px;
    color: #94a3b8;
  }}
  .stat-val {{
    font-size: 13px;
    font-weight: 800;
    color: #38bdf8;
  }}

  /* SECTION: Skills / Daily Drivers (Actual from index.html) */
  .skills-card {{
    background: #0e1524;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    align-items: center;
    gap: 12px;
  }}
  .skills-header {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5px;
    white-space: nowrap;
  }}
  .skills-header strong {{
    display: block;
    font-size: 9.5px;
    color: #38bdf8;
  }}
  .skills-pills-wrap {{
    display: flex;
    align-items: center;
    gap: 5px;
    flex-wrap: wrap;
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5px;
  }}
  .tool-tag {{
    background: #141f32;
    border: 1px solid #233451;
    color: #93c5fd;
    padding: 2.5px 7px;
    border-radius: 4px;
    font-weight: 600;
  }}

  /* SECTION 3: Projects + About (from index.html) */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 12px;
  }}
  .proj-card {{
    background: #0e1524;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card-label-top {{
    font-size: 8px;
    color: #38bdf8;
    font-weight: 700;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
  }}
  .card-h3 {{
    font-size: 12px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 8px;
  }}
  .proj-tabs-row {{
    display: flex;
    gap: 6px;
    margin-bottom: 8px;
  }}
  .tab-btn-mini {{
    background: #111e32;
    border: 1px solid #1e3a5f;
    color: #94a3b8;
    font-size: 8px;
    padding: 3px 8px;
    border-radius: 4px;
    font-weight: 600;
  }}
  .tab-btn-mini.active {{
    background: #2563eb;
    border-color: #3b82f6;
    color: #fff;
  }}
  .proj-preview-box {{
    background: #080d14;
    border: 1px solid #1e293b;
    border-radius: 6px;
    overflow: hidden;
    height: 105px;
    margin-bottom: 6px;
  }}
  .proj-preview-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .proj-title-live {{
    font-size: 9.5px;
    font-weight: 700;
    color: #cbd5e1;
    margin-bottom: 3px;
  }}
  .proj-desc-live {{
    font-size: 8px;
    color: #94a3b8;
    line-height: 1.35;
    margin-bottom: 6px;
  }}
  .btn-arch-detail {{
    font-size: 8px;
    color: #38bdf8;
    font-weight: 700;
    text-decoration: none;
    font-family: 'JetBrains Mono', monospace;
  }}

  /* About Card (from index.html) */
  .about-card {{
    background: #0e1524;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .about-bio-text {{
    font-size: 8.5px;
    color: #cbd5e1;
    line-height: 1.45;
    margin-bottom: 8px;
  }}
  .about-pills-grid {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4px;
    margin-bottom: 8px;
  }}
  .cred-pill-item {{
    background: #111a28;
    border: 1px solid #1e293b;
    border-radius: 4px;
    padding: 3px 6px;
    font-size: 7.5px;
    color: #38bdf8;
    font-weight: 600;
    font-family: 'JetBrains Mono', monospace;
  }}
  .btn-about-modal {{
    background: #111a28;
    border: 1px solid #2563eb;
    color: #60a5fa;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 8px;
    font-weight: 700;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }}

  /* ================= SECTION 4: CREDENTIALS (from index.html) ================= */
  .credentials-section-card {{
    background: #0e1524;
    border: 1px solid #0d9488;
    border-radius: 10px;
    padding: 12px 14px;
  }}
  .cred-header-strip {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }}
  .cred-grid-3 {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
  }}
  .cert-tile {{
    background: #080f1a;
    border: 1px solid #1a293e;
    border-radius: 8px;
    padding: 9px 10px;
    border-left: 3px solid #14b8a6;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .cert-top-info {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 7.5px;
    font-family: 'JetBrains Mono', monospace;
    color: #94a3b8;
    margin-bottom: 4px;
  }}
  .cert-verified-tag {{
    background: rgba(20, 184, 166, 0.15);
    color: #2dd4bf;
    padding: 1.5px 5px;
    border-radius: 3px;
    border: 1px solid #0d9488;
    font-weight: 700;
  }}
  .cert-title-text {{
    font-size: 9.5px;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.3;
    margin-bottom: 4px;
  }}
  .cert-id-tag {{
    background: #111a28;
    border: 1px solid #1e293b;
    border-radius: 3px;
    padding: 2px 5px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5px;
    color: #38bdf8;
    display: flex;
    justify-content: space-between;
    margin-bottom: 5px;
  }}
  .cert-tags-flex {{
    display: flex;
    gap: 3px;
    flex-wrap: wrap;
    margin-bottom: 6px;
  }}
  .c-tag {{
    background: #132032;
    color: #94a3b8;
    font-size: 6.5px;
    padding: 1.5px 4px;
    border-radius: 3px;
  }}
  .cert-verify-link {{
    font-size: 7.5px;
    color: #14b8a6;
    font-weight: 700;
    font-family: 'JetBrains Mono', monospace;
    text-align: right;
  }}

  /* ================= SECTION 5: SERVICES & VALUES (from index.html) ================= */
  .grid-services-values {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }}
  .sv-card {{
    background: #0e1524;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 12px;
  }}
  .sv-list {{
    list-style: none;
    font-size: 8px;
    display: flex;
    flex-direction: column;
    gap: 6px;
    margin-top: 6px;
  }}
  .sv-item {{
    background: #09101c;
    border: 1px solid #192538;
    border-radius: 5px;
    padding: 6px 8px;
  }}
  .sv-title {{
    font-weight: 700;
    color: #f1f5f9;
    font-size: 8.5px;
    margin-bottom: 2px;
  }}
  .sv-desc {{
    color: #94a3b8;
    font-size: 7.5px;
    line-height: 1.35;
  }}

  /* SECTION 6: Contact & Communication (from index.html) */
  .contact-section-card {{
    background: #0e1524;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 12px 14px;
  }}
  .contact-grid {{
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 16px;
  }}
  .contact-left-box {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .contact-card-label {{
    background: #08101a;
    border: 1px solid #1a273a;
    border-radius: 6px;
    padding: 6px 8px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 8px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .contact-card-label span {{
    color: #cbd5e1;
  }}
  .contact-card-label .val-bold {{
    color: #38bdf8;
    font-weight: 700;
  }}
  .contact-form-box {{
    display: flex;
    flex-direction: column;
    gap: 5px;
  }}
  .c-input {{
    background: #08101a;
    border: 1px solid #1e293b;
    border-radius: 5px;
    padding: 5px 8px;
    font-size: 8px;
    color: #64748b;
    font-family: 'JetBrains Mono', monospace;
  }}
  .btn-submit-live {{
    background: #2563eb;
    border: none;
    color: #ffffff;
    font-size: 9px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
  }}

  /* ================= SECTION 7: REAL FOOTER (from index.html lines 1014-1084) ================= */
  .footer-live-card {{
    background: #080d16;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 14px 16px;
  }}
  .footer-5col-grid {{
    display: grid;
    grid-template-columns: 1.3fr 1fr 1fr 1fr 1fr;
    gap: 12px;
    margin-bottom: 12px;
  }}
  .f-col-title {{
    font-size: 9px;
    font-weight: 700;
    color: #f1f5f9;
    margin-bottom: 6px;
    border-bottom: 1px solid #192538;
    padding-bottom: 3px;
  }}
  .f-col-desc {{
    font-size: 7.5px;
    color: #94a3b8;
    line-height: 1.4;
    margin-bottom: 6px;
  }}
  .f-loc-tag {{
    font-size: 7px;
    color: #14b8a6;
    font-family: 'JetBrains Mono', monospace;
  }}
  .f-links-list {{
    list-style: none;
    font-size: 7.5px;
    color: #94a3b8;
    display: flex;
    flex-direction: column;
    gap: 3px;
  }}
  .f-links-list li::before {{
    content: "› ";
    color: #38bdf8;
  }}
  .footer-copyright-strip {{
    border-top: 1px solid #151e2e;
    padding-top: 8px;
    text-align: center;
    font-size: 8px;
    color: #64748b;
  }}
  .footer-copyright-strip strong {{
    color: #cbd5e1;
  }}
</style>
</head>
<body>

<div class="canvas-wrapper">

  <!-- Numbered Callout Badges -->
  <div class="badge-pin pin-1">1</div>
  <div class="badge-pin pin-2">2</div>
  <div class="badge-pin pin-3">3</div>
  <div class="badge-pin pin-4">4</div>
  <div class="badge-pin pin-5">5</div>
  <div class="badge-pin pin-6">6</div>
  <div class="badge-pin pin-7">7</div>

  <!-- Main Wireframe Application Frame -->
  <div class="browser-mockup">
    
    <!-- Top Browser Bar -->
    <div class="browser-header">
      <div class="window-dots">
        <div class="dot red"></div>
        <div class="dot yellow"></div>
        <div class="dot green"></div>
      </div>
      <div class="url-bar">
        <span class="secure">[SECURE]</span>
        <span class="site-link">https://jeronopjer-portfolio.vercel.app</span>
        <span class="theme-tag">[DARK THEME ACTIVE]</span>
      </div>
      <div class="version-tag">v1.0.0</div>
    </div>

    <!-- Academic Topbar (from actual website index.html) -->
    <div class="academic-topbar-mock">
      <div>
        <span class="uni-badge-mock"><i class="bi bi-code-slash"></i> Portfolio</span>
        <span><strong>Jeron Opjer</strong> | Web Developer & Digital Solutions</span>
      </div>
      <div class="theme-btn-group">
        <span class="mock-theme-btn active">● Slate</span>
        <span class="mock-theme-btn">○ Charcoal</span>
        <span class="mock-theme-btn">☼ Soft Light</span>
      </div>
    </div>

    <!-- Interior Wireframe Grid -->
    <div class="wireframe-grid">
      
      <!-- ================= LEFT SIDEBAR ================= -->
      <aside class="sidebar-col">
        
        <!-- Profile Identity (Real Data from index.html) -->
        <div class="profile-box">
          <div class="avatar-wrap">
            <img src="{avatar_b64}" alt="Jeron Opjer" class="avatar-img">
            <div class="verified-icon">✓</div>
          </div>
          <div class="profile-name">Jeron Opjer</div>
          <div class="profile-role-pill">Web Developer</div>
          <div class="profile-meta">Silay City, Philippines</div>
          <div class="social-pills">
            <span class="soc-pill">GitHub</span>
            <span class="soc-pill">LinkedIn</span>
            <span class="soc-pill">Email</span>
            <span class="soc-pill">Phone</span>
          </div>
        </div>

        <!-- Real Navigation Stack (from index.html) -->
        <nav class="nav-stack">
          <div class="nav-item active-blue">
            <span><span style="color: #60a5fa; margin-right: 4px;">■</span> Overview</span>
            <span style="color: #60a5fa;">▸</span>
          </div>
          <div class="nav-item"><span>Skills</span></div>
          <div class="nav-item"><span>Featured Projects</span></div>
          <div class="nav-item"><span>About Me</span></div>
          <div class="nav-item"><span>Credentials</span></div>
          <div class="nav-item"><span>Services & Values</span></div>
          <div class="nav-item"><span>Contact</span></div>
        </nav>

        <!-- Real Sidebar Contact Brief (index.html lines 156-170) -->
        <div class="sidebar-contact-card">
          <div class="brief-title">Sidebar Contact Brief</div>
          <div class="brief-list">
            <div class="brief-item">
              <span class="brief-icon">📍</span>
              <span>Silay City, Negros Occ.</span>
            </div>
            <div class="brief-item">
              <span class="brief-icon">✉️</span>
              <span>jeronopjer@gmail.com</span>
            </div>
            <div class="brief-item">
              <span class="brief-icon">📞</span>
              <span>+63 966 964 8147</span>
            </div>
          </div>
        </div>

      </aside>

      <!-- ================= RIGHT MAIN COLUMN ================= -->
      <main class="main-col">
        
        <!-- SECTION 2: Hero Section (Actual Content from index.html) -->
        <section class="hero-card">
          <div class="hero-badge-pill">💻 Web Developer & Digital Solutions Specialist</div>
          <h1 class="hero-title">Building Responsive, User-Friendly <span>Digital Solutions</span></h1>
          <p class="hero-desc">
            To leverage my technical background in web development, database management, and digital document processing to build responsive, user-friendly digital solutions. Dedicated to applying strong problem-solving skills and technical proficiency to contribute effectively to a growing IT and software team.
          </p>
          <div class="hero-actions-row">
            <button class="btn-primary-blue">Get In Touch</button>
            <button class="btn-secondary-dark">Explore Projects</button>
            <button class="btn-secondary-dark">View Resume Details</button>
          </div>
          <div class="hero-stats-strip">
            <div class="stat-block">
              <span class="stat-val">2+</span>
              <span>Years Practical Experience</span>
            </div>
            <div class="stat-block">
              <span class="stat-val">100%</span>
              <span>Responsive & Semantic</span>
            </div>
          </div>
        </section>

        <!-- SECTION: Skills / Daily Drivers (Actual from index.html) -->
        <section class="skills-card">
          <div class="skills-header">
            <span>DAILY DRIVERS</span>
            <strong>Tools I work with:</strong>
          </div>
          <div class="skills-pills-wrap">
            <span class="tool-tag">HTML5</span>
            <span class="tool-tag">CSS3</span>
            <span class="tool-tag">JavaScript</span>
            <span class="tool-tag">Bootstrap 5</span>
            <span class="tool-tag">PHP</span>
            <span class="tool-tag">MySQL</span>
            <span class="tool-tag">PostgreSQL</span>
            <span class="tool-tag">Git</span>
            <span class="tool-tag">Vercel</span>
            <span class="tool-tag">Python</span>
            <span class="tool-tag">Tailwind CSS</span>
            <span class="tool-tag">UI/UX Wireframing</span>
          </div>
        </section>

        <!-- SECTION 3: Projects + About (Actual from index.html) -->
        <div class="grid-2col">
          
          <!-- Projects Card -->
          <div class="proj-card">
            <div>
              <div class="card-label-top">Showcase</div>
              <h2 class="card-h3">Featured Project Preview</h2>
              <div class="proj-tabs-row">
                <span class="tab-btn-mini active">GovSupply Connect</span>
                <span class="tab-btn-mini">Public Project Transparency</span>
              </div>
              <div class="proj-preview-box">
                <img src="{project_b64}" alt="GovSupply Connect Preview">
              </div>
              <div class="proj-title-live">GovSupply Connect: Municipal Procurement System</div>
              <p class="proj-desc-live">
                Municipal Government Portal engineered for the Municipality of E.B. Magalona for procurement transparency, inventory tracking, and audit-ready public accountability.
              </p>
            </div>
            <a href="#" class="btn-arch-detail">View Full Architecture & System Details -></a>
          </div>

          <!-- About Card -->
          <div class="about-card">
            <div>
              <div class="card-label-top" style="color: #60a5fa;">Profile Focus</div>
              <h2 class="card-h3">About Jeron Opjer</h2>
              <p class="about-bio-text">
                Dedicated web developer and digital solutions specialist with solid academic and practical foundations in information systems, civic workflow systems, and modern web application development.
              </p>
              <div class="about-pills-grid">
                <div class="cred-pill-item">✓ Google Certified</div>
                <div class="cred-pill-item">✓ Cyber & Audit</div>
                <div class="cred-pill-item">✓ Silay City LGU</div>
                <div class="cred-pill-item">✓ Frontend & UI/UX</div>
              </div>
            </div>
            <div class="btn-about-modal">
              <span>Read Bio, Mindset & Hobbies</span>
              <span>→</span>
            </div>
          </div>

        </div>

        <!-- ================= SECTION 4: CREDENTIALS (Actual from index.html) ================= -->
        <section class="credentials-section-card">
          <div class="cred-header-strip">
            <div>
              <span class="card-label-top" style="color: #2dd4bf;">Verified Honors</span>
              <h2 style="font-size: 11px; font-weight: 800; color: #f1f5f9;">Credentials & Certifications</h2>
            </div>
            <span style="font-family:'JetBrains Mono'; font-size:7.5px; color:#2dd4bf; border:1px solid #0d9488; padding:2px 6px; border-radius:4px;">
              LinkedIn Certifications ↗
            </span>
          </div>

          <div class="cred-grid-3">
            
            <div class="cert-tile">
              <div class="cert-top-info">
                <span>Google • Coursera</span>
                <span class="cert-verified-tag">✓ Verified</span>
              </div>
              <div class="cert-title-text">Google IT Support Specialization</div>
              <div class="cert-id-tag">
                <span>ID: DSTAYLANSH2V</span>
                <span>📋</span>
              </div>
              <div class="cert-tags-flex">
                <span class="c-tag">SysAdmin</span>
                <span class="c-tag">Linux/Win</span>
                <span class="c-tag">Networking</span>
              </div>
              <div class="cert-verify-link">Verify on Coursera -></div>
            </div>

            <div class="cert-tile">
              <div class="cert-top-info">
                <span>Google • Coursera</span>
                <span class="cert-verified-tag">✓ Verified</span>
              </div>
              <div class="cert-title-text">Google AI Essentials Certificate</div>
              <div class="cert-id-tag">
                <span>ID: YDV4MDT45OD4</span>
                <span>📋</span>
              </div>
              <div class="cert-tags-flex">
                <span class="c-tag">GenAI</span>
                <span class="c-tag">Prompt Eng</span>
                <span class="c-tag">Automation</span>
              </div>
              <div class="cert-verify-link">Verify on Coursera -></div>
            </div>

            <div class="cert-tile">
              <div class="cert-top-info">
                <span>Cybrary Continuing Ed</span>
                <span class="cert-verified-tag">✓ Verified</span>
              </div>
              <div class="cert-title-text">IT Fundamentals: Security</div>
              <div class="cert-id-tag">
                <span>ID: CC-158ee06e</span>
                <span>📋</span>
              </div>
              <div class="cert-tags-flex">
                <span class="c-tag">Security</span>
                <span class="c-tag">Defense</span>
                <span class="c-tag">3 CEUs</span>
              </div>
              <div class="cert-verify-link">View Cybrary Cert -></div>
            </div>

          </div>
        </section>

        <!-- ================= SECTION 5: SERVICES & VALUES (Actual from index.html) ================= -->
        <div class="grid-services-values">
          
          <div class="sv-card">
            <div class="card-label-top" style="color:#38bdf8;">Core Services</div>
            <h2 style="font-size:11px; font-weight:800; color:#f1f5f9; margin-bottom:4px;">Services & Capabilities</h2>
            <div class="sv-list">
              <div class="sv-item">
                <div class="sv-title">Web Application Development</div>
                <div class="sv-desc">Building dynamic, responsive, and mobile-friendly web applications with clean architecture.</div>
              </div>
              <div class="sv-item">
                <div class="sv-title">Database Design & SQL Architecture</div>
                <div class="sv-desc">Relational database schemas with MySQL and PostgreSQL ensuring robust data integrity.</div>
              </div>
              <div class="sv-item">
                <div class="sv-title">UI/UX Wireframing & Prototyping</div>
                <div class="sv-desc">Structured, user-centered interface blueprints translated into accessible code.</div>
              </div>
            </div>
          </div>

          <div class="sv-card">
            <div class="card-label-top" style="color:#fbbf24;">Professional Ethos</div>
            <h2 style="font-size:11px; font-weight:800; color:#f1f5f9; margin-bottom:4px;">Core Values & Principles</h2>
            <div class="sv-list">
              <div class="sv-item">
                <div class="sv-title">Precision & Attention to Detail</div>
                <div class="sv-desc">Dedicated to producing clean code, error-free document processing, and pixel-precise layouts.</div>
              </div>
              <div class="sv-item">
                <div class="sv-title">Problem-Solving Mindset</div>
                <div class="sv-desc">Approaching technical challenges methodically to formulate structured, scalable solutions.</div>
              </div>
              <div class="sv-item">
                <div class="sv-title">Continuous Growth & Integrity</div>
                <div class="sv-desc">Constantly learning modern web standards and demonstrating reliable team communication.</div>
              </div>
            </div>
          </div>

        </div>

        <!-- SECTION 6: Contact & Communication (Actual from index.html) -->
        <section class="contact-section-card">
          <div class="card-label-top" style="color:#38bdf8;">Get in Touch</div>
          <h2 style="font-size:11px; font-weight:800; color:#f1f5f9; margin-bottom:8px;">Contact & Communication</h2>
          <div class="contact-grid">
            <div class="contact-left-box">
              <p style="font-size:8px; color:#94a3b8; line-height:1.4;">
                Open to web development opportunities, internships, freelance projects, and technical roles.
              </p>
              <div class="contact-card-label">
                <span>Email Address:</span>
                <span class="val-bold">jeronopjer@gmail.com</span>
              </div>
              <div class="contact-card-label">
                <span>Phone / Mobile:</span>
                <span class="val-bold">+639669648147</span>
              </div>
              <div class="contact-card-label">
                <span>Location:</span>
                <span>Silay City, Negros Occ.</span>
              </div>
            </div>
            <div class="contact-form-box">
              <div class="c-input">Name: e.g. Maria Santos</div>
              <div class="c-input">Email: e.g. maria@example.com</div>
              <div class="c-input">Subject: Web Development Project / Inquiry</div>
              <div class="btn-submit-live">Send Message</div>
            </div>
          </div>
        </section>

        <!-- ================= SECTION 7: REAL FOOTER (Exact 1:1 from index.html lines 1014-1084) ================= -->
        <footer class="footer-live-card">
          <div class="footer-5col-grid">
            
            <!-- Col 1: Identity -->
            <div>
              <div class="f-col-title">Jeron Opjer</div>
              <p class="f-col-desc">
                Web Developer & Digital Solutions Specialist dedicated to crafting fast, accessible, and user-centric web applications.
              </p>
              <div class="f-loc-tag">Silay City, Negros Occidental</div>
            </div>

            <!-- Col 2: Navigation -->
            <div>
              <div class="f-col-title">Navigation</div>
              <ul class="f-links-list">
                <li>Overview</li>
                <li>Skills</li>
                <li>Featured Projects</li>
                <li>About Me</li>
                <li>Contact Me</li>
              </ul>
            </div>

            <!-- Col 3: Credentials -->
            <div>
              <div class="f-col-title">Credentials</div>
              <ul class="f-links-list">
                <li>Google IT Support</li>
                <li>Google AI Essentials</li>
                <li>ISACA CISA Prep</li>
                <li>Cybrary Security</li>
                <li>Data Analytics</li>
              </ul>
            </div>

            <!-- Col 4: Services -->
            <div>
              <div class="f-col-title">Services</div>
              <ul class="f-links-list">
                <li>Web Development</li>
                <li>UI/UX Wireframing</li>
                <li>Database Management</li>
                <li>Workflow Processing</li>
              </ul>
            </div>

            <!-- Col 5: Connect -->
            <div>
              <div class="f-col-title">Connect</div>
              <ul class="f-links-list">
                <li>jeronopjer@gmail.com</li>
                <li>+63 966 964 8147</li>
                <li>LinkedIn Profile</li>
                <li>GitHub Profile</li>
              </ul>
            </div>

          </div>

          <div class="footer-copyright-strip">
            © 2026 <strong>Jeron A. Opjer</strong>. All Rights Reserved.
          </div>
        </footer>

      </main>

    </div>

  </div>

</div>

</body>
</html>
"""

html_path = r"c:\Users\NITRO\PROFE7\hifi_wireframe_board_v2.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written 100% exact website HTML to {html_path}, length: {len(html_content)}")
