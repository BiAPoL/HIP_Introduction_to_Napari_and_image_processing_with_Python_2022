#!/usr/bin/env python
# coding: utf-8

# # Image Filters

# Image filters are mathematical operations that modify pixel values to achieve a desired transformation.
# 
# They have several applications, some of which are noise removal, background subraction and edge detection.

# In[1]:


import numpy as np
import napari
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage import data
from skimage import filters
from scipy.ndimage import correlate, convolve


# Let's analyze this simple array/image:

# In[2]:


image1 = np.array([[5, 0, 2, 0, 0],
                   [0, 0, 2, 0, 0],
                   [0, 0, 4, 2, 2],
                   [0, 0, 2, 0, 0],
                   [0, 0, 2, 0, 1]]).astype(float)
image1


# You can see it as an image with matplotlib (or napari, or skimage).

# In[3]:


plt.imshow(image1, cmap='gray')
plt.colorbar()


# ## Filtering an image with a custom kernel

# More specifically, image filters are the result of small arrays (a.k.a. kernels/footprints) that slide through the image and perform some mathematical operation over the pixels they overlay, assigning a new value to each pixel. This operation is called [cross-correlation](https://en.wikipedia.org/wiki/Cross-correlation), which is very similar to a [convolution](https://en.wikipedia.org/wiki/Convolution), sometimes also used. One of the simplest filters we could design is one with a uniform kernel, which is an array composed of the same value.

# ### 1. Uniform Kernel

# We will apply this uniform kernel over the image.

# In[4]:


kernel1 = np.array(
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]])
print('image = \n', image1)
print('kernel = \n', kernel1)


# Let's look what happens at the central pixel for example (the one with value 4). Let's call it **pixel4**.
# In this case, each of the surrounding pixels and **pixel4** itself will be multiplied by 1 and then summed, like this:
# 
# (1 * **0**) + (1 * **2**) + (1 * **0**) +
# 
# (1 * **0**) + (1 * **4**) + (1 * **2**) +
# 
# (1 * **0**) + (1 * **2**) + (1 * **0**) = 10

# We can apply this kernel to all the pixel, i.e. to the image, with the `correlate()` function from scipy:

# In[5]:


output1 = correlate(image1, kernel1)
output1


# In[6]:


plt.imshow(output1, cmap='gray')
plt.colorbar()


# Two things can be noted:
# 
#     1. The image becomes blurry;
#     
#     2. The pixel values increase;
#     
# The first one would be the expected behaviour of a uniform kernel. We are summing each pixel value with its surroundings. We could mitigate the second by normalizing the kernel.

# ### 2. Mean Filter

# If we normalize the kernel by dividing it by the number of elements, we essentially get the mean:

# In[7]:


kernel1_normalized = kernel1 / 9
kernel1_normalized


# or more generally:

# In[8]:


kernel1_normalized = kernel1 / kernel1.size
kernel1_normalized


# And when we apply it again on the original image, we get the following:

# In[9]:


output2 = correlate(image1, kernel1_normalized)
print(output2)

plt.imshow(output2, cmap='gray')
plt.colorbar()


# This is the mean filter. Like all filters, it does change the pixel values. Now, each new value is the mean of each pixel with its surroundings. It can work as a noise removal, but it is not very good at it. If we have unrepresentative pixels with high values, they will significantly affect the mean.
# 
# There are more efficient options for that, like the [median](https://en.wikipedia.org/wiki/Median_filter) and [gaussian](https://en.wikipedia.org/wiki/Gaussian_filter) filters.

# ### 3. Prewitt Filter (a simple edge detection)

# What if we use the following kernel instead?

# In[10]:


kernel3 = np.array(
    [[1/3, 0, -1/3],
     [1/3, 0, -1/3],
     [1/3, 0, -1/3]])


# In[11]:


output3 = correlate(image1, kernel3)
print(output3)

plt.imshow(output3, cmap='gray')
plt.colorbar()


# If we look at the columns number 1 and 3, we can see two vertical lines with high negative (dark) and positive (bright) values, respectively. 
# 
# Did you see that these columns lie exactly at each side of the central vertical line in the original image (column number 2 in image1)?
# 
# This means this filter can highlight vertical edges, i.e., strong transitions along the horizontal direction! Check it out with the brick image!

# In[12]:


image_brick = data.brick().astype(float)
plt.imshow(image_brick, cmap='gray')
plt.colorbar()


# In[13]:


brick_v = convolve(image_brick, kernel3)


# In[14]:


plt.imshow(brick_v, cmap='gray')
plt.colorbar()


# # Exercise 1

# Apply the horizontal Prewitt filter to the same image and display the resulting image.

# In[ ]:





# In[ ]:





# # Exercise 2

# Apply the [Prewitt](https://en.wikipedia.org/wiki/Prewitt_operator), [Gaussian](https://en.wikipedia.org/wiki/Gaussian_filter) and Median filters from scikit-image to the cells image and display the outputs.
# 
# What are each of these filters good at?
# 
# *Hint: you don't need to manually define a kernel anymore for these.*

# In[15]:


from skimage.filters import prewitt, gaussian, median


# In[16]:


image_path = '../data/mitosis_mod.tif'
image_cells = imread(image_path)


# In[17]:


plt.imshow(image_cells, cmap='gray')
plt.colorbar()


# In[ ]:





# # Exercise 3

# Binarize the results from exercise 2, including the original image, with Otsu threshold and display them.
# 
# In your opinion, which of these results is less noisy?

# In[18]:


from skimage.filters import threshold_otsu


# In[ ]:





# # Exercise 4 (optional)

# Now that you know how filters work on images, you can design your filter! Play with it by designing your own (small) kernel and see the results! :D 

# In[19]:


# my_kernel = 


# In[ ]:





# In[ ]:




