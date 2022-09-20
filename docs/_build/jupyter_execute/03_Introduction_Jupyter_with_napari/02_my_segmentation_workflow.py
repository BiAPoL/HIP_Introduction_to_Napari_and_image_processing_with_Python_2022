#!/usr/bin/env python
# coding: utf-8

# # My Segmentation Workflow

# This notebook segments a 3D nuclei image and measure their properties

# In[1]:


from skimage.io import imread
import napari_segment_blobs_and_things_with_membranes as nsbatwm
import napari
viewer = napari.Viewer()


# ## 1. Open the image and add it to napari

# In[2]:


image0_n = imread("../../data/3D/nuclei.tif")
viewer.add_image(image0_n, name="nuclei3d")


# ## 2. Apply voronoi otsu labeling from 'nsbatwm'

# In[3]:


image1_V = nsbatwm.voronoi_otsu_labeling(image0_n, 9.0, 3.0)
viewer.add_labels(image1_V, name='Result of Voronoi-Otsu-labeling (nsbatwm)')
napari.utils.nbscreenshot(viewer)


# ## 3. Apply remove labels on edges from 'nsbatwm'

# In[4]:


image2_R = nsbatwm.remove_labels_on_edges(image1_V)
viewer.add_labels(
    image2_R, name='Result of Remove labeled objects at the image border (scikit-image, nsbatwm)')
napari.utils.nbscreenshot(viewer)


# ## 4. Measure properties from 'scikit-image'

# In[5]:


from napari_skimage_regionprops._regionprops import regionprops_table
import pandas as pd


# In[6]:


df = pd.DataFrame(regionprops_table(image0_n, image2_R, shape = True))
df


# ## 5. Plot data

# In[7]:


df.plot.scatter('area', 'mean_intensity')


# ## 6. Save table to disk

# In[8]:


df.to_csv('../../data/3D/table_nuclei.csv')


# In[ ]:




