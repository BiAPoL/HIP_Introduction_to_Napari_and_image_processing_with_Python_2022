#!/usr/bin/env python
# coding: utf-8

# # Using Napari to visualize and interact with images

# [Matplotlib](https://matplotlib.org/stable/gallery/index.html) is the most flexible and traditional library to display images, also in jupyter notebooks. There are other very good options like [seaborn](https://seaborn.pydata.org/), [plotly](https://plotly.com/python/) and [bokeh](https://docs.bokeh.org/en/latest/docs/gallery.html#standalone-examples), with different pros and cons.
# 
# Regarding interaction, even though these libraries can be interative, [Napari](https://napari.org/gallery.html) stands out as a fast, interactive, multi-dimensional image viewer in Python.
# 
# In this notebook, we will open a napari viewer from here, add images and perform some interactions with them.

# # Opening the napari Viewer

# In order to open the viewer, we first have to import napari

# In[1]:


import napari


# For this demonstration, we will also import the function `nbscreenshot` to display screenshots from napari here in the notebook.

# In[2]:


from napari.utils import nbscreenshot


# Now, we can open the viewer with the following command:

# In[3]:


viewer = napari.Viewer()


# Napari should open in a separated window. Some warning messages in the cell above are normal.
# 
# Let's show a screenshot of the viewer here. We pass the variable viewer to the function.

# In[4]:


nbscreenshot(viewer)


# # Opening images in napari from a notebook

# Now, let's load some example images here and visualize them in napari.

# In[5]:


import numpy as np
from skimage import data


# We will open a 2D grayscale example image from scikit-image called `human_mitosis`.

# In[6]:


image_human_mitosis = data.human_mitosis() # read the example image 'human_mitosis' from scikit-image
image_human_mitosis.shape


# To open an image in napari from a notebook, we use the command `add_image()` from the `viewer`.

# In[7]:


viewer.add_image(image_human_mitosis)


# This adds the image as a `layer` in napari. The layers list can be seen at the bottom left of the screen. For now, we have a single image layer there. Let's take a new screenshot.

# In[8]:


nbscreenshot(viewer)


# # Interacting with the image

# In the viewer, we can interact with the image in several ways. We can zoom in/out with the mouse wheel for example.
# 
# Also, we can change something in the viewer, like the colormap, and retrieve this change back in code. Before we do that, let's get the current colormap of this layer.

# We have to follow a hierarchy to get to the image colormap:
#     
#     1. `viewer`
#     
#     2. `layers`
#     
#     3. `colormap`
#     
#     4. `name`
#     
# So the command becomes:

# In[9]:


current_colormap = viewer.layers[0].colormap.name
current_colormap


# The `[0]` index means we are accesssing a property of the first layer.

# Now we go to the napari viewer and select a different colormap.

# In[10]:


nbscreenshot(viewer)


# In[11]:


current_colormap = viewer.layers[0].colormap.name
current_colormap


# # Exercise 1
# Add the brick image below to the viewer and now do the other way around: by code, change the colormap to `red` and the opacity to `0.5`. Check the effects in the viewer.
# 
# *Hint: you can access and modify the opacity in a similar fashion to the colormap:
#     
#     1. viewer
#     
#     2. layers
#     
#     3. opacity

# In[12]:


image_brick = data.brick()


# In[ ]:




