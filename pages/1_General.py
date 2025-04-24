import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('Ecommerce Cleaned.csv')
st.set_page_config(page_title='General', page_icon='📈', layout='wide')


# Number of Orders Per Month, Number of Orders Per Day Hours
col1, col2 = st.columns(2)
with col1:
    st.markdown("""# Number of Orders Per Month""")
    fig = px.line(df.groupby('month')['quantity'].count().reset_index(),
            x='month', y='quantity', labels={'quantity':'# of Orders', 'month':'Month'},
            template='simple_white', markers=True)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.markdown("""# Number of Orders Per Day Hours""")
    fig = px.line(df.groupby('hour')['quantity'].count().reset_index(),
        x='hour', y='quantity', labels={'hour':'Hour', 'quantity':'Number Of Orders'},
        template='simple_white', markers=True)
    st.plotly_chart(fig, use_container_width=True)
st.divider()

# Number of Orders Per Quarter
st.markdown("""# Number of Orders Per Quarter""")
fig = px.line(df.groupby('quarter')['quantity'].count().reset_index(),
        x='quarter', y='quantity', labels={'quantity':'# of Orders', 'quarter':'Quarter'},
        template='simple_white', markers=True)
st.plotly_chart(fig, use_container_width=True)

# Total Ordervalue of Each Daytime
st.markdown("""# Total Ordervalue of Each Daytime""")
fig = px.bar(df.groupby('day_time')['order_value'].sum().reset_index().iloc[[2, 0, 1]],
       y='day_time', x='order_value',color='day_time', text_auto=True,
       labels={'order_value':'Order Value', 'day_time':'Daytime'}, template='simple_white')
fig.update_traces(marker_line_color = 'black', marker_line_width = 0.8, showlegend=False, textposition='outside')
st.plotly_chart(fig, use_container_width=True)
st.divider()

# Top 5 Sold Products
st.markdown("""# Top 5 Sold Products""")
fig = px.bar(df.groupby('description')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False).head(),
       y='description', x='quantity', color='description', text_auto=True,
       labels={'quantity':'Quantity', 'description':'Product'}, template='simple_white')
fig.update_traces(marker_line_color = 'black', marker_line_width = 0.8, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
