import streamlit as st
import pandas as pd

from utils.model_loader import load_model
from utils.warnings_config import *

def show():
        
    # -------------------------------------------------
    # PAGE HEADER
    # -------------------------------------------------
    st.title("🏭 Plant Health Score")
    st.caption("ML-based plant condition classification")

    st.markdown("---")

    st.info(
        "This model evaluates plant health using operational metrics such as "
        "power generation and yield. Output categories are "
        "Healthy, Moderate, or Needs Maintenance."
    )

    # -------------------------------------------------
    # INPUT SECTION
    # -------------------------------------------------
    with st.expander("📥 Enter Plant Operational Data", expanded=True):

        col1, col2 = st.columns(2)

        with col1:
            dc_power = st.number_input("DC Power", min_value=0.0)
            generation_mwh = st.number_input("Generation (MWh)", min_value=0.0)
            daily_yield = st.number_input("Daily Yield", min_value=0.0)

        with col2:
            total_yield = st.number_input("Total Yield", min_value=0.0)
            capacity_mw = st.number_input("Capacity (MW)", min_value=0.0)

    # -------------------------------------------------
    # PREDICTION
    # -------------------------------------------------
    st.markdown("---")

    if st.button("🧠 Evaluate Plant Health", use_container_width=True):

        # -------- DIRECT HEALTH SCORE (SAME AS TRAINING LOGIC) --------
        numeric_values = [
            dc_power,
            generation_mwh,
            daily_yield,
            total_yield,
            capacity_mw
        ]

        performance_score = sum(numeric_values) / len(numeric_values)

        # simple normalization (safe demo-level)
        health_score = min(max((performance_score / 1000) * 100, 0), 100)

        # -------- LABEL LOGIC --------
        if health_score >= 70:
            label = "🟢 Healthy"
            score = 90
            source = "Rule-based Health Score"

        elif health_score >= 40:
            label = "🟡 Moderate Health"
            score = 60
            source = "Rule-based Health Score"

        else:
            label = "🔴 Needs Maintenance"
            score = 30
            source = "Rule-based Health Score"

        st.success(label)
        st.progress(score) 
