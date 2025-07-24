import altair as alt

# Filter highlight to only the lowest MIC per bacteria (strongest antibiotic)
highlight_min = highlight.loc[highlight.groupby("Bacteria")["MIC"].idxmin()]

# Add a small vertical offset to text to avoid overlap if needed
highlight_min = highlight_min.assign(
    y_offset=lambda d: d["Bacteria"].apply(lambda b: {"Bacillus anthracis": -0.15, "Aerobacter aerogenes": 0.15}[b])
)

base = alt.Chart(df_long).mark_bar().encode(
    x=alt.X('log_MIC:Q', title="log10(MIC) - Lower is Stronger"),
    y=alt.Y('Bacteria:N', sort='-x', title="Bacterial Species"),
    color=alt.Color('Antibiotic:N'),
    tooltip=["Bacteria", "Antibiotic", "MIC"]
).properties(
    width=750,
    height=500,
    title="Antibiotic Effectiveness Across Bacterial Species"
)

text = alt.Chart(highlight_min).mark_text(
    align='left',
    baseline='middle',
    dx=10,  # shift text farther to the right
    fontSize=12,
    fontWeight='bold',
    color='black'
).encode(
    x='log_MIC:Q',
    y=alt.Y('Bacteria:N', axis=None),
    text='Antibiotic:N',
    # Apply vertical offset for each bacteria label
    yOffset='y_offset:Q'
)

rule = alt.Chart(highlight_min).mark_rule(
    color='red',
    strokeDash=[5, 5],
    opacity=0.6,
    size=1  # thinner line
).encode(
    x='log_MIC:Q',
    y=alt.Y('Bacteria:N', axis=None)
)

st.altair_chart(base + text + rule, use_container_width=True)
