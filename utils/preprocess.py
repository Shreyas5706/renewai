import pandas as pd

# Derived from training dataset
PLANT_MAP = {
    4135001: 0,
    4136001: 1
}

# Location was empty during training
LOCATION_MAP = {
    "Unknown": 0
}

FEATURE_ORDER = [
    "plant_name",
    "DC_POWER",
    "generation_mwh",
    "DAILY_YIELD",
    "TOTAL_YIELD",
    "capacity_mw",
    "plant_location"
]

def preprocess_energy_input(data: dict):
    processed = {
        "plant_name": PLANT_MAP[data["plant_name"]],
        "DC_POWER": float(data["DC_POWER"]),
        "generation_mwh": float(data["generation_mwh"]),
        "DAILY_YIELD": float(data["DAILY_YIELD"]),
        "TOTAL_YIELD": float(data["TOTAL_YIELD"]),
        "capacity_mw": float(data["capacity_mw"]),
        "plant_location": LOCATION_MAP["Unknown"]
    }

    return pd.DataFrame([processed], columns=FEATURE_ORDER)
