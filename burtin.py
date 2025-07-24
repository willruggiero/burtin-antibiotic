# burtin_annotated_chart.py

import streamlit as st
import pandas as pd
import altair as alt

# Streamlit config
st.set_page_config(page_title="Annotated Antibiotic Chart", layout="wide")
st.title("🦠 Annotated Chart: Antibiotic Effectiveness by Gram Type")
st.markdown("""
This annotated chart highlights how **Penicillin** performs very differently on **Gram-positive vs Gram-negative** bacteria.
MIC = Minimum Inhibitory Concentration (lower = more effective).
""")

# Data
data = [
    {"Bacteria":"Aerobacter aerogenes","Penicillin":870,"Gram_Staining":"negative"},
    {"Bacteria":"Bacillus anthracis","Penicillin":0.001,"Gram_Staining":"positive"},
    {"Bacteria":"Brucella abortus","Penicillin":1,"Gram_Staining":"negative"},
    {"Bacteria":"Diplococcus pneumoniae","Penicillin":0.005,"Gram_Staining":"positive"},
    {"Bacteria":"Escherichia coli","Penicillin":100,"Gram_Staining":"negative"},
    {"Bacteria":"Klebsiella pneumoniae","Penicillin":850,"Gram_Staining":"negative"},
    {"Bacteria":"Mycobacterium tuberculosis","Penicillin":800,"Gram_Staining":"negative"},
    {"Bacteria":"Proteus vulgaris","Penicillin":3,"Gram_Staining":"negative"},
    {"Bacteria":"Pseudomonas aeruginosa","Penicillin":850,"Gram_Staining":"negative"},
    {"Bacteria":"Salmonella (Eberthella) typhosa","Penicillin":1,"Gram_Staining":"negative"},
    {"Bacteria":"Salmonella schottmuelleri","Penicillin":10,"Gram_Staining":"negative"},
    {"Bacteria":"Staphylococcus albus","Penicillin":0.007,"Gram_Staining":"positive"},
    {"Bacteria":"Staphylococcus aureus","Penicillin":0.03,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus fecalis","Penicillin":1,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus hemolyticus","Penicillin":0.001,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus viridans","Penicillin":0.005,"Gram_Staining":"positive"}
]

df = pd.DataFrame(data)

# Create annotated chart
base = alt.Chart(df).mark_bar(size=18).encode(
    y=alt.Y('Bacteria:N', sort='-x', title=None),
    x=alt.X('Penicillin:Q', scale=alt.Scale(type='log'), title='MIC (log scale; lower = more effective)'),
    color=alt.Color('Gram_Staining:N', title='Gram Type',
                    scale=alt.Scale(domain=['positive', 'negative'],
                                    range=['#4CAF50', '#F44336'])),
    tooltip=['Bacteria', 'Penicillin', 'Gram_Staining']
)

# Highlight two bacteria for annotations
annotations = alt.Chart(pd.DataFrame([
    {'Bacteria': 'Bacillus anthracis', 'Penicillin': 0.001, 'text': 'Extremely sensitive\n(Gram-positive)'},
    {'Bacteria': 'Aerobacter aerogenes', 'Penicillin': 870, 'text': 'Highly resistant\n(Gram-negative)'}
])).mark_text(align='left', dx=10, dy=-5, fontSize=12).encode(
    y='Bacteria:N',
    x='Penicillin:Q',
    text='text:N'
)

final_chart = (base + annotations).properties(
    width=700,
    height=600,
    title="Penicillin is Powerful Against Gram-Positive Bacteria, but Fails Against Gram-Negative Ones"
).configure_axis(
    labelFontSize=12,
    titleFontSize=14
).configure_title(
    fontSize=18,
    anchor='start'
)

st.altair_chart(final_chart, use_container_width=True)
