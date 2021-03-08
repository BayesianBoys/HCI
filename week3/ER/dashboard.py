#%% 
#Prep modules and load data:
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
#%%

data = pd.read_csv("master.csv")
data = data.drop(['country-year', 'HDI for year',' gdp_for_year ($) '], axis=1)
data.head()


#%%
#To start run in terminal
#"streamlit run dashboard.py"
#to close "ctrl+c"
# %%
#Sidebar stuff
st.sidebar.title("Visualization Selector")
st.sidebar.markdown("Select the Charts/Plots accordingly:")

#st.sidebar.checkbox("Show Analysis by country", True, key=1)
select = st.sidebar.selectbox('Select a country',data['country'].unique())

#get the country selected in the selectbox
country_data = data[data['country'] == select]
select_status = st.sidebar.radio("Metrics", ('suicides_no',
'population', 'suicides/100k pop', 'gdp_per_capita ($)'))


#%%
#logistics:
st.title("Suicide data - We can't all choose the happiness dataset")

#Seeing the dataset:
st.write("Lets have a look at the data:")

#interactive: Show dataframe?
if st.checkbox('Show dataframe'):
    st.dataframe(data)

#more texr
st.write("With that out of the way - lets get the lay of the land")

#%% Making plots:

#pie chart:
if st.sidebar.checkbox("Show Analysis by country", True, key=1):
    fig1 = px.pie(country_data, values=country_data["suicides/100k pop"], names=country_data["sex"], color=country_data["sex"])
    fig1.update_layout(title="Suicide rate by gender")
    st.plotly_chart(fig1)
else:
    fig1 = px.pie(data, values=data["suicides/100k pop"], names=data["sex"], color=data["sex"])
    fig1.update_layout(title="Suicide rate by gender")
    st.plotly_chart(fig1)
   


# %%
