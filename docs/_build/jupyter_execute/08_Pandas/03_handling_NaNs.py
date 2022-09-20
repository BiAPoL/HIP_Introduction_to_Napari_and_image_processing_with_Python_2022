#!/usr/bin/env python
# coding: utf-8

# # Handling NaN values
# When analysing tabular data, sometimes table cells are present that does not contain data. In Python this typically means the value is _Not a Number_ ([NaN](https://en.wikipedia.org/wiki/NaN)). We cannot assume these values are `0` or `-1` or any other value because that would distort descriptive statistics, for example. We need to deal with these NaN entries differently and this notebook will introduce how.
# 
# To get a first view where NaNs play a role, we load again an example table and sort it.

# In[1]:


import numpy as np
import pandas as pd 


# In[2]:


data = pd.read_csv('../../data/Results.csv', index_col=0, delimiter=';')
data.sort_values(by = "Area", ascending=False)


# As you can see, there are rows at the bottom containing NaNs. These are at the bottom of the table because pandas cannot sort them.

# A quick check if there are NaNs anywhere in a DataFrame is an important quality check and good scientific practice.

# In[3]:


data.isnull().values.any()


# We can also get some deeper insights in which columns these NaN values are located.

# In[4]:


data.isnull().sum()


# For getting a glimpse about if we can further process that tabel, we may want to know the percentage of NaNs for each column?

# In[5]:


data.isnull().mean().sort_values(ascending=False) *100


# # Dropping rows that contain NaNs
# Depending on what kind of data analysis should be performed, it might make sense to just ignore columns that contain NaN values. Alternatively, it is possible to delete rows that contain NaNs.
# 
# It depends on your project and what is important or not for the analysis. Its not an easy answer.

# In[6]:


data_no_nan = data.dropna(how="any")
data_no_nan 


# On the bottom of that table, you can see that it still contains 374 of the original 391 columns. If you remove rows, you should document in your later scientific publication, home many out of how many datasets were analysed.
# 
# We can now also check again if NaNs are present.

# In[7]:


data_no_nan.isnull().values.any()


# ## Determining rows that contain NaNs
# In some use-cases it might be useful to have a list of row-indices where there are NaN values.

# In[8]:


data = {
    'A': [0, 1, 22, 21, 12, 23],
    'B': [2, 3, np.nan,  2,  12, 22],
    'C': [2, 3, 44,  2,  np.nan, 52],
}

table = pd.DataFrame(data)
table


# In[9]:


np.max(table.isnull().values, axis=1)


# ## Exercise
# Take the original `data` table and select the columns `Area` and `Mean`. Remove all rows that contain NaNs and count the remaining rows.
# Afterwards, take the original `data` table again and select the columns `Major` and `Minor`. Remove NaNs and count the remaining rows again. What do you conclude?

# In[ ]:




