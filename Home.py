"""
===============================================================================
NIH RESEARCH GRANTS ANALYSIS - HOME PAGE
===============================================================================
Main entry point for the multi-page Streamlit application.
Corewell Health Capstone Project | Michigan State University
===============================================================================
"""

import streamlit as st

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="NIH Research Grants Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# CUSTOM CSS
# ============================================================================

st.markdown("""
    <style>
    .main {padding: 2rem;}
    .stMetric {background-color: #f0f2f6; padding: 15px; border-radius: 10px;}
    h1 {color: #1f77b4; text-align: center;}
    h2 {color: #2ca02c;}
    h3 {color: #d62728;}
    .big-stat {font-size: 48px; font-weight: bold; color: #1f77b4; text-align: center;}
    .intro-box {
        background-color: #f8f9fa;
        border-left: 5px solid #1f77b4;
        padding: 20px;
        margin: 20px 0;
        border-radius: 5px;
    }
    .team-box {
        background-color: #e8f4f8;
        padding: 15px;
        margin: 10px 0;
        border-radius: 8px;
        border: 2px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================

st.title("NIH Research Grants Analysis")
st.markdown("### Comprehensive Intelligence Dashboard for Grant Competitiveness")
st.markdown("**Corewell Health Capstone Project | Michigan State University**")

st.markdown("---")

# ============================================================================
# PROJECT OVERVIEW
# ============================================================================

st.markdown('<div class="intro-box">', unsafe_allow_html=True)
st.markdown("## Project Overview")

st.markdown("""
This comprehensive analytics platform provides strategic insights into NIH research grant patterns,
funding trends, and competitive intelligence to support **Corewell Health's** research strategy and
grant proposal optimization.

**Key Objectives:**
- Identify high-value funding opportunities and emerging research priorities
- Analyze award patterns across institutions, research topics, and PI demographics
- Benchmark Corewell Health against peer healthcare systems
- Understand foundation grant distributions and strategic giving patterns
- Track temporal trends in funding amounts, project durations, and research focus areas
""")
st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# KEY HIGHLIGHTS
# ============================================================================

st.markdown("## What You'll Find Here")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="team-box">', unsafe_allow_html=True)
    st.markdown("### Foundation Grants Analysis")
    st.markdown("""
    **Comprehensive analysis of foundation giving patterns:**
    - 4 major healthcare systems compared
    - State-level geographic distribution
    - Category-based grant analysis
    - Statistical testing & transformations
    - Time series trends (2006-2025)
    - $500M+ in total grants analyzed
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="team-box">', unsafe_allow_html=True)
    st.markdown("### NIH Awards Analysis")
    st.markdown("""
    **Deep dive into NIH funding dynamics:**
    - Award size & duration patterns
    - Organization & agency comparisons
    - Top 10 research topics & diseases
    - Method-based funding trends
    - Geographic funding distribution
    - 20 years of NIH grant data
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="team-box">', unsafe_allow_html=True)
    st.markdown("### Advanced Analytics")
    st.markdown("""
    **Research themes, portfolio & predictions:**
    - Q1: Research themes (Disease & Methods)
    - Q2: Institutional funding comparison
    - Q3: Portfolio evolution over time
    - Q4: Predictive features for grant size
    - Q6: Top topics & institutional strengths
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# ============================================================================
# ORGANIZATIONS ANALYZED
# ============================================================================

st.markdown("## Healthcare Systems Analyzed")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Corewell Health", "Primary Focus", delta="MI-based")

with col2:
    st.metric("Henry Ford Health", "Peer Comparison", delta="MI-based")

with col3:
    st.metric("Kaiser Permanente", "National Leader", delta="CA-based")

with col4:
    st.metric("University of Pittsburgh", "Academic Benchmark", delta="PA-based")

st.markdown("---")

# ============================================================================
# HOW TO USE THIS DASHBOARD
# ============================================================================

st.markdown("## How to Navigate This Dashboard")

st.markdown("""
1. **Use the sidebar** (top-left) to navigate between 7 analysis pages
2. **Page 1 - Foundation Grants**: Explore foundation giving patterns, geographic distributions, and statistical insights
3. **Page 2 - NIH Awards**: Dive into NIH funding trends by topic, disease area, research method, and institution
4. **Page 3 - Q1 Research Themes**: Analyze disease/organ-system areas and methods/modalities (58 categories)
5. **Page 4 - Q2 Institutional Funding**: Compare funding across 4 institutions in disease and methods domains
6. **Page 5 - Q3 Portfolio Evolution**: Track funding trends, mechanism shifts, and portfolio changes over time
7. **Page 6 - Q4 Predictive Features**: Discover key features that predict grant size and success
8. **Page 7 - Q6 Top Topics**: Identify top 15 research topics and institutional domain strengths
9. **Interactive Visualizations**: All charts are interactive - hover for details, zoom, and download as needed

**Tip:** Start with Foundation Grants or Q1 Research Themes for high-level overviews, then explore specific pages for targeted insights.
""")

st.markdown("---")

# ============================================================================
# KEY INSIGHTS PREVIEW
# ============================================================================

st.markdown("## Key Insights Preview")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Foundation Grants Highlights")
    st.markdown("""
    - **Right-skewed distributions** across all organizations
    - **Healthcare & Community Development** dominate grant categories
    - **Geographic concentration** in organization home states
    - **Statistical significance** in asset-to-grant-size correlations
    - **Positive correlation** between grant count and total funding
    """)

with col2:
    st.markdown("### NIH Awards Highlights")
    st.markdown("""
    - **Steady funding growth** across top agencies (NIA, NCI leading)
    - **AI/ML & Genomics** show strongest award amount increases
    - **Environmental Health** consistently receives largest funding
    - **Average award amounts** rising from $300K (2006) to $550K (2025)
    - **University of Pittsburgh** shows widest award distribution range
    """)

st.markdown("---")

# ============================================================================
# CALL TO ACTION
# ============================================================================

st.info("""
**Get Started:** Select an analysis page from the sidebar to begin exploring the data.

Each page contains detailed visualizations, statistical analyses, and actionable insights for strategic decision-making.
""")

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <small>
    <b>NIH Research Grants Analysis Dashboard</b><br>
    Corewell Health Capstone Project | Michigan State University<br>
    Data Science MS Program | 2025<br>
    <i>Empowering research strategy through data-driven insights</i>
    </small>
</div>
""", unsafe_allow_html=True)
