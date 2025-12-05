"""
===============================================================================
STREAMLIT PAGE - NIH Awards Analysis
===============================================================================
Award size and Duration differ across institutions, research topics, and PI demographics
===============================================================================
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import os

# ============================================================================
# PAGE CONFIGURATION & DATA LOADING
# ============================================================================

st.set_page_config(
    page_title="Q5 NIH Awards Analysis",
    layout="wide"
)

# Get the data directory (relative to the pages directory)
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "Sreamlit_data")

# ============================================================================
# SECTION 2: BUSINESS NARRATIVE
# ============================================================================

st.title("Award size and Duration differ across institutions, research topics, and PI demographics")

# Subheader with context
st.markdown("### Why This Matters for Corewell Health")

st.markdown("""
**Context:** Understanding how award size and duration vary across institutions,
research areas, and PI demographics is essential for Corewell Health's strategic
research planning. These insights help Corewell prioritize high-value proposal
opportunities, allocate internal resources more effectively, and identify areas
where targeted support could improve competitiveness and equity in funding outcomes.

*Example: Understanding which features predict grant size helps Corewell optimize
proposal strategy and allocate resources to high-value research areas.*
""")

# Key Insights Section
st.markdown("---")
st.markdown("### Organizations and Locations")

org = pd.read_csv(os.path.join(DATA_DIR, "Org_loc.csv"))
agn = pd.read_csv(os.path.join(DATA_DIR, "ic_location_map.csv"))
df = pd.read_csv(os.path.join(DATA_DIR, "Main_Agen_loc.csv"))

# Create tabs
tab1, tab2 = st.tabs(["Organization Location Data", "Agency Location Data"])

# Tab 1 — Scrollable dataframe with 7 rows visible
with tab1:
    st.markdown("### Organization Location Data")
    st.dataframe(
        org,
        use_container_width=True,
        height=300  # Controls scroll height (~7 rows visible)
    )
    st.markdown("According to the data reported in the NIH records.")

# Tab 2 — Scrollable dataframe with 7 rows visible
with tab2:
    st.markdown("### Agency Location Data")
    st.dataframe(
        agn,
        use_container_width=True,
        height=300  # Controls scroll height
    )
    st.markdown("Researched each agency's headquarters and recorded their locations.")

# ============================================================================
# SECTION 3: KEY VISUALIZATIONS (High-Level Summary)
# ============================================================================

st.markdown("---")
st.markdown("## Key Findings at a Glance")
st.markdown("### Award amount and location analysis")

# --- Ensure fiscal_year is numeric ---
df['fiscal_year'] = df['fiscal_year'].astype(int)

# --- Select 4 main organizations for comparison ---
selected_orgs = [
    'Corewell Health',
    'Henry Ford Health',
    'Kaiser Permanente',
    'University of Pittsburgh'
]

# ---------------------------
# Create Tabs
# ---------------------------
tab1, tab2, tab3 = st.tabs([
    "Organization State",
    "Agency State",
    "Award Amount"
])


# ======================================================
# TAB 1: Organization State Choropleth
# ======================================================
with tab1:

    st.subheader("NIH Award Distribution by Organization State (Animated by Year)")

    subset = df[df['Main_Organization'].isin(selected_orgs)]

    state_summary = (
        subset.groupby(['Main_Organization', 'organization_org_state', 'fiscal_year'], as_index=False)
        .agg(total_award_amount=('award_amount', 'sum'))
    )

    fig1 = px.choropleth(
        state_summary,
        locations='organization_org_state',
        locationmode='USA-states',
        color='total_award_amount',
        facet_col='Main_Organization',
        facet_col_wrap=2,
        animation_frame='fiscal_year',
        color_continuous_scale='Viridis',
        scope='usa',
        title='NIH Award Distribution by Organization State',
        hover_name='organization_org_state',
    )

    fig1.update_coloraxes(cmin=0, cmax=state_summary['total_award_amount'].max())
    fig1.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    fig1.update_layout(
        geo=dict(showcoastlines=True, landcolor='lightgray'),
        title_font=dict(size=18),
        legend_title_text='Total Award ($)',
    )

    st.plotly_chart(fig1, use_container_width=True)


# ======================================================
# TAB 2: Agency State Choropleth
# ======================================================
with tab2:

    st.subheader("NIH Award Distribution by Agency State (Animated by Year)")

    subset2 = df[df['Main_Organization'].isin(selected_orgs)]

    state_summary2 = (
        subset2.groupby(['Main_Organization', 'agency_state', 'fiscal_year'], as_index=False)
        .agg(total_award_amount=('award_amount', 'sum'))
    )

    fig2 = px.choropleth(
        state_summary2,
        locations='agency_state',
        locationmode='USA-states',
        color='total_award_amount',
        facet_col='Main_Organization',
        facet_col_wrap=2,
        animation_frame='fiscal_year',
        color_continuous_scale='Viridis',
        scope='usa',
        title='NIH Award Distribution by Agency State',
        hover_name='agency_state',
    )

    fig2.update_coloraxes(cmin=0, cmax=state_summary2['total_award_amount'].max())
    fig2.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    fig2.update_layout(
        geo=dict(showcoastlines=True, landcolor='lightgray'),
        title_font=dict(size=18),
        legend_title_text='Total Award ($)',
    )

    st.plotly_chart(fig2, use_container_width=True)


# ======================================================
# TAB 3: Award Amount Distribution (Box Plot)
# ======================================================
with tab3:

    st.subheader("Award Amount Distribution by Main Organization")

    fig3 = px.box(
        df,
        x='Main_Organization',
        y='award_amount',
        color='Main_Organization',
        title='NIH Project Award Amount Distribution by Main Organization',
        labels={
            'award_amount': 'Award Amount ($)',
            'Main_Organization': 'Organization'
        },
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig3.update_layout(
        xaxis_title='Main Organization',
        yaxis_title='Award Amount ($)',
        title_font=dict(size=18),
        showlegend=False,
        plot_bgcolor='white'
    )

    fig3.update_xaxes(categoryorder='median descending')

    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("Among the four organizations, the University of Pittsburgh exhibits the widest and highest award distribution, suggesting larger grant volumes and higher-value projects relative to the others.")




    # ---------------------------
# Create Tabs
# ---------------------------
tab1, tab2, tab3 = st.tabs([
    "Organization State",
    "Agency State",
    "Duration Days"
])


# ======================================================
# TAB 1: Organization State Choropleth
# ======================================================
with tab1:

    st.subheader("NIH Award Duration by Organization State (Animated by Year)")

    subset = df[df['Main_Organization'].isin(selected_orgs)]

    state_summary = (
        subset.groupby(['Main_Organization', 'organization_org_state', 'fiscal_year'], as_index=False)
        .agg(total_duration_days=('duration_days', 'sum'))
    )

    fig1 = px.choropleth(
        state_summary,
        locations='organization_org_state',
        locationmode='USA-states',
        color='total_duration_days',
        facet_col='Main_Organization',
        facet_col_wrap=2,
        animation_frame='fiscal_year',
        color_continuous_scale='Viridis',
        scope='usa',
        title='NIH Award Duration by Organization State',
        hover_name='organization_org_state',
    )

    fig1.update_coloraxes(cmin=0, cmax=state_summary['total_duration_days'].max())
    fig1.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    fig1.update_layout(
        geo=dict(showcoastlines=True, landcolor='lightgray'),
        title_font=dict(size=18),
        legend_title_text='Total Award ($)',
    )

    st.plotly_chart(fig1, use_container_width=True)


# ======================================================
# TAB 2: Agency State Choropleth
# ======================================================
with tab2:

    st.subheader("NIH Award Duration by Agency State (Animated by Year)")

    subset2 = df[df['Main_Organization'].isin(selected_orgs)]

    state_summary2 = (
        subset2.groupby(['Main_Organization', 'agency_state', 'fiscal_year'], as_index=False)
        .agg(total_duration_days=('duration_days', 'sum'))
    )

    fig2 = px.choropleth(
        state_summary2,
        locations='agency_state',
        locationmode='USA-states',
        color='total_duration_days',
        facet_col='Main_Organization',
        facet_col_wrap=2,
        animation_frame='fiscal_year',
        color_continuous_scale='Viridis',
        scope='usa',
        title='NIH Award Distribution by Agency State',
        hover_name='agency_state',
    )

    fig2.update_coloraxes(cmin=0, cmax=state_summary2['total_duration_days'].max())
    fig2.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

    fig2.update_layout(
        geo=dict(showcoastlines=True, landcolor='lightgray'),
        title_font=dict(size=18),
        legend_title_text='Total Award ($)',
    )

    st.plotly_chart(fig2, use_container_width=True)


# ======================================================
# TAB 3: Duration Days Distribution (Box Plot)
# ======================================================
with tab3:

    st.subheader("Duration Days Distribution by Main Organization")

    fig3 = px.box(
        df,
        x='Main_Organization',
        y='duration_days',
        color='Main_Organization',
        title='NIH Project duration days Distribution by Main Organization',
        labels={
            'duration_days': 'duration_days',
            'Main_Organization': 'Organization'
        },
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig3.update_layout(
        xaxis_title='Main Organization',
        yaxis_title='Duration Days',
        title_font=dict(size=18),
        showlegend=False,
        plot_bgcolor='white'
    )

    fig3.update_xaxes(categoryorder='median descending')

    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("NIH projects at the University of Pittsburgh tend to last significantly longer than those at Kaiser Permanente, Henry Ford Health, or Corewell Health.")



    st.header("Top 10 NIH Agencies — Award Amount & Duration Trends (Dark Theme)")

# Ensure fiscal_year is numeric
df['fiscal_year'] = df['fiscal_year'].astype(int)

# ===========================
# Aggregate base summary
# ===========================
agency_summary_award = (
    df.groupby(['agency_ic_admin_name', 'fiscal_year'], as_index=False)
    .agg(total_award_amount=('award_amount', 'sum'))
)

agency_summary_duration = (
    df.groupby(['agency_ic_admin_name', 'fiscal_year'], as_index=False)
    .agg(avg_duration_days=('duration_days', 'mean'))
)

# ===========================
# Identify Top 10 agencies by funding
# ===========================
top_agencies = (
    agency_summary_award.groupby('agency_ic_admin_name')['total_award_amount']
    .sum()
    .nlargest(10)
    .index
)

award_top10 = agency_summary_award[agency_summary_award['agency_ic_admin_name'].isin(top_agencies)]
duration_top10 = agency_summary_duration[agency_summary_duration['agency_ic_admin_name'].isin(top_agencies)]

# ===========================
# Create Tabs
# ===========================
tab1, tab2 = st.tabs(["Award Amount Over Years", "Duration Days Over Years"])

# Shared dark layout
dark_layout = dict(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(size=12, color='white'),
    title_font=dict(size=20, color='white'),
    legend=dict(font=dict(color='white')),
    xaxis=dict(color='white'),
    yaxis=dict(color='white')
)

# ======================================================
# TAB 1 — Award Amount Trend
# ======================================================
with tab1:
    st.subheader("Total Award Amount Over Fiscal Years (Top 10 Agencies)")

    fig_award = px.line(
        award_top10,
        x='fiscal_year',
        y='total_award_amount',
        color='agency_ic_admin_name',
        markers=True,
        title="Top 10 Agencies — Total Award Amount Over Time",
        labels={
            'fiscal_year': 'Fiscal Year',
            'total_award_amount': 'Total Award ($)',
            'agency_ic_admin_name': 'Agency'
        },
        color_discrete_sequence=px.colors.qualitative.Bold
    )

    fig_award.update_traces(line=dict(width=3))
    fig_award.update_layout(**dark_layout)
    fig_award.update_yaxes(tickformat=',.0f', color='white')
    fig_award.update_xaxes(type='category', color='white')

    st.plotly_chart(fig_award, use_container_width=True)
    st.markdown("The trends show that NIH funding has steadily increased across most major agencies over the past two decades, with notable peaks in recent years. Agencies such as the National Institute of Aging (NIA) and the National Cancer Institute (NCI) exhibit the largest growth, reflecting rising national priorities in aging research and oncology. Overall, the top agencies maintain consistent investment levels, indicating stable long-term funding commitments.")


# ======================================================
# TAB 2 — Duration Days Trend
# ======================================================
with tab2:
    st.subheader("Average Duration (Days) Over Fiscal Years (Top 10 Agencies)")

    fig_duration = px.line(
        duration_top10,
        x='fiscal_year',
        y='avg_duration_days',
        color='agency_ic_admin_name',
        markers=True,
        title="Top 10 Agencies — Project Duration Over Time",
        labels={
            'fiscal_year': 'Fiscal Year',
            'avg_duration_days': 'Average Duration (Days)',
            'agency_ic_admin_name': 'Agency'
        },
        color_discrete_sequence=px.colors.qualitative.Dark2
    )

    fig_duration.update_traces(line=dict(width=3))
    fig_duration.update_layout(**dark_layout)
    fig_duration.update_xaxes(type='category', color='white')
    fig_duration.update_yaxes(color='white')

    st.plotly_chart(fig_duration, use_container_width=True)
    st.markdown("The average duration of NIH-funded projects across the top 10 agencies remains relatively stable over the two-decade period, generally fluctuating between 380 and 460 days. While individual agencies experience occasional peaks and dips, no major long-term upward or downward trend is evident. This consistency suggests that NIH project timelines are fairly standardized, regardless of agency focus or funding volume.")



st.markdown("---")



df = pd.read_csv(os.path.join(DATA_DIR, "main_topic1.csv"))


# Convert types
df["Topic"] = df["Topic"].astype(str)
df["fiscal_year"] = df["fiscal_year"].astype(int)

st.markdown("### Top 10 Topics — Multi-Line Trends Over Fiscal Years")

# ============================
# Select Top 10 Topics
# ============================
topic_totals = (
    df.groupby("Topic")["award_amount_sum"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .index.tolist()
)

top10_df = df[df["Topic"].isin(topic_totals)]

# ============================
# Melt data in LONG format
# ============================
long_df = top10_df.melt(
    id_vars=["Topic", "fiscal_year"],
    value_vars=[
        "duration_days_sum",
        "duration_days_avg",
        "award_amount_sum",
        "award_amount_avg",
        "num_projects"
    ],
    var_name="metric",
    value_name="value"
)

# ============================
# Helper: Create line charts
# ============================
def plot_metric(metric_name, title, y_label):
    metric_df = long_df[long_df["metric"] == metric_name]

    fig = px.line(
        metric_df,
        x="fiscal_year",
        y="value",
        color="Topic",
        markers=True,
        title=title,
        labels={"fiscal_year": "Fiscal Year", "value": y_label}
    )
    fig.update_layout(
        height=500,
        legend_title_text="Topic",
        xaxis=dict(type="category")
    )
    return fig


# ============================
# Create Tabs
# ============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Duration Days (Sum)",
    "Duration Days (Average)",
    "Award Amount (Sum)",
    "Award Amount (Average)",
    "Number of Projects"
])


# ============================
# 1️⃣ Duration Days (Sum)
# ============================
with tab1:
    st.subheader("Sum of Duration Days — Top 10 Topics")
    fig1 = plot_metric(
        "duration_days_sum",
        "Duration Days (Sum) by Year — Top 10 Topics",
        "Duration Days (Sum)"
    )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown("The top NIH research topics show a strong upward trend in total project duration days from 2006 through 2010, followed by a noticeable contraction around 2011–2014. From 2015 onward, durations steadily rise again, peaking around 2020–2023 before dipping slightly in 2025. Topics such as Omics & Data Science, Population & Environmental Health, and Infectious & Immune Diseases consistently remain among the longest-duration research areas, indicating sustained large-scale programs.")


# ============================
# 2️⃣ Duration Days (Average)
# ============================
with tab2:
    st.subheader("Average Duration Days — Top 10 Topics")
    fig2 = plot_metric(
        "duration_days_avg",
        "Average Duration Days by Year — Top 10 Topics",
        "Duration Days (Avg)"
    )
    st.plotly_chart(fig2, use_container_width=True)
    st.markdown("Average project durations across the top NIH research topics remain highly consistent over the 20-year span, typically ranging between 400 and 440 days. Despite some short-term fluctuations, all topics follow a broadly similar pattern, with mild increases around 2009–2010 and again in 2019–2021. The recent downward shift after 2023 suggests either shorter project cycles or incomplete duration data for newer grants.")


# ============================
# 3️⃣ Award Amount (Sum)
# ============================
with tab3:
    st.subheader("Total Award Amount — Top 10 Topics")
    fig3 = plot_metric(
        "award_amount_sum",
        "Total Award Amount by Year — Top 10 Topics",
        "Award Amount (Sum)"
    )
    st.plotly_chart(fig3, use_container_width=True)
    st.markdown("Total NIH award amounts across the top 10 research topics show a strong upward trend from 2006 to 2010, followed by a noticeable dip in the early 2010s and a renewed surge after 2016. Topics such as Omics & Data Science, Population & Environmental Health, and Infectious & Immune Diseases consistently receive the highest funding. The sharp rise around 2020–2023 reflects heightened investment in large-scale, multidisciplinary research areas.")


# ============================
# 4️⃣ Award Amount (Average)
# ============================
with tab4:
    st.subheader("Average Award Amount — Top 10 Topics")
    fig4 = plot_metric(
        "award_amount_avg",
        "Average Award Amount by Year — Top 10 Topics",
        "Award Amount (Avg)"
    )
    st.plotly_chart(fig4, use_container_width=True)
    st.markdown("Average award amounts across the top NIH research topics show a steady long-term upward trend, rising from the mid-$300k range in 2006 to over $550k by 2025. While short-term fluctuations occur, especially around 2010 and 2018, all topics follow a similar growth trajectory. This consistent increase suggests expanding project scopes, higher research costs, and stronger NIH investment across major biomedical domains.")


# ============================
# 5️⃣ Number of Projects
# ============================
with tab5:
    st.subheader("Project Count — Top 10 Topics")
    fig5 = plot_metric(
        "num_projects",
        "Number of Projects by Year — Top 10 Topics",
        "Projects"
    )
    st.plotly_chart(fig5, use_container_width=True)
    st.markdown("The number of NIH-funded projects across the top research topics rises consistently from 2006 to 2010, followed by a noticeable dip in the early 2010s and a recovery beginning around 2016. Topics such as Omics & Data Science, Diagnostics & Therapeutics, and Population & Environmental Health consistently lead in project volume, reflecting broad research activity and diversified grant portfolios. The decline around 2024–2025 may indicate incomplete data or a shift toward fewer but larger projects.")



df = pd.read_csv(os.path.join(DATA_DIR, "disease_topic_summary_df.csv"))

# Convert datatypes
df["Topic"] = df["Topic"].astype(str)
df["fiscal_year"] = df["fiscal_year"].astype(int)

# ============================
# Select Top 10 Topics (by award_amount_sum)
# ============================
topic_totals = (
    df.groupby("Topic")["award_amount_sum"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .index.tolist()
)

top10_df = df[df["Topic"].isin(topic_totals)]

# ============================
# Melt into LONG FORMAT
# ============================
long_df = top10_df.melt(
    id_vars=["Topic", "fiscal_year"],
    value_vars=[
        "duration_days_sum",
        "duration_days_avg",
        "award_amount_sum",
        "award_amount_avg",
        "num_projects"
    ],
    var_name="metric",
    value_name="value"
)

# ============================
# Line chart helper
# ============================
def plot_metric(metric_name, title, y_label):
    metric_df = long_df[long_df["metric"] == metric_name]

    fig = px.line(
        metric_df,
        x="fiscal_year",
        y="value",
        color="Topic",
        markers=True,
        title=title,
        labels={"fiscal_year": "Fiscal Year", "value": y_label}
    )
    fig.update_layout(
        height=500,
        legend_title_text="Disease Topic",
        xaxis=dict(type="category")
    )
    return fig


# ============================
# Create Tabs
# ============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Duration Days (Sum)",
    "Duration Days (Average)",
    "Award Amount (Sum)",
    "Award Amount (Average)",
    "Number of Projects"
])


# ============================
# 1️⃣ Duration Days (Sum)
# ============================
with tab1:
    st.subheader("Total Duration Days — Top 10 Disease Sub-Topics")
    st.plotly_chart(
        plot_metric(
            "duration_days_sum",
            "Duration Days (Sum) by Year — Top 10 Disease Topics",
            "Duration Days (Sum)"
        ),
        use_container_width=True
    )
    st.markdown("The total duration days for the top disease-focused research areas show a clear rise from 2006 to a peak around 2009–2010, followed by a gradual decline through 2014 and a steady recovery after 2016. Environmental Health / Exposure / Toxicology consistently dominates in total duration, suggesting longer and more resource-intensive projects. Other major topics like Autoimmunity, Neurology, and Endocrine/Metabolic disorders follow similar cyclical patterns, reflecting shifts in long-term research activity.")


# ============================
# 2️⃣ Duration Days (Average)
# ============================
with tab2:
    st.subheader("Average Duration Days — Top 10 Disease Sub-Topics")
    st.plotly_chart(
        plot_metric(
            "duration_days_avg",
            "Average Duration Days by Year — Top 10 Disease Topics",
            "Duration Days (Avg)"
        ),
        use_container_width=True
    )
    st.markdown("The average project duration across the top 10 disease-focused topics remains relatively stable year over year, generally fluctuating within a narrow band of ~400–440 days. A few topics (e.g., Neurology, Aging, Metabolic/Endocrine) show slightly higher peaks at times, but no disease area consistently dominates. Most disease topics follow a similar temporal pattern, suggesting that NIH project duration standards are fairly uniform across research areas. The noticeable decline around 2024–2025 indicates project completion cycles or reduced durations in recent awards.")


# ============================
# 3️⃣ Award Amount (Sum)
# ============================
with tab3:
    st.subheader("Total Award Amount — Top 10 Disease Sub-Topics")
    st.plotly_chart(
        plot_metric(
            "award_amount_sum",
            "Award Amount (Sum) by Year — Top 10 Disease Topics",
            "Award Amount (Sum)"
        ),
        use_container_width=True
    )
    st.markdown("The distribution shows that Environmental Health / Exposure / Toxicology consistently receives the largest total funding among the disease topics across years, with a noticeable rise after 2018. Most other disease areas follow a steady but modest upward trend, indicating balanced growth across multiple biomedical priorities. The widening gap in recent years highlights how environmental and exposure-related research has become a major funding focus within NIH's disease-oriented portfolio.")



# ============================
# 4️⃣ Award Amount (Average)
# ============================
with tab4:
    st.subheader("Average Award Amount — Top 10 Disease Sub-Topics")
    st.plotly_chart(
        plot_metric(
            "award_amount_avg",
            "Award Amount (Average) by Year — Top 10 Disease Topics",
            "Award Amount (Avg)"
        ),
        use_container_width=True
    )
    st.markdown("The average award amount shows a steady upward trend across nearly all disease research areas from 2006 to 2025, reflecting increasing NIH investment over time. Peaks around 2020–2025 appear across multiple disease categories, particularly in Aging/Alzheimer's, Oncology, Neurology, and Endocrine/Metabolic fields. Despite year-to-year fluctuations, most disease topics converge toward higher funding averages in recent years, suggesting broad strengthening of NIH support across research domains. This consistent rise highlights growing prioritization of biomedical and public health research needs.")


# ============================
# 5️⃣ Number of Projects
# ============================
with tab5:
    st.subheader("Project Count — Top 10 Disease Sub-Topics")
    st.plotly_chart(
        plot_metric(
            "num_projects",
            "Number of Projects by Year — Top 10 Disease Topics",
            "Projects"
        ),
        use_container_width=True
    )
    st.markdown("The chart shows a clear leadership of Environmental Health / Exposure / Toxicology, which consistently maintains the highest number of projects across all years. Most other disease areas follow similar cyclical patterns, peaking around 2009–2010 and again after 2017, reflecting broader NIH funding cycles. While some categories—like Autoimmunity, Neurology, and Oncology—show gradual long-term growth, the widening gap highlights the sustained priority placed on environmental and exposure-related research.")



df = pd.read_csv(os.path.join(DATA_DIR, "method_topic_summary_df.csv"))

# Convert datatypes
df["Method_Topic"] = df["Method_Topic"].astype(str)
df["fiscal_year"] = df["fiscal_year"].astype(int)

st.markdown("### Total Duration Days — Top 10 Method Sub-Topics")

# ============================
# Select Top 10 Method Topics
# ============================
top_methods = (
    df.groupby("Method_Topic")["award_amount_sum"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
      .index.tolist()
)

top10_df = df[df["Method_Topic"].isin(top_methods)]

# ============================
# Melt into LONG FORMAT
# ============================
long_df = top10_df.melt(
    id_vars=["Method_Topic", "fiscal_year"],
    value_vars=[
        "duration_days_sum",
        "duration_days_avg",
        "award_amount_sum",
        "award_amount_avg",
        "num_projects"
    ],
    var_name="metric",
    value_name="value"
)

# ============================
# Line chart helper
# ============================
def plot_metric(metric_name, title, y_label):
    metric_df = long_df[long_df["metric"] == metric_name]

    fig = px.line(
        metric_df,
        x="fiscal_year",
        y="value",
        color="Method_Topic",
        markers=True,
        title=title,
        labels={"fiscal_year": "Fiscal Year", "value": y_label}
    )
    fig.update_layout(
        height=500,
        legend_title_text="Method Topic",
        xaxis=dict(type="category")
    )
    return fig


# ============================
# Create Tabs
# ============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Duration Days (Sum)",
    "Duration Days (Average)",
    "Award Amount (Sum)",
    "Award Amount (Average)",
    "Number of Projects"
])


# ============================
# 1️⃣ Duration Days (Sum)
# ============================
with tab1:
    st.subheader("Total Duration Days — Top 10 Method Topics")
    st.plotly_chart(
        plot_metric(
            "duration_days_sum",
            "Duration Days (Sum) by Year — Top 10 Method Topics",
            "Duration Days (Sum)"
        ),
        use_container_width=True
    )
    st.markdown("The chart shows that Genomics/Genetics/Sequencing and Machine Learning / AI / Data Science consistently contribute the highest total duration days, reflecting their central role in modern biomedical research. Methods like Systems/Cell/Molecular Biology and Drug Discovery/Pharmacology follow closely, showing steady long-term investment. Most method categories exhibit a rise around 2008–2010, a dip, and then another climb after 2017, mirroring broader NIH funding cycles. Overall, the trends highlight NIH's sustained emphasis on foundational molecular methods and rapidly growing data-driven research approaches.")


# ============================
# 2️⃣ Duration Days (Average)
# ============================
with tab2:
    st.subheader("Average Duration Days — Top 10 Method Topics")
    st.plotly_chart(
        plot_metric(
            "duration_days_avg",
            "Average Duration Days by Year — Top 10 Method Topics",
            "Duration Days (Avg)"
        ),
        use_container_width=True
    )
    st.markdown("The average duration days for method-based projects remain remarkably stable across all topics, generally hovering between 390–450 days each year. Despite minor fluctuations, no method shows a strong upward or downward long-term trend, indicating consistent project timelines across methodological areas. Peaks around 2009–2010 and again around 2018–2020 align with broader NIH funding surges. Overall, the uniformity suggests that method type has little influence on project duration, with most methods following similar lifecycle lengths.")


# ============================
# 3️⃣ Award Amount (Sum)
# ============================
with tab3:
    st.subheader("Total Award Amount — Top 10 Method Topics")
    st.plotly_chart(
        plot_metric(
            "award_amount_sum",
            "Total Award Amount by Year — Top 10 Method Topics",
            "Award Amount (Sum)"
        ),
        use_container_width=True
    )
    st.markdown("The funding for different research methods has generally increased over the years. Topics like AI/ML, genomics, and drug discovery show especially strong growth, meaning these areas are becoming more important. Even though the amounts go up and down slightly each year, the overall trend shows more investment in modern, technology-driven research methods.")


# ============================
# 4️⃣ Award Amount (Average)
# ============================
with tab4:
    st.subheader("Average Award Amount — Top 10 Method Topics")
    st.plotly_chart(
        plot_metric(
            "award_amount_avg",
            "Average Award Amount by Year — Top 10 Method Topics",
            "Award Amount (Avg)"
        ),
        use_container_width=True
    )
    st.markdown("The chart shows that funding for the top 10 method-based research areas has generally increased over time, even though there are small ups and downs in certain years. Methods such as AI/ML, genomics and sequencing, and drug discovery/pharmacology receive noticeably higher growth, indicating that these areas are becoming more important in modern research. Overall, the trend suggests that NIH is steadily investing more in advanced, technology-driven, and translational research methods.")


# ============================
# 5️⃣ Number of Projects
# ============================
with tab5:
    st.subheader("Project Count — Top 10 Method Topics")
    st.plotly_chart(
        plot_metric(
            "num_projects",
            "Number of Projects by Year — Top 10 Method Topics",
            "Projects"
        ),
        use_container_width=True
    )
    st.markdown("The chart shows that the number of NIH-funded projects across the top 10 method topics has generally increased over the years, with Machine Learning/AI, Genomics/Sequencing, and Systems/Cell/Molecular Biology consistently leading in project volume. Most method areas show steady growth, small fluctuations, and a noticeable rise after 2016, indicating expanding research activity. Overall, the upward trend suggests that NIH is funding more projects in advanced, technology-focused methods, reflecting growing interest and investment in these scientific approaches.")
st.markdown("---")


# ============================================================================
# Conclusion
# ============================================================================
st.markdown("### Conclusion")
st.markdown("Across NIH-funded research, clear patterns emerge in how award amounts, project durations, and project volumes evolve over time. Both disease-focused and method-focused topics show steady growth, with especially strong increases in areas such as AI/ML, genomics, drug discovery, neuroscience, and aging-related research. Funding trends and project counts highlight NIH's shift toward technology-driven, data-intensive, and translational research, while the distribution of award sizes and durations across organizations and agencies reflects differing strategic priorities and research strengths. Overall, the analysis provides a comprehensive view of how NIH invests across scientific domains—helping organizations like Corewell Health identify opportunities, align research priorities, and plan strategically for future funding.")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <small>
    NIH Grants Competitive Intelligence | Corewell Health Capstone Project<br>
    Michigan State University | Data Science MS Program
    </small>
</div>
""", unsafe_allow_html=True)
