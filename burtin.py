# burtin_story.py

import streamlit as st
import pandas as pd
import altair as alt

# Title
st.title("Antibiotic Effectiveness Against Bacteria")
st.markdown("""
### 📖 Story: Penicillin’s Performance Problem
Penicillin, the legendary antibiotic, struggles dramatically against Gram-negative bacteria.
This app explores the effectiveness of three antibiotics (Penicillin, Streptomycin, Neomycin)
against 16 bacterial species, using MIC (Minimum Inhibitory Concentration) data.
Lower MIC = more effective antibiotic.
""")

# Dataset
data = [
    {"Bacteria":"Aerobacter aerogenes","Penicillin":870,"Streptomycin":1,"Neomycin":1.6,"Gram_Staining":"negative"},
    {"Bacteria":"Bacillus anthracis","Penicillin":0.001,"Streptomycin":0.01,"Neomycin":0.007,"Gram_Staining":"positive"},
    {"Bacteria":"Brucella abortus","Penicillin":1,"Streptomycin":2,"Neomycin":0.02,"Gram_Staining":"negative"},
    {"Bacteria":"Diplococcus pneumoniae","Penicillin":0.005,"Streptomycin":11,"Neomycin":10,"Gram_Staining":"positive"},
    {"Bacteria":"Escherichia coli","Penicillin":100,"Streptomycin":0.4,"Neomycin":0.1,"Gram_Staining":"negative"},
    {"Bacteria":"Klebsiella pneumoniae","Penicillin":850,"Streptomycin":1.2,"Neomycin":1,"Gram_Staining":"negative"},
    {"Bacteria":"Mycobacterium tuberculosis","Penicillin":800,"Streptomycin":5,"Neomycin":2,"Gram_Staining":"negative"},
    {"Bacteria":"Proteus vulgaris","Penicillin":3,"Streptomycin":0.1,"Neomycin":0.1,"Gram_Staining":"negative"},
    {"Bacteria":"Pseudomonas aeruginosa","Penicillin":850,"Streptomycin":2,"Neomycin":0.4,"Gram_Staining":"negative"},
    {"Bacteria":"Salmonella (Eberthella) typhosa","Penicillin":1,"Streptomycin":0.4,"Neomycin":0.008,"Gram_Staining":"negative"},
    {"Bacteria":"Salmonella schottmuelleri","Penicillin":10,"Streptomycin":0.8,"Neomycin":0.09,"Gram_Staining":"negative"},
    {"Bacteria":"Staphylococcus albus","Penicillin":0.007,"Streptomycin":0.1,"Neomycin":0.001,"Gram_Staining":"positive"},
    {"Bacteria":"Staphylococcus aureus","Penicillin":0.03,"Streptomycin":0.03,"Neomycin":0.001,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus fecalis","Penicillin":1,"Streptomycin":1,"Neomycin":0.1,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus hemolyticus","Penicillin":0.001,"Streptomycin":14,"Neomycin":10,"Gram_Staining":"positive"},
    {"Bacteria":"Streptococcus viridans","Penicillin":0.005,"Streptomycin":10,"Neomycin":40,"Gram_Staining":"positive"}
]

df = pd.DataFrame(data)

# Reshape data
df_long = df.melt(id_vars=["Bacteria", "Gram_Staining"], 
                  var_name="Antibiotic", value_name="MIC")

# Chart
chart = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('MIC:Q', scale=alt.Scale(type='log'), title='MIC (Lower = More Effective)'),
    y=alt.Y('Bacteria:N', sort='-x'),
    color=alt.Color('Gram_Staining:N', scale=alt.Scale(scheme='set1'), legend=alt.Legend(title="Gram Stain")),
    column=alt.Column('Antibiotic:N', header=alt.Header(title="Antibiotic")),
    tooltip=['Bacteria', 'Antibiotic', 'MIC', 'Gram_Staining']
).properties(
    title="Antibiotic Effectiveness by Gram Type",
    width=250,
    height=400
)

st.altair_chart(chart, use_container_width=True)

st.markdown("""
---  
**Takeaways:**
- Penicillin is highly effective against **Gram-positive** bacteria (e.g., *Staphylococcus* and *Streptococcus*).
- It fails against most **Gram-negative** bacteria (e.g., *E. coli*, *Klebsiella*, *Pseudomonas*).
- Streptomycin and Neomycin show broader effectiveness.

🔬 Understanding Gram staining is essential for antibiotic treatment planning.
""")
