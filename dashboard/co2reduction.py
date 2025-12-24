import streamlit as st
import pandas as pd
from utils.model_loader import load_model

# ---------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------
def show():
    st.title("♻️ CO₂ Emission Reduction")
    st.caption("Estimate carbon emission reduction using renewable energy generation")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input(
            "Year",
            min_value=2010,
            max_value=2035,
            value=2022,
            step=1
        )

        month = st.selectbox(
            "Month",
            options=list(range(1, 13)),
            format_func=lambda x: [
                "January","February","March","April","May","June",
                "July","August","September","October","November","December"
            ][x-1]
        )

        solar_gen = st.number_input(
            "Solar Generation (MWh)",
            min_value=0.0,
            value=3000.0,
            step=100.0
        )

    with col2:
        wind_gen = st.number_input(
            "Wind Generation (MWh)",
            min_value=0.0,
            value=4000.0,
            step=100.0
        )

        hydro_gen = st.number_input(
            "Hydro Generation (MWh)",
            min_value=0.0,
            value=2500.0,
            step=100.0
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------
    # PREDICTION
    # ---------------------------------------------
    if st.button("🌱 Estimate CO₂ Reduction"):

        model = load_model("models/CO2_Reduction.pkl")

        if model is None:
            st.error("❌ CO₂ Reduction model not found.")
            return

        input_df = pd.DataFrame([{
            "year": year,
            "month": month,
            "solar_generation_mwh": solar_gen,
            "wind_generation_mwh": wind_gen,
            "hydro_generation_mwh": hydro_gen
        }])

        predicted_total_generation = model.predict(input_df)[0]

        CO2_FACTOR = 0.9  # tonnes CO₂ per MWh (coal replacement)
        estimated_co2_reduction = predicted_total_generation * CO2_FACTOR

        st.success(
            f"🌍 Estimated CO₂ Reduction: **{estimated_co2_reduction:,.2f} tonnes**"
        )
