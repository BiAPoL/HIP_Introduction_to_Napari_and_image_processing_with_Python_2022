#!/usr/bin/env python
# coding: utf-8

# # Appending tables
# When processing multiple images, potentially using multiple image processing libraries, a common task is to combine tables.
# 
# We start with two small tables of measurements.

# In[1]:


import pandas as pd


# In[2]:


table1 = pd.DataFrame({
    "label":       [1,   2,   3],
    "circularity": [0.3, 0.5, 0.7],
    "elongation":  [2.3, 3.4, 1.2],
    })
table1


# In[3]:


table2 = pd.DataFrame({
    "label":    [3,   2,   1,   4],
    "area":     [22,  32,  25,  18],
    "skewness": [0.5, 0.6, 0.3, 0.3],
    })
table2


# ## Combining columns of tables
# According to the [pandas documentation](https://pandas.pydata.org/docs/user_guide/merging.html) there are multiple ways for combining tables. We first use a _wrong_ example to highlight pitfalls when combining tables.
# 
# In the following example, measurements of label 1 and 3 are mixed. Furthermore, one of our tables did not contain measurements for label 4.

# In[4]:


wrongly_combined_tables = pd.concat([table1, table2], axis=1)
wrongly_combined_tables


# A better way for combining tables is the `merge` command. It allows to explicitly specify `on` which column the tables should be combined. Data scientists speak of the 'index' or 'identifier' of rows in the tables.

# In[5]:


correctly_combined_tables1 = pd.merge(table1, table2, how='inner', on='label')
correctly_combined_tables1


# You may note that in the above example, label 4 is missing. We can also get it by out table by performing an `outer join`.  

# In[6]:


correctly_combined_tables2 = pd.merge(table1, table2, how='outer', on='label')
correctly_combined_tables2


# ## Exercise
# The following additional table is given. Combine it with the tables above.

# In[7]:


table3 = pd.DataFrame({
    "label":       [1, 2, 3, 4],
    "folder":      ["E:/data/experiment5/"] * 4,
    "filename":    ["image1.tif"] * 4,
    })
table3


# In[ ]:




