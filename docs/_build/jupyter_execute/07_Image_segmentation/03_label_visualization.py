#!/usr/bin/env python
# coding: utf-8

# # Label image visualization
# Depending on with which image processing library you work, label images may be visualized differently. A common way for visualizing labels is to draw objects in different colours.
# 
# See also
# * [scikit-image label2rgb](https://scikit-image.org/docs/dev/api/skimage.color.html#skimage.color.label2rgb)

# In[1]:


from skimage.io import imread, imshow
from skimage.measure import label
from skimage.color import label2rgb


# ## Visualizing label images using scikit-image
# Per default, when using python/numpy/scikit-image, label images are shown in yellow-blue, which may  make it hard to differentiate objects that are touching or surrounded by black background.

# In[2]:


image = imread("../../data/blobs.tif")
label_image = label(image > 128)

imshow(label_image)


# One way for improving visualization works using the [label2rgb function](https://scikit-image.org/docs/dev/api/skimage.color.html#skimage.color.label2rgb).
# 
# Note: The resulting `rgb_label_image` must not be further processed. It is for visualization purposes only.

# In[3]:


rgb_label_image = label2rgb(label_image)

imshow(rgb_label_image)


# ## Visualizing label images using some other libraries
# We spent some effort to make label image visualization more straight-forward in the some napari-related image processing libraries.

# In[4]:


import napari_segment_blobs_and_things_with_membranes as nsbatwm

label_image_2 = nsbatwm.connected_component_labeling(image > 128)
label_image_2


# In[5]:


import napari_simpleitk_image_processing as nsitk

label_image_3 = nsitk.connected_component_labeling(image > 128)
label_image_3


# In[7]:


import pyclesperanto_prototype as cle

label_image_4 = cle.label(image > 128)
label_image_4

