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

/* CARD STYLE */
.card {
    padding: 20px;
    border-radius: 14px;
    background: #f5f7fa;
    box-shadow: 0 8px 22px rgba(0,0,0,0.15);
    color: #111111;
}

.card h4 {
    color: #0f2027;
}

.card p {
    color: #333333;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SIDEBAR (HIERARCHICAL NAVIGATION)
# -------------------------------------------------
st.sidebar.title("🌱 RenewAI")

main_menu = st.sidebar.radio(
    "Navigation",
    ["📊 Dashboard", "👨‍💻 Developers"]
)

st.sidebar.markdown("---")

# -------------------------------------------------
# DASHBOARD ROUTING
# -------------------------------------------------
if main_menu == "📊 Dashboard":

    sub_menu = st.sidebar.radio(
        "Dashboard Modules",
        [
            "🏠 Dashboard Home",
            "🔮 Energy Forecasting",
            "⚡ Energy Consumption",
            "🌍 Site Suitability",
            "🏭 Plant Performance",
            "♻️ CO₂ Reduction"
        ]
    )

    # -------------------------------------------------
    # DASHBOARD HOME (YOUR ORIGINAL UI)
    # -------------------------------------------------
    if sub_menu == "🏠 Dashboard Home":

        # HERO SECTION
        st.markdown("""
        <div class="fade-in" style="
        padding:30px;
        border-radius:16px;
        background:linear-gradient(90deg,#0f2027,#203a43,#2c5364);
        ">
            <h1 style="color:white;margin-bottom:5px;">🌱 RenewAI</h1>
            <h4 style="color:#d1f7ff;margin-top:0;">
                AI-Driven Renewable Energy Analytics & Sustainability Dashboard
            </h4>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # METRICS
        col1, col2, col3, col4 = st.columns(4)

        col1.metric("⚡ Energy Sources", "3", "Solar • Wind • Hydro")
        col2.metric("📊 Analytical Modules", "5")
        col3.metric("🌍 Focus Area", "Sustainability")
        col4.metric("🧠 ML Enabled", "Yes")

        st.markdown("---")

        # OVERVIEW
        st.markdown("## 🔍 Platform Overview")

        st.markdown("""
        **RenewAI** is an intelligent analytics platform designed to help  
        governments, energy planners, and sustainability teams analyze and
        optimize **renewable energy generation, consumption, and environmental impact**.

        This dashboard demonstrates:
        - Clean, interactive UI with animations
        - Modular analytical architecture
        - Hybrid ML + rule-based intelligence
        """)

        st.markdown("---")

        # CORE MODULE CARDS
        st.markdown("## ⚙️ Core Analytical Modules")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown("""
            <div class="card slide-up">
                <h4>🔮 Energy Forecasting</h4>
                <p>Predict total renewable energy generation using hybrid analytics.</p>
            </div>
            """, unsafe_allow_html=True)

        with c2:
            st.markdown("""
            <div class="card slide-up">
                <h4>⚡ Energy Consumption</h4>
                <p>Analyze state-wise and regional energy consumption patterns.</p>
            </div>
            """, unsafe_allow_html=True)

        with c3:
            st.markdown("""
            <div class="card slide-up">
                <h4>🌍 Site Suitability</h4>
                <p>Evaluate feasibility for solar, wind, and hydro installations.</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        c4, c5 = st.columns(2)

        with c4:
            st.markdown("""
            <div class="card slide-up">
                <h4>🏭 Plant Performance</h4>
                <p>Assess operational health and efficiency of power plants.</p>
            </div>
            """, unsafe_allow_html=True)

        with c5:
            st.markdown("""
            <div class="card slide-up">
                <h4>♻️ CO₂ Reduction</h4>
                <p>Estimate carbon emission savings via renewable adoption.</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")
        st.info("👈 Use the sidebar to explore individual analytical modules.")

    # -------------------------------------------------
    # DASHBOARD MODULES
    # -------------------------------------------------
    elif sub_menu == "🔮 Energy Forecasting":
        from dashboard.Energy_Forecasting import show
        show()

    elif sub_menu == "⚡ Energy Consumption":
        from dashboard.Energy_Consumption import show
        show()

    elif sub_menu == "🌍 Site Suitability":
        from dashboard.Site_Suitability import show
        show()

    elif sub_menu == "🏭 Plant Performance":
        from dashboard.Plant_Health import show
        show()

    elif sub_menu == "♻️ CO₂ Reduction":
        from dashboard.CO2_Reduction import show
        show()

# -------------------------------------------------
# DEVELOPERS PAGE
# -------------------------------------------------
elif main_menu == "👨‍💻 Developers":
    from static_pages.Developers import show
    show()
