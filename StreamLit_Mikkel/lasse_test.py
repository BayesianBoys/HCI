import numpy as np
import pandas as pd

## Make weird dataframe

random_df = pd.DataFrame([np.random.random(10) for i in range(10)])

## Add a song column

random_df["song"] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

## Our input is the song "a"

array_interest = random_df[random_df["song"] == "a"].values[0]

# Quick fix for not including the song-column in our equation.

array_interest = array_interest[:-1]

def get_dist(a, r = array_interest):
    '''
    Function designed to find the distance between the two vectors
    '''
    return sum([(a[i]-r[i])**2 for i in range(len(r))])

# Now for the fancy stuff. Requires a bit explanation:

# We find the column we are interested in first. 
#           we take out the values
#                        find the index of the minimum
#                                           quick fix to exclude the columns
#                                                                    apply to the whole row
random_df["song"].values[np.argmin(random_df[random_df.columns[:-1]].apply(get_dist))]