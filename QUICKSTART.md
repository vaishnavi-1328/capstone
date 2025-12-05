# Quick Start Guide - NIH Research Grants Analysis Dashboard

## Running the Application

### Step 1: Open Terminal/Command Prompt

Navigate to the project directory:

```bash
cd /Users/vaishnavis/Desktop/Capstone_Private
```

### Step 2: Run Streamlit

```bash
streamlit run Home.py
```

### Step 3: Access the Dashboard

The application will automatically open in your browser at:
```
http://localhost:8501
```

If it doesn't open automatically, copy the URL from the terminal and paste it into your browser.

## Navigation

The integrated dashboard now has:

- **Home Page** - Project overview and introduction
- **Foundation Grants Analysis** - Comprehensive analysis of 4 healthcare systems
- **NIH Awards Analysis** - Award patterns by institution, topic, disease, and method

Use the **sidebar** (☰ icon in top-left) to switch between pages.

## What Changed?

### Before Integration
- Two separate Streamlit applications
- Absolute file paths (only worked on your machine)
- No unified navigation

### After Integration
- Single unified multi-page application
- Relative file paths (works on any machine)
- Clean sidebar navigation
- Professional home page
- Easy to add more pages for team members

## File Structure

```
Capstone_Private/
├── Home.py                                    # Launch this file
├── pages/
│   ├── 1_Foundation_Grants_Analysis.py       # Your foundation analysis
│   ├── 2_NIH_Awards_Analysis.py              # NIH awards analysis
│   └── [Future team member pages go here]
├── Streamlit/
│   └── Streamlit_data/                        # NIH data files
└── [Foundation CSV files in root]             # Foundation data files
```

## For Team Members Adding Pages

1. Create a file in `pages/` directory
2. Name it: `3_Your_Analysis_Name.py`
3. Use the template in `README_STREAMLIT_INTEGRATION.md`
4. Your page will automatically appear in the sidebar!

## Stopping the Application

Press `Ctrl + C` in the terminal where Streamlit is running.

## Troubleshooting

**Problem:** "File not found" error
**Solution:** Make sure you're running from the project root: `/Users/vaishnavis/Desktop/Capstone_Private`

**Problem:** Page doesn't show in sidebar
**Solution:** Make sure your file is in `pages/` and starts with a number (e.g., `3_My_Analysis.py`)

**Problem:** Port already in use
**Solution:** Run with a different port: `streamlit run Home.py --server.port 8502`

## Next Steps

1. Review the integrated application
2. Share `README_STREAMLIT_INTEGRATION.md` with your team
3. Team members can add their analysis pages to `pages/` directory
4. All pages will automatically appear in the navigation

---

**Ready to go!** Just run `streamlit run Home.py` and explore your integrated dashboard.
