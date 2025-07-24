# annotated_chart_app.py

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Antibiotic Comparison", layout="wide")
st.title("💊 Which Antibiotic is Most Effective — And When?")
st.markdown("This annotated chart compares the MIC (Minimum Inhibitory Concentration) of **Penicillin**, **Streptomycin**, and **Neomycin** across 16 bacterial species. Lower MIC = greater effectiveness.")

# Data
data = [
    {"Bacteria": "Aerobacter aerogenes", "Penicillin": 870, "Streptomycin": 1, "Neomycin": 1.6, "Gram": "negative"},
    {"Bacteria": "Bacillus anthracis", "Penicillin": 0.001, "Streptomycin": 0.01, "Neomycin": 0.007, "Gram": "positive"},
    {"Bacteria": "Brucella abortus", "Penicillin": 1, "Streptomycin": 2, "Neomycin": 0.02, "Gram": "negative"},
    {"Bacteria": "Diplococcus pneumoniae", "Penicillin": 0.005, "Streptomycin": 11, "Neomycin": 10, "Gram": "positive"},
    {"Bacteria": "Escherichia coli", "Penicillin": 100, "Streptomycin": 0.4, "Neomycin": 0.1, "Gram": "negative"},
    {"Bacteria": "Klebsiella pneumoniae", "Penicillin": 850, "Streptomycin": 1.2, "Neomycin": 1, "Gram": "negative"},
    {"Bacteria": "Mycobacterium tuberculosis", "Penicillin": 800, "Streptomycin": 5, "Neomycin": 2, "Gram": "negative"},
    {"Bacteria": "Proteus vulgaris", "Penicillin": 3, "Streptomycin": 0.1, "Neomycin": 0.1, "Gram": "negative"},
    {"Bacteria": "Pseudomonas aeruginosa", "Penicillin": 850, "Streptomycin": 2, "Neomycin": 0.4, "Gram": "negative"},
    {"Bacteria": "Salmonella typhosa", "Penicillin": 1, "Streptomycin": 0.4, "Neomycin": 0.008, "Gram": "negative"},
    {"Bacteria": "Salmonella schottmuelleri", "Penicillin": 10, "Streptomycin": 0.8, "Neomycin": 0.09, "Gram": "negative"},
    {"Bacteria": "Staphylococcus albus", "Penicillin": 0.007, "Streptomycin": 0.1, "Neomycin": 0.001, "Gram": "positive"},
    {"Bacteria": "Staphylococcus aureus", "Penicillin": 0.03, "Streptomycin": 0.03, "Neomycin": 0.001, "Gram": "positive"},
    {"Bacteria": "Streptococcus fecalis", "Penicillin": 1, "Streptomycin": 1, "Neomycin": 0.1, "Gram": "positive"},
    {"Bacteria": "Streptococcus hemolyticus", "Penicillin": 0.001, "Streptomycin": 14, "Neomycin": 10, "Gram": "positive"},
    {"Bacteria": "Streptococcus viridans", "Penicillin": 0.005, "Streptomycin": 10, "Neomycin": 40, "Gram": "positive"}
]
df = pd.DataFrame(data)
df_long = df.melt(id_vars=["Bacteria", "Gram"], var_name="Antibiotic", value_name="MIC")

# Main bar chart
bar = alt.Chart(df_long).mark_bar().encode(
    y=alt.Y("Bacteria:N", sort="-x", title=None),
    x=alt.X("MIC:Q", scale=alt.Scale(type='log'), title="MIC (log scale, lower = more effective)"),
    color=alt.Color("Antibiotic:N", title="Antibiotic"),
    tooltip=["Bacteria", "Antibiotic", "MIC", "Gram"]
)

# Annotation labels
annotated_points = alt.Chart(pd.DataFrame([
    {"Bacteria": "Bacillus anthracis", "Antibiotic": "Penicillin", "MIC": 0.001, "label": "Highly sensitive"},
    {"Bacteria": "Aerobacter aerogenes", "Antibiotic": "Penicillin", "MIC": 870, "label": "Highly resistant"},
])).mark_text(align='left', dx=10, dy=-10, fontSize=12).encode(
    y="Bacteria:N",
    x="MIC:Q",
    text="label:N"
)

# Combine
final = (bar + annotated_points).properties(
    title="Annotated Comparison of Antibiotic Effectiveness (MIC Values)",
    width=800,
    height=600
)

st.altair_chart(final, use_container_width=True)

st.markdown("---")
st.markdown("📌 **Key Takeaways**")
st.markdown("""
- Penicillin is **extremely effective** on some Gram-positive bacteria but fails against most Gram-negative ones.
- Streptomycin and Neomycin show broader effectiveness, but some bacteria (like *Streptococcus hemolyticus*) remain resistant.
""")
