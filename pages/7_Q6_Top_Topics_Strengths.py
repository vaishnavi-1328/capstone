"""
===============================================================================
Q6: TOP RESEARCH TOPICS & INSTITUTIONAL STRENGTHS
===============================================================================
What are the hottest research topics being funded, and which institutions 
excel in which research domains?

Analysis covers:
- Top 15 disease topics ranked by volume and funding
- Top 15 methods topics ranked by volume and funding
- Institutional domain leadership across 4 peer organizations
- Corewell Health's portfolio composition
===============================================================================
"""

import streamlit as st
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Q6: Top Topics & Strengths",
    page_icon="🏆",
    layout="wide"
)

# Get directories (relative to this file)
CURRENT_DIR = Path(__file__).parent
IMG_DIR = CURRENT_DIR / "q6_images"

# Check if images directory exists
if not IMG_DIR.exists():
    st.error(f"❌ Images directory not found: {IMG_DIR}")
    st.info("Expected location: pages/q6_images/")
    st.info("Run generate_q6_visuals_improved.py first, then copy images to pages/q6_images/")
    st.stop()

# ============================================================================
# HELPER FUNCTION
# ============================================================================

def show_image(filename, caption=None):
    """Display an image from the q6_images folder"""
    img_path = IMG_DIR / filename
    
    if not img_path.exists():
        st.warning(f"⚠️ Image not found: {filename}")
        return
    
    st.image(str(img_path), caption=caption, use_column_width=True)

# ============================================================================
# BUSINESS NARRATIVE
# ============================================================================

st.title("Q6: Top Research Topics & Institutional Strengths")

st.markdown("### Why This Matters for Corewell Health")

st.markdown("""
**Research Question:** What are the most funded research topics across NIH and 
philanthropic organizations? Where do different institutions have competitive advantages?

**Strategic Value:**
- **Market Intelligence**: Identify the hottest research areas attracting funding
- **Competitive Positioning**: Understand where peer institutions focus their efforts
- **Portfolio Strategy**: Compare Corewell's mix against competitors
- **Opportunity Identification**: Find high-value topics with manageable competition
""")

# ============================================================================
# KEY INSIGHTS
# ============================================================================

st.markdown("---")
st.markdown("### 🔑 Key Insights from Topic & Leadership Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**#1 Disease Topic:**")
    st.metric("Neurology/Neuroscience", "2,734 grants")
    st.markdown("Brain research dominates NIH funding")

with col2:
    st.markdown("**#1 Methods Topic:**")
    st.metric("Machine Learning/AI", "5,629 grants")
    st.markdown("Data science leads all methods")

with col3:
    st.markdown("**Scale Gap:**")
    st.metric("UPMC vs Corewell", "130x larger")
    st.markdown("Requires strategic niche focus")

st.markdown("""
**Business Recommendation:**

Our topic analysis reveals:
1. **Neuro + Aging dominate disease research** - Combined 5,332 grants, but highly competitive
2. **AI/ML methods are exploding** - Fastest growing area, Corewell should invest here
3. **UPMC leads 9/10 domains** - Direct competition unrealistic, focus on specialized niches
4. **Corewell's portfolio is focused** - Oncology and Organ-Specific areas are relative strengths

**Strategic Focus:** Rather than compete in crowded neuroscience, Corewell should leverage 
clinical advantages in: (1) Health equity research, (2) Pragmatic trials using EHR data, 
(3) Implementation science, (4) Population health in diverse communities.
""")

# ============================================================================
# MAIN CONTENT TABS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Research Topics & Institutional Leadership")

tab1, tab2 = st.tabs([
    "🔬 Top Research Topics",
    "🏥 Institutional Strengths"
])

# ============================================================================
# TAB 1: TOP RESEARCH TOPICS
# ============================================================================

with tab1:
    st.markdown("## Hottest Research Topics Across All Institutions")
    
    st.markdown("""
    **What this shows:** Research topics ranked by total activity across all 4 institutions 
    (UPMC, Kaiser, Henry Ford, Corewell). These are the areas attracting the most NIH and 
    philanthropic funding.
    
    **How to use:** Identify high-volume topics (competitive) vs. lower-volume topics (potential 
    white space). Compare grant count vs. funding to find high-value areas.
    """)
    
    st.markdown("---")
    
    # ========================================================================
    # DISEASE TOPICS
    # ========================================================================
    
    st.markdown("### 🦠 Top 15 Disease Research Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### By Grant Count (Research Volume)")
        show_image("01_disease_top15_count.png")
        
        st.markdown("""
        **Key Insight:**
        - **Neurology** (2,734 grants) and **Aging** (2,598 grants) lead by far
        - **Autoimmunity/Inflammation** (2,237) is a cross-cutting theme
        - **Dental/Oral Health** (2,228) surprisingly high volume
        
        **For Corewell:** High grant count = high competition. Consider topics ranked #10-15 
        where competition is lower but funding is still substantial.
        """)
    
    with col2:
        st.markdown("#### By Total Funding (Dollar Amount)")
        show_image("02_disease_top15_funding.png")
        
        st.markdown("""
        **Key Insight:**
        - **Aging/Alzheimer's** gets most funding despite being #2 in count (higher $/grant)
        - **Neurology** close second in funding
        - Some topics shift ranking: higher funding = more expensive research (trials, imaging)
        
        **For Corewell:** Topics with high funding but moderate count have fewer but larger grants. 
        These require strong infrastructure but face less competition.
        """)
    
    st.markdown("""
    ---
    **Strategic Takeaway - Disease Topics:**
    
    - **Avoid:** Neurology, Aging (saturated, UPMC dominates)
    - **Consider:** Autoimmunity, GI/Hepatology, Cardiovascular (still substantial, less crowded)
    - **Target:** Oncology with Corewell's clinical strengths (relative strength in portfolio)
    - **White Space:** Mental health, substance use (growing priority, less institutional competition)
    """)
    
    st.markdown("---")
    
    # ========================================================================
    # METHODS TOPICS
    # ========================================================================
    
    st.markdown("### 🔬 Top 15 Methods Research Topics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### By Grant Count (Research Volume)")
        show_image("03_methods_top15_count.png")
        
        st.markdown("""
        **Key Insight:**
        - **Machine Learning/AI/Data Science** dominates (5,629 grants)
        - **Systems Biology** and **Environmental Health** follow
        - **Drug Discovery** remains strong (3,814 grants)
        
        **For Corewell:** AI/ML is the future - invest in computational capabilities. 
        Health Services/Implementation methods are underrepresented (opportunity).
        """)
    
    with col2:
        st.markdown("#### By Total Funding (Dollar Amount)")
        show_image("04_methods_top15_funding.png")
        
        st.markdown("""
        **Key Insight:**
        - **ML/AI** leads in both volume AND funding (most important methods area)
        - **Systems Biology** gets more $ per grant than count suggests
        - **Environmental Health** highly funded (regulatory/EPA partnerships)
        
        **For Corewell:** High-cost methods (genomics, imaging) require partnerships. 
        Focus on methods where clinical operations provide natural advantages (EHR analytics, 
        pragmatic trials, implementation science).
        """)
    
    st.markdown("""
    ---
    **Strategic Takeaway - Methods Topics:**
    
    - **Must Build:** AI/ML and data science capabilities (industry trend)
    - **Leverage:** EHR-based methods, pragmatic trials (health system advantage)
    - **Partner:** Genomics, advanced imaging (too expensive to build alone)
    - **White Space:** Implementation science, health services research (ranked #5 but underutilized)
    - **Avoid:** Wet-lab molecular biology (UPMC dominance, capital intensive)
    """)

# ============================================================================
# TAB 2: INSTITUTIONAL STRENGTHS
# ============================================================================

with tab2:
    st.markdown("## Institutional Domain Leadership: Who Excels Where?")
    
    st.markdown("""
    **What this shows:** How the 4 peer institutions (UPMC, Kaiser, Henry Ford, Corewell) compare 
    across research domains. Charts use **log scale** to make Corewell visible despite being 130x 
    smaller than UPMC.
    
    **How to use:** Identify domain leaders, find Corewell's relative strengths, spot partnership 
    opportunities with complementary institutions.
    """)
    
    st.markdown("---")
    
    # ========================================================================
    # DISEASE DOMAIN LEADERSHIP
    # ========================================================================
    
    st.markdown("### 🦠 Disease Domain Leadership")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Portfolio Composition (Log Scale)")
        show_image("05_disease_domain_log.png")
        
        st.markdown("""
        **Key Insight:**
        - **UPMC** dominant across all 5 domains (tallest bars everywhere)
        - **Kaiser** relatively stronger in Neurological and Organ-Specific
        - **Corewell** visible on log scale - has presence in all domains
        
        **Corewell Position:** Smallest portfolio but balanced distribution. 
        No single domain is neglected.
        """)
    
    with col2:
        st.markdown("#### Funding Intensity Heatmap (Log Scale)")
        show_image("06_disease_domain_heatmap_log.png")
        
        st.markdown("""
        **Key Insight:**
        - **UPMC** darkest cells = $2-3B per domain (deep blue)
        - **Kaiser** $100-500M range (lighter blue)
        - **Corewell** $2-28M range (lightest blue) - but present in all areas
        
        **Corewell Strengths:** Strongest in Oncology ($28M) and Organ-Specific ($28M). 
        Weakest in Infectious ($2M) and Cardiometabolic ($4M).
        """)
    
    st.markdown("""
    ---
    **Strategic Implications - Disease Domains:**
    
    **UPMC Strategy:** "Do everything, dominate everything" (scale advantage)
    
    **Kaiser Strategy:** Balanced with slight neuro emphasis (integrated care model)
    
    **Corewell Strategy:** Should focus on:
    - **Oncology** (relative strength at $28M) - build on clinical volume
    - **Organ-Specific** (tied strength at $28M) - leverage specialty services
    - **Avoid competing** in Infectious Disease ($2M) unless strategic partnership
    """)
    
    st.markdown("---")
    
    # ========================================================================
    # METHODS DOMAIN LEADERSHIP
    # ========================================================================
    
    st.markdown("### 🔬 Methods Domain Leadership")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Portfolio Composition (Log Scale)")
        show_image("07_methods_domain_log.png")
        
        st.markdown("""
        **Key Insight:**
        - **UPMC** leads in all methods domains (tallest bars)
        - **Kaiser** relatively strong in Population Health (their model)
        - **Corewell** log scale shows balanced methods portfolio
        
        **Corewell Position:** Not overspecialized in methods - maintains capabilities 
        across molecular, omics, diagnostics, population health.
        """)
    
    with col2:
        st.markdown("#### Funding Intensity Heatmap (Log Scale)")
        show_image("08_methods_domain_heatmap_log.png")
        
        st.markdown("""
        **Key Insight:**
        - **UPMC** $1.7-2.4B per domain (deep orange)
        - **Kaiser** $200-600M range, strongest in Population Health ($623M)
        - **Corewell** $12-20M range (lightest orange)
        
        **Corewell Strengths:** Most balanced - all domains within $12-20M range. 
        No major gaps, but no standout strengths either.
        """)
    
    st.markdown("""
    ---
    **Strategic Implications - Methods Domains:**
    
    **UPMC Strategy:** "Build all capabilities in-house" (wet-lab, omics, trials, everything)
    
    **Kaiser Strategy:** "Population health focus" ($623M) - leverage integrated data
    
    **Corewell Strategy:** Should focus on:
    - **Population Health methods** (follow Kaiser playbook - use EHR, registries)
    - **Omics as service** (partner rather than build expensive infrastructure)
    - **Diagnostics/Therapeutics** (clinical trial embedded in care delivery)
    - **Avoid expensive wet-lab** molecular biology (Corewell has no scale advantage)
    """)
    
    st.markdown("---")
    
    # ========================================================================
    # COREWELL-SPECIFIC ANALYSIS
    # ========================================================================
    
    st.markdown("### ⭐ Corewell Health: Portfolio Deep Dive")
    
    show_image("09_corewell_portfolio_pies.png")
    
    st.markdown("""
    **Corewell's Research Portfolio Composition:**
    
    **Disease Focus:**
    - **Neurological Health** likely largest slice (national priority = must participate)
    - **Organ-Specific** strong (specialty services strength)
    - **Oncology** visible presence (cancer center capabilities)
    - **Infectious/Cardiometabolic** smaller (gap or opportunity?)
    
    **Methods Focus:**
    - **Population Health** likely largest (health system advantage)
    - **Omics/Data Science** moderate (must grow this)
    - **Molecular Biology** present but small (don't compete with UPMC here)
    - **Diagnostics/Therapeutics** solid (clinical trial capabilities)
    
    **Overall Assessment:**
    Corewell has a **balanced, diversified portfolio** across both disease and methods domains. 
    This is strategic for a smaller institution - maintain presence everywhere to capture 
    opportunities, but don't try to dominate any single area where UPMC has overwhelming advantages.
    """)
    
    st.markdown("---")
    
    # Summary recommendations
    st.markdown("### 💡 Strategic Recommendations for Corewell")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Build on Existing Strengths:**
        - **Oncology research** - clinical volume supports trials
        - **Organ-specific specialties** - cardio, GI, renal, etc.
        - **Population health** - EHR data, diverse patient population
        - **Pragmatic trials** - embedded in care delivery
        
        **Grow These Capabilities:**
        - **AI/ML and data science** - hire computational researchers
        - **Implementation science** - operationalize research findings
        - **Health equity** - leverage Detroit/SE Michigan demographics
        - **Biobanking** - clinical access to samples
        """)
    
    with col2:
        st.markdown("""
        **Partner Rather Than Build:**
        - **Genomics/sequencing** - too expensive, use commercial or academic partners
        - **Advanced imaging** - partner with UM or MSU
        - **Molecular biology** - collaborate with UPMC or regional universities
        - **Training programs** - send junior faculty to T32 programs elsewhere
        
        **Avoid Direct Competition:**
        - **Basic neuroscience** - UPMC has $3.2B, Corewell has $17M (impossible gap)
        - **Wet-lab intensive research** - capital requirements too high
        - **Trying to match UPMC scale** - focus on impact per dollar, not volume
        """)
    
    st.markdown("""
    ---
    **Final Strategic Positioning:**
    
    Corewell should position as a **"health system research powerhouse"** rather than competing 
    as a traditional academic medical center:
    
    1. **Leverage operational advantages** - EHR data, care delivery infrastructure, diverse population
    2. **Focus on translational impact** - pragmatic trials, implementation, health equity
    3. **Partner strategically** - collaborate with universities for basic science, build internal 
       strengths in population health and data science
    4. **Target white space** - implementation science, health services research, community-engaged 
       research (underrepresented across all institutions)
    
    This strategy plays to Corewell's strengths and avoids head-to-head competition with UPMC's 
    $10.4B research enterprise.
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
    Top Topics Analysis: 58 Research Categories, 4 Peer Institutions
    </small>
</div>
""", unsafe_allow_html=True)
