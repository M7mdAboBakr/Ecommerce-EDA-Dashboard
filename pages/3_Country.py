import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Ecommerce Cleaned.csv')
st.set_page_config(page_title='Country', page_icon='🌍', layout='wide')


# Total Ordervalue with Country
st.markdown("""# Total Ordervalue with Country""")
fig = px.bar(df.groupby('country')['order_value'].sum().reset_index(), x='country', y='order_value',
       color='country', text_auto='0.3s',
         labels={'order_value':'Order Value', 'country':'Country'}, template='simple_white')
fig.update_traces(marker_line_color = 'black', marker_line_width = 0.8, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()


st.markdown("""# Total Ordevalue for Major Category with Month""")
st.dataframe(pd.pivot_table(df, index='major_category', columns='month', values='order_value', aggfunc='sum').style.background_gradient(cmap='Reds').format("{:.2f}"), use_container_width=True)
st.divider()

# Filter by Country
st.title("Filter by Country")
country_selection = st.selectbox('Country', (list(df.country.unique())))
df_country = df[df.country == country_selection]
st.markdown("\n")
st.markdown("\n")

# Top 5 Sold Products
st.markdown("""## Top 5 Sold Products""")
fig = px.bar(df_country.groupby('description')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False).head(),
       y='description', x='quantity', color='description', text_auto=True,
       labels={'quantity':'Quantity', 'description':'Product'}, template='simple_white')
fig.update_traces(marker_line_color = 'black', marker_line_width = 0.8, showlegend=False)
st.plotly_chart(fig, use_container_width=True)

