import streamlit as st 
import pandas as pd 
import numpy as np
from streamlit_option_menu import option_menu
import plotly.express as px
st.set_page_config(page_title="Tourism Analysis", page_icon="🚀", layout='wide')

df1= pd.read_csv('tourism/2- number-of-individuals-employed-in-tourism-related-industries-per-1000-people.csv')
country_list= df1.Entity.unique().tolist()

df2= pd.read_csv('tourism/3- international-tourist-departures-per-1000.csv')

df3= pd.read_csv('tourism/4- international-tourist-trips.csv')

df4= pd.read_csv('tourism/5- monthly-co2-emissions-from-international-and-domestic-flights.csv')

df7= pd.read_csv('tourism/7- tourism-gdp-proportion-of-total-gdp.csv')

df5= pd.read_csv('tourism/21- average-expenditures-of-international-tourists-domestically.csv')


country_list= df1.Entity.unique().tolist()
# st.dataframe(df1, use_container_width=True)
with st.sidebar:
    opt= st.selectbox("Select", options=country_list, index=2)
    
    
col1, col2= st.columns(2, gap='large')
with col1:
    df1_fil= df1[df1['Entity']==opt]
    fig= px.bar(df1_fil,x='Year',y='Employment (total) per 1000 people', hover_data=['Entity'], color='Year', title="Number of Individuals Employed In Tourism Related Industries Per 1000 People")
    st.plotly_chart(fig)
    
    df2_fil= df2[df2['Entity']==opt]
    global_trend = df2_fil.groupby('Year')['Outbound departures (tourists) per 1000 people'].mean().reset_index()
    fig2 = px.line(global_trend, x='Year', y='Outbound departures (tourists) per 1000 people',
                title='Global Trend of Outbound Departures per 1000 People')
    st.plotly_chart(fig2)
    
    df3_fil= df3[df3['Entity']==opt]
    fig= px.pie(df3_fil,names='Year',values='Inbound arrivals (tourists)', hover_data=['Entity'], title="Inbound Arrivals (tourists)")
    st.plotly_chart(fig)
    
    df8_fil= df5[df5['Entity']==opt]
    fig_pie= px.pie(df8_fil,names='Year',values='Inbound Tourism Expenditure (adjusted for inflation and cost of living)', hover_data=['Entity'], title="Inbound Tourism Expenditure")
    st.plotly_chart(fig_pie)
    
    
    
    
    
    
    
    
    
with col2:
    df2_fil= df2[df2['Entity']==opt]
    fig= px.bar(df2_fil,x='Year',y='Outbound departures (tourists) per 1000 people', hover_data=['Entity'], color='Year', title="International Tourist Departures Per 1000 People")
    st.plotly_chart(fig)
    
    df4_fil= df4[df4['Entity']==opt] 
    fig= px.bar(df4_fil,x='Day',y='Monthly CO₂ emissions from domestic aviation', hover_data=['Entity'], color='Day', title="Monthly CO₂ emissions from domestic aviation")
    st.plotly_chart(fig)    
    
    
    # Create a scatter plot to show the relationship between year and tourism GDP proportion
    df7_fil= df7[df7['Entity']==opt] 
    fig_scatter = px.scatter(df7_fil, x='Year', y='Tourism GDP as a proportion of Total',hover_data=['Entity'], color='Year',
            title='Tourism GDP Proportion vs Year for Country',
            labels={'Tourism GDP as a proportion of Total': 'Tourism GDP Proportion (%)'})
    
    st.plotly_chart(fig_scatter)
    
    
    
df6 = pd.read_csv('tourism/30- monthly-co2-emissions-from-international-aviation.csv')
df6['Day'] = pd.to_datetime(df6['Day'])

top_10_countries = df6.groupby('Entity')['Monthly CO2 total emissions from aviation'].sum().nlargest(10).index.tolist()
df_top_10 = df6[df6['Entity'].isin(top_10_countries)]
fig = px.line(df_top_10, x='Day', y='Monthly CO2 total emissions from aviation', color='Entity',
            title='Total CO2 Emissions from Aviation for Top 10 Countries',
            labels={'Monthly CO2 total emissions from aviation': 'Total CO2 Emissions'},
            animation_frame='Day', animation_group='Entity', range_y=[0, df_top_10['Monthly CO2 total emissions from aviation'].max()])

# st.plotly_chart(fig)

# df_latest = df6[df6['Day'] == df6['Day'].max()]

df_map = df6.groupby(['Entity', 'Code', 'Day'])['Monthly CO2 total emissions from aviation'].sum().reset_index()
fig10 = px.choropleth(df_map, locations='Code', color='Monthly CO2 total emissions from aviation',
                     hover_name='Entity', animation_frame='Day',
                     color_continuous_scale=px.colors.sequential.Aggrnyl,
                     title='Total CO2 Emissions from Aviation by Country',
                     labels={'Monthly CO2 total emissions from aviation': 'Total CO2 Emissions'})


st.plotly_chart(fig10)

    
    
# Load the dataset
df_24 = pd.read_csv('tourism/24- international-trips-for-business-and-professional-reasons.csv')

# 1. Animated line chart
fig_ = px.line(df_24, x='Year', y='Inbound tourism purpose (business and professional)', 
               color='Entity', animation_frame='Year', animation_group='Entity',
               title='Business Trips Over Time by Country')
st.plotly_chart(fig_)

fig2 = px.bar(df_24, x='Entity', y='Inbound tourism purpose (business and professional)', 
              animation_frame='Year', color='Entity',
              title='Business Trips Comparison Across Countries')
st.plotly_chart(fig2)


