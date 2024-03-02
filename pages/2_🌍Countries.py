import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Countries",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded",
)
df = pd.read_csv("../df_EDA.csv")
df.columns = df.columns.str.replace("_", " ").str.title()
# droping the outlier
df.drop(619, axis=0, inplace=True)
df.drop(84, axis=0, inplace=True)


st.title("Number of Orders per Country")
fig = px.bar(df.groupby('Country')['Invoiceno'].count().reset_index(), x='Country', y='Invoiceno', color='Country', template='simple_white', text_auto=True, labels={'Invoiceno': 'Number of Orders'})
fig.update_traces(marker_line_color='white', marker_line_width=1.5)
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.title("Total Ordervalues per Country")
fig = px.pie(df.groupby('Country')['Ordervalue'].sum().reset_index(), names='Country', values='Ordervalue', color='Country', labels={'Ordervalue': 'Total Ordervalues'}, template='simple_white')
fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.update_traces(marker_line_color='black', marker_line_width=1.5)
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.title("Select The Country")
selected_country = st.selectbox("Select The Country", options=df['Country'].unique(), label_visibility="hidden")

if st.checkbox("Date & Time Filter", help="Filter The Data by (Year, Month, Time Of Day)"):
    c1, c2, c3 = st.columns(3)

    year_selection = c1.selectbox("Select The Year(s)", options=list(df['Year'].unique()) + ["All"])
    if year_selection == "All":
        pass
    else:
        df = df[df['Year'] == year_selection]
    
    month_selection = c2.multiselect("Select The Month(s)", options=sorted(df['Month'].unique()), default=sorted(df['Month'].unique()))
    df = df[df['Month'].isin(month_selection)]

    day_time_selection = c3.selectbox("Select The Day Time", options=list(df['Time Of Day'].unique()) + ["All"])
    if day_time_selection == "All":
        pass
    else:
        df = df[df['Time Of Day'] == day_time_selection]

st.divider()

c1, c2, c3 = st.columns(3)
con1 = c1.container(border=True)
con1.metric("Number of Orders", value= df[df['Country'] == selected_country]['Quantity'].sum())
con2 = c2.container(border=True)
con2.metric("Total Ordervalues", value= "{:.3f}".format(df[df['Country'] == selected_country]['Ordervalue'].sum()))
con3 = c3.container(border=True)
con3.metric("Average Ordervalue", value= "{:.3f}".format(df[df['Country'] == selected_country]['Ordervalue'].mean()))

st.header("Top 5 Selled Products")
df_country = df[df['Country'] == selected_country].groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(5).reset_index()
fig = px.bar(df_country, x='Description', y='Quantity', color='Description', text_auto=True)
st.plotly_chart(fig, use_container_width=True)
