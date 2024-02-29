import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Categories",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)
df = pd.read_csv("df_EDA.csv")
df.columns = df.columns.str.replace("_", " ").str.title()
# droping the outlier
df.drop(619, axis=0, inplace=True)
df.drop(84, axis=0, inplace=True)

st.title("Number of Orders per Major Category")
fig = px.bar(df.groupby('Major Category')['Invoiceno'].count().reset_index(), x='Major Category', y='Invoiceno', color='Major Category', template='simple_white', text_auto=True, labels={'Invoiceno': 'Number of Orders'})
fig.update_traces(marker_line_color='white', marker_line_width=1.5)
st.plotly_chart(fig, use_container_width=True)
st.divider()


st.title("Total Ordervalues per Major Category")
fig = px.pie(df.groupby('Major Category')['Ordervalue'].sum().reset_index(), names='Major Category', values='Ordervalue', color='Major Category', labels={'Ordervalue': 'Total Ordervalues'}, template='simple_white')
fig.update_traces(textposition='inside', textinfo='percent+label')
# fig.update_traces(marker_line_color='black', marker_line_width=1.5)
st.plotly_chart(fig, use_container_width=True)
st.divider()
st.title("Select The Major & Minor Categories")

c1, c2 = st.columns(2)
major_selection = c1.selectbox("Select The Major Category", options=df['Major Category'].unique())
minor_selection = c2.selectbox("Select The Minor Category", list(df[df['Major Category'] == major_selection]['Minor Category'].unique()) + ["All"])

if minor_selection == 'All':
    df_major_minor = df[df['Major Category'] == major_selection]
else:
    df_major_minor = df[(df['Major Category'] == major_selection) & (df['Minor Category'] == minor_selection)]

c1, c2, c3 = st.columns(3)
con1 = c1.container(border=True)
con1.metric("Total Number of Orders", value= df_major_minor['Quantity'].sum())
con2 = c2.container(border=True)
con2.metric("Total Ordervalues", value= "{:.3f}".format(df_major_minor['Ordervalue'].sum()))
con3 = c3.container(border=True)
con3.metric("Average Ordervalue", value= "{:.3f}".format(df_major_minor['Ordervalue'].mean()))

c1, c2 = st.columns(2)
con1 = c1.container(border=True)
con2 = c2.container(border=True)
con1.metric("The Most Expensive Product", value= df_major_minor.nlargest(1, 'Unitprice')['Description'].iloc[0])
con1.write(f"The Unitprice : {df_major_minor[(df_major_minor['Description'] == df_major_minor.nlargest(1, 'Unitprice')['Description'].iloc[0]) & (df_major_minor['Major Category'] == major_selection)]['Unitprice'].iloc[0]}")
con2.metric("The Cheapest Product",value= df_major_minor.nsmallest(1, 'Unitprice')['Description'].iloc[0])
con2.write(f"The Unitprice : {df_major_minor[(df_major_minor['Description'] == df_major_minor.nsmallest(1, 'Unitprice')['Description'].iloc[0]) & (df_major_minor['Major Category'] == major_selection)]['Unitprice'].iloc[0]}")


st.header(f"Top 5 Selled Products")
top5_category = df_major_minor.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(5).reset_index()
fig = px.bar(top5_category, x='Description', y='Quantity', color='Description', text_auto=True)
st.plotly_chart(fig, use_container_width=True)
   
