import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="RenewAI",
    page_icon="🌱",
    layout="wide"
)

# -------------------------------------------------
# CUSTOM CSS (ANIMATIONS + STYLE)
# -------------------------------------------------
st.markdown("""
<style>
.fade-in {
    animation: fadeIn 1.3s ease-in;
}
.slide-up {
    animation: slideUp 1.1s ease-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes slideUp {
    from { opacity: 0; transform: translateY(35px); }
    to { opacity: 1; transform: translateY(0); }
}

/* FIXED CARD STYLE */
.card {
    padding: 20px;
    border-radius: 14px;
    background: #f5f7fa;
    box-shadow: 0 8px 22px rgba(0,0,0,0.15);
    color: #111111;        /* 🔥 THIS FIXES IT */
}

.card h4 {
    color: #0f2027;        /* dark heading */
}

.card p {
    color: #333333;        /* readable text */
}
</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# HERO SECTION
# -------------------------------------------------
st.markdown("""
<div class="fade-in" style="
padding:30px;
border-radius:16px;
background:linear-gradient(90deg,#0f2027,#203a43,#2c5364);
">
    <h1 style="color:white;margin-bottom:5px;">🌱 RenewAI</h1>
    <h4 style="color:#d1f7ff;margin-top:0;">
        AI-Driven Renewable Energy Forecasting & Sustainability Dashboard
    </h4>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# METRICS (DASHBOARD FEEL)
# -------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("⚡ Energy Sources", "3", "Solar • Wind • Hydro")
col2.metric("📊 AI Modules", "5")
col3.metric("🌍 Focus Area", "Sustainability")
col4.metric("🧠 ML Ready", "Yes")

st.markdown("---")

# -------------------------------------------------
# PLATFORM OVERVIEW
# -------------------------------------------------
st.markdown("## 🔍 Platform Overview")

st.markdown("""
**RenewAI** is an intelligent analytics platform designed to help  
governments, energy planners, and sustainability teams understand and
optimize **renewable energy generation and environmental impact**.

This version demonstrates:
- Interactive frontend structure
- Smooth animations & UI flow
- Modular design for AI integration
""")

st.markdown("---")

# -------------------------------------------------
# CORE MODULES (ANIMATED CARDS)
# -------------------------------------------------
st.markdown("## ⚙️ Core Analytical Modules")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card slide-up">
        <h4>🔆 Solar Forecasting</h4>
        <p>Estimate solar energy generation using environmental parameters.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card slide-up">
        <h4>🌬️ Wind Forecasting</h4>
        <p>Analyze wind-based energy potential and trends.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card slide-up">
        <h4>💧 Hydro Forecasting</h4>
        <p>Assess hydroelectric power generation feasibility.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c4, c5 = st.columns(2)

with c4:
    st.markdown("""
    <div class="card slide-up">
        <h4>🏭 Plant Health Analysis</h4>
        <p>Evaluate plant efficiency, losses, and operational health.</p>
    </div>
    """, unsafe_allow_html=True)

with c5:
    st.markdown("""
    <div class="card slide-up">
        <h4>🌍 CO₂ Emission Reduction</h4>
        <p>Estimate carbon emission savings from renewable adoption.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------
# INSTRUCTION SECTION
# -------------------------------------------------
st.markdown("---")
st.info("👈 Use the **sidebar** to select a module and explore its interface.")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.markdown("---")
st.caption("© 2025 RenewAI | Interactive Streamlit Dashboard Prototype")
