# burtin_annotated_chart.py

import streamlit as st
import pandas as pd
import altair as alt

# Page config
st.set_page_config(page_title="Penicillin Effectiveness", layout="wide")

# Header
st.title("🦠 Penicillin vs. Bacteria: An Annotated Chart")
st.markdown("""
This chart shows how effective **Penicillin** is against various bacterial species,
highlighting a clear contrast between **Gram-positive** and **Gram-negative** bacteria.
The lower the MIC (Minimum Inhibitory Concentration), the more effective the antibiotic.
""")

# Dataset (only Penicillin for clarity)
data = [
    {"Bacteria": "Aerobacter aerogenes", "Penicillin": 870, "Gram_Staining": "negative"},
    {"Bacteria": "Bacillus anthracis", "Penicillin": 0.001, "Gram_Staining": "positive"},
    {"Bacteria": "Brucella abortus", "Penicillin": 1, "Gram_Staining": "negative"},
    {"Bacteria": "Diplococcus pneumoniae", "Penicillin": 0.005, "Gram_Staining": "positive"},
    {"Bacteria": "Escherichia coli", "Penicillin": 100, "Gram_Staining": "negative"},
    {"Bacteria": "Klebsiella pneumoniae", "Penicillin": 850, "Gram_Staining": "negative"},
    {"Bacteria": "Mycobacterium tuberculosis", "Penicillin": 800, "Gram_Staining": "negative"},
    {"Bacteria": "Proteus vulgaris", "Penicillin": 3, "Gram_Staining": "negative"},
    {"Bacteria": "Pseudomonas aeruginosa", "Penicillin": 850, "Gram_Staining": "negative"},
    {"Bacteria": "Salmonella typhosa", "Penicillin": 1, "Gram_Staining": "negative"},
    {"Bacteria": "Salmonella schottmuelleri", "Penicillin": 10, "Gram_Staining": "negative"},
    {"Bacteria": "Staphylococcus albus", "Penicillin": 0.007, "Gram_Staining": "positive"},
    {"Bacteria": "Staphylococcus aureus", "Penicillin": 0.03, "Gram_Staining": "positive"},
    {"Bacteria": "Streptococcus fecalis", "Penicillin": 1, "Gram_Staining": "positive"},
    {"Bacteria": "Streptococcus hemolyticus", "Penicillin": 0.001, "Gram_Staining": "positive"},
    {"Bacteria": "Streptococcus viridans", "Penicillin": 0.005, "Gram_Staining": "positive"}
]

df = pd.DataFrame(data)

# Sort for cleaner layout
df = df.sort_values(by="Penicillin", ascending=False)

# Bar chart
bars = alt.Chart(df).mark_bar().encode(
    y=alt.Y('Bacteria:N', sort=df['Bacteria'].tolist()),
    x=alt.X('Penicillin:Q',
            scale=alt.Scale(type='log'),
            title='MIC (Minimum Inhibitory Concentration) — Log Scale'),
    color=alt.Color('Gram_Staining:N',
                    scale=alt.Scale(domain=['positive', 'negative'],
                                    range=['#4CAF50', '#F44336']),
                    title='Gram Stain'),
    tooltip=['Bacteria', 'Penicillin', 'Gram_Staining']
)

# Annotations
annotations = alt.Chart(pd.DataFrame({
    'Bacteria': ['Bacillus anthracis', 'Aerobacter aerogenes'],
    'Penicillin': [0.001, 870],
    'Annotation': ['Extremely sensitive (Gram+)', 'Highly resistant (Gram−)']
})).mark_text(align='left', dx=5, dy=-5, fontSize=12).encode(
    x='Penicillin:Q',
    y='Bacteria:N',
    text='Annotation:N'
)

# Combine chart + annotation
final_chart = (bars + annotations).properties(
    width=800,
    height=600,
    title='Penicillin is Powerful Against Gram-Positive Bacteria, but Fails Against Gram-Negative Ones'
).configure_title(anchor='start', fontSize=18)

st.altair_chart(final_chart, use_container_width=True)
