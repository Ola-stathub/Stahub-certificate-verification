import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Certificate Verification | StatHub Datametrics",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Pull cert number from URL — works even with components.html
cert_number = st.query_params.get("cert", "")

cert_line = (
    f'<p class="hero-cert">Certificate No: <strong>{cert_number}</strong></p>'
    if cert_number else ""
)

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<style>
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

  body {{
    font-family: 'Inter', sans-serif;
    background: #F5F7FA;
    color: #1A1A2E;
    padding: 32px 16px 48px;
    min-height: 100vh;
  }}

  .page {{
    max-width: 640px;
    margin: 0 auto;
  }}

  /* ── Hero ── */
  .hero {{
    background: linear-gradient(135deg, #0D2B8E 0%, #123DCE 58%, #2AB7B0 100%);
    border-radius: 20px;
    padding: 48px 36px 44px;
    text-align: center;
    color: #fff;
    box-shadow: 0 20px 60px rgba(18,61,206,0.28);
    margin-bottom: 20px;
  }}
  .hero-icon  {{ font-size: 58px; display: block; margin-bottom: 14px; }}
  .hero-title {{ font-size: 26px; font-weight: 800; margin-bottom: 10px; letter-spacing: -0.4px; }}
  .hero-sub   {{ font-size: 15px; color: rgba(255,255,255,0.82); line-height: 1.6; margin-bottom: 24px; }}
  .hero-cert  {{ font-size: 13px; color: rgba(255,255,255,0.75); margin-bottom: 20px; letter-spacing: 0.5px; }}
  .hero-cert strong {{ color: #fff; font-weight: 700; }}
  .pill {{
    display: inline-block;
    background: rgba(255,255,255,0.16);
    border: 1.5px solid rgba(255,255,255,0.36);
    border-radius: 50px;
    padding: 10px 28px;
    font-size: 14px;
    font-weight: 700;
    color: #fff;
  }}

  /* ── Info card ── */
  .card {{
    background: #fff;
    border: 1.5px solid #E5E9F0;
    border-radius: 16px;
    padding: 32px 32px 28px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.05);
    margin-bottom: 20px;
  }}
  .card-title {{
    font-size: 16px;
    font-weight: 700;
    color: #0D2B8E;
    margin-bottom: 20px;
  }}
  .info-row {{
    display: flex;
    gap: 14px;
    align-items: flex-start;
    margin-bottom: 18px;
  }}
  .info-icon {{ font-size: 19px; flex-shrink: 0; margin-top: 2px; }}
  .info-text {{ font-size: 14px; color: #374151; line-height: 1.65; }}
  .info-text b {{ color: #111827; }}

  .divider {{ border: none; border-top: 1.5px solid #F0F2F5; margin: 22px 0; }}

  /* ── WhatsApp button ── */
  .wa-wrap {{ text-align: center; margin-top: 10px; }}
  .wa-btn {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #25D366;
    color: #fff;
    font-family: 'Inter', sans-serif;
    font-size: 15px;
    font-weight: 700;
    padding: 14px 38px;
    border-radius: 50px;
    text-decoration: none;
    box-shadow: 0 8px 28px rgba(37,211,102,0.38);
    transition: transform 0.15s ease, box-shadow 0.15s ease;
  }}
  .wa-btn:hover {{
    transform: translateY(-2px);
    box-shadow: 0 12px 36px rgba(37,211,102,0.48);
    color: #fff;
  }}

  /* ── Footer ── */
  .footer {{
    text-align: center;
    font-size: 12px;
    color: #9CA3AF;
    line-height: 1.7;
    margin-top: 28px;
  }}
</style>
</head>
<body>
<div class="page">

  <!-- Hero -->
  <div class="hero">
    <span class="hero-icon">🎓</span>
    <p class="hero-title">Certificate of Authenticity</p>
    <p class="hero-sub">
      This document confirms the validity of a certificate<br>
      issued by <strong>StatHub Datametrics Limited</strong>.
    </p>
    {cert_line}
    <div class="pill">✅ &nbsp; Verified &amp; Authentic Certificate</div>
  </div>

  <!-- About -->
  <div class="card">
    <p class="card-title">📋 About This Certificate</p>

    <div class="info-row">
      <span class="info-icon">🏢</span>
      <p class="info-text">
        This certificate was officially issued by
        <b>StatHub Datametrics Limited</b>, a professional data analytics
        and training organisation committed to empowering individuals
        with high-impact data skills.
      </p>
    </div>

    <div class="info-row">
      <span class="info-icon">🔒</span>
      <p class="info-text">
        Each certificate carries a unique certificate number and QR code
        to ensure authenticity. Scanning the QR code on the original
        document redirects here for instant, tamper-proof verification.
      </p>
    </div>

    <div class="info-row">
      <span class="info-icon">🌟</span>
      <p class="info-text">
        StatHub Datametrics certificates recognise genuine achievement
        in our programmes — including completion of training, workshops,
        and project-based learning tracks.
      </p>
    </div>

    <hr class="divider">

    <p class="card-title">📞 Contact &amp; Enquiries</p>

    <div class="info-row">
      <span class="info-icon">💬</span>
      <p class="info-text">
        Have questions about this certificate or want to verify its
        authenticity directly with our team? Reach us instantly on
        WhatsApp — we respond promptly.
      </p>
    </div>

    <div class="wa-wrap">
      <a class="wa-btn"
         href="https://wa.me/2347037095663"
         target="_blank"
         rel="noopener noreferrer">
        💬 &nbsp; Contact Us on WhatsApp
      </a>
    </div>
  </div>

  <!-- Footer -->
  <div class="footer">
    &copy; 2026 <strong>StatHub Datametrics Limited</strong> &nbsp;&middot;&nbsp; All rights reserved.<br>
    Certificate verification powered by StatHub Certificate Studio.
  </div>

</div>
</body>
</html>
"""

# Render via components.html — bypasses Streamlit's HTML sanitiser entirely
components.html(html_content, height=920, scrolling=False)
