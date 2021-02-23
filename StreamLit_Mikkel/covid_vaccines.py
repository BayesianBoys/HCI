import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
"""
# Covid Vaccines - how are things going? 

Let's visualize how vaccinations are going over time! 

"""

expander = st.beta_expander("The Data")
expander.write(f"The data was downloaded from Kaggle. However, several preproccessing steps were taken. The countries differed in terms of how many days they had recorded data. This was padded with NAs. Furthermore, the $pd.DateTime()$ function was used extensively. You can find the data here: https://www.kaggle.com/gpreda/covid-world-vaccination-progress")

df = pd.read_csv("country_vaccinations.csv")

df_pivot = df.pivot(columns = "country", values = "daily_vaccinations_per_million")

countries = list(df_pivot.columns)

df["date"] = pd.to_datetime(df["date"])

date_ranging = pd.date_range(min(df["date"]), max(df["date"]))

list_of_dfs = []

for i in countries:
    df_new = df[df["country"] == i]
    df_new = df_new.set_index("date").reindex(date_ranging).fillna(np.nan).rename_axis("date").reset_index()
    df_new["country"] = i
    list_of_dfs.append(df_new)

df = pd.concat(list_of_dfs)

if st.checkbox('Show the dataframe'):
    df

'''
## Guide to the interactive plot
'''

'''
This website is for plotting the development of vaccines for COVID-19 for each country over the recent month. 
Select different values on the left to explore the data. Below are explanations for each selection you can make.
'''

options = st.sidebar.multiselect(
    "What countries do you want to compare?",
    countries, None
)

interesting_columns = ["total_vaccinations", "people_vaccinated", "people_fully_vaccinated", "daily_vaccinations_raw", "daily_vaccinations", "total_vaccinations_per_hundred", "people_vaccinated_per_hundred", "people_fully_vaccinated_per_hundred", "daily_vaccinations_per_million"]

y_col = st.sidebar.selectbox('What variable would you like to compare between countries?', interesting_columns)

interpol = st.sidebar.selectbox('Do you want to interpolate values of NA?', ["Yes", "No"])


expander = st.beta_expander("Countries")
expander.write(f"This variable is used to select the countries you want to compare. Currently you have selected: {options}")

expander = st.beta_expander("The Y-axis")
expander.write(f"The second variable determines what you want to compare the countries on. You have currently selected {y_col}.")

expander = st.beta_expander("Interpolation")
expander.write(f"The third variable is used to select whether to interpolate values when there are NAs in the data. This is a consequence of there being a disparity between how much data each country has. Some have just started later than other. The method used is $pd.interpolate(method = time)$. To the question of whether or not to interpolate, you have currently answered '{interpol}!'")


if options:
    dictionary_comp = {option: df[df["country"] == option][y_col].values for option in options}
    dictionary_comp["date"] = list(date_ranging)
    #dictionary_comp = 
    #df_subset = [df[df["country"] == i]["daily_vaccinations_per_million"] for i in options]
    df_subset = pd.DataFrame(dictionary_comp)

    df_subset = df_subset.rename(columns={'date':'index'}).set_index('index')
    #boolean_rows = df["country"].isin(options)
    #df_subset = df[boolean_rows]
    #df_subset = df_subset.interpolate()

    if interpol == "Yes":
        df_subset = df_subset.interpolate(method = "time")
    
    st.line_chart(df_subset)
    expander = st.beta_expander("Area Chart (click for information)")
    expander.write(f"The plot belows shows the area under the curve for the variable {y_col}. When multiple countries are chosen, the countries will be stacked on top of each other. As such, this plot is best used to get better intuitions about how countries differ in terms of volume.")

    st.area_chart(df_subset)
    #st.map()

#df_subset = pd.DataFrame(df_pivot["Albania"].values, index = df_pivot.index)

#st.line_chart(df_pivot.unstack())

# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(map_data)

# if st.checkbox('Show dataframe'):
#     chart_data = pd.DataFrame(
#        np.random.randn(20, 3),
#        columns=['a', 'b', 'c'])

#     st.line_chart(chart_data)

# # option = st.selectbox(
# #     'Which number do you like best?',
# #      df['first column'])

# # 'You selected: ', option

# option = st.sidebar.selectbox(
#     'Which number do you like best?',
#      df['first column'])

# 'You selected:', option

# left_column, right_column = st.beta_columns(2)
# pressed = left_column.button('Press me?')
# if pressed:
#     right_column.write("Woohoo!")

# expander = st.beta_expander("FAQ")
# expander.write("Here you could put in some really, really long explanations...")

# 'Starting a long computation...'

# # Add a placeholder
# latest_iteration = st.empty()
# bar = st.progress(0)

# for i in range(100):
#   # Update the progress bar with each iteration.
#   latest_iteration.text(f'Iteration {i+1}')
#   bar.progress(i + 1)
#   time.sleep(0.1)

# '...and now we\'re done!'