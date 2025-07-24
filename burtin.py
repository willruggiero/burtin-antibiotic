import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import subprocess
import sys

# ✅ Ensure Altair is installed
try:
    import altair
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "altair"])
    import altair

# --- Page setup
st.set_page_config(page_title="Antibiotic Effectiveness Chart", layout="centered")
st.title("💊 Antibiotic Strength Against Bacteria")
st.markdown("""
This chart explores how three antibiotics—**Penicillin**, **Streptomycin**, and **Neomycin**—perform against 16 bacterial species.  
Lower MIC (Minimum Inhibitory Concentration) values mean **stronger antibiotic performance**.
""")

# --- Dataset
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

# --- Add log10 column for visualization
df_long["log_MIC"] = np.log10(df_long["MIC"])

# --- Chart without annotations
chart = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('log_MIC:Q', title="log10(MIC) - Lower is Stronger"),
    y=alt.Y('Bacteria:N', sort='-x', title="Bacterial Species"),
    color=alt.Color('Antibiotic:N', legend=alt.Legend(title="Antibiotic")),
    tooltip=["Bacteria", "Antibiotic", "MIC"]
).properties(
    width=750,
    height=500,
    title="Antibiotic Effectiveness Across Bacterial Species"
)

st.altair_chart(chart, use_container_width=True)

# --- Final note
st.markdown("""
This chart reveals key insights:
- **Penicillin** is ineffective against some bacteria like *Aerobacter aerogenes* (MIC = 870).
- **Streptomycin** and **Neomycin** show stronger, broader effectiveness, especially against Gram-negative species.
""")
