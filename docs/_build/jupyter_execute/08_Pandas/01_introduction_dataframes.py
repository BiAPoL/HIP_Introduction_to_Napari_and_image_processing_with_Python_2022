#!/usr/bin/env python
# coding: utf-8

# # Introduction to working with DataFrames
# In basic python, we often use dictionaries containing our measurements as vectors. While these basic structures are handy for collecting data, they are suboptimal for further data processing. For that we introduce [panda DataFrames](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) which are more handy in the next steps. In Python, scientists often call tables "DataFrames".  

# In[1]:


import pandas as pd


# ## Creating DataFrames from a dictionary of lists
# Assume we did some image processing and have some results in available in a dictionary that contains lists of numbers:

# In[2]:


measurements = {
    "labels":      [1, 2, 3],
    "area":       [45, 23, 68],
    "minor_axis": [2, 4, 4],
    "major_axis": [3, 4, 5],
}


# This data structure can be nicely visualized using a DataFrame:

# In[3]:


df = pd.DataFrame(measurements)
df


# Using these DataFrames, data modification is straighforward. For example one can append a new column and compute its values from existing columns:

# In[4]:


df["aspect_ratio"] = df["major_axis"] / df["minor_axis"]
df


# ## Saving data frames
# We can also save this table for continuing to work with it.

# In[5]:


df.to_csv("../../data/short_table.csv")


# ## Creating DataFrames from lists of lists
# Sometimes, we are confronted to data in form of lists of lists. To make pandas understand that form of data correctly, we also need to provide the headers in the same order as the lists

# In[6]:


header = ['labels', 'area', 'minor_axis', 'major_axis']

data = [
    [1, 2, 3],
    [45, 23, 68],
    [2, 4, 4],
    [3, 4, 5],
]
          
# convert the data and header arrays in a pandas data frame
data_frame = pd.DataFrame(data, header)

# show it
data_frame


# As you can see, this tabls is _rotated_. We can bring it in the usual form like this:

# In[7]:


# rotate/flip it
data_frame = data_frame.transpose()

# show it
data_frame


# ## Loading data frames
# Tables can also be read from CSV files.

# In[8]:


df_csv = pd.read_csv('../../data/blobs_statistics.csv')
df_csv


# Typically, we don't need all the information in these tables and thus, it makes sense to reduce the table. For that, we print out the column names first.

# In[9]:


df_csv.keys()


# ## Selecting columns
# We can then copy&paste the colum names we're interested in and create a new data frame. This is recommended especially when tables are overwhelmingly large.

# In[18]:


df_analysis = df_csv[['area', 'mean_intensity']]
df_analysis


# ## Selecting rows
# In case we want to focus our further analysis on cells that have a certain minimum area. We can do this by selecting rows. The process is also sometimes call masking.

# In[16]:


selected_data  = df_analysis[ df_analysis["area"] > 50]
selected_data


# ## Adding new columns
# You can then access columns and add new columns.

# In[15]:


df_analysis['total_intensity'] = df_analysis['area'] * df_analysis['mean_intensity']
df_analysis


# ## Exercise
# For the loaded CSV file, create a table that only contains these columns:
# * `minor_axis_length`
# * `major_axis_length`
# * `aspect_ratio`

# In[13]:


df_shape = pd.read_csv('../../data/blobs_statistics.csv')
df_shape


# In[ ]:




