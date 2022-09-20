#!/usr/bin/env python
# coding: utf-8

# # Statistics using SimpleITK
# We can use [Simple](https://simpleitk.readthedocs.io/) for extracting features from label images. For convenience reasons we use the [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing) library.

# In[1]:


import numpy as np
import pandas as pd
from skimage.io import imread
from pyclesperanto_prototype import imshow
from napari_simpleitk_image_processing import watershed_otsu_labeling
from napari_simpleitk_image_processing import label_statistics


# In[2]:


blobs = imread('../../data/blobs.tif')
imshow(blobs)


# ## Starting point: a segmented label image

# In[3]:


labels = watershed_otsu_labeling(blobs)
imshow(labels, labels=True)


# ## Label statistics

# In[4]:


statistics = label_statistics(blobs, labels, None, True, True, True, True, True, True)

df = pd.DataFrame(statistics)
df


# These are all columns that are available:

# In[5]:


print(statistics.keys())


# In[6]:


df.describe()


# In[ ]:




