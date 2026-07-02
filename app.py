import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Certificate Verification | StatHub Datametrics",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Hide Streamlit chrome */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 680px;
    }

    /* ── Hero card ── */
    .hero-card {
        background: linear-gradient(135deg, #0D2B8E 0%, #123DCE 60%, #2AB7B0 100%);
        border-radius: 20px;
        padding: 48px 40px 40px 40px;
        text-align: center;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 20px 60px rgba(18, 61, 206, 0.25);
    }

    .badge-icon {
        font-size: 64px;
        margin-bottom: 12px;
        display: block;
    }

    .hero-title {
        font-size: 28px;
        font-weight: 800;
        margin: 0 0 8px 0;
        letter-spacing: -0.5px;
    }

    .hero-sub {
        font-size: 15px;
        color: rgba(255,255,255,0.80);
        margin: 0 0 28px 0;
        line-height: 1.5;
    }

    /* ── Valid badge ── */
    .valid-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(255,255,255,0.18);
        border: 1.5px solid rgba(255,255,255,0.35);
        border-radius: 50px;
        padding: 8px 22px;
        font-size: 14px;
        font-weight: 700;
        color: #ffffff;
        backdrop-filter: blur(6px);
    }

    /* ── Info card ── */
    .info-card {
        background: #ffffff;
        border: 1.5px solid #E5E9F0;
        border-radius: 16px;
        padding: 28px 32px;
        margin-bottom: 20px;
        box-shadow: 0 4px 24px rgba(0,0,0,0.05);
    }

    .info-card h3 {
        color: #0D2B8E;
        font-size: 16px;
        font-weight: 700;
        margin: 0 0 16px 0;
    }

    .info-row {
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-bottom: 14px;
    }

    .info-icon {
        font-size: 18px;
        flex-shrink: 0;
        margin-top: 1px;
    }

    .info-text {
        font-size: 14px;
        color: #374151;
        line-height: 1.55;
    }

    .info-text strong {
        color: #111827;
    }

    /* ── Divider ── */
    .divider {
        border: none;
        border-top: 1.5px solid #F0F2F5;
        margin: 20px 0;
    }

    /* ── WhatsApp button ── */
    .wa-btn-wrap {
        text-align: center;
        margin-top: 8px;
    }

    .wa-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: #25D366;
        color: #ffffff !important;
        font-size: 15px;
        font-weight: 700;
        padding: 14px 36px;
        border-radius: 50px;
        text-decoration: none !important;
        box-shadow: 0 8px 24px rgba(37, 211, 102, 0.35);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .wa-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 32px rgba(37, 211, 102, 0.45);
    }

    .wa-icon {
        font-size: 20px;
    }

    /* ── Footer ── */
    .page-footer {
        text-align: center;
        font-size: 12px;
        color: #9CA3AF;
        margin-top: 28px;
        line-height: 1.6;
    }

    .page-footer a {
        color: #123DCE;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Cert number from query param ──────────────────────────────────────────
query_params = st.query_params
cert_number = query_params.get("cert", None)

# ── Hero card ─────────────────────────────────────────────────────────────
cert_display = f"<br><span style='font-size:13px;opacity:0.85;font-weight:500;letter-spacing:1px;'>{cert_number}</span>" if cert_number else ""

st.markdown(
    f"""
    <div class="hero-card">
        <span class="badge-icon">🎓</span>
        <p class="hero-title">Certificate of Authenticity</p>
        <p class="hero-sub">
            This document confirms the validity of a certificate<br>
            issued by <strong>StatHub Datametrics Limited</strong>.{cert_display}
        </p>
        <div class="valid-badge">
            ✅ &nbsp; Verified &amp; Authentic Certificate
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Info card ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="info-card">
        <h3>📋 About This Certificate</h3>

        <div class="info-row">
            <span class="info-icon">🏢</span>
            <p class="info-text">
                This certificate was officially issued by
                <strong>StatHub Datametrics Limited</strong>, a professional
                data analytics and training organisation committed to empowering
                individuals with high-impact data skills.
            </p>
        </div>

        <div class="info-row">
            <span class="info-icon">🔒</span>
            <p class="info-text">
                Each certificate carries a unique certificate number and QR code
                to ensure authenticity. Scanning the QR code on the original
                document should redirect here for instant verification.
            </p>
        </div>

        <div class="info-row">
            <span class="info-icon">🌟</span>
            <p class="info-text">
                StatHub Datametrics certificates recognise genuine achievement
                in our programmes, including completion of training, workshops,
                and project-based learning tracks.
            </p>
        </div>

        <hr class="divider">

        <h3>📞 Contact &amp; Enquiries</h3>

        <div class="info-row">
            <span class="info-icon">💬</span>
            <p class="info-text">
                Have questions about this certificate or want to verify its
                authenticity directly with our team? Reach us instantly on
                WhatsApp — we respond promptly.
            </p>
        </div>

        <div class="wa-btn-wrap">
            <a class="wa-btn"
               href="https://wa.me/2347037095663"
               target="_blank"
               rel="noopener noreferrer">
                <span class="wa-icon">💬</span>
                Contact Us on WhatsApp
            </a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Footer ────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="page-footer">
        © 2026 <strong>StatHub Datametrics Limited</strong> · All rights reserved.<br>
        Certificate verification system powered by StatHub Certificate Studio.
    </div>
    """,
    unsafe_allow_html=True,
)
