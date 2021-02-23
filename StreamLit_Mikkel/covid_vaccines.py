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

new_names = {'total_vaccinations':"Total Vaccinations", 'people_vaccinated': "People Vaccinated", 'people_fully_vaccinated': "People Fully Vaccinated", 'daily_vaccinations_raw': "Raw Daily Vaccinations", 'daily_vaccinations': "Daily Vaccinations", 'total_vaccinations_per_hundred':"Total Vaccinations Pr. Hundred", 'people_vaccinated_per_hundred':"People Vaccinated Pr. Hundred", 'people_fully_vaccinated_per_hundred': "People Fully Vaccinated Pr. Hundred", 'daily_vaccinations_per_million': "Daily Vaccinations Pr. Million"}

df = df.rename(columns = new_names)

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

interesting_columns = list(new_names.values())

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
    df_subset = pd.DataFrame(dictionary_comp)

    df_subset = df_subset.rename(columns={'date':'index'}).set_index('index')


    if interpol == "Yes":
        df_subset = df_subset.interpolate(method = "time")
    
    ## CURRENTLY NOT SHOWING y-label. This can be fixed here: https://github.com/streamlit/streamlit/issues/1129

    st.line_chart(df_subset)
    expander = st.beta_expander("Area Chart (click for information)")
    expander.write(f"The plot belows shows the area under the curve for the variable {y_col}. When multiple countries are chosen, the countries will be stacked on top of each other. As such, this plot is best used to get better intuitions about how countries differ in terms of volume.")

    st.area_chart(df_subset)
    #st.map()

