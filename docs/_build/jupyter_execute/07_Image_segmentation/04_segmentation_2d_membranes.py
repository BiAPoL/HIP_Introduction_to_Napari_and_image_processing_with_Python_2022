#!/usr/bin/env python
# coding: utf-8

# # Seeded watershed for membrane-based cell segmentation
# In this section we will use a seeded watershed approach to cell segmentation. This approach is very common when cell segmentation based on images of membrane markers are given. Therefore, we use the napari plugin [napari-segment-blobs-and-things-with-membranes](https://github.com/haesleinhuepf/napari-segment-blobs-and-things-with-membranes). Under the hood, this plugins uses functions from [scikit-image](http://scikit-image.org/).
# 
# See also
# * [Robert Haase's lecture 02a Image Filtering and Segmentation, watershed explanation at 35:30](https://youtu.be/LT8L3vSLQ2Q?t=2124)

# In[1]:


from napari_segment_blobs_and_things_with_membranes import voronoi_otsu_labeling, \
                                                           seeded_watershed, \
                                                           local_minima_seeded_watershed
from skimage.io import imread, imshow, imsave
from skimage.filters import gaussian


# We load the [cells3d example image from scikit-image](https://scikit-image.org/docs/stable/api/skimage.data.html?highlight=data#skimage.data.cells3d) which is a two-channel image showing nuclei and membrains. For simplicity, we will use a single 2D slice. The shown procedure also works in 3D.

# In[2]:


nuclei_channel = imread("../../data/nuclei.tif")[30]

imshow(nuclei_channel)


# In[11]:


membrane_channel = imread("../../data/membrane.tif")[30]

imshow(membrane_channel, vmax=6000)


# ## Voronoi-Otsu-Labeling for nuclei segmentation
# First, we start with segmenting the nuclei using the [Voronoi-Otsu-Labeling algorithm](image-segmentation:voronoi-otsu-labeling).

# In[4]:


labeled_nuclei = voronoi_otsu_labeling(nuclei_channel, spot_sigma=10, outline_sigma=2)

labeled_nuclei


# ## Seeded watershed
# We can use the image of labeled nuclei as starting point for flooding the low-intensity areas in the membrane image. This allows us to determine a cell segmentation.

# In[15]:


labeled_cells = seeded_watershed(membrane_channel, labeled_nuclei)

labeled_cells


# If the outlines of the cells are not 100% accurate, it may make sense to blur the membrane image a bit before segmenting the cells.

# In[6]:


blurred = gaussian(membrane_channel, sigma=3)

labeled_cells = seeded_watershed(blurred, labeled_nuclei)

labeled_cells


# ## Seeded watershed using automatic seed detection
# 
# In case we didn't image a separate nuclei channel and only have the membrane channel available for segmentation, we can use the membrane image to search for local minima (dark areas).

# In[7]:


labeles_cells2 = local_minima_seeded_watershed(membrane_channel)
                              
labeles_cells2


# This function also has some parameters to allow fine tuning the segmentation. The parameter `outline_sigma` allows to control a Gaussian blur filter that allows fine-tuning the outlines of the segmented cells as shown above.

# In[8]:


labeles_cells3 = local_minima_seeded_watershed(membrane_channel, outline_sigma=3)
                              
labeles_cells3


# If there multiple cells sticking together, it may make sense to specify `spot_sigma`. This parameter allows to configure how close / large cells are.

# In[9]:


labeles_cells4 = local_minima_seeded_watershed(membrane_channel, spot_sigma=9, outline_sigma=3)
                              
labeles_cells4


# ## Exercise
# Load the following dataset and find good parameters for processing it using a seeded watershed approach. This example image data is a courtesy of Sascha M. Kuhn, Nadler Lab, MPI-CBG Dresden.

# In[10]:


image_slice = imread("../../data/membrane_2d_timelapse.tif")[2]

imshow(image_slice)


# In[ ]:




