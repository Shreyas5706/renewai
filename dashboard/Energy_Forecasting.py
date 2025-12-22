import streamlit as st
import pandas as pd
import numpy as np

from utils.model_loader import load_model
from utils.warnings_config import *

def show():
        
    # --------------------------------------------------
    # PAGE HEADER
    # --------------------------------------------------
    st.title("🔮 Energy Forecasting (India)")
    st.caption("Predict total renewable energy generation using ML")

    st.markdown("---")

    st.info(
        "This model forecasts total renewable energy generation (MWh) "
        "based on year, month, and source-wise generation inputs."
    )

    # --------------------------------------------------
    # INPUT SECTION
    # --------------------------------------------------
    import datetime

    st.subheader("📥 Input Parameters")

    selected_date = st.date_input(
        "Select Month & Year",
        value=datetime.date(2022, 1, 1),
        min_value=datetime.date(2000, 1, 1),
        max_value=datetime.date(2035, 12, 31)
    )

    year = selected_date.year
    month = selected_date.month

    col1, col2, col3 = st.columns(3)

    with col1:
        solar_gen = st.number_input(
            "Solar Generation (MWh)",
            min_value=0.0,
            max_value=50000.0,
            value=3000.0,
            step=100.0
        )

    with col2:
        wind_gen = st.number_input(
            "Wind Generation (MWh)",
            min_value=0.0,
            max_value=70000.0,
            value=4000.0,
            step=100.0
        )

    with col3:
        hydro_gen = st.number_input(
            "Hydro Generation (MWh)",
            min_value=0.0,
            max_value=80000.0,
            value=5000.0,
            step=100.0
        )


    # --------------------------------------------------
    # PREDICTION
    # --------------------------------------------------
    st.markdown("---")

    if st.button("⚡ Forecast Total Energy", use_container_width=True):

        with st.spinner("Forecasting energy generation..."):

            # -----------------------------
            # RULE-BASED ESTIMATION
            # -----------------------------
            rule_estimate = solar_gen + wind_gen + hydro_gen

            # -----------------------------
            # ML-BASED BASELINE
            # -----------------------------
            model = load_model("models/energy_forecast_model.pkl")

            input_df = pd.DataFrame([{
                "year": year,
                "month": month,
                "solar_generation_mwh": solar_gen,
                "wind_generation_mwh": wind_gen,
                "hydro_generation_mwh": hydro_gen
            }])

            ml_prediction = model.predict(input_df)[0]

            # -----------------------------
            # HYBRID FINAL PREDICTION
            # -----------------------------
            final_prediction = (0.8 * rule_estimate) + (0.2 * ml_prediction)

            # -----------------------------
            # OUTPUT
            # -----------------------------
        

            col1, col2, col3 = st.columns(3)

            st.success(
                f"🔋 Predicted Total Energy Generation: **{final_prediction:,.2f} MWh**"
            )


