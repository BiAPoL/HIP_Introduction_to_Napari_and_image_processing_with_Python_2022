#!/usr/bin/env python
# coding: utf-8

# ## Interacting with measurements in Napari
# When exploring data, it often makes sense to explore measurements as parametric images interactively.

# In[1]:


import napari
from napari_simpleitk_image_processing import label_statistics, touching_objects_labeling
from napari_skimage_regionprops import add_table
from skimage.data import cells3d
from skimage.filters import gaussian
import pandas as pd


# We start by loading a 3D image into napari and segmenting the nuclei.

# In[2]:


import napari
viewer = napari.Viewer()


# In[3]:


image = cells3d()[:,1]

viewer.add_image(image)
napari.utils.nbscreenshot(viewer)


# In[4]:


blurred = gaussian(image, 1, preserve_range=True)
binary = blurred > 6000
labels = touching_objects_labeling(binary)

labels_layer = viewer.add_labels(labels)

napari.utils.nbscreenshot(viewer)


# ## Feature extraction 
# We next extract features using [napari-simpleitk-image-processing](https://github.com/haesleinhuepf/napari-simpleitk-image-processing) and send the result as table to napari.

# In[5]:


statistics = label_statistics(image, labels, shape=True)

pd.DataFrame(statistics)


# In[6]:


labels_layer.features = statistics

add_table(labels_layer, viewer)

napari.utils.nbscreenshot(viewer)


# ## Exercise
# Double-click a column header in the napari viewer and execute the next cell afterwards.

# In[8]:


napari.utils.nbscreenshot(viewer)


# In[ ]:




