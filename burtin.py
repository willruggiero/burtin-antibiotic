import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Antibiotic Magazine Story", layout="centered")

st.title("📰 The Antibiotic Dilemma: When One Drug Isn't Enough")
st.subheader("A Magazine-Style Data Story")

st.markdown("""
This chart visualizes the effectiveness of three antibiotics using MIC (Minimum Inhibitory Concentration) values.
Lower MIC = more effective.
""")

# ✅ Simpler, cleaner data with safe log values
data = [
    {"Bacteria": "E. coli", "Penicillin": 100, "Streptomycin": 0.4, "Neomycin": 0.1},
    {"Bacteria": "S. aureus", "Penicillin": 0.03, "Streptomycin": 0.03, "Neomycin": 0.001},
    {"Bacteria": "B. anthracis", "Penicillin": 0.001, "Streptomycin": 0.01, "Neomycin": 0.007},
    {"Bacteria": "S. hemolyticus", "Penicillin": 0.001, "Streptomycin": 14, "Neomycin": 10},
    {"Bacteria": "A. aerogenes", "Penicillin": 870, "Streptomycin": 1, "Neomycin": 1.6}
]

df = pd.DataFrame(data)
df_long = df.melt(id_vars=["Bacteria"], var_name="Antibiotic", value_name="MIC")

# ✅ Filter out zeros or negatives (not allowed in log scale)
df_long = df_long[df_long["MIC"] > 0]

# Chart
chart = alt.Chart(df_long).mark_bar(size=40).encode(
    x=alt.X("MIC:Q", scale=alt.Scale(type='log'), title="MIC (log scale)"),
    y=alt.Y("Bacteria:N", sort="-x", title="Bacteria"),
    color=alt.Color("Antibiotic:N", title="Antibiotic"),
    tooltip=["Bacteria", "Antibiotic", "MIC"]
).properties(
    width=700,
    height=400,
    title="Antibiotic Strength Varies Widely by Bacterium"
)

st.altair_chart(chart, use_container_width=True)

In short: treating infections isn't just about using “an antibiotic.” It's about choosing **the right one** — and data like this saves lives by helping us make better decisions.

""")
