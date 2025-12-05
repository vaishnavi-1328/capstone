# Quick Start Guide

## Running the Application

### Local Development
```bash
# 1. Navigate to project directory
cd /Users/vaishnavis/Desktop/integrated_capsone

# 2. Install dependencies (first time only)
pip install -r requirements.txt

# 3. Run the application
streamlit run Home.py

# 4. Open browser to http://localhost:8501
```

## Application Structure

### 7 Analysis Pages
1. **Foundation Grants** - Foundation giving patterns
2. **NIH Awards** - NIH funding trends  
3. **Q1 Research Themes** - 58 research categories
4. **Q2 Institutional Funding** - 4 institutions compared
5. **Q3 Portfolio Evolution** - Trends over time
6. **Q4 Predictive Features** - Grant size predictors
7. **Q6 Top Topics** - Top 15 topics & strengths

### Resource Folders
- `pages/plotly_charts/` - 14 interactive HTML charts
- `pages/csv_tables/` - 4 data tables
- `pages/images/` - 37 visualizations
- `pages/q6_images/` - 9 topic visualizations

## Dependencies
All required packages are in `requirements.txt`:
- streamlit
- pandas
- numpy
- plotly
- scipy

## Deployment to Streamlit Cloud

1. **Commit to GitHub**
   ```bash
   git add .
   git commit -m "Integrated all Q packages"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your repository
   - Main file: `Home.py`
   - Click "Deploy"

## Troubleshooting

**Pages not showing?**
- Restart Streamlit (Ctrl+C, then run again)
- Check files are in `pages/` folder

**Missing charts/images?**
- Verify resource folders are in `pages/` directory
- Check folder names are exact (case-sensitive)

**Import errors?**
- Run: `pip install -r requirements.txt`

## Support Files
- `INTEGRATION_COMPLETE.md` - Detailed integration documentation
- `requirements.txt` - Python dependencies
- `Home.py` - Main application entry point

---
Ready to explore! 🚀
