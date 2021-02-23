# importing stuff
import streamlit as st
import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

'''
# Welcome to Earth! 

This is a playground for exploring the the world. Here, you are the master.

Questions such as: 

* "Can money buy happiness?" 

* "Is Denmark really the happiest country in the world?"

* "What has love got to do with it?" 

Can be answered here! Well... possibly not the last one... 

'''

data = pd.read_csv('2015.csv')

# gapminder stuff instead 
g_15 = pd.read_csv("2015.csv")

# rename some columns
g_15.rename(columns={'Economy (GDP per Capita)': 'GDP_capita', 
                     'Health (Life Expectancy)': 'life_expectancy',
                     'Trust (Government Corruption)': 'trust'}, inplace=True)

'''
## 1. Exploring associations 
In this first plot you can explore association between
variables in the data (2015). Each dot you are seeing 
corresponds to one country. When you have done so,
you can move on to the next plot 
'''
# selecting stuff
x = st.selectbox('Select X variable', g_15.columns)
y = st.selectbox('Select Y variable', g_15.columns)

# very simple function
def plot_scatter(df, x = "GDP_capita", y = "life_expectancy", size = None, hue = None): 
    
    p = sns.scatterplot(x = x, y = y, 
                    size = size, hue = hue, 
                    data = df)

    fig = p.get_figure()
    
    st.pyplot(fig)


p1 = plot_scatter(g_15, x = x, y = y)

'''
## 2. Exploring associations pt. 2
Bow that you have a grasp of the data, I will 
let you add additional facets to the plot. 
For instance, you can add base the size of the
dots on "Happiness Rank". Additionally, you could
also base the color (hue) of the dots on things
like "Region" to explore whether countries in 
the same parts of the world show similar patterns. 
It is of course up to you! 
'''

# selecting stuff
x = st.selectbox('Select new X variable', g_15.columns)
y = st.selectbox('Select new Y variable', g_15.columns)
size = st.selectbox('Select SIZE variable', g_15.columns)
hue = st.selectbox('Select COLOR to group by', g_15.columns)

p2 = plot_scatter(g_15, x = x, y = y, size = size, hue = hue)

'''
## 3. I forgot about time...
Now you have hopefully explored our little data set. 
I will now allow you to tweak one last thing. 
Time.
'''

