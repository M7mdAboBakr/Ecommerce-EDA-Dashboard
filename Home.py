import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_lottie import st_lottie
import requests

df = pd.read_csv('Ecommerce Cleaned.csv')
st.set_page_config(page_title='Ecommerce Analysis', page_icon=':bar_chart:', layout='wide')

st.markdown("""# 🛍️ E-Commerce Analysis Dashboard

Welcome to the E-Commerce Analysis Dashboard! This interactive tool helps you explore and understand sales performance across different dimensions.
""")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


col1, col2 = st.columns(2)

with col1:
    lottie_coding = load_lottieurl("https://lottie.host/3e37d93a-14a9-4eef-b6e0-ceaed8003381/dHEfuHynFY.json")
    st_lottie(lottie_coding, height=600, width=500)

with col2:
    lottie_coding = load_lottieurl("https://lottie.host/f88c154b-03ab-44c1-94ae-0cd827b81070/VEmvtyr8jU.json")
    st_lottie(lottie_coding, height=550, width=400)    



st.markdown("""
## 📊 About the Data
#### This dataset contains comprehensive e-commerce metrics including:
- **Pricing & Orders**: Unit price, order value, and quantity sold  
- **Product Catalog**: Major/minor categories with product descriptions  
- **Temporal Patterns**: Year, month, quarter, hour, and day time analysis  
- **Geographic Distribution**: Sales across different countries""")

st.markdown("""
## 🔍 Key Insights Available

### 🌍 Geographic Analysis
- **Total order values by country** - View revenue distribution across markets
- **Monthly order values per country** - Track regional sales trends over time

### 🏷️ Product Performance
- **Sales quantity by major category** - Compare performance across product groups
- **Top 5 best-selling products** - Identify your most popular items
- **Kitchen category breakdown** - Analyze sub-category performance for kitchen items

### ⏰ Temporal Trends
- **High-demand months** - Discover seasonal shopping patterns
- **Peak ordering hours** - Identify busiest times of day
- **Most profitable time of day** - Pinpoint when customers spend the most
""")

