# magazine_style_story.py

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Antibiotic Magazine Story", layout="centered")

st.title("📰 The Antibiotic Dilemma: When One Drug Isn't Enough")
st.subheader("A Magazine-Style Data Story Exploring Effectiveness of Penicillin, Streptomycin & Neomycin")

st.markdown("""
In the golden age of antibiotics, one truth remains unchanged: **no single drug works for everything**. Burtin's dataset comparing three antibiotics against 16 bacterial species uncovers this reality with stunning clarity.

Each antibiotic — **Penicillin**, **Streptomycin**, and **Neomycin** — offers a unique pattern of effectiveness. When examined together, we see why doctors often hesitate before prescribing — because bacterial identity and cell wall structure make all the difference.
""")

# Data
data = [
    {"Bacteria": "Aerobacter aerogenes", "Penicillin": 870, "Streptomycin": 1, "Neomycin": 1.6},
    {"Bacteria": "Bacillus anthracis", "Penicillin": 0.001, "Streptomycin": 0.01, "Neomycin": 0.007},
    {"Bacteria": "Escherichia coli", "Penicillin": 100, "Streptomycin": 0.4, "Neomycin": 0.1},
    {"Bacteria": "Streptococcus hemolyticus", "Penicillin": 0.001, "Streptomycin": 14, "Neomycin": 10},
    {"Bacteria": "Staphylococcus aureus", "Penicillin": 0.03, "Streptomycin": 0.03, "Neomycin": 0.001},
]
df = pd.DataFrame(data)
df_long = df.melt(id_vars=["Bacteria"], var_name="Antibiotic", value_name="MIC")

# Chart
chart = alt.Chart(df_long).mark_bar(size=40).encode(
    x=alt.X("MIC:Q", scale=alt.Scale(type='log'), title="MIC (Log Scale)"),
    y=alt.Y("Bacteria:N", sort="-x"),
    color=alt.Color("Antibiotic:N"),
    tooltip=["Bacteria", "Antibiotic", "MIC"]
).properties(
    width=700,
    height=400,
    title="Antibiotic Strength Varies Widely by Bacterium"
)

st.altair_chart(chart, use_container_width=True)

st.markdown("""
---

### 🎯 Key Insights:

- Penicillin is incredibly effective against *Bacillus anthracis* and *Staphylococcus aureus* — both Gram-positive.
- It is virtually useless against *Aerobacter aerogenes* and *E. coli*.
- Streptomycin and Neomycin offer more reliable performance across species, but even they struggle with some *Streptococcus* strains.

---

In short: treating infections isn't just about using “an antibiotic.” It's about choosing **the right one** — and data like this saves lives by helping us make better decisions.

""")
