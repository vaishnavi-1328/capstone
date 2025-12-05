"""
===============================================================================
Q2: INSTITUTIONAL FUNDING ANALYSIS
===============================================================================
Which institutions receive the most NIH and foundation funding, and in what 
research domains?

Analysis covers:
- 4 peer institutions (UPMC, Kaiser, Henry Ford, Corewell)
- Disease domain funding comparison
- Methods domain funding comparison
- Institutional rankings and performance metrics
===============================================================================
"""

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Q2: Institutional Funding",
    page_icon="🏥",
    layout="wide"
)

# Get directories (relative to this file)
CURRENT_DIR = Path(__file__).parent
PLOTLY_DIR = CURRENT_DIR / "plotly_charts"
CSV_DIR = CURRENT_DIR / "csv_tables"

# Check if directories exist
if not PLOTLY_DIR.exists():
    st.error(f"❌ Plotly charts directory not found: {PLOTLY_DIR}")
    st.info("Expected location: pages/plotly_charts/")
    st.stop()

if not CSV_DIR.exists():
    st.error(f"❌ CSV tables directory not found: {CSV_DIR}")
    st.info("Expected location: pages/csv_tables/")
    st.stop()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def load_plotly_chart(filename, height=600):
    """Load and display an interactive Plotly chart from HTML file"""
    chart_path = PLOTLY_DIR / filename
    
    if not chart_path.exists():
        st.warning(f"⚠️ Chart not found: {filename}")
        return
    
    with open(chart_path, 'r', encoding='utf-8') as f:
        chart_html = f.read()
    
    components.html(chart_html, height=height, scrolling=False)

def load_csv_table(filename):
    """Load CSV table as pandas DataFrame"""
    csv_path = CSV_DIR / filename
    
    if not csv_path.exists():
        st.warning(f"⚠️ Table not found: {filename}")
        return None
    
    return pd.read_csv(csv_path)

# ============================================================================
# BUSINESS NARRATIVE
# ============================================================================

st.title("Q2: Institutional Funding Landscape")

st.markdown("### Why This Matters for Corewell Health")

st.markdown("""
**Research Question:** Which institutions receive the most NIH and foundation funding? 
In which specific research domains do they excel?

**Strategic Value:**
- **Competitive Benchmarking**: Compare Corewell against UPMC, Kaiser, and Henry Ford
- **Domain Positioning**: Identify where Corewell leads vs. lags in specific areas
- **Partnership Opportunities**: Find complementary strengths across institutions
- **Resource Allocation**: Target domains where Corewell can compete effectively
""")

# ============================================================================
# KEY INSIGHTS
# ============================================================================

st.markdown("---")
st.markdown("### 🔑 Key Insights from Institutional Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Funding Leader:**")
    st.metric("University of Pittsburgh", "$10.4B")
    st.markdown("Dominates across all research domains")

with col2:
    st.markdown("**Corewell Position:**")
    st.metric("Total Funding", "$79.5M")
    st.markdown("Smallest portfolio but strategic niches")

with col3:
    st.markdown("**Key Finding:**")
    st.metric("Domain Diversity", "4 Institutions")
    st.markdown("Each institution has unique domain strengths")

st.markdown("""
**Business Recommendation:**

Institutional comparison reveals:
1. **UPMC is 130x larger** than Corewell - direct competition unrealistic in volume
2. **Domain specialization matters** - Kaiser leads population health, UPMC leads neuroscience
3. **Corewell's niche opportunities** - Focus on high-impact, lower-competition domains
4. **Average grant size varies widely** - Some institutions target larger, fewer grants

**Strategic Focus:** Rather than compete head-to-head with UPMC, Corewell should identify 
underserved domains where clinical strengths translate to research advantages (e.g., 
pragmatic trials, implementation science, health equity research).
""")

# ============================================================================
# MAIN CONTENT TABS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Institutional Funding Comparison")

tab1, tab2, tab3 = st.tabs([
    "🦠 Disease Domain Funding",
    "🔬 Methods Domain Funding",
    "📈 Overall Rankings"
])

# ============================================================================
# TAB 1: DISEASE DOMAIN FUNDING
# ============================================================================

with tab1:
    st.markdown("## Disease Domain: Institutional Comparison")
    
    st.markdown("""
    **Analysis Question:** How do the 4 institutions compare in disease-focused research? 
    Which organizations dominate which disease areas?
    
    **Disease Domains Analyzed:**
    - Infectious & Immune Diseases
    - Neurological, Mental & Behavioral Health
    - Cardiometabolic & Endocrine Systems
    - Oncology & Genetic Diseases
    - Organ-Specific Systems & Developmental Health
    """)
    
    st.markdown("---")
    
    # Chart 1: Count Mix
    st.markdown("### Grant Count Distribution by Institution (% Mix)")
    st.markdown("How does each institution allocate its disease research portfolio?")
    
    load_plotly_chart("05_disease_institution_count_mix.html", height=500)
    
    st.markdown("""
    **Key Insight - Portfolio Composition:**
    
    This stacked bar shows each institution's **research focus** as a percentage:
    - **UPMC**: Likely balanced across disease areas (largest, most diverse)
    - **Kaiser**: May over-index on population health and chronic disease (their clinical model)
    - **Henry Ford**: Check for specialization patterns
    - **Corewell**: Smaller portfolio may show concentration in 2-3 areas
    
    **Strategic Implication:** Diversification vs. specialization - UPMC can afford to be 
    everywhere, Corewell should strategically concentrate. Identify Corewell's white space.
    """)
    
    st.markdown("---")
    
    # Chart 2: Award Mix
    st.markdown("### Funding Distribution by Institution (% Mix)")
    st.markdown("How do funding dollars distribute across disease domains?")
    
    load_plotly_chart("06_disease_institution_award_mix.html", height=500)
    
    st.markdown("""
    **Key Insight - Dollar Allocation:**
    
    Compare **grant count %** vs. **funding %**:
    - Areas where funding % > grant count % indicate **higher average grant sizes**
    - Areas where funding % < grant count % indicate **many small grants**
    - Example: If Oncology is 15% of grants but 25% of funding → expensive cancer trials
    
    **Strategic Use:** Target disease areas where Corewell has clinical volume (patient access) 
    AND funding intensity is high. Avoid areas where average grant sizes are too small to 
    justify effort.
    """)
    
    st.markdown("---")
    
    # Chart 3: Bubble Scatter (Actually Heatmap)
    st.markdown("### Institutional Funding Heatmap: Disease Domains")
    st.markdown("Absolute funding amounts ($M) by institution and disease area")
    
    load_plotly_chart("07_disease_bubble_scatter_REAL.html", height=600)
    
    st.markdown("""
    **Key Insight - Absolute Funding Comparison:**
    
    This chart shows **raw dollar amounts**:
    - **Darkest cells** = Highest funding (likely UPMC in Neurological Health ~$3B+)
    - **Lightest cells** = Lowest funding (likely Corewell in most areas <$30M)
    - **Patterns to spot**: Which disease areas show relative strength for Corewell?
    
    **Strategic Takeaway:** Even if Corewell is small in absolute terms, look for areas where 
    the funding gap is smallest. These are winnable domains. Also identify UPMC's weak spots.
    """)
    
    st.markdown("---")
    
    # Table: Disease Funding by Institution
    st.markdown("### 📊 Disease Funding Table: Institution Rankings")
    
    df_disease_funding = load_csv_table("disease_03_table.csv")
    
    if df_disease_funding is not None:
        st.dataframe(df_disease_funding, use_container_width=True)
        
        st.markdown("""
        **How to Read This Table:**
        - Each row = one institution
        - Each column = one disease domain ($ millions)
        - Rank institutions by total or by specific disease area
        
        **Action Item:** Download this table to calculate:
        - Corewell's market share by domain
        - Gap analysis (where are we most behind?)
        - Average grant size by institution by domain
        """)
    
    st.markdown("---")
    
    # Table: Institution Totals
    st.markdown("### 📊 Overall Disease Research Metrics")
    
    df_disease_totals = load_csv_table("disease_06_table.csv")
    
    if df_disease_totals is not None:
        st.dataframe(df_disease_totals, use_container_width=True)
        
        st.markdown("""
        **Key Metrics:**
        - **Total_Grants**: Number of active disease-related grants
        - **Total_$ (M)**: Aggregate disease research funding
        - **Average $/Grant**: Mean grant size (funding intensity)
        
        **Interpretation:**
        - High total + high avg → Large, well-funded portfolio (UPMC)
        - Low total + high avg → Selective, high-value grants (potential Corewell strategy)
        - High total + low avg → Many small grants (less strategic)
        """)

# ============================================================================
# TAB 2: METHODS DOMAIN FUNDING
# ============================================================================

with tab2:
    st.markdown("## Methods Domain: Institutional Comparison")
    
    st.markdown("""
    **Analysis Question:** How do institutions compare in methodological capabilities? 
    Who leads in omics, data science, clinical trials, etc.?
    
    **Methods Domains Analyzed:**
    - Molecular & Cellular Biology
    - Omics & Data Science
    - Diagnostics, Therapeutics & Interventions
    - Population & Environmental Health
    - Cross-Cutting & Enabling Areas
    """)
    
    st.markdown("---")
    
    # Chart 4: Methods Count Mix
    st.markdown("### Grant Count Distribution by Institution (% Mix)")
    st.markdown("How does each institution allocate its methods research portfolio?")
    
    load_plotly_chart("12_methods_institution_count_mix.html", height=500)
    
    st.markdown("""
    **Key Insight - Methodological Focus:**
    
    Compare methods portfolio composition:
    - **UPMC**: Likely strong in molecular biology (wet-lab infrastructure)
    - **Kaiser**: Probably over-indexed on population health, EHR-based methods
    - **Henry Ford**: Check for clinical trial strength
    - **Corewell**: May show concentration in applied/clinical methods vs. basic science
    
    **Strategic Implication:** Methods reveal institutional DNA. Academic medical centers 
    (UPMC) excel in basic science. Integrated delivery systems (Kaiser, Corewell) should 
    leverage population health methods where they have natural advantages.
    """)
    
    st.markdown("---")
    
    # Chart 5: Methods Award Mix
    st.markdown("### Funding Distribution by Institution (% Mix)")
    st.markdown("How do funding dollars distribute across methods domains?")
    
    load_plotly_chart("13_methods_institution_award_mix.html", height=500)
    
    st.markdown("""
    **Key Insight - Methods Investment:**
    
    Funding allocation reveals priorities:
    - **Omics/Data Science**: High funding % indicates investment in computational infrastructure
    - **Clinical Trials**: High funding % indicates translational focus
    - **Molecular Biology**: High funding % indicates wet-lab capacity
    
    **Strategic Use:** Corewell should over-index on methods where:
    1. Clinical operations provide natural data (EHR, registries, biobanks)
    2. Infrastructure costs are moderate (avoid expensive sequencing/imaging unless partnered)
    3. Methodological innovation is feasible (pragmatic trial designs, implementation science)
    """)
    
    st.markdown("---")
    
    # Chart 6: Methods Bubble Scatter (Actually Heatmap)
    st.markdown("### Institutional Funding Heatmap: Methods Domains")
    st.markdown("Absolute funding amounts ($M) by institution and methods area")
    
    load_plotly_chart("14_methods_bubble_scatter_REAL.html", height=600)
    
    st.markdown("""
    **Key Insight - Methods Funding Landscape:**
    
    Absolute dollar comparison:
    - **UPMC dominance**: Likely $2B+ in omics and molecular biology
    - **Kaiser strength**: Check population health and health services research
    - **Corewell positioning**: Identify methods domains where funding gap is manageable
    
    **Strategic Takeaway:** Build on existing methodological strengths. If Corewell has 
    strong EHR analytics, double down on data science methods. If biobanking exists, 
    emphasize biomarker discovery. Don't compete where infrastructure gaps are too large.
    """)
    
    st.markdown("---")
    
    # Table: Methods Funding by Institution
    st.markdown("### 📊 Methods Funding Table: Institution Rankings")
    
    df_methods_funding = load_csv_table("methods_03_table.csv")
    
    if df_methods_funding is not None:
        st.dataframe(df_methods_funding, use_container_width=True)
        
        st.markdown("""
        **How to Read This Table:**
        - Each row = one institution
        - Each column = one methods domain ($ millions)
        - Compare Corewell's position in each methods area
        
        **Action Item:** Identify methods where:
        - Corewell is closest to peers (competitive opportunity)
        - Corewell is far behind (avoid or partner)
        - Corewell is absent (greenfield opportunity if strategically aligned)
        """)
    
    st.markdown("---")
    
    # Table: Methods Institution Totals
    st.markdown("### 📊 Overall Methods Research Metrics")
    
    df_methods_totals = load_csv_table("methods_06_table.csv")
    
    if df_methods_totals is not None:
        st.dataframe(df_methods_totals, use_container_width=True)
        
        st.markdown("""
        **Key Metrics:**
        - **Total_Grants**: Number of active methods-related grants
        - **Total_$ (M)**: Aggregate methods research funding
        - **Average $/Grant**: Mean grant size for methods research
        
        **Comparison Note:** Methods grants may have different average sizes than disease grants. 
        Infrastructure grants (e.g., biobanking, core facilities) can be very large. Training 
        grants (K-series) are typically smaller.
        """)

# ============================================================================
# TAB 3: OVERALL RANKINGS
# ============================================================================

with tab3:
    st.markdown("## Overall Institutional Rankings & Metrics")
    
    st.markdown("""
    **Analysis Question:** How do the 4 institutions rank overall? What are the key 
    differentiators in scale, focus, and performance?
    """)
    
    st.markdown("---")
    
    # Combined Analysis
    st.markdown("### 🏆 Institutional Performance Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Disease Research Rankings")
        
        df_disease_totals = load_csv_table("disease_06_table.csv")
        if df_disease_totals is not None:
            # Sort by total funding
            df_disease_sorted = df_disease_totals.sort_values('Total_$ (M)', ascending=False)
            
            st.dataframe(df_disease_sorted, use_container_width=True)
            
            st.markdown("""
            **Ranking Insights:**
            1. Check UPMC's dominance in total $ and grant count
            2. Compare Kaiser vs. Henry Ford (similar scale?)
            3. Assess Corewell's position and average grant size
            """)
    
    with col2:
        st.markdown("#### Methods Research Rankings")
        
        df_methods_totals = load_csv_table("methods_06_table.csv")
        if df_methods_totals is not None:
            # Sort by total funding
            df_methods_sorted = df_methods_totals.sort_values('Total_$ (M)', ascending=False)
            
            st.dataframe(df_methods_sorted, use_container_width=True)
            
            st.markdown("""
            **Ranking Insights:**
            1. Rankings may differ slightly from disease (methodological strengths vary)
            2. Look for institutions with higher methods funding than disease funding
            3. Compare average $/grant across methods vs. disease
            """)
    
    st.markdown("---")
    
    # Domain-Specific Leadership
    st.markdown("### 🎯 Domain-Specific Leaders")
    
    st.markdown("""
    **Who Leads in Each Domain?**
    
    Analyze the funding tables to identify domain leaders:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Disease Domain Leaders (Likely):**
        - **Neurological Health**: UPMC (academic neuroscience powerhouse)
        - **Infectious Disease**: UPMC (largest volume)
        - **Cardiometabolic**: Check UPMC vs. Kaiser (clinical trial strength)
        - **Oncology**: UPMC (cancer center designation)
        - **Organ Systems**: UPMC (breadth of specialties)
        
        *Note: Actual leaders visible in funding table above*
        """)
    
    with col2:
        st.markdown("""
        **Methods Domain Leaders (Likely):**
        - **Omics & Data Science**: UPMC (computational resources)
        - **Population Health**: Kaiser (integrated delivery system advantage)
        - **Molecular Biology**: UPMC (wet-lab infrastructure)
        - **Clinical Trials**: Check UPMC vs. Kaiser
        - **Cross-Cutting**: UPMC (training programs, cores)
        
        *Note: Actual leaders visible in funding table above*
        """)
    
    st.markdown("---")
    
    # Corewell-Specific Analysis
    st.markdown("### ⭐ Corewell Health: Competitive Positioning")
    
    st.markdown("""
    **Where Does Corewell Stand?**
    
    Based on the data above, Corewell Health should focus on:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Competitive Advantages:**
        - **Clinical access**: Large patient population for pragmatic trials
        - **EHR data**: Rich longitudinal data for observational studies
        - **Population diversity**: Southeast Michigan demographics
        - **Operational efficiency**: Integrated delivery system model
        
        **Recommended Disease Focus:**
        - Areas where clinical volume is high (cardio, oncology, primary care)
        - Health equity and underserved populations
        - Chronic disease management and prevention
        """)
    
    with col2:
        st.markdown("""
        **Strategic Gaps:**
        - **Scale**: 100x smaller than UPMC in total funding
        - **Basic science**: Limited wet-lab infrastructure
        - **Training programs**: Fewer T32, K-series awards
        - **Core facilities**: Imaging, sequencing, computational resources
        
        **Recommended Methods Focus:**
        - EHR-based research and data science
        - Pragmatic clinical trials (embedded in care)
        - Implementation science
        - Health services research and quality improvement
        """)
    
    st.markdown("---")
    
    # Strategic Recommendations
    st.markdown("### 💡 Strategic Recommendations for Corewell")
    
    st.markdown("""
    **Three-Pronged Strategy Based on Institutional Analysis:**
    
    **1. Compete Where You Have Advantages:**
    - **Population health research**: Kaiser does this well - study their portfolio
    - **Pragmatic trials**: Partner with PCORI, NIH pragmatic trial networks
    - **Implementation science**: Underrepresented across all 4 institutions
    - **Health equity**: Leverage diverse patient population
    
    **2. Partner Where You Have Gaps:**
    - **Omics/sequencing**: Partner with UPMC or commercial providers
    - **Basic science**: Collaborate with University of Michigan, Michigan State
    - **Training**: Send junior faculty to T32 programs at partner institutions
    - **Core facilities**: Use shared resources rather than build
    
    **3. Avoid Head-to-Head Competition:**
    - **Don't compete** with UPMC in molecular neuroscience (their strength)
    - **Don't compete** on volume - focus on impact per grant
    - **Don't spread thin** - concentrate in 3-5 strategic domains
    
    **Target Domains for Corewell:**
    - Disease: Cardiometabolic health, primary care, health equity
    - Methods: EHR analytics, pragmatic trials, implementation science
    - Cross-cutting: Community-engaged research, dissemination & implementation
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
    Institutional Funding Analysis: 4 Peer Organizations Compared
    </small>
</div>
""", unsafe_allow_html=True)
