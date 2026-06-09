import streamlit as st
import pandas as pd
from filters import apply_filters
import charts as ch

# Page Layout Configuration
st.set_page_config(page_title="Luxury Titanic Dashboard", layout="wide")

# Custom CSS to inject the Red-Brown Header Ribbon, Sidebar, and Text alignment
st.markdown("""
    <style>
    /* 1. Top Header Ribbon Line: Changing to a beautiful Brown-Red Mixed color */
    header[data-testid="stHeader"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 6px;  /* Thickness of the top ribbon */
        background: linear-gradient(90deg, #8b2635, #5c1d24) !important; /* Premium Brownish Red Mix */
        z-index: 9999;
    }
    header[data-testid="stHeader"] {
        background-color: transparent !important;
    }
    
    /* 2. Main Dashboard Background */
    .stApp { 
        background-color: #0e1117 !important; 
    }
    
    /* 3. Sidebar Area: Beautiful Mixed Medium Pink & Red Color */
    section[data-testid="stSidebar"] {
        background-color: #d94156 !important;
        box-shadow: 4px 0px 10px rgba(0, 0, 0, 0.4) !important;
    }
    
    /* 4. Dropdown Drop-boxes Styling */
    div[data-baseweb="select"] > div {
        background-color: #ff3333 !important;
        border: 2px solid #b3001b !important;
        border-radius: 6px !important;
    }
    
    /* Force text inside active selection boxes to be solid black */
    div[data-testid="stSelectboxVirtualDropdown"] span, 
    div[data-baseweb="select"] span,
    div[aria-haspopup="listbox"] {
        color: #000000 !important; 
        font-weight: bold !important;
    }
    svg {
        fill: #000000 !important;
    }
    
    /* 5. Sidebar Writing Customization (Solid Pure Black) */
    section[data-testid="stSidebar"] .stSelectbox label p {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 15px !important;
    }
    section[data-testid="stSidebar"] p {
        color: #000000 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
        opacity: 0.9 !important;
    }
    
    /* 6. Main Content Heading Visibility */
    h1 { 
        color: #ffffff !important; 
        font-family: 'Segoe UI', system-ui, sans-serif !important; 
        font-weight: 800 !important;
    }
    h3 { 
        color: #56cfe1 !important; 
        font-family: 'Segoe UI', system-ui, sans-serif !important; 
        border-bottom: 1px solid #21262d !important; 
        padding-bottom: 10px !important; 
    }
    
    /* 7. Main Dashboard Regular Text Color */
    .main p, .main span { 
        color: #c9d1d9 !important; 
    }
    
    /* 8. KPI Metric Boxes Styling */
    div[data-testid="stMetricWidget"] {
        background-color: #161b22 !important;
        border: 1px solid #21262d !important;
        border-radius: 10px !important;
        padding: 15px 20px !important;
    }
    div[data-testid="stMetricValue"] { 
        font-size: 36px !important; 
        font-weight: bold !important; 
        color: #56cfe1 !important; 
    }
    div[data-testid="stMetricLabel"] { 
        font-size: 14px !important; 
        color: #8b949e !important; 
        text-transform: uppercase !important; 
    }
    </style>
""", unsafe_allow_html=True)

# Main Content Header Area
st.markdown("<h1>🚢 Titanic Executive Analytics Dashboard</h1>", unsafe_allow_html=True)
st.write("An immersive data analysis application mapping passenger dynamics, pricing tier layouts, and historical survival distributions.")

# Load Dataset
df = pd.read_csv('data/titanic.csv')

# Sidebar Panel Configuration
st.sidebar.markdown("<h3 style='color:#56cfe1; border:none; margin:0; font-weight:800;'>Global Filters</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p>Slice data live across charts</p>", unsafe_allow_html=True)

gender_options = ["All"] + list(df['sex'].unique())
gender = st.sidebar.selectbox("Passenger Gender Selection:", gender_options)

class_options = ["All"] + [str(c) for c in sorted(df['pclass'].unique())]
pclass = st.sidebar.selectbox("Ticket Class Tier:", class_options)

# Process Filtered Rows
filtered_df = apply_filters(df, gender, pclass)

# KPI Highlights Row
st.subheader("Key Performance Indicators (KPIs)")
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
with col_kpi1:
    st.metric(label="Total Analyzed Passengers", value=f"{len(filtered_df):,}")
with col_kpi2:
    avg_fare = filtered_df['fare'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Fare Paid", value=f"${avg_fare:.2f}")
with col_kpi3:
    avg_age = filtered_df['age'].mean() if not filtered_df.empty else 0
    st.metric(label="Average Passenger Age", value=f"{avg_age:.1f} Yrs")

# Interactive Charts Layout System (Grid of 2 columns)
st.subheader("Advanced Data Visualization Grid")

row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    st.pyplot(ch.draw_bar_chart(filtered_df))
with row1_col2:
    st.pyplot(ch.draw_pie_chart(filtered_df))

row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    st.pyplot(ch.draw_age_dist(filtered_df))
with row2_col2:
    st.pyplot(ch.draw_scatter_fare_age(filtered_df))

row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    st.pyplot(ch.draw_gender_survival(filtered_df))
with row3_col2:
    st.pyplot(ch.draw_embark_count(filtered_df))

row4_col1, row4_col2 = st.columns(2)
with row4_col1:
    st.pyplot(ch.draw_fare_box(filtered_df))
with row4_col2:
    st.pyplot(ch.draw_age_violin(filtered_df))

row5_col1, row5_col2 = st.columns(2)
with row5_col1:
    st.pyplot(ch.draw_sibsp_count(filtered_df))
with row5_col2:
    st.pyplot(ch.draw_parch_count(filtered_df))