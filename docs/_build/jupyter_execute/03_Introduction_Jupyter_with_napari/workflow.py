#!/usr/bin/env python
# coding: utf-8

# In[1]:


from skimage.io import imread
import pyclesperanto_prototype as cle
import napari_segment_blobs_and_things_with_membranes as nsbatwm
import napari
viewer = napari.Viewer()


# In[2]:


image0_n = imread(
    "C:/Users/mazo260d/Documents/GitHub/I2K2022-napari-workshop/notebooks_and_napari/data/nuclei3d.tif")
viewer.add_image(image0_n, name="nuclei3d")


# ## voronoi otsu labeling

# This function

# In[3]:


image1_vol = cle.voronoi_otsu_labeling(image0_n, None, 9.0, 3.0)
viewer.add_labels(
    image1_vol, name='Result of voronoi_otsu_labeling (clesperanto)')
napari.utils.nbscreenshot(viewer)


# ## remove labels on edges

# In[4]:


image2_R = nsbatwm.remove_labels_on_edges(image1_vol)
viewer.add_labels(
    image2_R, name='Result of Remove labeled objects at the image border (scikit-image, nsbatwm)')
napari.utils.nbscreenshot(viewer)


# In[ ]:




