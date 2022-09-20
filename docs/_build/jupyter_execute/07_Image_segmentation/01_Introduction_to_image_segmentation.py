#!/usr/bin/env python
# coding: utf-8

# # Image segmentation
# Image segmentation is the process of separating an image into multiple regions. 
# 
# See also
# * [Image manipulation and processing using Numpy and Scipy by Emmanuelle Gouillart and Gaël Varoquaux](https://scipy-lectures.org/advanced/image_processing/index.html#basic-image)
# * [Tutorial on image segmentation with scikit-image](https://scikit-image.org/docs/dev/user_guide/tutorial_segmentation.html)
# 
# Let's start again by defining an image as a two dimensional array and visualize it using pyclesperanto.

# In[1]:


import numpy as np
from pyclesperanto_prototype import imshow
import napari


# In[2]:


image = np.asarray([
    [1, 0, 2, 1, 0, 0, 0],
    [0, 3, 1, 0, 1, 0, 1],
    [0, 5, 5, 1, 0, 1, 0],
    [0, 6, 6, 5, 1, 0, 2],
    [0, 0, 5, 6, 3, 0, 1],
    [0, 1, 2, 1, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0]
])


# In[3]:


imshow(image, colorbar=True)


# ## Binary images
# The most basic way of that is binarization, turning the image into a "positive" and a "negative" region. Typically, binary images are used for that, which could for example contain two different pixel values `True` and `False` representing "positive" and "negative", respectively. Technically, every image can be interpreted as a binary image using the rationale "Every pixel is considered positive that is neither `False` nor `0`."
# 
# ## Image thresholding
# A very basic algorithm for separating low intensity regions from high intensity regions in the image is thresholding.
# We will now make a new image containing `True` and `False` as pixel values depending on if the original image had intensity lower or higher a given threshold. As this image has just two different pixel values, it is a binary image:

# In[4]:


threshold = 4

binary_image = image > threshold


# In[5]:


binary_image


# In[6]:


imshow(binary_image)


# ## Exercise
# Show the original image in napari with a half-transparent overlay showing the binary image.

# In[ ]:


viewer = napari.Viewer()


# In[ ]:





# In[ ]:


napari.utils.nbscreenshot(viewer)

