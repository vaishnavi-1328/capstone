"""
===============================================================================
Q3: PORTFOLIO EVOLUTION & STRATEGIC POSITIONING
===============================================================================
How have NIH funding patterns, grant mechanisms, and research priorities 
evolved from 2006-2025?

Analysis covers:
- Overall growth trends (volume, size, funding)
- Grant mechanism evolution (R01, K-series, etc.)
- Research area intensity patterns
- Strategic positioning for future investment
===============================================================================
"""

import streamlit as st
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Q3: Portfolio Evolution",
    page_icon="📊",
    layout="wide"
)

# Get image directory (relative to this file)
CURRENT_DIR = Path(__file__).parent
IMG_DIR = CURRENT_DIR / "images"

# Check if images directory exists
if not IMG_DIR.exists():
    st.error(f"❌ Images directory not found: {IMG_DIR}")
    st.stop()

# ============================================================================
# BUSINESS NARRATIVE
# ============================================================================

st.title("Q3: Portfolio Evolution & Strategic Positioning")

st.markdown("### Why This Matters for Corewell Health")

st.markdown("""
**Research Question:** How have NIH award types, funding amounts, and research priorities 
shifted over time (2006-2025) across institutions and research areas?

**Strategic Value:**
- **Portfolio Planning**: Understand long-term trends in grant volume and size
- **Mechanism Strategy**: Identify optimal mix of R01, K-series, and other grant types
- **Research Focus**: Pinpoint growing vs. declining research areas
- **Competitive Intelligence**: Compare Corewell's evolution against peer institutions
""")

# ============================================================================
# KEY INSIGHTS
# ============================================================================

st.markdown("---")
st.markdown("### 🔑 Key Insights from 20-Year Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Portfolio Consolidation:**")
    st.metric("Trend", "Fewer, Larger Grants")
    st.markdown("Grant counts declined but average size increased 45%")

with col2:
    st.markdown("**Mechanism Shift:**")
    st.metric("R01 Dominance", "~40% Stable")
    st.markdown("K-series declining, exploratory grants growing")

with col3:
    st.markdown("**Research Focus:**")
    st.metric("Top Area", "Neuroscience")
    st.markdown("Neurological research leads in both activity and funding")

st.markdown("""
**Business Recommendation:**

Our 20-year analysis reveals:
1. **Strategic consolidation** - Fewer grants with higher average awards indicates quality over quantity
2. **Stable R01 focus** - Traditional research grants remain the portfolio foundation (~40%)
3. **Neuroscience dominance** - Neurological research shows highest intensity and funding
4. **Growth opportunities** - Omics & Data Science emerging as high-activity areas
""")

# ============================================================================
# MAIN CONTENT TABS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Portfolio Evolution Analysis")

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overall Growth Trends",
    "🎯 Grant Mechanisms",
    "🔬 Research Area Heatmaps",
    "⭐ Strategic Positioning"
])

# ============================================================================
# TAB 1: OVERALL GROWTH TRENDS
# ============================================================================

with tab1:
    st.markdown("## Overall Growth: Volume, Size, and Funding (2006-2025)")
    
    st.markdown("""
    **Analysis Question:** How have grant volumes, average sizes, and total funding 
    evolved over the past 20 years across all four institutions?
    
    **Key Metrics:**
    - Grant Count: Number of active grants per year
    - Average Grant Size: Mean award amount per grant
    - Total Funding: Aggregate dollars awarded annually
    """)
    
    # Chart 1: Dual Axis
    st.markdown("### Grant Volume vs. Average Size Trend")
    img_path = IMG_DIR / "q3_2_dual_axis_count_size.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** Clear inverse relationship - as grant counts declined from peak in 2009 
        (~1750 grants), average grant sizes increased steadily from ~$370K to ~$590K by 2025. 
        This reflects **portfolio consolidation**: institutions pursuing fewer, more substantial awards.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Chart 2: Total Funding by Institution
    st.markdown("### Total Funding Trends by Institution")
    img_path = IMG_DIR / "q3_2_total_funding_line.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **UPMC dominates** with $600-750M annually (largest academic portfolio)
        - **Kaiser steady** at ~$100-130M (focused clinical research)
        - **Henry Ford growing** from $20M to $60M (3x increase since 2006)
        - **Corewell stable** at $20-40M (consistent niche positioning)
        
        **Strategic Takeaway:** Each institution has distinct scale, but all show sustained 
        NIH engagement over 20 years.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Chart 3: Average Grant Size
    st.markdown("### Average Grant Size by Institution")
    st.markdown("Are grants getting bigger or smaller?")
    img_path = IMG_DIR / "q3_avg_grant_size_trends.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **All institutions show upward trend** in average grant size (2006-2025)
        - **UPMC leads** with highest average (~$560K in 2025)
        - **Corewell converging** toward peer levels (~$580K in 2025)
        - **Henry Ford spike** in 2023 (~$910K) suggests large program grants
        
        **Strategic Implication:** Rising grant sizes across the board indicates NIH shift 
        toward larger, more comprehensive research projects. Corewell is keeping pace.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")

# ============================================================================
# TAB 2: GRANT MECHANISMS
# ============================================================================

with tab2:
    st.markdown("## Grant Mechanism Evolution: R01, K-series, P-series, and More")
    
    st.markdown("""
    **Analysis Question:** How has the portfolio composition shifted across different 
    NIH grant mechanisms over 20 years?
    
    **Grant Mechanisms:**
    - **R01**: Traditional research project grants (most common)
    - **K-series**: Career development awards for early investigators
    - **P-series**: Program project and center grants (large, multi-PI)
    - **U-series**: Cooperative agreements (NIH collaborative)
    - **R21**: Exploratory/developmental research
    - **Other**: SBIR, training grants, and specialized mechanisms
    """)
    
    # Chart 1: Mechanism Distribution Stacked
    st.markdown("### Portfolio Composition Over Time")
    st.markdown("Percentage distribution shows shifting priorities")
    img_path = IMG_DIR / "q3_mechanism_distribution_stacked.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **R01 remarkably stable** at ~40% across entire 20-year period
        - **P-series declining** from ~20% (2006) to ~15% (2025)
        - **K-series relatively stable** at ~10%
        - **U-series growing** from ~10% to ~15% (increased collaborations)
        - **Other mechanisms expanding** (SBIR, small business research)
        
        **Strategic Takeaway:** R01 remains the portfolio backbone, but diversification 
        into cooperative agreements (U-series) reflects more collaborative research models.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Chart 2: Mechanism Trends Line
    st.markdown("### Mechanism Trends Over Time")
    st.markdown("Absolute grant counts by mechanism")
    img_path = IMG_DIR / "q3_mechanism_trends_line.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **R01 peaked ~2009** at 750 grants, now ~620-650 (portfolio consolidation)
        - **K-series declining** from ~180 to ~100 grants (career development shift)
        - **P-series volatile** but trending down (large center grants becoming rarer)
        - **Other mechanisms growing** steadily (diversification)
        
        **Strategic Implication:** Declining K-series suggests fewer early-career awards 
        or longer tenure before independence. Growing "Other" category indicates emergence 
        of new funding mechanisms.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Chart 3: Mechanism Shift Comparison
    st.markdown("### Institutional Mechanism Pivots (2010-2015 vs 2020-2025)")
    st.markdown("How did grant portfolios shift over time?")
    img_path = IMG_DIR / "q3_mechanism_shift_comparison.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight (Log Scale):** 
        - **UPMC dominates all mechanisms** (10-100x larger than peers)
        - **R01 growth across all institutions** (darker bars in 2020-2025)
        - **K-series mixed results** - some institutions growing, others declining
        - **P-series relatively stable** for larger institutions
        - **Small business (SBIR) minimal** for all health systems
        
        **Strategic Takeaway:** Log scale reveals that while UPMC has absolute volume advantage, 
        **growth patterns are similar** across institutions. All show R01 emphasis in recent period.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Chart 4: Total Funding Log Scale
    st.markdown("### Total Funding by Institution (Log Scale)")
    st.markdown("Shows Corewell trends clearly despite size difference vs UPMC")
    img_path = IMG_DIR / "q3_total_funding_by_institution.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **Log scale reveals growth trajectories** that are hidden in linear charts
        - **Corewell shows steady upward trend** from ~$3M to ~$5M (log scale)
        - **Henry Ford stronger growth** from ~$2M to ~$5.5M
        - **Kaiser stable** around $100M throughout period
        - **UPMC consistent leader** with gradual growth
        
        **Strategic Takeaway:** Despite vastly different scales, Corewell's growth rate 
        is visible and competitive with peers. The gap is size, not trajectory.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")

# ============================================================================
# TAB 3: RESEARCH AREA HEATMAPS
# ============================================================================

with tab3:
    st.markdown("## Research Area Intensity: Where Is Activity Concentrated?")
    
    st.markdown("""
    **Analysis Question:** Which research areas show highest activity (grant count) 
    and funding intensity over the 2007-2025 period?
    
    **Heatmap Interpretation:**
    - **Darker colors** = Higher intensity (more grants or more funding)
    - **Lighter colors** = Lower intensity
    - **Patterns over time** reveal strategic shifts in research priorities
    
    We examine both:
    - **Top-Level**: 9 broad disease/method categories
    - **Sub-Level**: 15 specific research areas for detailed view
    """)
    
    # Heatmap 1: Top-Level Grant Count
    st.markdown("### Top-Level Research Activity (Grant Count, 2007-2025)")
    img_path = IMG_DIR / "1_heatmap_top_grant_count.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **Omics & Data Science**: Highest activity (1100-1300 grants) - green throughout
        - **Population & Environmental Health**: Second highest (1000-1200 grants)
        - **Neurological Research**: Consistent activity (~850-980 grants)
        - **Oncology & Genetic Diseases**: Lowest activity (~300-350 grants) - red shading
        
        **Strategic Takeaway:** Data science and population health dominate research 
        activity, reflecting modern emphasis on big data and public health.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Heatmap 2: Top-Level Funding
    st.markdown("### Top-Level Research Funding Intensity ($ Millions, 2007-2025)")
    img_path = IMG_DIR / "2_heatmap_top_funding.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **Omics & Data Science**: Highest funding ($600-780M in peak years) - dark blue
        - **Population & Environmental Health**: Strong funding ($500-720M)
        - **Diagnostics & Therapeutics**: Consistent mid-range funding ($400-660M)
        - **Infectious & Immune Diseases**: Lower funding despite importance
        
        **Strategic Takeaway:** Funding intensity doesn't always match grant count. 
        Some areas have fewer but larger grants. Omics/Data Science leads in both metrics.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Heatmap 3: Sub-Level Grant Count
    st.markdown("### Sub-Level Research Activity (15 Specific Areas, 2007-2025)")
    img_path = IMG_DIR / "3_heatmap_sub_grant_count.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **Systems/Cell/Molecular Biology**: Highest activity (800-950 grants) - dark green
        - **Drug Discovery/Pharmacology**: High activity (600-680 grants)
        - **Health Services/Outcomes**: Growing activity over time
        - **Aging/Geriatrics**: Notably absent (NaN) - not tracked or no grants
        - **Clinical Trials**: Lower activity (300-400 grants) - orange/red
        
        **Strategic Takeaway:** Basic science (systems biology) dominates, while clinical 
        translation (trials) shows lower activity. Gap suggests opportunity for translational focus.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Heatmap 4: Sub-Level Funding
    st.markdown("### Sub-Level Research Funding Intensity ($ Millions, 2007-2025)")
    img_path = IMG_DIR / "4_heatmap_sub_funding.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight:** 
        - **Systems/Cell/Molecular Biology**: Highest funding ($400-500M) - dark blue
        - **Drug Discovery**: Strong funding ($300-400M)
        - **Health Services/Outcomes**: Growing funding intensity (2015-2025)
        - **Clinical Trials/Translational**: Moderate funding ($200-310M)
        - **Biophysics/Biochemistry**: Consistent mid-range funding
        
        **Strategic Takeaway:** Basic science commands highest dollars per grant. 
        Health services research showing upward funding trend reflects healthcare delivery focus.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")

# ============================================================================
# TAB 4: STRATEGIC POSITIONING
# ============================================================================

with tab4:
    st.markdown("## ⭐ Strategic Positioning: Where to Invest? (2023-2025 Focus)")
    
    st.markdown("""
    **Analysis Question:** Based on recent 3-year trends (2023-2025), which research 
    areas should Corewell prioritize for investment?
    
    **Strategic Framework - Portfolio Quadrants:**
    - 🟢 **STARS** (High Activity + Growing): INVEST MORE - Winners with momentum
    - 🔵 **CASH COWS** (High Activity + Stable): MAINTAIN - Reliable core areas
    - 🟠 **QUESTION MARKS** (Low Activity + Growing): MONITOR - Emerging opportunities
    - 🔴 **DOGS** (Low Activity + Declining): CONSIDER EXIT - Limited ROI potential
    
    **How to Read Quadrant Charts:**
    - **X-axis**: % change in activity/funding (2023→2025)
    - **Y-axis**: 2025 absolute level (grants or dollars)
    - **Color**: Strategic classification
    """)
    
    st.markdown("---")
    
    # Quadrant 1: Top-Level Grant Count
    st.markdown("### Top-Level Research Activity Portfolio (Grant Count)")
    st.markdown("Which broad areas are growing vs. declining?")
    img_path = IMG_DIR / "9_quadrant_top_grant_count.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight - Strategic Classification:**
        
        🟢 **STARS (Invest More):**
        - None clearly identified (no areas in top-right quadrant)
        
        🔵 **CASH COWS (Maintain):**
        - **Omics & Data Science** (~1100 grants, stable)
        - **Population & Environmental Health** (~1000 grants, slight decline)
        - **Molecular & Cellular Biology** (~1000 grants, declining)
        - **Diagnostics & Therapeutics** (~980 grants, declining)
        
        🟠 **QUESTION MARKS (Monitor):**
        - None visible (no low-activity growing areas)
        
        🔴 **DOGS (Consider Reducing):**
        - **Infectious & Immune Diseases** (~600 grants, declining -10%)
        - **Cardiometabolic & Endocrine** (~440 grants, declining -15%)
        - **Oncology & Genetic Diseases** (~310 grants, declining -12%)
        
        **Strategic Recommendation:** Portfolio shows **consolidation pattern** - most areas 
        stable or declining. No clear growth stars. Consider investing in external growth 
        opportunities or pivoting existing portfolios.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Quadrant 2: Top-Level Funding
    st.markdown("### Top-Level Funding Portfolio ($ Millions)")
    st.markdown("Which broad areas command highest dollars and growth?")
    img_path = IMG_DIR / "7_quadrant_top_funding.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight - Strategic Classification:**
        
        🟢 **STARS (Invest More):**
        - None clearly identified (all declining)
        
        🔵 **CASH COWS (Maintain):**
        - **Omics & Data Science** ($162M, declining -40%)
        - **Population & Environmental Health** ($155M, declining -50%)
        - **Diagnostics & Therapeutics** ($134M, declining -45%)
        - **Neurological Research** ($131M, declining -37%)
        
        🟠 **QUESTION MARKS (Monitor):**
        - None visible
        
        🔴 **DOGS (Consider Reducing):**
        - **Infectious & Immune Diseases** ($79M, declining -32%)
        - **Cardiometabolic & Endocrine** ($73M, declining -65%)
        - **Oncology & Genetic Diseases** ($44M, declining -60%)
        
        **Strategic Recommendation:** **Entire portfolio declining in 2023-2025** - 
        reflects post-COVID normalization and reduced emergency funding. Focus on maintaining 
        Cash Cows while seeking external growth catalysts.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Quadrant 3: Sub-Level Funding
    st.markdown("### Sub-Level Funding Portfolio (15 Specific Areas)")
    st.markdown("Detailed strategic view of specific research domains")
    img_path = IMG_DIR / "8_quadrant_sub_funding.png"
    if img_path.exists():
        st.image(str(img_path), use_column_width=True)
        st.markdown("""
        **Key Insight - Strategic Classification:**
        
        🟢 **STARS (Invest More):**
        - None identified (all areas declining or stable)
        
        🔵 **CASH COWS (Maintain):**
        - **Systems/Cell/Molecular Biology** ($100M, highest funding)
        - **Health Services/Outcomes** ($86M, stable)
        - **Drug Discovery/Pharmacology** ($79M, declining -30%)
        - **Genomics/Genetics/Sequencing** ($73M, declining -25%)
        - **Neurology/Neuroscience** ($66M, declining -30%)
        
        🟠 **QUESTION MARKS (Monitor):**
        - Most specific areas fall here - low funding but some growth potential
        
        🔴 **DOGS (Consider Reducing):**
        - **Clinical Trials/Translational** ($31M, declining -68%)
        - **Cardiovascular** ($39M, declining -30%)
        - **Endocrine/Metabolic/Diabetes** ($40M, declining -40%)
        - **Oncology (Cancer)** ($42M, declining -35%)
        
        **Strategic Recommendation:** **Systems biology** and **health services research** 
        are stable high-value areas. Clinical translation severely declining - potential gap 
        or strategic pivot away from bedside research. Consider whether this aligns with 
        institutional mission.
        """)
    else:
        st.warning(f"Image not found: {img_path.name}")
    
    st.markdown("---")
    
    # Summary Insights
    st.markdown("### 🎯 Strategic Summary & Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Portfolio Strengths:**
        - Strong foundation in Omics & Data Science
        - Stable systems biology expertise
        - Diversified mechanism portfolio (R01 backbone)
        - Sustained 20-year NIH engagement
        """)
    
    with col2:
        st.markdown("""
        **Areas of Concern:**
        - No clear growth "Stars" in 2023-2025
        - Post-COVID portfolio consolidation
        - Declining clinical translation funding
        - Infectious disease research declining
        """)
    
    st.markdown("""
    **Strategic Recommendations for Corewell Health:**
    
    1. **Maintain Core Excellence**: Double down on Cash Cow areas (Omics, Systems Biology, 
       Health Services) where Corewell has demonstrated consistent performance
    
    2. **Seek External Growth Catalysts**: With internal portfolio consolidating, identify 
       emerging opportunities outside current classification (e.g., AI in healthcare, 
       long COVID research, health equity initiatives)
    
    3. **Evaluate Clinical Translation Gap**: Declining clinical trials funding may indicate 
       strategic shift. Assess whether this aligns with institutional mission or represents 
       an opportunity for differentiation
    
    4. **Monitor Emerging Mechanisms**: Growing "Other" category in grant mechanisms suggests 
       new NIH funding pathways. Investigate and position for early advantage
    
    5. **Leverage Portfolio Insights for Proposals**: Use predictability patterns from 
       heatmaps to optimize proposal keywords and positioning in high-success areas
    """)

# ============================================================================
# FOOTER
# ============================================================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <small>
    NIH Grants Competitive Intelligence | Corewell Health Capstone Project<br>
    Michigan State University | Data Science MS Program<br>
    Portfolio Analysis: 20-Year Longitudinal Study (2006-2025)
    </small>
</div>
""", unsafe_allow_html=True)
