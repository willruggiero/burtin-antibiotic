import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import subprocess
import sys

# Ensure Altair is installed
try:
    import altair
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "altair"])
    import altair

# Page setup
st.set_page_config(page_title="Antibiotic Effectiveness Chart", layout="centered")
st.title("Antibiotic Strength Against Bacteria")
st.markdown("""
Lower MIC (Minimum Inhibitory Concentration) values indicate stronger antibiotic effectiveness.
""")

# Dataset
data = [
    {"Bacteria":"Aerobacter aerogenes","Penicillin":870,"Streptomycin":1,"Neomycin":1.6},
    {"Bacteria":"Bacillus anthracis","Penicillin":0.001,"Streptomycin":0.01,"Neomycin":0.007},
    {"Bacteria":"Brucella abortus","Penicillin":1,"Streptomycin":2,"Neomycin":0.02},
    {"Bacteria":"Diplococcus pneumoniae","Penicillin":0.005,"Streptomycin":11,"Neomycin":10},
    {"Bacteria":"Escherichia coli","Penicillin":100,"Streptomycin":0.4,"Neomycin":0.1},
    {"Bacteria":"Klebsiella pneumoniae","Penicillin":850,"Streptomycin":1.2,"Neomycin":1},
    {"Bacteria":"Mycobacterium tuberculosis","Penicillin":800,"Streptomycin":5,"Neomycin":2},
    {"Bacteria":"Proteus vulgaris","Penicillin":3,"Streptomycin":0.1,"Neomycin":0.1},
    {"Bacteria":"Pseudomonas aeruginosa","Penicillin":850,"Streptomycin":2,"Neomycin":0.4},
    {"Bacteria":"Salmonella typhosa","Penicillin":1,"Streptomycin":0.4,"Neomycin":0.008},
    {"Bacteria":"Salmonella schottmuelleri","Penicillin":10,"Streptomycin":0.8,"Neomycin":0.09},
    {"Bacteria":"Staphylococcus albus","Penicillin":0.007,"Streptomycin":0.1,"Neomycin":0.001},
    {"Bacteria":"Staphylococcus aureus","Penicillin":0.03,"Streptomycin":0.03,"Neomycin":0.001},
    {"Bacteria":"Streptococcus fecalis","Penicillin":1,"Streptomycin":1,"Neomycin":0.1},
    {"Bacteria":"Streptococcus hemolyticus","Penicillin":0.001,"Streptomycin":14,"Neomycin":10},
    {"Bacteria":"Streptococcus viridans","Penicillin":0.005,"Streptomycin":10,"Neomycin":40}
]

df = pd.DataFrame(data)
df_long = df.melt(id_vars=["Bacteria"], var_name="Antibiotic", value_name="MIC")

# Define effectiveness zones in MIC (mg/ml)
zones = pd.DataFrame([
    {"Effectiveness": "Strongly Effective", "xmin": 0, "xmax": 1, "color": "#d4f0d4"},  # light green
    {"Effectiveness": "Merely Effective", "xmin": 1, "xmax": 10, "color": "#fff3b0"},    # light yellow
    {"Effectiveness": "Ineffective", "xmin": 10, "xmax": 900, "color": "#f7c6c5"},       # light red
])

# Base bars chart with raw MIC values on x-axis
bars = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('MIC:Q', scale=alt.Scale(domain=(0, 900)), title="MIC (mg/ml) - Lower is Stronger"),
    y=alt.Y('Bacteria:N', sort='-x', title="Bacterial Species"),
    color=alt.Color('Antibiotic:N', legend=alt.Legend(title="Antibiotic")),
    tooltip=["Bacteria", "Antibiotic", "MIC"]
).properties(
    width=750,
    height=500,
    title="Antibiotic Effectiveness Across Bacterial Species"
)

# Effectiveness bands at bottom of chart (horizontal bars)
bands = alt.Chart(zones).mark_rect(opacity=0.15).encode(
    x=alt.X('xmin:Q', scale=alt.Scale(domain=(0, 900)), axis=None),
    x2='xmax:Q',
    y=alt.value(490),  # position near bottom (pixels)
    y2=alt.value(510),
    color=alt.Color('color:N', scale=None, legend=None)
).properties(width=750)

# Labels for bands
labels = alt.Chart(zones).mark_text(dy=-5, fontSize=11).encode(
    x=alt.X('xmin:Q', scale=alt.Scale(domain=(0, 900))),
    y=alt.value(490),
    text='Effectiveness'
)

# Combine chart + bands + labels
chart = bars + bands + labels

st.altair_chart(chart, use_container_width=True)

st.markdown("""
### Effectiveness Zones:
- **Green:** Strongly Effective (MIC ≤ 1 mg/ml)
- **Yellow:** Merely Effective (1 < MIC ≤ 10 mg/ml)
- **Red:** Ineffective (MIC > 10 mg/ml)
""")
