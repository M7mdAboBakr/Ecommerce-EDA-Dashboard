import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Ecommerce Dashboard",
    page_icon="🏠",
    layout="wide",
)

df = pd.read_csv("ecommerce.csv")

st.title("Ecommerce Dashboard")
st.image("https://miro.medium.com/v2/resize:fit:828/format:webp/1*34GfkhLFydPjZWUde1EzRg.jpeg", width= 1050)


st.markdown("""- ##### This is a dashboard from Ecommerce dataset""")
st.markdown("""- ##### Here we can see the top selling products, number of orders and other details""")
st.markdown("""- ##### We can also filter the data by date, time, and country""")
st.header(f"Take a Look at The Original Dataset")
if st.checkbox("Show Data"):
    st.dataframe(df.head())
