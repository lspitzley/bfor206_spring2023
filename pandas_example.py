"""
This script will create an random dataframe 
and then show how to use core pandas functionality.
"""

#%% imports
import numpy as np
import pandas as pd


#%% random variables

# generate a matrix with 100 rows and 4 columns
# each cell gets a random value between 0 and 100
matrix = np.random.randint(0, 100, size=(100, 4))
print(matrix)

# access rows 90 through 100 in column 0
print(matrix[90:100, 0])

# %% create a dataframe

# convert the array into a dataframe
random_df = pd.DataFrame(matrix, columns=['A', 'B', 'C', 'D'])
print(random_df['A'])
random_df['A'].plot.hist()

# %% add another column

# generate 100 observations from random normal distribution 
new_col = np.random.normal(loc=5, scale=2, size=100)

# add this to our dataframe
random_df['E'] = new_col
random_df['E'].plot.hist()

# %% non-numeric data

labels = np.random.choice(['A_1', 'A_2', 'B_1', 'B_2'], 100)
random_df['labels'] = labels

# see the column names
list(random_df)


# %% split the labels column

label_group = random_df['labels'].str.split('_')

# add the first part of each row to the dataframe
random_df['group'] = label_group.str[0]

# show the first 5 rows
random_df.head()

# %% get some summary stats from the dataframe

# only shows numerical columns
random_df.describe()

# include numerical and non-numeric columns
random_df.describe(include='all')



# %% grouping (like PivotTables)

# groupby MUST use categorical data
random_df.groupby('group')['C', 'D'].mean()

# see the mean for each column
random_df.groupby('group').mean()


# %%
