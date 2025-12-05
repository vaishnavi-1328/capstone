# NIH Research Grants Analysis - Streamlit Multi-Page Application

## Project Overview

This is a comprehensive multi-page Streamlit application for analyzing NIH research grant patterns, funding trends, and competitive intelligence to support Corewell Health's research strategy.

## Application Structure

```
Capstone_Private/
├── Home.py                          # Main entry point (Home page)
├── pages/                           # Multi-page directory
│   ├── 1_Foundation_Grants_Analysis.py
│   ├── 2_NIH_Awards_Analysis.py
│   └── [Add your analysis pages here]
├── Streamlit/
│   └── Streamlit_data/              # NIH Awards data files
│       ├── Org_loc.csv
│       ├── ic_location_map.csv
│       ├── Main_Agen_loc.csv
│       ├── main_topic1.csv
│       ├── disease_topic_summary_df.csv
│       └── method_topic_summary_df.csv
├── [Foundation data CSV files]      # Foundation grants data
│   ├── Corewell_grantmakers.csv
│   ├── Corewell_grants.csv
│   ├── HenryFord_grantmakers.csv
│   ├── HenryFord_grants.csv
│   ├── Kaiser_grantmakers.csv
│   ├── Kaiser_grants.csv
│   ├── Pittsburgh_grantmakers.csv
│   └── Pittsburgh_grants.csv
└── README_STREAMLIT_INTEGRATION.md  # This file
```

## How to Run the Application

### 1. Install Required Dependencies

```bash
pip install streamlit pandas numpy plotly scipy
```

### 2. Navigate to Project Directory

```bash
cd /Users/vaishnavis/Desktop/Capstone_Private
```

### 3. Run the Application

```bash
streamlit run Home.py
```

The application will open in your default browser at `http://localhost:8501`

## Current Pages

1. **Home** - Landing page with project overview and navigation guide
2. **Foundation Grants Analysis** - Comprehensive analysis of foundation giving patterns across 4 healthcare systems
3. **NIH Awards Analysis** - Deep dive into NIH funding dynamics across topics, diseases, and methods

## Adding Your Own Analysis Page

### Step 1: Create Your Page File

Create a new file in the `pages/` directory following this naming convention:
- `3_Your_Analysis_Name.py`
- `4_Another_Analysis.py`
- etc.

**Note:** The number prefix determines the order in the sidebar.

### Step 2: Page Template

Use this template for your page:

```python
"""
Your Analysis Page Title
Brief description of what this page analyzes
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Page configuration
st.set_page_config(
    page_title="Your Analysis Name",
    page_icon="📊",
    layout="wide"
)

# Get the base directory for relative paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Title and description
st.title("Your Analysis Title")
st.markdown("### Brief Description")

# Load your data using relative paths
# Example:
# data = pd.read_csv(os.path.join(BASE_DIR, "your_data_folder", "your_file.csv"))

# Your analysis code here
st.markdown("## Key Findings")

# Add your visualizations
# fig = px.bar(data, x='column1', y='column2')
# st.plotly_chart(fig, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; padding: 20px;'>
    <small>
    NIH Grants Competitive Intelligence | Corewell Health Capstone Project<br>
    Michigan State University | Data Science MS Program
    </small>
</div>
""", unsafe_allow_html=True)
```

### Step 3: Data Organization

**Option 1: Use existing data directories**
- Place your CSV files in the project root or in `Streamlit/Streamlit_data/`
- Load using: `pd.read_csv(os.path.join(BASE_DIR, "your_file.csv"))`

**Option 2: Create your own data folder**
```python
# Create a new folder: your_name_data/
# Load using:
DATA_DIR = os.path.join(BASE_DIR, "your_name_data")
data = pd.read_csv(os.path.join(DATA_DIR, "your_file.csv"))
```

### Step 4: Test Your Page

1. Save your file in the `pages/` directory
2. Run `streamlit run Home.py`
3. Your page should automatically appear in the sidebar
4. Click on it to test

## Best Practices

### 1. Use Relative Paths (IMPORTANT!)

```python
# GOOD - Uses relative paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data = pd.read_csv(os.path.join(BASE_DIR, "data.csv"))

# BAD - Uses absolute paths (will break on other machines)
data = pd.read_csv("/Users/yourname/Desktop/Capstone_Private/data.csv")
```

### 2. Page Configuration

Always include at the top of your page:

```python
st.set_page_config(
    page_title="Your Page Title",
    page_icon="📊",  # Choose an appropriate emoji
    layout="wide"    # Use full width
)
```

### 3. Use Tabs for Organization

For complex analyses, use tabs:

```python
tab1, tab2, tab3 = st.tabs(["Overview", "Detailed Analysis", "Conclusions"])

with tab1:
    st.markdown("### Overview")
    # Your overview content

with tab2:
    st.markdown("### Detailed Analysis")
    # Your detailed analysis

with tab3:
    st.markdown("### Conclusions")
    # Your conclusions
```

### 4. Cache Data Loading

Use `@st.cache_data` for expensive operations:

```python
@st.cache_data
def load_data():
    return pd.read_csv("large_file.csv")

data = load_data()
```

### 5. Add Descriptive Text

Always explain what your visualizations show:

```python
st.plotly_chart(fig, use_container_width=True)
st.markdown("This chart shows that...")
```

## Styling Guidelines

### Colors
- Primary: `#1f77b4` (blue)
- Secondary: `#2ca02c` (green)
- Accent: `#d62728` (red)

### Common Plotly Settings

```python
# For consistent dark theme charts
dark_layout = dict(
    plot_bgcolor='black',
    paper_bgcolor='black',
    font=dict(size=12, color='white'),
    title_font=dict(size=20, color='white')
)

fig.update_layout(**dark_layout)
```

## Common Issues and Solutions

### Issue 1: "File not found" error
**Solution:** Check that you're using relative paths with `os.path.join(BASE_DIR, ...)`

### Issue 2: Page doesn't appear in sidebar
**Solution:**
- Ensure file is in `pages/` directory
- Ensure filename starts with a number (e.g., `3_My_Page.py`)
- Restart the Streamlit app

### Issue 3: Data loads slowly
**Solution:** Use `@st.cache_data` decorator on your data loading function

### Issue 4: Charts overlap or look weird
**Solution:** Use `st.columns()` for side-by-side layouts:

```python
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.plotly_chart(fig2, use_container_width=True)
```

## File Size Limits

- Keep individual CSV files under 50 MB
- For large datasets, consider:
  - Aggregating data beforehand
  - Using Parquet format instead of CSV
  - Filtering data before loading

## Team Collaboration

### Adding Your Page (Quick Checklist)

- [ ] Create file in `pages/` directory with number prefix
- [ ] Use relative paths for all data files
- [ ] Include page configuration (`st.set_page_config`)
- [ ] Add title and description
- [ ] Test locally before sharing
- [ ] Document any new data files you add
- [ ] Use consistent styling (see guidelines above)

### Testing Before Sharing

1. Run `streamlit run Home.py`
2. Navigate to your page in the sidebar
3. Check all visualizations load correctly
4. Check all tabs work (if applicable)
5. Verify all text is readable
6. Test on a fresh browser window

## Getting Help

### Streamlit Documentation
- Main docs: https://docs.streamlit.io
- Plotly charts: https://plotly.com/python/
- Layout: https://docs.streamlit.io/develop/api-reference/layout

### Team Contact
If you encounter issues:
1. Check this README first
2. Review the existing pages (`1_Foundation_Grants_Analysis.py` and `2_NIH_Awards_Analysis.py`) for examples
3. Contact team lead

## Advanced Features

### Interactive Filters

```python
# Add a filter sidebar
with st.sidebar:
    year = st.selectbox("Select Year", [2020, 2021, 2022, 2023])

filtered_data = data[data['year'] == year]
```

### Download Buttons

```python
# Allow users to download filtered data
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Download Data as CSV",
    data=csv,
    file_name='filtered_data.csv',
    mime='text/csv'
)
```

### Metrics Display

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Grants", "1,234", delta="10%")

with col2:
    st.metric("Avg Award", "$500K", delta="-5%")

with col3:
    st.metric("Projects", "567", delta="15%")
```

## Version History

- **v1.0** (2025-12-02): Initial integrated multi-page application
  - Home page
  - Foundation Grants Analysis
  - NIH Awards Analysis
  - Relative path support
  - Extensible structure for team contributions

---

**Questions?** Contact the project team or refer to the Streamlit documentation.

**Happy Analyzing!**
