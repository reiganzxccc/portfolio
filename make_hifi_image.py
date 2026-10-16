import base64
import os
import subprocess

def get_b64(path, mime):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:{mime};base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

avatar_b64 = get_b64(r"c:\Users\NITRO\PROFE7\assets\profile_photo.jpg", "image/jpeg")
project_b64 = get_b64(r"c:\Users\NITRO\PROFE7\assets\govsupply_connect.png", "image/png")
cert_b64 = get_b64(r"C:\Users\NITRO\.gemini\antigravity-ide\brain\6be15b9e-35b8-446a-93fe-83cb646ff231\coursera_cert_1_1791980073925.png", "image/png")

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>HI-FI Wireframe Architecture - Jeron Opjer Portfolio</title>
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
      linear-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,0.03) 1px, transparent 1px);
    background-size: 24px 24px;
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    color: #e2e8f0;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    padding: 24px 20px 40px;
    min-height: 100vh;
  }}

  /* Main Wireframe Canvas Container */
  .canvas-wrapper {{
    position: relative;
    width: 1000px;
    max-width: 1000px;
  }}

  .browser-mockup {{
    background: #0c121d;
    border-radius: 16px;
    border: 1px solid #1e293b;
    box-shadow: 0 25px 60px -15px rgba(0,0,0,0.8), 0 0 0 1px rgba(255,255,255,0.05);
    overflow: visible;
    position: relative;
  }}

  /* Top Browser Bar */
  .browser-header {{
    background: #090e17;
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
    background: #111a28;
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
  .url-bar .theme-tag {{ color: #f97316; font-weight: 600; }}

  .version-tag {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    color: #64748b;
  }}

  /* Main Two-Column Layout */
  .wireframe-grid {{
    display: grid;
    grid-template-columns: 270px 1fr;
    gap: 14px;
    padding: 16px;
  }}

  /* Numbered Annotations Badge */
  .badge-pin {{
    position: absolute;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: #ea580c;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 0 2px #0c121d, 0 2px 6px rgba(234, 88, 12, 0.6);
    z-index: 50;
  }}
  .pin-1 {{ top: 200px; left: -11px; }}
  .pin-2 {{ top: 58px; right: -11px; }}
  .pin-3 {{ top: 310px; right: -11px; }}
  .pin-4 {{ top: 560px; right: -11px; }}
  .pin-5 {{ top: 780px; right: -11px; }}
  .pin-6 {{ bottom: 80px; right: -11px; }}

  /* Generic Card Styles */
  .wf-card {{
    background: #0f1726;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 14px;
    position: relative;
  }}
  .border-orange {{
    border-color: #ea580c !important;
  }}
  .border-blue {{
    border-color: #3b82f6 !important;
  }}

  /* ================= LEFT SIDEBAR ================= */
  .sidebar-col {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  .profile-box {{
    background: #0f1726;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 16px 12px;
    text-align: center;
  }}
  .avatar-wrap {{
    position: relative;
    width: 84px;
    height: 84px;
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
    width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 11px;
    border: 2px solid #0f1726;
  }}
  .profile-name {{
    font-size: 14px;
    font-weight: 800;
    color: #f8fafc;
    margin-bottom: 2px;
    letter-spacing: -0.2px;
  }}
  .profile-tag {{
    font-size: 10px;
    color: #94a3b8;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 4px;
  }}
  .profile-role {{
    font-size: 9px;
    font-weight: 700;
    color: #60a5fa;
    text-transform: uppercase;
    letter-spacing: 0.6px;
    margin-bottom: 12px;
  }}
  .social-pills {{
    display: flex;
    justify-content: center;
    gap: 6px;
  }}
  .soc-pill {{
    background: #1e293b;
    border: 1px solid #334155;
    color: #cbd5e1;
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
    background: #111a28;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 11px;
    color: #94a3b8;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-weight: 600;
    font-family: 'Plus Jakarta Sans', sans-serif;
  }}
  .nav-item.active {{
    background: #ea580c;
    border-color: #ea580c;
    color: #ffffff;
    font-weight: 700;
  }}
  .nav-bullet {{
    color: #ea580c;
    font-size: 10px;
    margin-right: 4px;
  }}
  .nav-item.active .nav-bullet {{
    color: #ffffff;
  }}

  /* Status Card */
  .status-box {{
    background: #09131a;
    border: 1px solid #0f766e;
    border-radius: 8px;
    padding: 9px 12px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }}
  .status-left {{
    display: flex;
    align-items: center;
    gap: 8px;
  }}
  .status-dot {{
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #10b981;
    box-shadow: 0 0 8px #10b981;
  }}
  .status-title {{
    font-size: 10px;
    font-weight: 800;
    color: #34d399;
    letter-spacing: 0.4px;
  }}
  .status-sub {{
    font-size: 8px;
    color: #64748b;
  }}
  .status-badge {{
    background: rgba(16, 185, 129, 0.15);
    color: #10b981;
    font-size: 8px;
    font-weight: 700;
    padding: 2px 5px;
    border-radius: 4px;
    border: 1px solid #059669;
  }}

  /* Specs Card */
  .specs-box {{
    background: #0a111a;
    border: 1px dashed #1e3a5f;
    border-radius: 8px;
    padding: 10px;
  }}
  .specs-title {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
    font-weight: 700;
    color: #38bdf8;
    margin-bottom: 6px;
    text-transform: uppercase;
  }}
  .specs-list {{
    list-style: none;
    font-size: 9px;
    color: #94a3b8;
    display: flex;
    flex-direction: column;
    gap: 3px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .specs-list li::before {{
    content: "• ";
    color: #38bdf8;
  }}

  /* ================= RIGHT MAIN COLUMN ================= */
  .main-col {{
    display: flex;
    flex-direction: column;
    gap: 12px;
  }}

  /* SECTION 2: Hero Architecture */
  .hero-card {{
    background: #0f1726;
    border: 1px solid #ea580c;
    border-radius: 10px;
    padding: 16px 18px;
    position: relative;
  }}
  .arch-tag {{
    display: inline-block;
    border: 1px solid #b45309;
    background: rgba(245, 158, 11, 0.08);
    color: #f59e0b;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 4px;
    margin-bottom: 8px;
  }}
  .hero-top-row {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 16px;
    margin-bottom: 12px;
  }}
  .hero-headline {{
    font-size: 19px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.3px;
    line-height: 1.25;
  }}
  .hero-sub {{
    font-size: 10.5px;
    color: #94a3b8;
    line-height: 1.45;
    margin-top: 4px;
    max-width: 480px;
  }}
  .btn-orange {{
    background: #ea580c;
    color: #ffffff;
    font-size: 11px;
    font-weight: 800;
    padding: 9px 18px;
    border-radius: 6px;
    border: none;
    cursor: pointer;
    white-space: nowrap;
    box-shadow: 0 4px 14px rgba(234, 88, 12, 0.4);
    letter-spacing: 0.3px;
  }}
  .stack-strip {{
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
    border-top: 1px solid #1e293b;
    padding-top: 10px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9px;
  }}
  .stack-label {{
    color: #64748b;
    font-weight: 700;
    font-size: 8.5px;
    margin-right: 4px;
  }}
  .tech-pill {{
    background: #172338;
    border: 1px solid #2d3f5e;
    color: #93c5fd;
    padding: 2.5px 7px;
    border-radius: 4px;
    font-weight: 600;
  }}

  /* SECTION 3: Projects + About */
  .grid-2col {{
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 12px;
  }}
  .proj-card {{
    background: #0f1726;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .card-top {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
  }}
  .section-tag-title {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 800;
    color: #38bdf8;
    text-transform: uppercase;
  }}
  .badge-btn {{
    background: #ea580c;
    color: #fff;
    font-size: 8.5px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 4px;
  }}
  .proj-preview-box {{
    background: #080d14;
    border: 1px solid #1e293b;
    border-radius: 6px;
    overflow: hidden;
    position: relative;
    height: 120px;
    margin-bottom: 8px;
  }}
  .proj-preview-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .proj-stats-row {{
    display: flex;
    gap: 5px;
    margin-bottom: 8px;
  }}
  .stat-pill {{
    flex: 1;
    background: #111e30;
    border: 1px solid #1e3a5f;
    padding: 4px 6px;
    border-radius: 4px;
    text-align: center;
    font-size: 8px;
    font-family: 'JetBrains Mono', monospace;
    color: #38bdf8;
    font-weight: 600;
  }}
  .proj-footer-link {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8.5px;
    color: #64748b;
    border-top: 1px solid #17253b;
    padding-top: 6px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .proj-footer-link a {{
    color: #ea580c;
    font-weight: 700;
    text-decoration: none;
  }}

  /* About Box */
  .about-card {{
    background: #0f1726;
    border: 1px solid #b45309;
    border-radius: 10px;
    padding: 12px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .about-inner-frame {{
    background: #090e17;
    border: 1px solid #78350f;
    border-radius: 6px;
    padding: 10px;
    text-align: center;
    margin-bottom: 8px;
  }}
  .about-title {{
    font-size: 11px;
    font-weight: 800;
    color: #fbbf24;
    margin-bottom: 2px;
    letter-spacing: 0.3px;
  }}
  .about-role {{
    font-size: 8.5px;
    color: #94a3b8;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 6px;
  }}
  .about-desc {{
    font-size: 9px;
    color: #cbd5e1;
    line-height: 1.4;
  }}
  .about-values-text {{
    font-size: 8.5px;
    color: #94a3b8;
    line-height: 1.35;
    margin-bottom: 6px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .about-link {{
    font-size: 8.5px;
    color: #f97316;
    font-weight: 700;
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
  }}

  /* SECTION 4: 3 Columns */
  .grid-3col {{
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 10px;
  }}
  .col-card {{
    background: #0f1726;
    border: 1px solid #1e293b;
    border-radius: 10px;
    padding: 11px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .cert-img-box {{
    background: #090e17;
    border: 1px solid #1e293b;
    border-radius: 6px;
    height: 52px;
    overflow: hidden;
    margin-bottom: 7px;
  }}
  .cert-img-box img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .mini-item-list {{
    list-style: none;
    font-size: 8.5px;
    display: flex;
    flex-direction: column;
    gap: 4px;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 8px;
  }}
  .mini-item-list li {{
    display: flex;
    justify-content: space-between;
    color: #cbd5e1;
  }}
  .mini-item-list .verified-tag {{
    color: #10b981;
    font-weight: 700;
  }}
  .mini-card-btn {{
    font-size: 8px;
    color: #f97316;
    font-weight: 700;
    text-align: right;
    font-family: 'JetBrains Mono', monospace;
  }}

  /* SECTION 5: Contact */
  .contact-card {{
    background: #0f1726;
    border: 1px solid #1e3a5f;
    border-radius: 10px;
    padding: 14px;
  }}
  .contact-header {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 10px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 12px;
  }}
  .contact-grid {{
    display: grid;
    grid-template-columns: 1fr 1.25fr;
    gap: 16px;
    align-items: center;
  }}
  .channel-box {{
    display: flex;
    flex-direction: column;
    gap: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 9.5px;
  }}
  .channel-label {{
    color: #64748b;
    font-size: 8.5px;
    font-weight: 700;
    margin-bottom: 2px;
  }}
  .channel-val {{
    color: #cbd5e1;
  }}
  .channel-val span {{
    color: #38bdf8;
    font-weight: 700;
  }}
  .btn-blue-outline {{
    margin-top: 6px;
    background: #0369a1;
    border: 1px solid #0284c7;
    color: #ffffff;
    font-size: 9.5px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 5px;
    cursor: pointer;
    text-align: center;
    font-family: 'JetBrains Mono', monospace;
  }}

  /* Mockup Form */
  .mock-form {{
    display: flex;
    flex-direction: column;
    gap: 6px;
  }}
  .mock-input {{
    background: #0a111a;
    border: 1px solid #1e293b;
    border-radius: 5px;
    padding: 6px 10px;
    font-size: 9px;
    color: #64748b;
    font-family: 'JetBrains Mono', monospace;
  }}
  .btn-submit-orange {{
    background: #ea580c;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 7px 12px;
    font-size: 10px;
    font-weight: 800;
    cursor: pointer;
    text-align: center;
    letter-spacing: 0.3px;
  }}

  /* SECTION 6: Sitemap Footer */
  .footer-card {{
    background: #0a1019;
    border: 1px solid #78350f;
    border-radius: 10px;
    padding: 12px 14px;
  }}
  .footer-top-strip {{
    display: flex;
    justify-content: space-between;
    font-size: 9.5px;
    font-family: 'JetBrains Mono', monospace;
    color: #f97316;
    margin-bottom: 8px;
    font-weight: 700;
  }}
  .sitemap-outer-box {{
    background: #06090e;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 10px 12px;
    margin-bottom: 10px;
  }}
  .sitemap-heading {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 8.5px;
    font-weight: 700;
    color: #f97316;
    margin-bottom: 8px;
    text-transform: uppercase;
  }}
  .sitemap-cols {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 8px;
  }}
  .sm-col-box {{
    background: #0d1522;
    border: 1px solid #1a2538;
    border-radius: 4px;
    padding: 6px;
  }}
  .sm-col-head {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 7.5px;
    font-weight: 800;
    color: #38bdf8;
    margin-bottom: 4px;
    text-transform: uppercase;
    border-bottom: 1px solid #1a2538;
    padding-bottom: 3px;
  }}
  .sm-col-links {{
    list-style: none;
    font-size: 7px;
    color: #94a3b8;
    display: flex;
    flex-direction: column;
    gap: 2.5px;
    font-family: 'JetBrains Mono', monospace;
  }}
  .footer-bottom-line {{
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 8px;
    color: #64748b;
    font-family: 'JetBrains Mono', monospace;
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

    <!-- Interior Wireframe Grid -->
    <div class="wireframe-grid">
      
      <!-- ================= LEFT SIDEBAR ================= -->
      <aside class="sidebar-col">
        
        <!-- Profile Identity Card -->
        <div class="profile-box border-blue">
          <div class="avatar-wrap">
            <img src="{avatar_b64}" alt="Jeron Opjer" class="avatar-img">
            <div class="verified-icon">✓</div>
          </div>
          <div class="profile-name">Jeron A. Opjer</div>
          <div class="profile-tag">@jeronopjer • 2026</div>
          <div class="profile-role">Web Architect & Solutions</div>
          <div class="social-pills">
            <span class="soc-pill">GH</span>
            <span class="soc-pill">IN</span>
            <span class="soc-pill">Mail</span>
            <span class="soc-pill">PDF</span>
          </div>
        </div>

        <!-- Navigation Stack -->
        <nav class="nav-stack">
          <div class="nav-item" style="border: 1.5px solid #4f7bf5; color: #ffffff; background: rgba(79, 123, 245, 0.22); box-shadow: 0 0 16px rgba(79, 123, 245, 0.4), inset 0 0 8px rgba(79, 123, 245, 0.15); font-weight: 700;">
            <span><span style="color: #60a5fa; margin-right: 4px;">■</span> Home / Overview</span>
            <span style="color: #60a5fa;">▸</span>
          </div>
          <div class="nav-item">
            <span>[01] Skills & Stack [12]</span>
          </div>
          <div class="nav-item">
            <span>[02] Featured Projects [3]</span>
          </div>
          <div class="nav-item">
            <span>[03] About & Bio</span>
          </div>
          <div class="nav-item">
            <span>[04] Credentials [6]</span>
          </div>
          <div class="nav-item">
            <span>[05] Services & Ethos</span>
          </div>
          <div class="nav-item">
            <span>[06] Contact & Hire</span>
          </div>
        </nav>

        <!-- Availability Status Indicator -->
        <div class="status-box">
          <div class="status-left">
            <div class="status-dot"></div>
            <div>
              <div class="status-title">AVAILABLE FOR HIRE</div>
              <div class="status-sub">Quezon City, PH • Fast Response</div>
            </div>
          </div>
          <span class="status-badge">ACTIVE</span>
        </div>

        <!-- Wireframe Technical Spec Blueprint Box -->
        <div class="specs-box">
          <div class="specs-title">COMPONENT / SYSTEM SPEC</div>
          <ul class="specs-list">
            <li>Fluid 1920px Desktop Width</li>
            <li>Accessible WCAG 2.1 AA</li>
            <li>Modular Overlay Handlers</li>
            <li>High-Contrast Dark Palette</li>
            <li>Zero External CSS Bloat</li>
            <li>Full Vercel Edge Cache</li>
            <li>Real-time Interactive Canvas</li>
          </ul>
        </div>

      </aside>

      <!-- ================= RIGHT MAIN COLUMN ================= -->
      <main class="main-col">
        
        <!-- SECTION 2: Hero Architecture Banner -->
        <section class="hero-card">
          <div class="arch-tag">[1x FULL-STACK WEB ARCHITECTURE & DIGITAL SOLUTIONS]</div>
          <div class="hero-top-row">
            <div>
              <h1 class="hero-headline">DESIGNED WITH INTENT. BUILT TO SCALE.</h1>
              <p class="hero-sub">From dynamic front-end interaction to resilient backend logic & secure data pipelines. Engineer high-performance web solutions built for longevity and real-world impact.</p>
            </div>
            <button class="btn-orange">Get in Touch -></button>
          </div>
          <div class="stack-strip">
            <span class="stack-label">DAILY STACK:</span>
            <span class="tech-pill">HTML5</span>
            <span class="tech-pill">CSS3</span>
            <span class="tech-pill">JavaScript ES6+</span>
            <span class="tech-pill">Bootstrap 5.3</span>
            <span class="tech-pill">PHP / MVC</span>
            <span class="tech-pill">MySQL</span>
            <span class="tech-pill">REST APIs</span>
            <span class="tech-pill">Git / CI-CD</span>
          </div>
        </section>

        <!-- SECTION 3: Featured Projects & About Row -->
        <div class="grid-2col">
          
          <!-- Projects Card -->
          <div class="proj-card">
            <div class="card-top">
              <span class="section-tag-title">FEATURED PROJECTS: #projects</span>
              <span class="badge-btn">Featured [01/03]</span>
            </div>
            <div class="proj-preview-box">
              <img src="{project_b64}" alt="GovSupply Connect Preview">
            </div>
            <div class="proj-stats-row">
              <div class="stat-pill">Efficiency: 94%</div>
              <div class="stat-pill">Audit: Zone 1</div>
              <div class="stat-pill">Records: 1,420+</div>
            </div>
            <div class="proj-footer-link">
              <span>Stack: PHP · MySQL · Bootstrap · REST</span>
              <a href="#">Inspect Architecture -></a>
            </div>
          </div>

          <!-- About Card -->
          <div class="about-card">
            <div class="card-top">
              <span class="section-tag-title" style="color: #f59e0b;">ABOUT & ETHOS: #about</span>
            </div>
            <div class="about-inner-frame">
              <div class="about-title">JERON A. OPJER</div>
              <div class="about-role">"Web Architect & Solutions Specialist"</div>
              <div class="about-desc">Passionate about full-stack engineering, clean intuitive human interfaces, and robust data persistence.</div>
            </div>
            <div class="about-values-text">
              Values: Clean Code • Resilient Logic • Continuous Deployment • Zero Bloat
            </div>
            <div class="about-link">Read Full Bio Modal -></div>
          </div>

        </div>

        <!-- SECTION 4: Credentials, Services, Values (3-Column) -->
        <div class="grid-3col">
          
          <!-- Credentials -->
          <div class="col-card" style="border-color: #0d9488;">
            <div>
              <div class="card-top" style="margin-bottom:6px;">
                <span class="section-tag-title" style="color: #2dd4bf;">VERIFIED CREDENTIALS: [6]</span>
              </div>
              <div class="cert-img-box">
                <img src="{cert_b64}" alt="Credential Badges">
              </div>
              <ul class="mini-item-list">
                <li><span>[1] Google Cyber Pro</span> <span class="verified-tag">✓ Verified</span></li>
                <li><span>[2] Cloud Data Analytics</span> <span class="verified-tag">✓ Verified</span></li>
                <li><span>[3] Cyber Foundations</span> <span class="verified-tag">✓ Verified</span></li>
                <li><span>[4] Enterprise Cloud IT</span> <span class="verified-tag">✓ Verified</span></li>
              </ul>
            </div>
            <div class="mini-card-btn" style="color: #2dd4bf;">[6 ACTIVE VERIFIED BADGES]</div>
          </div>

          <!-- Services -->
          <div class="col-card" style="border-color: #0284c7;">
            <div>
              <div class="card-top" style="margin-bottom:6px;">
                <span class="section-tag-title" style="color: #38bdf8;">SERVICES: [3 Core Pillars]</span>
              </div>
              <ul class="mini-item-list" style="margin-top: 4px; gap: 7px;">
                <li><span>01 Frontend Web & UX</span> <span style="color:#64748b;">Tailored UI</span></li>
                <li><span>02 Backend & Data Logic</span> <span style="color:#64748b;">PHP / MySQL</span></li>
                <li><span>03 Web Hardening & SEO</span> <span style="color:#64748b;">Audits</span></li>
                <li><span>04 Responsive Architecture</span> <span style="color:#64748b;">Bootstrap</span></li>
              </ul>
            </div>
            <div class="mini-card-btn" style="color: #38bdf8;">Request Custom Build -></div>
          </div>

          <!-- Mindset & Values -->
          <div class="col-card" style="border-color: #d97706;">
            <div>
              <div class="card-top" style="margin-bottom:6px;">
                <span class="section-tag-title" style="color: #fbbf24;">MINDSET & VALUES: [Ethos]</span>
              </div>
              <ul class="mini-item-list" style="margin-top: 4px; gap: 7px;">
                <li><span>P1 Craft / Hypertrophy</span> <span style="color:#64748b;">Clean Code</span></li>
                <li><span>P2 Ultimate Rigor</span> <span style="color:#64748b;">Security</span></li>
                <li><span>P3 Radical Growth</span> <span style="color:#64748b;">Velocity</span></li>
                <li><span>P4 User Empathy</span> <span style="color:#64748b;">Inclusive</span></li>
              </ul>
            </div>
            <div class="mini-card-btn" style="color: #fbbf24;">Explore Engineering Ethos -></div>
          </div>

        </div>

        <!-- SECTION 5: Contact Card -->
        <section class="contact-card">
          <div class="contact-header">SECTION: #contact (Direct Communication & Inquiries)</div>
          <div class="contact-grid">
            <div class="channel-box">
              <div class="channel-label">Direct Channels:</div>
              <div class="channel-val"><span>[MAIL]:</span> jeronopjer@gmail.com</div>
              <div class="channel-val"><span>[TEL]:</span> +63 966 964 8147</div>
              <div class="channel-val"><span>[LOC]:</span> Quezon City, Philippines</div>
              <div class="btn-blue-outline">[x] Copy Email to Clipboard</div>
            </div>
            <div class="mock-form">
              <div class="mock-input">Your Name / Org Unit</div>
              <div class="mock-input">Email Address: client@company.com</div>
              <div class="mock-input">Message: Describe project scope, timeline & requirements...</div>
              <div class="btn-submit-orange">Send Email Directly to Jeron -></div>
            </div>
          </div>
        </section>

        <!-- SECTION 6: Site Directory & Sitemap Footer -->
        <footer class="footer-card">
          <div class="footer-top-strip">
            <span>Jeron A. Opjer | Web Author & Full-Stack | [ACTIVE] Open to Work</span>
            <span>Get in Touch [^ Top]</span>
          </div>
          <div class="sitemap-outer-box">
            <div class="sitemap-heading">[SITEMAP] SITE DIRECTORY & STRUCTURAL SITEMAP (5 Interactive Columns)</div>
            <div class="sitemap-cols">
              <div class="sm-col-box">
                <div class="sm-col-head">1. Main Pages</div>
                <ul class="sm-col-links">
                  <li>• Overview</li>
                  <li>• Skills</li>
                  <li>• Projects</li>
                  <li>• About</li>
                  <li>• Credentials</li>
                  <li>• Services</li>
                  <li>• Values</li>
                  <li>• Contact</li>
                </ul>
              </div>
              <div class="sm-col-box">
                <div class="sm-col-head">2. Projects</div>
                <ul class="sm-col-links">
                  <li>• GovSupply Connect</li>
                  <li>• Public Transparency</li>
                  <li>• Web Platform</li>
                  <li>• Student Hub</li>
                  <li>• Cloud Engine</li>
                </ul>
              </div>
              <div class="sm-col-box">
                <div class="sm-col-head">3. Credentials</div>
                <ul class="sm-col-links">
                  <li>• Google Cyber</li>
                  <li>• Cloud Security</li>
                  <li>• Foundations</li>
                  <li>• Agile Mgmt</li>
                  <li>• Full Stack</li>
                </ul>
              </div>
              <div class="sm-col-box">
                <div class="sm-col-head">4. Services</div>
                <ul class="sm-col-links">
                  <li>• UI Frontend</li>
                  <li>• Backend PHP</li>
                  <li>• Relational DB</li>
                  <li>• Web Hardening</li>
                  <li>• Prototyping</li>
                </ul>
              </div>
              <div class="sm-col-box">
                <div class="sm-col-head">5. Connect</div>
                <ul class="sm-col-links">
                  <li>• jeronopjer@gmail</li>
                  <li>• +63 966 964</li>
                  <li>• LinkedIn /in</li>
                  <li>• GitHub /reigan</li>
                  <li>• Resume PDF</li>
                </ul>
              </div>
            </div>
          </div>
          <div class="footer-bottom-line">
            <span>© 2026 Jeron A. Opjer. All rights reserved. • HTML5 / CSS3 / Vanilla JS • Bootstrap 5.3</span>
            <span>Deployed on Vercel Edge Network [27]</span>
          </div>
        </footer>

      </main>

    </div>

  </div>

</div>

</body>
</html>
"""

html_path = r"c:\Users\NITRO\PROFE7\hifi_wireframe_board.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Written HTML to {html_path}, length: {len(html_content)}")
