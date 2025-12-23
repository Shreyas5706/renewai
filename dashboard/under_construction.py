import streamlit as st

def show(module_name, description):
    st.markdown("""
    <style>
    .uc-card {
        padding: 40px;
        border-radius: 18px;
        background: linear-gradient(135deg,#1f2933,#111827);
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }
    .uc-card h1 {
        margin-bottom: 10px;
        font-size: 2.2rem;
    }
    .uc-card p {
        font-size: 1.05rem;
        color: #d1d5db;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="uc-card">
        <h1>🚧 {module_name}</h1>
        <p>{description}</p>
        <p><b>Status:</b> Under Construction</p>
        <p>🔧 This module is currently being developed and will be available soon.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.info("👨‍💻 Our team is actively working on this module. Stay tuned!")
    