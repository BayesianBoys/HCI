# packages
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns

# gapminder stuff instead 
g_15 = pd.read_csv("2015.csv")

# rename some columns 
g_15.columns

g_15.rename(columns={'Economy (GDP per Capita)': 'GDP per capita', 
                     'Health (Life Expectancy)': 'Life expectancy',
                     'Trust (Government Corruption)': 'Trust'}, inplace=True)

# very simple function
def plot_scatter(df, x, y, size = None, hue = None): 
    
    p = sns.scatterplot(x = x, y = y, 
                    size = size, hue = hue, 
                    data = df)

    plt.legend(loc = 'upper left', fontsize = 'xx-small')

    fig = p.get_figure()
    fig
    

plot_scatter(g_15, x = "GDP per capita", y = "Life expectancy", size = "Happiness Rank")

plot_scatter(g_15, x = "GDP per capita", y = "Life expectancy", hue = "Trust")
