"""
Foundation Data Analysis - Comprehensive Streamlit Dashboard
Complete analysis including data cleaning, engineering, visualizations, and statistical testing.
Designed for presentation and team project integration.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
from scipy.stats import boxcox, shapiro, normaltest, probplot
import warnings
import os
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Foundation Data Analysis - Complete",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {padding: 0rem 1rem;}
    .stMetric {background-color: #f0f2f6; padding: 10px; border-radius: 5px;}
    .big-font {font-size: 24px !important; font-weight: bold;}
    h1 {color: #1f77b4;}
    h2 {color: #2ca02c;}
    </style>
""", unsafe_allow_html=True)

# Get the base directory (parent of pages directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@st.cache_data
def load_and_clean_data():
    """Load and clean the foundation grant data for all 4 companies with detailed cleaning steps."""
    try:
        # Load raw data for all companies using relative paths
        companies = {
            'Corewell': {
                'grantmakers': pd.read_csv(os.path.join(BASE_DIR, "Corewell_grantmakers.csv")).rename(columns=lambda x: x.replace(" ", ".")),
                'grants': pd.read_csv(os.path.join(BASE_DIR, "Corewell_grants.csv")).rename(columns=lambda x: x.replace(" ", "."))
            },
            'Henry Ford': {
                'grantmakers': pd.read_csv(os.path.join(BASE_DIR, "HenryFord_grantmakers.csv")).rename(columns=lambda x: x.replace(" ", ".")),
                'grants': pd.read_csv(os.path.join(BASE_DIR, "HenryFord_grants.csv")).rename(columns=lambda x: x.replace(" ", "."))
            },
            'Kaiser': {
                'grantmakers': pd.read_csv(os.path.join(BASE_DIR, "Kaiser_grantmakers.csv")).rename(columns=lambda x: x.replace(" ", ".")),
                'grants': pd.read_csv(os.path.join(BASE_DIR, "Kaiser_grants.csv")).rename(columns=lambda x: x.replace(" ", "."))
            },
            'Pittsburgh': {
                'grantmakers': pd.read_csv(os.path.join(BASE_DIR, "Pittsburgh_grantmakers.csv")).rename(columns=lambda x: x.replace(" ", ".")),
                'grants': pd.read_csv(os.path.join(BASE_DIR, "Pittsburgh_grants.csv")).rename(columns=lambda x: x.replace(" ", "."))
            }
        }

        # Store cleaning reports for each company
        cleaning_reports = {}
        all_grants_clean = []
        all_grantmakers_clean = []
        all_merged_data = []

        # Process each company
        for company_name, data in companies.items():
            # Store original counts
            cleaning_report = {
                'grants_original': len(data['grants']),
                'grantmakers_original': len(data['grantmakers'])
            }

            # Clean grants data
            grants_clean = data['grants'].copy()
            grants_clean['Company'] = company_name  # Add company identifier

            numeric_cols_grants = ['Grant.Amount', 'Year.Authorized']
            for col in numeric_cols_grants:
                if col in grants_clean.columns:
                    grants_clean[col] = pd.to_numeric(grants_clean[col], errors='coerce')

            before_drop = len(grants_clean)
            grants_clean = grants_clean.dropna(subset=['Grant.Amount', 'Year.Authorized'])
            cleaning_report['grants_removed'] = before_drop - len(grants_clean)
            cleaning_report['grants_final'] = len(grants_clean)

            # Clean grantmakers data
            grantmakers_clean = data['grantmakers'].copy()
            grantmakers_clean['Company'] = company_name  # Add company identifier

            numeric_cols_data = ['Total.Assets', 'Total.Giving']
            for col in numeric_cols_data:
                if col in grantmakers_clean.columns:
                    grantmakers_clean[col] = pd.to_numeric(grantmakers_clean[col], errors='coerce')

            before_drop_gm = len(grantmakers_clean)
            grantmakers_clean = grantmakers_clean.dropna(subset=['Total.Assets', 'Total.Giving'])
            cleaning_report['grantmakers_removed'] = before_drop_gm - len(grantmakers_clean)
            cleaning_report['grantmakers_final'] = len(grantmakers_clean)

            # Merge datasets
            merged_data = grants_clean.merge(
                grantmakers_clean[['Grantmaker.Name', 'Total.Assets', 'Total.Giving', 'State']],
                on='Grantmaker.Name',
                how='left',
                suffixes=('', '_grantmaker')
            )

            # Store cleaned data
            all_grants_clean.append(grants_clean)
            all_grantmakers_clean.append(grantmakers_clean)
            all_merged_data.append(merged_data)
            cleaning_reports[company_name] = cleaning_report

        # Combine all companies
        combined_grants = pd.concat(all_grants_clean, ignore_index=True)
        combined_grantmakers = pd.concat(all_grantmakers_clean, ignore_index=True)
        combined_merged = pd.concat(all_merged_data, ignore_index=True)

        return combined_grants, combined_grantmakers, combined_merged, cleaning_reports
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None, None, None, None

@st.cache_data
def categorize_grants(grants_df):
    """Categorize grants based on description keywords."""
    def categorize_description(desc):
        if pd.isna(desc):
            return 'Uncategorized'
        desc_lower = str(desc).lower()

        if any(word in desc_lower for word in ['health', 'medical', 'hospital', 'clinic', 'patient']):
            return 'Healthcare'
        elif any(word in desc_lower for word in ['education', 'school', 'student', 'scholarship', 'university']):
            return 'Education'
        elif any(word in desc_lower for word in ['community', 'social', 'development', 'service']):
            return 'Community Development'
        elif any(word in desc_lower for word in ['research', 'science', 'study']):
            return 'Research'
        elif any(word in desc_lower for word in ['art', 'culture', 'museum', 'music']):
            return 'Arts & Culture'
        elif any(word in desc_lower for word in ['environment', 'conservation', 'sustainability']):
            return 'Environment'
        else:
            return 'Other'

    grants_df['Category'] = grants_df['Description'].apply(categorize_description)
    return grants_df

@st.cache_data
def calculate_transformations(data):
    """Calculate Box-Cox and log transformations."""
    grant_amounts = data[data > 0]
    transformed_boxcox, lambda_param = boxcox(grant_amounts)
    transformed_log = np.log(grant_amounts)
    transformed_log10 = np.log10(grant_amounts)

    return {
        'original': grant_amounts,
        'boxcox': transformed_boxcox,
        'lambda': lambda_param,
        'log': transformed_log,
        'log10': transformed_log10
    }

def main():
    """Main function to render the comprehensive Streamlit dashboard."""

    # Header
    st.title("Foundation Grant Data Analysis")
    st.markdown("### Comprehensive Analysis Dashboard")
    st.markdown("---")

    # Load data
    with st.spinner("Loading and cleaning data..."):
        grants_data, grantmakers_data, merged_data, cleaning_report = load_and_clean_data()

    if grants_data is None:
        st.error("Failed to load data. Please check the file paths.")
        return

    # Categorize grants
    grants_data = categorize_grants(grants_data)

    # Display info about companies being compared
    st.info(f"Comparing data from: {', '.join(sorted(grants_data['Company'].unique()))}")

    st.markdown("---")

    # Get available years across all companies
    years = sorted(grants_data['Year.Authorized'].dropna().unique())

    # Use all data for filtering
    filtered_grants = grants_data

    st.markdown("---")

    # Key metrics at top - Overall
    st.header("Executive Summary Metrics")
    st.subheader("Overall Metrics (All Companies Combined)")
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    with col1:
        st.metric("Total Grants", f"{len(filtered_grants):,}")
    with col2:
        st.metric("Grantmakers", f"{filtered_grants['Grantmaker.Name'].nunique():,}")
    with col3:
        st.metric("Total Amount", f"${filtered_grants['Grant.Amount'].sum()/1e6:.1f}M")
    with col4:
        st.metric("Avg Grant", f"${filtered_grants['Grant.Amount'].mean()/1e3:.1f}K")
    with col5:
        st.metric("Median Grant", f"${filtered_grants['Grant.Amount'].median()/1e3:.1f}K")
    with col6:
        st.metric("Categories", f"{filtered_grants['Category'].nunique()}")

    # Company-by-company comparison
    st.subheader("Company Comparison")
    company_metrics = filtered_grants.groupby('Company').agg({
        'Grant.Amount': ['count', 'sum', 'mean', 'median'],
        'Grantmaker.Name': 'nunique'
    }).round(2)
    company_metrics.columns = ['Total_Grants', 'Total_Amount', 'Avg_Grant', 'Median_Grant', 'Num_Grantmakers']

    # Create comparison visualization
    fig_company_comparison = go.Figure()

    companies_list = company_metrics.index.tolist()
    fig_company_comparison.add_trace(go.Bar(
        name='Total Amount (M$)',
        x=companies_list,
        y=company_metrics['Total_Amount'] / 1e6,
        text=[f'${x/1e6:.1f}M' for x in company_metrics['Total_Amount']],
        textposition='auto',
        marker_color='steelblue'
    ))

    fig_company_comparison.update_layout(
        title='Total Grant Amount by Company',
        xaxis_title='Company',
        yaxis_title='Total Amount (Million $)',
        showlegend=False,
        height=400
    )
    st.plotly_chart(fig_company_comparison, use_container_width=True)

    # Display detailed metrics table
    st.markdown("**Detailed Company Metrics:**")
    display_metrics = company_metrics.copy()
    display_metrics['Total_Amount'] = display_metrics['Total_Amount'].apply(lambda x: f'${x/1e6:.2f}M')
    display_metrics['Avg_Grant'] = display_metrics['Avg_Grant'].apply(lambda x: f'${x/1e3:.1f}K')
    display_metrics['Median_Grant'] = display_metrics['Median_Grant'].apply(lambda x: f'${x/1e3:.1f}K')
    display_metrics.columns = ['Total Grants', 'Total Amount', 'Avg Grant', 'Median Grant', 'Grantmakers']
    st.dataframe(display_metrics, use_container_width=True)

    st.markdown("---")

    # Create comprehensive tabs
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs([
        "Data Cleaning",
        "State Analysis",
        "Distribution & Outliers",
        "Time Series Analysis",
        "Category Analysis",
        "Transformations & Normality",
        "Statistical Testing",
        "Recipient & Subject Analysis",
        "Summary & Insights"
    ])

    # TAB 1: Data Cleaning
    with tab1:
        st.header("Data Cleaning & Engineering")
        st.markdown("**Overview of data preprocessing steps performed for all companies**")

        # Show cleaning summary for each company
        st.subheader("Cleaning Summary by Company")

        if cleaning_report:
            cleaning_data = []
            for company, report in cleaning_report.items():
                cleaning_data.append({
                    'Company': company,
                    'Grants Original': report['grants_original'],
                    'Grants Removed': report['grants_removed'],
                    'Grants Final': report['grants_final'],
                    'Grants Retention %': f"{report['grants_final']/report['grants_original']*100:.1f}%",
                    'Grantmakers Original': report['grantmakers_original'],
                    'Grantmakers Removed': report['grantmakers_removed'],
                    'Grantmakers Final': report['grantmakers_final'],
                    'Grantmakers Retention %': f"{report['grantmakers_final']/report['grantmakers_original']*100:.1f}%"
                })

            cleaning_df = pd.DataFrame(cleaning_data)
            st.dataframe(cleaning_df, use_container_width=True, hide_index=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Data Quality Steps:**")
            st.markdown("""
            1. Converted numeric columns to proper data types
            2. Removed records with missing critical values
            3. Merged datasets on Grantmaker.Name
            4. Created category classifications
            5. Validated year and amount ranges
            6. Added company identifier to all records
            """)

        with col2:
            st.subheader("Missing Data Analysis")

            # Missing data visualization
            missing_data = pd.DataFrame({
                'Column': grants_data.columns,
                'Missing Count': [grants_data[col].isna().sum() for col in grants_data.columns],
                'Missing %': [grants_data[col].isna().sum() / len(grants_data) * 100 for col in grants_data.columns]
            }).sort_values('Missing Count', ascending=False).head(10)

            fig_missing = px.bar(
                missing_data,
                x='Column',
                y='Missing %',
                title='Top 10 Columns by Missing Data %',
                labels={'Missing %': 'Missing Percentage (%)'},
                color='Missing %',
                color_continuous_scale='Reds'
            )
            st.plotly_chart(fig_missing, use_container_width=True)

        # Data types summary
        st.subheader("Data Types & Sample Records")
        col1, col2 = st.columns([1, 2])

        with col1:
            dtypes_df = pd.DataFrame({
                'Column': grants_data.dtypes.index,
                'Data Type': grants_data.dtypes.values.astype(str)
            })
            st.dataframe(dtypes_df.head(15), use_container_width=True, hide_index=True)

        with col2:
            st.markdown("**Sample of Cleaned Data:**")
            st.dataframe(
                grants_data[['Grantmaker.Name', 'Recipient.Name', 'Grant.Amount',
                             'Year.Authorized', 'Category']].head(10),
                use_container_width=True
            )

    # TAB 2: State Analysis
    with tab2:
        st.header("State-Based Analysis - Company Comparison")
        st.markdown("**Geographic distribution of grantmakers and their giving patterns**")

        if grantmakers_data is not None:
            companies_list = sorted(grantmakers_data['Company'].unique())

            # Top 15 States by Number of Grantmakers - 4 companies side by side
            st.subheader("Top 15 States by Number of Grantmakers")
            cols = st.columns(4)

            for idx, company in enumerate(companies_list):
                company_data = grantmakers_data[grantmakers_data['Company'] == company]
                state_analysis = company_data.groupby('State').agg({
                    'Grantmaker.Name': 'count'
                }).round(2).reset_index()
                state_analysis.columns = ['State', 'Org_Count']
                state_analysis = state_analysis.sort_values('Org_Count', ascending=False).head(15)

                with cols[idx]:
                    fig_state_orgs = px.bar(
                        state_analysis,
                        x='State',
                        y='Org_Count',
                        title=f'{company}',
                        labels={'Org_Count': 'Number of Organizations'},
                        color='Org_Count',
                        color_continuous_scale='Blues'
                    )
                    fig_state_orgs.update_layout(showlegend=False, height=400)
                    st.plotly_chart(fig_state_orgs, use_container_width=True)

            # Top 15 States by Total Giving - 4 companies side by side
            st.subheader("Top 15 States by Total Giving")
            cols = st.columns(4)

            for idx, company in enumerate(companies_list):
                company_data = grantmakers_data[grantmakers_data['Company'] == company]
                state_analysis = company_data.groupby('State').agg({
                    'Total.Giving': 'sum'
                }).round(2).reset_index()
                state_analysis.columns = ['State', 'Total_Giving']
                state_analysis = state_analysis.sort_values('Total_Giving', ascending=False).head(15)

                with cols[idx]:
                    fig_state_giving = px.bar(
                        state_analysis,
                        x='State',
                        y='Total_Giving',
                        title=f'{company}',
                        labels={'Total_Giving': 'Total Giving ($)'},
                        color='Total_Giving',
                        color_continuous_scale='Greens'
                    )
                    fig_state_giving.update_layout(showlegend=False, height=400)
                    st.plotly_chart(fig_state_giving, use_container_width=True)

            # Top 5 States Distribution - Pie charts side by side
            st.subheader("Top 5 States - Total Giving Distribution")
            cols = st.columns(4)

            for idx, company in enumerate(companies_list):
                company_data = grantmakers_data[grantmakers_data['Company'] == company]
                state_analysis = company_data.groupby('State').agg({
                    'Total.Giving': 'sum'
                }).round(2).reset_index()
                state_analysis = state_analysis.sort_values('Total.Giving', ascending=False).head(5)

                with cols[idx]:
                    fig_pie_state = px.pie(
                        state_analysis,
                        values='Total.Giving',
                        names='State',
                        title=f'{company}'
                    )
                    fig_pie_state.update_layout(height=400)
                    st.plotly_chart(fig_pie_state, use_container_width=True)

    # TAB 3: Distribution & Outliers
    with tab3:
        st.header("Grant Amount Distribution & Outlier Analysis - Company Comparison")

        companies_list = sorted(filtered_grants['Company'].unique())

        # Histogram - 4 companies side by side
        st.subheader("Distribution of Grant Amounts")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]

            with cols[idx]:
                fig_hist = px.histogram(
                    company_grants,
                    x='Grant.Amount',
                    nbins=50,
                    title=f'{company}',
                    labels={'Grant.Amount': 'Grant Amount ($)'},
                    color_discrete_sequence=['steelblue']
                )
                fig_hist.add_vline(x=company_grants['Grant.Amount'].mean(),
                                  line_dash="dash", line_color="red",
                                  annotation_text=f"Mean: ${company_grants['Grant.Amount'].mean()/1e3:.0f}K")
                fig_hist.add_vline(x=company_grants['Grant.Amount'].median(),
                                  line_dash="dash", line_color="green",
                                  annotation_text=f"Median: ${company_grants['Grant.Amount'].median()/1e3:.0f}K")
                fig_hist.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig_hist, use_container_width=True)

        # Box plot - 4 companies side by side
        st.subheader("Box Plot: Showing Outliers")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]

            with cols[idx]:
                fig_box = px.box(
                    company_grants,
                    y='Grant.Amount',
                    title=f'{company}',
                    labels={'Grant.Amount': 'Grant Amount ($)'}
                )
                fig_box.update_layout(height=400, showlegend=False)
                st.plotly_chart(fig_box, use_container_width=True)

        # Violin plot by category for each company
        st.subheader("Violin Plot: Grant Distribution by Category (Top 6)")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            top_categories = company_grants['Category'].value_counts().head(6).index
            filtered_for_violin = company_grants[company_grants['Category'].isin(top_categories)]

            with cols[idx]:
                fig_violin = px.violin(
                    filtered_for_violin,
                    y='Grant.Amount',
                    x='Category',
                    title=f'{company}',
                    color='Category',
                    box=True,
                    points='outliers'
                )
                fig_violin.update_layout(height=500, showlegend=False)
                fig_violin.update_xaxes(tickangle=45)
                st.plotly_chart(fig_violin, use_container_width=True)

        # Statistics comparison table
        st.subheader("Distribution Statistics Comparison")
        stats_data = []

        for company in companies_list:
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            Q1 = company_grants['Grant.Amount'].quantile(0.25)
            Q3 = company_grants['Grant.Amount'].quantile(0.75)
            IQR = Q3 - Q1
            outliers = company_grants[
                (company_grants['Grant.Amount'] < Q1 - 1.5 * IQR) |
                (company_grants['Grant.Amount'] > Q3 + 1.5 * IQR)
            ]

            stats_data.append({
                'Company': company,
                'Skewness': f"{company_grants['Grant.Amount'].skew():.4f}",
                'Kurtosis': f"{company_grants['Grant.Amount'].kurtosis():.4f}",
                'Outliers': f"{len(outliers):,} ({len(outliers)/len(company_grants)*100:.1f}%)",
                'IQR': f"${IQR:,.0f}",
                'Q1': f"${Q1:,.0f}",
                'Q3': f"${Q3:,.0f}"
            })

        stats_df = pd.DataFrame(stats_data)
        st.dataframe(stats_df, use_container_width=True, hide_index=True)

    # TAB 4: Time Series Analysis
    with tab4:
        st.header("Time Series Analysis - Company Comparison")

        companies_list = sorted(filtered_grants['Company'].unique())

        # Total Grant Amounts by Year - 4 companies side by side
        st.subheader("Total Grant Amounts by Year")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            yearly_data = company_grants.groupby('Year.Authorized').agg({
                'Grant.Amount': ['sum', 'mean', 'count']
            }).reset_index()
            yearly_data.columns = ['Year', 'Total_Amount', 'Avg_Amount', 'Grant_Count']

            with cols[idx]:
                fig_time = go.Figure()
                fig_time.add_trace(go.Bar(
                    x=yearly_data['Year'],
                    y=yearly_data['Total_Amount'],
                    name='Total Amount',
                    marker_color='steelblue',
                    text=yearly_data['Total_Amount'],
                    texttemplate='$%{text:.2s}',
                    textposition='outside'
                ))
                fig_time.update_layout(
                    title=f'{company}',
                    xaxis_title='Year',
                    yaxis_title='Total Grant Amount ($)',
                    showlegend=False,
                    height=400
                )
                st.plotly_chart(fig_time, use_container_width=True)

        # Grant Count by Year - 4 companies side by side
        st.subheader("Number of Grants by Year")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            yearly_data = company_grants.groupby('Year.Authorized').agg({
                'Grant.Amount': 'count'
            }).reset_index()
            yearly_data.columns = ['Year', 'Grant_Count']

            with cols[idx]:
                fig_count = px.line(
                    yearly_data,
                    x='Year',
                    y='Grant_Count',
                    title=f'{company}',
                    markers=True
                )
                fig_count.update_layout(
                    xaxis_title='Year',
                    yaxis_title='Number of Grants',
                    showlegend=False,
                    height=400
                )
                st.plotly_chart(fig_count, use_container_width=True)

        # Average Grant Amount by Year - 4 companies side by side
        st.subheader("Average Grant Amount by Year")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            yearly_data = company_grants.groupby('Year.Authorized').agg({
                'Grant.Amount': 'mean'
            }).reset_index()
            yearly_data.columns = ['Year', 'Avg_Amount']

            with cols[idx]:
                fig_avg = px.line(
                    yearly_data,
                    x='Year',
                    y='Avg_Amount',
                    title=f'{company}',
                    markers=True
                )
                fig_avg.update_layout(
                    xaxis_title='Year',
                    yaxis_title='Average Grant Amount ($)',
                    showlegend=False,
                    height=400
                )
                st.plotly_chart(fig_avg, use_container_width=True)

        # Year-over-Year Statistics Comparison Table
        st.subheader("Year-over-Year Statistics by Company")

        for company in companies_list:
            st.markdown(f"**{company}**")
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            yearly_data = company_grants.groupby('Year.Authorized').agg({
                'Grant.Amount': ['sum', 'mean', 'count']
            }).reset_index()
            yearly_data.columns = ['Year', 'Total_Amount', 'Avg_Amount', 'Grant_Count']
            yearly_data['YoY_Growth_%'] = yearly_data['Total_Amount'].pct_change() * 100

            st.dataframe(
                yearly_data.style.format({
                    'Total_Amount': '${:,.0f}',
                    'Avg_Amount': '${:,.0f}',
                    'Grant_Count': '{:,.0f}',
                    'YoY_Growth_%': '{:+.2f}%'
                }),
                use_container_width=True
            )

    # TAB 5: Category Analysis
    with tab5:
        st.header("Category & Description Analysis - Company Comparison")
        st.markdown("**Grants categorized by description keywords**")

        companies_list = sorted(filtered_grants['Company'].unique())

        # Category distribution by amount - Pie charts side by side
        st.subheader("Grant Amount Distribution by Category")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            category_summary = company_grants.groupby('Category').agg({
                'Grant.Amount': 'sum'
            }).round(2).reset_index()
            category_summary.columns = ['Category', 'Total_Amount']
            category_summary = category_summary.sort_values('Total_Amount', ascending=False)

            with cols[idx]:
                fig_pie = px.pie(
                    category_summary,
                    values='Total_Amount',
                    names='Category',
                    title=f'{company}',
                    color_discrete_sequence=px.colors.qualitative.Set3
                )
                fig_pie.update_layout(height=400)
                st.plotly_chart(fig_pie, use_container_width=True)

        # Number of Grants by Category - Bar charts side by side
        st.subheader("Number of Grants by Category")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            category_summary = company_grants.groupby('Category').agg({
                'Grant.Amount': 'count'
            }).round(2).reset_index()
            category_summary.columns = ['Category', 'Grant_Count']
            category_summary = category_summary.sort_values('Grant_Count', ascending=True)

            with cols[idx]:
                fig_cat_count = px.bar(
                    category_summary,
                    x='Grant_Count',
                    y='Category',
                    orientation='h',
                    title=f'{company}',
                    color='Grant_Count',
                    color_continuous_scale='Viridis'
                )
                fig_cat_count.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig_cat_count, use_container_width=True)

        # Category Trends Over Time - Line charts side by side
        st.subheader("Category Trends Over Time")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            category_time = company_grants.groupby(['Year.Authorized', 'Category'])['Grant.Amount'].sum().reset_index()

            with cols[idx]:
                fig_cat_time = px.line(
                    category_time,
                    x='Year.Authorized',
                    y='Grant.Amount',
                    color='Category',
                    title=f'{company}',
                    markers=True
                )
                fig_cat_time.update_layout(showlegend=False, height=400)
                st.plotly_chart(fig_cat_time, use_container_width=True)

        # Category statistics table by company
        st.subheader("Category Statistics Summary by Company")

        for company in companies_list:
            st.markdown(f"**{company}**")
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            category_summary = company_grants.groupby('Category').agg({
                'Grant.Amount': ['sum', 'mean', 'count']
            }).round(2)
            category_summary.columns = ['Total_Amount', 'Avg_Amount', 'Grant_Count']
            category_summary = category_summary.sort_values('Total_Amount', ascending=False).reset_index()

            category_display = category_summary.copy()
            category_display['Total_Amount'] = category_display['Total_Amount'].apply(lambda x: f'${x:,.0f}')
            category_display['Avg_Amount'] = category_display['Avg_Amount'].apply(lambda x: f'${x:,.0f}')
            st.dataframe(category_display, use_container_width=True, hide_index=True)

    # TAB 6: Transformations & Normality
    with tab6:
        st.header("Data Transformations & Normality Tests")
        st.markdown("**Addressing right-skewed distribution through transformations**")

        # Calculate transformations
        transformations = calculate_transformations(filtered_grants['Grant.Amount'])

        # Create 2x2 subplot
        fig_trans = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Original (Right-Skewed)', 'Box-Cox Transformation',
                          'Natural Log (ln)', 'Q-Q Plot: Box-Cox'),
            specs=[[{'type': 'histogram'}, {'type': 'histogram'}],
                   [{'type': 'histogram'}, {'type': 'scatter'}]]
        )

        # Original
        fig_trans.add_trace(
            go.Histogram(x=transformations['original'], name='Original',
                        marker_color='steelblue', nbinsx=50),
            row=1, col=1
        )

        # Box-Cox
        fig_trans.add_trace(
            go.Histogram(x=transformations['boxcox'], name='Box-Cox',
                        marker_color='darkred', nbinsx=50),
            row=1, col=2
        )

        # Log
        fig_trans.add_trace(
            go.Histogram(x=transformations['log'], name='Natural Log',
                        marker_color='green', nbinsx=50),
            row=2, col=1
        )

        # Q-Q Plot
        qq_data = probplot(transformations['boxcox'], dist="norm")
        fig_trans.add_trace(
            go.Scatter(x=qq_data[0][0], y=qq_data[0][1], mode='markers',
                      name='Q-Q Plot', marker=dict(color='blue')),
            row=2, col=2
        )
        fig_trans.add_trace(
            go.Scatter(x=qq_data[0][0], y=qq_data[1][1] + qq_data[1][0]*qq_data[0][0],
                      mode='lines', name='Reference Line', line=dict(color='red')),
            row=2, col=2
        )

        fig_trans.update_layout(height=700, showlegend=False, title_text="Transformation Comparison")
        st.plotly_chart(fig_trans, use_container_width=True)

        # Normality tests
        st.subheader("Normality Test Results")

        # Test original
        sample_size = min(5000, len(transformations['original']))
        shapiro_orig = shapiro(transformations['original'].sample(sample_size, random_state=42))
        dagostino_orig = normaltest(transformations['original'])

        # Test transformed
        shapiro_trans = shapiro(transformations['boxcox'][:5000])
        dagostino_trans = normaltest(transformations['boxcox'])

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown("**Original Data**")
            st.write(f"Skewness: {pd.Series(transformations['original']).skew():.4f}")
            st.write(f"Shapiro p: {shapiro_orig[1]:.4e}")

        with col2:
            st.markdown(f"**Box-Cox (λ={transformations['lambda']:.4f})**")
            st.write(f"Skewness: {pd.Series(transformations['boxcox']).skew():.4f}")
            st.write(f"Shapiro p: {shapiro_trans[1]:.4e}")

        with col3:
            st.markdown("**Natural Log**")
            st.write(f"Skewness: {pd.Series(transformations['log']).skew():.4f}")

        with col4:
            st.markdown("**Common Log**")
            st.write(f"Skewness: {pd.Series(transformations['log10']).skew():.4f}")

        # Recommendation
        abs_skews = {
            'Box-Cox': abs(pd.Series(transformations['boxcox']).skew()),
            'Natural Log': abs(pd.Series(transformations['log']).skew()),
            'Common Log': abs(pd.Series(transformations['log10']).skew())
        }
        best_transform = min(abs_skews, key=abs_skews.get)

        st.success(f"**Best Transformation:** {best_transform} (Lowest skewness: {abs_skews[best_transform]:.4f})")
        st.info("**Interpretation:** Q-Q plot shows transformed data follows normal distribution more closely")

    # TAB 7: Statistical Testing
    with tab7:
        st.header("Hypothesis Testing & Statistical Analysis")

        if merged_data is not None and len(merged_data) > 0:
            st.subheader("H1: Organizations with Higher Assets Give Larger Grants")

            # Split by asset median
            asset_median = merged_data['Total.Assets'].median()
            high_assets = merged_data[merged_data['Total.Assets'] >= asset_median]['Grant.Amount'].dropna()
            low_assets = merged_data[merged_data['Total.Assets'] < asset_median]['Grant.Amount'].dropna()

            if len(high_assets) > 0 and len(low_assets) > 0:
                # T-test
                t_stat, p_value = stats.ttest_ind(high_assets, low_assets)

                # Mann-Whitney U
                u_stat, u_pvalue = stats.mannwhitneyu(high_assets, low_assets, alternative='two-sided')

                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric("High Assets Group", f"n={len(high_assets):,}")
                    st.write(f"Mean: ${high_assets.mean():,.0f}")
                    st.write(f"Median: ${high_assets.median():,.0f}")

                with col2:
                    st.metric("Low Assets Group", f"n={len(low_assets):,}")
                    st.write(f"Mean: ${low_assets.mean():,.0f}")
                    st.write(f"Median: ${low_assets.median():,.0f}")

                with col3:
                    st.metric("T-Test Result", "SIGNIFICANT" if p_value < 0.05 else "NOT SIGNIFICANT")
                    st.write(f"t-statistic: {t_stat:.4f}")
                    st.write(f"p-value: {p_value:.6f}")

                # Visualization
                comparison_data = pd.DataFrame({
                    'Grant Amount': list(high_assets) + list(low_assets),
                    'Group': ['High Assets']*len(high_assets) + ['Low Assets']*len(low_assets)
                })

                fig_comparison = px.box(
                    comparison_data,
                    x='Group',
                    y='Grant Amount',
                    title='Grant Amount Distribution: High vs Low Assets',
                    color='Group',
                    color_discrete_map={'High Assets': 'green', 'Low Assets': 'orange'}
                )
                st.plotly_chart(fig_comparison, use_container_width=True)

                st.markdown("**Test Results:**")
                st.write(f"- Student's t-test: t={t_stat:.4f}, p={p_value:.6f}")
                st.write(f"- Mann-Whitney U: U={u_stat:.4f}, p={u_pvalue:.6f}")

                if p_value < 0.05:
                    st.success("Conclusion: Organizations with higher assets give significantly larger grants")
                else:
                    st.warning("Conclusion: No significant difference found")

            # H2: Grant Count vs Total Funding Correlation
            st.subheader("H2: Higher Grant Count Correlates with Higher Funding")

            # Aggregate by grantmaker: count of grants and total funding
            grantmaker_stats = filtered_grants.groupby('Grantmaker.Name').agg({
                'Grant.Amount': ['sum', 'count']
            }).reset_index()
            grantmaker_stats.columns = ['Grantmaker', 'Total_Funding', 'Grant_Count']

            # Pearson correlation
            corr_coef, corr_pvalue = stats.pearsonr(grantmaker_stats['Grant_Count'], grantmaker_stats['Total_Funding'])

            # Spearman correlation (non-parametric)
            spearman_coef, spearman_pvalue = stats.spearmanr(grantmaker_stats['Grant_Count'], grantmaker_stats['Total_Funding'])

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Pearson Correlation", f"{corr_coef:.4f}")
                st.write(f"p-value: {corr_pvalue:.6f}")

            with col2:
                st.metric("Spearman Correlation", f"{spearman_coef:.4f}")
                st.write(f"p-value: {spearman_pvalue:.6f}")

            with col3:
                st.metric("Result", "SIGNIFICANT" if corr_pvalue < 0.05 else "NOT SIGNIFICANT")
                st.write(f"n={len(grantmaker_stats):,} grantmakers")

            # Scatter plot
            fig_scatter = px.scatter(
                grantmaker_stats,
                x='Grant_Count',
                y='Total_Funding',
                title='Grant Count vs Total Funding by Grantmaker',
                labels={'Grant_Count': 'Number of Grants', 'Total_Funding': 'Total Funding ($)'},
                trendline='ols',
                hover_data=['Grantmaker']
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

            st.markdown("**Test Results:**")
            st.write(f"- Pearson r={corr_coef:.4f}, p={corr_pvalue:.6f}")
            st.write(f"- Spearman rho={spearman_coef:.4f}, p={spearman_pvalue:.6f}")

            if corr_pvalue < 0.05 and corr_coef > 0:
                st.success(f"Conclusion: Positive correlation ({corr_coef:.2f}) - Higher grant count is associated with higher funding")
            elif corr_pvalue < 0.05 and corr_coef < 0:
                st.warning(f"Conclusion: Negative correlation ({corr_coef:.2f}) - Higher grant count is associated with lower funding")
            else:
                st.warning("Conclusion: No significant correlation found between grant count and total funding")

            st.markdown("---")

            # ANOVA - Categories
            st.subheader("H3: Grant Amounts Differ Across Categories")

            category_groups = [filtered_grants[filtered_grants['Category'] == cat]['Grant.Amount'].dropna()
                             for cat in filtered_grants['Category'].unique() if len(filtered_grants[filtered_grants['Category'] == cat]) > 0]

            if len(category_groups) > 2:
                f_stat, anova_p = stats.f_oneway(*category_groups)

                col1, col2 = st.columns(2)
                with col1:
                    st.metric("ANOVA F-statistic", f"{f_stat:.4f}")
                    st.metric("p-value", f"{anova_p:.6f}")
                    st.metric("Result", "SIGNIFICANT" if anova_p < 0.05 else "NOT SIGNIFICANT")

                with col2:
                    if anova_p < 0.05:
                        st.success("Grant amounts significantly differ across categories")
                    else:
                        st.warning("No significant difference across categories")
        else:
            st.warning("Merged data not available for hypothesis testing")

    # TAB 8: Recipient & Subject Analysis
    with tab8:
        st.header("Recipient & Subject Analysis - Company Comparison")

        companies_list = sorted(filtered_grants['Company'].unique())

        # Top Recipients - 4 companies side by side
        st.subheader("Top 15 Grant Recipients by Company")
        cols = st.columns(4)

        for idx, company in enumerate(companies_list):
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            top_recipients = company_grants.groupby('Recipient.Name')['Grant.Amount'].agg([
                ('Total', 'sum'),
                ('Count', 'count')
            ]).sort_values('Total', ascending=False).head(15)

            with cols[idx]:
                fig_recipients = px.bar(
                    top_recipients.reset_index(),
                    y='Recipient.Name',
                    x='Total',
                    orientation='h',
                    title=f'{company}',
                    color='Total',
                    color_continuous_scale='Purples'
                )
                fig_recipients.update_layout(yaxis={'categoryorder': 'total ascending'}, showlegend=False, height=500)
                st.plotly_chart(fig_recipients, use_container_width=True)

        # Subject analysis (if Primary.Subject exists)
        if 'Primary.Subject' in filtered_grants.columns:
            st.subheader("Primary Subject Analysis by Company")
            cols = st.columns(4)

            for idx, company in enumerate(companies_list):
                company_grants = filtered_grants[filtered_grants['Company'] == company]
                subject_summary = company_grants.groupby('Primary.Subject')['Grant.Amount'].agg([
                    ('Total', 'sum'),
                    ('Count', 'count')
                ]).sort_values('Total', ascending=False).head(10)

                with cols[idx]:
                    fig_subject = px.bar(
                        subject_summary.reset_index(),
                        x='Primary.Subject',
                        y='Total',
                        title=f'{company}',
                        color='Total',
                        color_continuous_scale='Teal'
                    )
                    fig_subject.update_layout(showlegend=False, height=400)
                    fig_subject.update_xaxes(tickangle=45)
                    st.plotly_chart(fig_subject, use_container_width=True)

        # Repeat recipients analysis by company
        st.subheader("Repeat Recipients Analysis by Company")

        repeat_data = []
        for company in companies_list:
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            recipient_counts = company_grants['Recipient.Name'].value_counts()
            repeat_recipients = recipient_counts[recipient_counts > 1]

            repeat_data.append({
                'Company': company,
                'Total Unique Recipients': f"{len(recipient_counts):,}",
                'Repeat Recipients': f"{len(repeat_recipients):,}",
                'Repeat %': f"{len(repeat_recipients)/len(recipient_counts)*100:.1f}%"
            })

        repeat_df = pd.DataFrame(repeat_data)
        st.dataframe(repeat_df, use_container_width=True, hide_index=True)

    # TAB 9: Summary & Insights
    with tab9:
        st.header("Executive Summary & Key Insights - Company Comparison")

        companies_list = sorted(filtered_grants['Company'].unique())

        # Data Overview by Company
        st.subheader("Data Overview by Company")

        overview_data = []
        for company in companies_list:
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            company_grantmakers = grantmakers_data[grantmakers_data['Company'] == company] if grantmakers_data is not None else None

            overview_data.append({
                'Company': company,
                'Total Grants': f"{len(company_grants):,}",
                'Grantmakers': f"{company_grants['Grantmaker.Name'].nunique():,}",
                'Total Amount': f"${company_grants['Grant.Amount'].sum()/1e6:.2f}M",
                'Avg Grant': f"${company_grants['Grant.Amount'].mean()/1e3:.1f}K",
                'Median Grant': f"${company_grants['Grant.Amount'].median()/1e3:.1f}K",
                'Years': f"{int(company_grants['Year.Authorized'].min())}-{int(company_grants['Year.Authorized'].max())}",
                'States': f"{company_grantmakers['State'].nunique()}" if company_grantmakers is not None else "N/A"
            })

        overview_df = pd.DataFrame(overview_data)
        st.dataframe(overview_df, use_container_width=True, hide_index=True)

        st.markdown("---")

        # Statistical Summary by Company
        st.subheader("Statistical Summary by Company")

        stats_data = []
        for company in companies_list:
            company_grants = filtered_grants[filtered_grants['Company'] == company]

            stats_data.append({
                'Company': company,
                'Mean': f"${company_grants['Grant.Amount'].mean():,.0f}",
                'Median': f"${company_grants['Grant.Amount'].median():,.0f}",
                'Std Dev': f"${company_grants['Grant.Amount'].std():,.0f}",
                'Skewness': f"{company_grants['Grant.Amount'].skew():.4f}",
                'Min': f"${company_grants['Grant.Amount'].min():,.0f}",
                'Max': f"${company_grants['Grant.Amount'].max():,.0f}",
                'Q1': f"${company_grants['Grant.Amount'].quantile(0.25):,.0f}",
                'Q3': f"${company_grants['Grant.Amount'].quantile(0.75):,.0f}"
            })

        stats_df = pd.DataFrame(stats_data)
        st.dataframe(stats_df, use_container_width=True, hide_index=True)

        st.markdown("---")

        # Key findings by company
        st.subheader("Key Findings by Company")

        for company in companies_list:
            company_grants = filtered_grants[filtered_grants['Company'] == company]
            Q1 = company_grants['Grant.Amount'].quantile(0.25)
            Q3 = company_grants['Grant.Amount'].quantile(0.75)
            IQR = Q3 - Q1
            outliers = company_grants[
                (company_grants['Grant.Amount'] < Q1 - 1.5 * IQR) |
                (company_grants['Grant.Amount'] > Q3 + 1.5 * IQR)
            ]

            st.markdown(f"### {company}")

            total_grants = 0
            total_original = 0
            for comp_name, report in cleaning_report.items():
                if comp_name == company:
                    total_grants = report['grants_final']
                    total_original = report['grants_original']
                    break

            retention_rate = (total_grants / total_original * 100) if total_original > 0 else 0

            findings = [
                f"**Data Quality:** Processed {total_grants:,} grants with {retention_rate:.1f}% retention rate",
                f"**Distribution:** Skewness of {company_grants['Grant.Amount'].skew():.2f} indicates right-skewed distribution",
                f"**Total Funding:** ${company_grants['Grant.Amount'].sum()/1e6:.2f}M across {len(company_grants):,} grants",
                f"**Top Category:** {company_grants['Category'].value_counts().index[0]} is the most funded category",
                f"**Outliers:** {len(outliers)/len(company_grants)*100:.1f}% of grants are statistical outliers (IQR method)",
                f"**Grant Range:** From ${company_grants['Grant.Amount'].min():,.0f} to ${company_grants['Grant.Amount'].max():,.0f}"
            ]

            for finding in findings:
                st.markdown(f"- {finding}")

            st.markdown("")

        st.markdown("---")

        # Overall comparative insights
        st.subheader("Overall Comparative Insights")

        comparative_insights = [
            f"**Total Dataset:** Analyzed {len(filtered_grants):,} grants across {len(companies_list)} companies",
            f"**Combined Funding:** ${filtered_grants['Grant.Amount'].sum()/1e6:.2f}M in total grant amounts",
            f"**Company Diversity:** Comparing healthcare foundations from different regions and systems",
            "**Statistical Methods:** Applied transformations, hypothesis testing, and distribution analysis",
            "**Geographic Coverage:** Multi-state analysis showing regional patterns in grantmaking"
        ]

        for insight in comparative_insights:
            st.markdown(f"- {insight}")


if __name__ == "__main__":
    main()
