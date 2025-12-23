import streamlit as st
import pandas as pd

# -----------------------------------------
# REGION OPTIONS
# -----------------------------------------
REGION_MAP = {
    "NR": "North Region",
    "WR": "West Region",
    "SR": "South Region",
    "ER": "East Region",
    "NER": "North East Region",
    "ESR": "East South Region",
    "SWR": "South West Region",
    "WNR": "West North Region"
}

# -----------------------------------------
# MAIN UI
# -----------------------------------------
def show():
    st.title("⚡ Energy Consumption Analysis")
    st.caption("Predict electricity consumption based on regional demand patterns")

    st.markdown("---")

    # ---------------- INPUT CARD ----------------
    st.markdown("""
    <div class="card slide-up">
        <h4>🔢 Input Parameters</h4>
        <p>Provide regional and demand-related details</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        region_label = st.selectbox(
            "Region",
            options=list(REGION_MAP.keys()),
            format_func=lambda x: REGION_MAP[x]
        )

        year = st.number_input(
            "Year",
            min_value=2010,
            max_value=2035,
            value=2022,
            step=1
        )

    with col2:
        month = st.selectbox(
            "Month",
            options=list(range(1, 13)),
            format_func=lambda x: [
                "January","February","March","April","May","June",
                "July","August","September","October","November","December"
            ][x-1]
        )

        peak_demand = st.number_input(
            "Peak Demand (MW)",
            min_value=100.0,
            max_value=100000.0,
            value=5000.0,
            step=100.0
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------- PREDICT BUTTON ----------------
    if st.button("🔍 Predict Electricity Consumption"):
        
        # Create input dataframe (model-ready)
        input_df = pd.DataFrame([{
            "region": region_label,
            "year": year,
            "month": month,
            "peak_demand_mw": peak_demand
        }])

        # -----------------------------------------
        # TEMP DEMO LOGIC (until model is plugged)
        # -----------------------------------------
        estimated_consumption = peak_demand * 24 * 30 * 0.6

        st.success(
            f"⚡ Predicted Electricity Consumption: "
            f"**{estimated_consumption:,.2f} MWh**"
        )

        st.caption(
            "Note: This is a placeholder estimation. "
            "The ML-based consumption model will replace this logic."
        )
