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

g_15 = g_15.drop(['Happiness Rank', 'Standard Error', 'Family', 'Dystopia Residual'], axis = 1)

# rename some columns
g_15.rename(columns={'Economy (GDP per Capita)': 'GDP per capita', 
                     'Health (Life Expectancy)': 'Life expectancy',
                     'Trust (Government Corruption)': 'Trust'}, inplace=True)

'''
## 1. Our data. 
Take a quick glance at the variables. 
Then move on.
'''

# show this properly
g_15

'''
## 2. Exploring associations 
In this first plot you can explore association between
variables in the data (2015). Each dot you are seeing 
corresponds to one country. I have sat the x-axis to 
represent GDP per capita and the y-axis to represent
life expectancy, but feel free to change these values. 
When you have done so, you can move on to the next plot 
'''

# selecting stuff
x = st.selectbox('Select X variable', g_15.columns, 3)
y = st.selectbox('Select Y variable', g_15.columns, 4)

# very simple function
def plot_scatter(df, x, y, size = None, hue = None): 
    
    p = sns.scatterplot(x = x, y = y, 
                    size = size, hue = hue, 
                    sizes = (5, 150),
                    data = df)

    plt.legend(loc = 'upper left', fontsize = 'xx-small')

    fig = p.get_figure()
    
    return(fig)
    #st.pyplot(fig)


fig1 = plot_scatter(g_15, x = x, y = y)
st.pyplot(fig1)

'''
## 3. Exploring associations pt. 2
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

fig2 = plot_scatter(g_15, x = x, y = y, size = size, hue = hue)
st.pyplot(fig2)

'''
## 4. I forgot about time...
Now you have hopefully explored our little data set. 
I will now allow you to tweak one last thing. 
Time.
'''

