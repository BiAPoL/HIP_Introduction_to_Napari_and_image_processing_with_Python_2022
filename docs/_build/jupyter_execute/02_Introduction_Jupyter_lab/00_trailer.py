#!/usr/bin/env python
# coding: utf-8

# # Trailer: Bio-image Analysis with Python and Napari
# During this course we will dive into image analysis, machine learning and bio-statistics with python. This notebook serves as a trailer of what we will be doing until July. Every step will be explained in detail in future sessions. This is just a trailer.
# 
# What typically comes first in Python Juptyer notebooks is a block of import statements. By executing it, we can make sure that everything we need is installed.

# In[1]:


from skimage.io import imread, imshow
from skimage import measure
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from napari_segment_blobs_and_things_with_membranes import voronoi_otsu_labeling
import napari


# In[2]:


viewer = napari.Viewer()


# ## Working with image data
# We can load images into variables. The path "../data/blobs.tif" suggests, that from the current directory, where this notebook is saved, we need to go one folder up ("..") and there should be a "data" folder in which "blobs.tif" is stored.

# In[3]:


# open an image file
image = imread("../../data/nuclei.tif")


# In[4]:


# visualizing an image
viewer.add_image(image)

# take a screenshot of napari
napari.utils.nbscreenshot(viewer)


# ## Image segmentation
# There is an endless number of image segmentation techniques available. A straight-forward way for segmenting nuclei is [Voronoi-Otsu-Labeling](https://haesleinhuepf.github.io/BioImageAnalysisNotebooks/20_image_segmentation/11_voronoi_otsu_labeling.html) (see also [this Video](https://www.youtube.com/watch?v=evgRgDfVuEc) by DigitalSreeni).

# In[5]:


labels = voronoi_otsu_labeling(image,
                                       spot_sigma=9,
                                       outline_sigma=3)

viewer.add_labels(labels)

napari.utils.nbscreenshot(viewer)


# ## Measurements and feature extraction
# From segmented images we can derive quantitative measurements. The process is called "feature extraction".

# In[6]:


# analyse objects
table = measure.regionprops_table(labels, 
                                  intensity_image=image,
                                  properties=('label', 'area', 'centroid', 'mean_intensity', 'feret_diameter_max'))


# ## Working with tables

# In[7]:


# show table
dataframe = pd.DataFrame(table)
dataframe


# ## Statistical analysis

# In[8]:


print("Mean blob area is ", np.mean(dataframe['area']))


# ## Data visualization
# For understanding realationships between object properties, plotting is a commonly used technique. Here we plot area versus elongation of objects.

# In[9]:


plt.scatter(dataframe['area'], dataframe['feret_diameter_max'])


# Parametric maps allow us to visualize properties of objects in image space. In the following example, elongate objects are brighter than roundish objects.

# In[11]:


import pyclesperanto_prototype as cle

parametric_map = cle.replace_intensities(labels, np.asarray([0] + list(dataframe['feret_diameter_max'])))

layer = viewer.add_image(parametric_map)

# fine-tune visualization
layer.colormap = 'turbo'
layer.contrast_limits = [20, 70]

napari.utils.nbscreenshot(viewer)


# In[ ]:





# In[ ]:




