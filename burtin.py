import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

# Page setup
st.set_page_config(page_title="Antibiotic Effectiveness Chart", layout="centered")
st.title("Antibiotic Strength Against Bacteria")
st.markdown("""
MIC (Minimum Inhibitory Concentration) values in mg/ml. Lower MIC means stronger antibiotic effectiveness.
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

# Define effectiveness function
def effectiveness_category(mic):
    if mic <= 1:
        return "Strongly Effective"
    elif mic <= 10:
        return "Merely Effective"
    else:
        return "Ineffective"

# Antibiotics list
antibiotics = ["Penicillin", "Streptomycin", "Neomycin"]

# Colors for categories
category_colors = {
    "Strongly Effective": "#4caf50",  # Green
    "Merely Effective": "#ffeb3b",    # Yellow
    "Ineffective": "#f44336"           # Red
}

for ab in antibiotics:
    st.subheader(f"{ab}")
    # Prepare data for this antibiotic
    df_ab = df[["Bacteria", ab]].rename(columns={ab: "MIC"})
    df_ab["Effectiveness"] = df_ab["MIC"].apply(effectiveness_category)

    # Sort bacteria by MIC ascending (strongest at top)
    df_ab = df_ab.sort_values("MIC")

    chart = alt.Chart(df_ab).mark_bar().encode(
        x=alt.X("MIC:Q", scale=alt.Scale(domain=[0, df_ab["MIC"].max()*1.1]), title="MIC (mg/ml)"),
        y=alt.Y("Bacteria:N", sort=alt.EncodingSortField(field="MIC", order="ascending"), title="Bacterial Species"),
        color=alt.Color("Effectiveness:N", scale=alt.Scale(domain=list(category_colors.keys()), range=list(category_colors.values())), legend=alt.Legend(title="Effectiveness")),
        tooltip=["Bacteria", "MIC", "Effectiveness"]
    ).properties(
        width=700,
        height=400,
        title=f"{ab} Effectiveness"
    )

    st.altair_chart(chart, use_container_width=True)

st.markdown("""
### Effectiveness Legend:
- **Green:** Strongly Effective (MIC ≤ 1 mg/ml)
- **Yellow:** Merely Effective (1 < MIC ≤ 10 mg/ml)
- **Red:** Ineffective (MIC > 10 mg/ml)
""")
