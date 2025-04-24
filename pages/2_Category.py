import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Ecommerce Cleaned.csv')
st.set_page_config(page_title='Category', page_icon='📈', layout='wide')


# Major Category Sold Quantities
st.markdown("""# Major Category Sold Quantities""")
fig = px.pie(df.groupby('major_category')['quantity'].sum().reset_index(), names='major_category', 
             values='quantity',
             template='simple_white', hole=0.6)
fig.update_traces(marker_line_width = 1, marker_line_color = 'black', showlegend=False, textinfo='label+percent')
st.plotly_chart(fig, use_container_width=True)
st.divider()


# Total Ordervalue of Kitchen Minor Categories
st.markdown("""# Total Ordervalue of Kitchen Minor Categories""")
fig = px.bar(df[df.major_category == 'Kitchen'].groupby('minor_category')['order_value'].sum().reset_index().sort_values(by='order_value', ascending=False),
       y='minor_category', x='order_value',color='minor_category',text_auto=True,
       labels={'order_value':'Order Value', 'minor_category':'Minor Category'}, template='simple_white')
fig.update_traces(marker_line_color = 'black', marker_line_width = 0.8, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()

st.title("Filter by Major & Minor Categories")
col1, col2 = st.columns(2)
major_selection = col1.selectbox('Major Category', (list(df.major_category.unique())))
minor_selection = col2.selectbox('Minor Category', ['All'] + list(df[df.major_category == major_selection].minor_category.unique()), 0)

if minor_selection == 'All':
    df_major_minor = df[df.major_category == major_selection]
else:
    df_major_minor = df[(df.major_category == major_selection) & (df.minor_category == minor_selection)]

col1, col2, col3 = st.columns(3)
con1 = col1.container(border=True)
con1.metric('Total Number of Orders', df_major_minor.order_value.count())
con2 = col2.container(border=True)
con2.metric("Total Ordervalue", round(df_major_minor.order_value.sum(), 2))
con3 = col3.container(border=True)
con3.metric('Average Ordervalue', round(df_major_minor.order_value.mean(), 2))

col1, col2 = st.columns(2)
con1 = col1.container(border=True)
con1.metric('Most Expensive Product', df_major_minor[df_major_minor.unit_price == df_major_minor.unit_price.max()].description.values[0])
con1.write(f'Unit Price: {df_major_minor.unit_price.max()}')
con2 = col2.container(border=True)
con2.metric('Cheapest Product', df_major_minor[df_major_minor.unit_price == df_major_minor.unit_price.min()].description.values[0])
con2.write(f'Unit Price: {df_major_minor.unit_price.min()}')