"""
===============================================================================
Q1: RESEARCH THEMES ANALYSIS
===============================================================================
What are the most common themes or research aims in project titles and 
abstracts funded by NIH and philanthropic organizations?

Analysis covers:
- Disease & Organ-System Areas (5 top-level, 31 sub-categories)
- Methods & Modalities (5 top-level, 27 sub-categories)
===============================================================================
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Q1: Research Themes",
    page_icon="🔬",
    layout="wide"
)

# Get directories (relative to this file)
CURRENT_DIR = Path(__file__).parent
PLOTLY_DIR = CURRENT_DIR / "plotly_charts"

# Check if plotly_charts directory exists
if not PLOTLY_DIR.exists():
    st.error(f"❌ Plotly charts directory not found: {PLOTLY_DIR}")
    st.info("Expected location: pages/plotly_charts/")
    st.stop()

# ============================================================================
# HELPER FUNCTION
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

# ============================================================================
# BUSINESS NARRATIVE
# ============================================================================

st.title("Q1: Research Themes & Funding Priorities")

st.markdown("### Why This Matters for Corewell Health")

st.markdown("""
**Research Question:** What are the most common themes and research aims funded by 
NIH and philanthropic organizations? Where is the money flowing?

**Strategic Value:**
- **Portfolio Alignment**: Understand major funding trends across disease areas and methods
- **Gap Analysis**: Identify underrepresented research themes
- **Competitive Positioning**: See where peer institutions focus their efforts
- **Strategic Planning**: Align Corewell's research agenda with funding priorities
""")

# ============================================================================
# KEY INSIGHTS
# ============================================================================

st.markdown("---")
st.markdown("### 🔑 Key Insights from Theme Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Top Disease Theme:**")
    st.metric("Most Funded", "Organ-Specific Systems")
    st.markdown("5,717 grants - includes GI, pulmonary, renal systems")

with col2:
    st.markdown("**Top Methods Theme:**")
    st.metric("Most Funded", "Omics & Data Science")
    st.markdown("7,226 grants - genomics, bioinformatics dominate")

with col3:
    st.markdown("**Total Coverage:**")
    st.metric("Research Areas", "58 Categories")
    st.markdown("31 disease areas + 27 methods tracked")

st.markdown("""
**Business Recommendation:**

Our thematic analysis reveals:
1. **Organ-specific research dominates** - Neurological and organ system health lead in volume
2. **Data science is exploding** - Omics and computational methods are top priority
3. **Infectious disease remains critical** - Despite COVID decline, sustained high funding
4. **Population health growing** - Environmental and community health gaining traction

**Strategic Focus:** Corewell should strengthen capabilities in data-intensive organ system 
research (e.g., neuroinformatics, computational cardiology) to align with funding trends.
""")

# ============================================================================
# MAIN CONTENT TABS
# ============================================================================

st.markdown("---")
st.markdown("## 📊 Research Theme Analysis")

tab1, tab2 = st.tabs([
    "🦠 Disease & Organ-System Areas",
    "🔬 Methods & Modalities"
])

# ============================================================================
# TAB 1: DISEASE & ORGAN-SYSTEM AREAS
# ============================================================================

with tab1:
    st.markdown("## Disease & Organ-System Research Themes")
    
    st.markdown("""
    **Analysis Question:** Which disease and organ-system areas receive the most NIH 
    and philanthropic funding?
    
    **Top-Level Categories (5):**
    - Infectious & Immune Diseases
    - Neurological, Mental & Behavioral Health
    - Cardiometabolic & Endocrine Systems
    - Oncology & Genetic Diseases
    - Organ-Specific Systems & Developmental Health
    """)
    
    st.markdown("---")
    
    # Chart 1: Top-Level Grant Count
    st.markdown("### Top-Level Disease Categories by Grant Volume")
    st.markdown("Which broad disease areas attract the most research projects?")
    
    load_plotly_chart("01_disease_top_level_count.html", height=500)
    
    st.markdown("""
    **Key Insight:** 
    - **Organ-Specific Systems** leads with 5,717 grants - reflects breadth of specialties 
      (GI, pulmonary, renal, musculoskeletal, etc.)
    - **Neurological Health** close second with 5,344 grants - includes neuroscience, 
      psychiatry, addiction, and aging research
    - **Infectious & Immune** third with 4,027 grants - sustained priority despite 
      post-COVID normalization
    - **Cardiometabolic** and **Oncology** follow with 2,853 and 1,969 grants respectively
    
    **Strategic Takeaway:** These 5 categories represent the entire disease research 
    landscape. Organ systems and neuroscience dominate, suggesting opportunities for 
    integrated cross-system research.
    """)
    
    st.markdown("---")
    
    # Chart 2: Top-Level Funding
    st.markdown("### Top-Level Disease Categories by Total Funding")
    st.markdown("Which areas command the highest dollar amounts?")
    
    load_plotly_chart("02_disease_top_level_funding.html", height=500)
    
    st.markdown("""
    **Key Insight:** 
    - Funding distribution roughly matches grant count, but with key differences:
    - **Neurological Health** may have higher average grant sizes (check if it overtakes 
      Organ-Specific in funding despite fewer grants)
    - **Infectious Disease** funding intensity reflects high-cost clinical trials and 
      large-scale epidemiological studies
    - **Oncology** likely has highest $/grant ratio (expensive translational research)
    
    **Strategic Takeaway:** Volume doesn't always equal dollars. Some areas (like oncology) 
    have smaller portfolios but higher per-grant funding.
    """)
    
    st.markdown("---")
    
    # Chart 3: Sub-Category Grant Count
    st.markdown("### Detailed Sub-Categories by Grant Volume (31 Specific Areas)")
    st.markdown("Breaking down the 5 top-level categories into specific disease domains")
    
    load_plotly_chart("03_disease_sub_category_count.html", height=700)
    
    st.markdown("""
    **Key Insight - Most Active Specific Areas:**
    
    This granular view reveals the **specific disease domains** driving research volume:
    - Individual specialties like **Neurology/Neuroscience**, **Cardiology**, **Oncology**, 
      **Gastroenterology**, **Infectious Diseases** emerge
    - Cross-cutting themes like **Autoimmunity/Inflammation** appear across multiple systems
    - Emerging areas like **COVID-19**, **Aging/Alzheimer's** show dedicated focus
    
    **Strategic Use:** Identify niche opportunities by comparing Corewell's strengths 
    against these 31 specific domains. Where does Corewell have expertise but low grant 
    activity? Where are competitors overrepresented?
    """)
    
    st.markdown("---")
    
    # Chart 4: Sub-Category Funding
    st.markdown("### Detailed Sub-Categories by Total Funding (31 Specific Areas)")
    st.markdown("Which specific domains command the highest funding?")
    
    load_plotly_chart("04_disease_sub_category_funding.html", height=700)
    
    st.markdown("""
    **Key Insight - Highest Funded Specific Areas:**
    
    Compare funding intensity to grant count:
    - **High $ per grant areas**: Likely includes clinical trials, translational oncology, 
      advanced imaging studies
    - **High volume, lower $ per grant**: Epidemiology, population health, basic science
    - **Emerging high-value**: COVID-19, precision medicine initiatives
    
    **Strategic Takeaway:** Target areas where Corewell has clinical capacity for high-value 
    grants (e.g., cancer trials, cardiovascular interventions) vs. basic science grants 
    with smaller budgets.
    """)
    
    st.markdown("---")
    
    # Summary for Disease Tab
    st.markdown("### 🎯 Disease Areas Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Portfolio Strengths:**
        - Organ systems research (5,717 grants)
        - Neurological/behavioral health (5,344 grants)
        - Strong infectious disease base (4,027 grants)
        - Diverse cardiometabolic portfolio (2,853 grants)
        """)
    
    with col2:
        st.markdown("""
        **Strategic Opportunities:**
        - Cross-system integration (neuro + cardio + metabolic)
        - Aging as a cross-cutting theme
        - Post-COVID infectious disease pivots
        - Rare disease and genetic disorders (lower competition)
        """)

# ============================================================================
# TAB 2: METHODS & MODALITIES
# ============================================================================

with tab2:
    st.markdown("## Methods & Modalities Research Themes")
    
    st.markdown("""
    **Analysis Question:** What research methods, technologies, and modalities are 
    being funded? Where is methodological innovation happening?
    
    **Top-Level Categories (5):**
    - Omics & Data Science
    - Population & Environmental Health
    - Molecular & Cellular Biology
    - Diagnostics, Therapeutics & Interventions
    - Cross-Cutting & Enabling Areas
    """)
    
    st.markdown("---")
    
    # Chart 5: Methods Top-Level Grant Count
    st.markdown("### Top-Level Methods Categories by Grant Volume")
    st.markdown("Which research approaches are most prevalent?")
    
    load_plotly_chart("08_methods_top_level_count.html", height=500)
    
    st.markdown("""
    **Key Insight:** 
    - **Omics & Data Science** dominates with 7,226 grants - includes genomics, proteomics, 
      bioinformatics, AI/ML applications
    - **Population & Environmental Health** strong with 6,573 grants - epidemiology, 
      health services research, environmental exposures
    - **Molecular & Cellular Biology** remains foundational with 6,139 grants - 
      basic science backbone
    - **Diagnostics & Therapeutics** follows with 5,975 grants - translational focus
    - **Cross-Cutting** areas (5,395 grants) include training, infrastructure, methodology
    
    **Strategic Takeaway:** Data-intensive methods are the future. Omics and computational 
    approaches receive the most grants, signaling NIH's priority on big data and precision medicine.
    """)
    
    st.markdown("---")
    
    # Chart 6: Methods Top-Level Funding
    st.markdown("### Top-Level Methods Categories by Total Funding")
    st.markdown("Which methodological areas command the highest budgets?")
    
    load_plotly_chart("09_methods_top_level_funding.html", height=500)
    
    st.markdown("""
    **Key Insight:** 
    - Funding likely mirrors grant volume for methods (unlike disease areas)
    - **Omics** may have highest average grant sizes due to expensive sequencing, 
      computational infrastructure
    - **Diagnostics & Therapeutics** potentially high $/grant (clinical trials, 
      device development)
    - **Population Health** may have lower $/grant (survey-based, observational studies)
    
    **Strategic Takeaway:** Methodological diversity is key. Institutions need capabilities 
    across wet-lab (molecular), dry-lab (omics/data), and translational (diagnostics) methods.
    """)
    
    st.markdown("---")
    
    # Chart 7: Methods Sub-Category Grant Count
    st.markdown("### Detailed Methods Sub-Categories by Grant Volume (27 Specific Areas)")
    st.markdown("Breaking down the 5 top-level categories into specific methodologies")
    
    load_plotly_chart("10_methods_sub_category_count.html", height=700)
    
    st.markdown("""
    **Key Insight - Most Active Specific Methods:**
    
    This reveals the **specific techniques and approaches** being funded:
    - **Genomics/Genetics/Sequencing**: NGS, GWAS, precision medicine
    - **Systems Biology**: Network analysis, computational modeling
    - **Drug Discovery/Pharmacology**: Screening, medicinal chemistry, ADME
    - **Epidemiology/Population Health**: Cohort studies, biobanks
    - **Bioinformatics/Data Science**: AI/ML, algorithm development
    - **Clinical Trials/Translational**: Phase I-III trials, implementation science
    
    **Strategic Use:** Match Corewell's core capabilities (clinical trials, biobanking, 
    electronic health records) to high-volume methods categories.
    """)
    
    st.markdown("---")
    
    # Chart 8: Methods Sub-Category Funding
    st.markdown("### Detailed Methods Sub-Categories by Total Funding (27 Specific Areas)")
    st.markdown("Which specific methods command the highest funding?")
    
    load_plotly_chart("11_methods_sub_category_funding.html", height=700)
    
    st.markdown("""
    **Key Insight - Highest Funded Specific Methods:**
    
    Compare funding intensity:
    - **High-cost methods**: Clinical trials, advanced imaging (MRI/PET), large-scale sequencing
    - **Infrastructure-heavy**: Biobanking, data repositories, computational clusters
    - **Lower-cost but high-volume**: Epidemiology, survey research, registry studies
    
    **Strategic Takeaway:** Corewell should invest in mid-cost, high-impact methods like 
    EHR-based research, pragmatic clinical trials, and computational biology - areas where 
    health systems have natural advantages over pure research institutions.
    """)
    
    st.markdown("---")
    
    # Summary for Methods Tab
    st.markdown("### 🎯 Methods & Modalities Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Portfolio Strengths:**
        - Omics & data science leadership (7,226 grants)
        - Strong population health methods (6,573 grants)
        - Solid molecular biology foundation (6,139 grants)
        - Translational diagnostics/therapeutics (5,975 grants)
        """)
    
    with col2:
        st.markdown("""
        **Strategic Opportunities:**
        - AI/ML in healthcare (hot area)
        - EHR-based pragmatic trials (Corewell advantage)
        - Biobanking and biorepositories
        - Implementation science (underrepresented)
        """)

# ============================================================================
# CROSS-TAB SYNTHESIS
# ============================================================================

st.markdown("---")
st.markdown("## 🎯 Cross-Cutting Insights: Disease × Methods")

st.markdown("""
The most impactful research combines **disease focus** with **methodological innovation**. 
Key intersections to watch:

1. **Neurological Health × Omics**: Alzheimer's genomics, psychiatric genetics
2. **Oncology × Data Science**: Precision oncology, predictive modeling
3. **Infectious Disease × Population Health**: Epidemic modeling, vaccine effectiveness
4. **Cardiometabolic × Molecular Biology**: Metabolomics, pathway analysis
5. **Organ Systems × Diagnostics**: Biomarker discovery, imaging innovations

**Corewell's Strategic Positioning:**
- Leverage clinical data (EHR) + population health methods
- Build computational capabilities for omics analysis
- Focus on pragmatic trials in high-volume disease areas
- Partner on expensive methods (sequencing, imaging) rather than build in-house
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
    Research Theme Analysis: 58 Categories Across Disease & Methods
    </small>
</div>
""", unsafe_allow_html=True)
