# -*- coding: utf-8 -*-
"""
Episode 02 Introduction to Image Data

"""

from tensorflow import keras
from keras.utils import img_to_array
from keras.utils import load_img
import numpy as np
from sklearn.model_selection import train_test_split

#### Pre-existing image data

# load the CIFAR-10 dataset included with the keras packages
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()


#### Custom image data

# specify the image path
new_img_path = "../data/Jabiru_TGS.JPG" # path to image

# read in the image with default arguments
new_img_pil = load_img(new_img_path)

# confirm the data class and size
print('The new image is of type :', new_img_pil.__class__, 'and has the size', new_img_pil.size)

### Image Dimensions - Resizing

# read in the new image and specify the target size to be the same as our training images
new_img_pil_small = load_img(new_img_path, target_size=(32,32))

# confirm the data class and shape
print('The new image is still of type:', new_img_pil_small.__class__, 'but now has the same size', new_img_pil_small.size, 'as our training data.')# convert the Image into an array for processing
new_img_arr = img_to_array(new_img_pil)

### Normalization

# convert the Image into an array for normalization
new_img_arr = img_to_array(new_img_pil_small)

# confirm the data class and shape
print('The new image is now of type :', new_img_arr.__class__, 'and has the shape', new_img_arr.shape)

# extract the min, max, and mean pixel values BEFORE
print('The min, max, and mean pixel values are', new_img_arr.min(), ',', new_img_arr.max(), ', and', new_img_arr.mean().round(), 'respectively.')

# normalize the RGB values to be between 0 and 1
new_img_arr_norm = new_img_arr / 255.0

# extract the min, max, and mean pixel values AFTER
print('After normalization, the min, max, and mean pixel values are', new_img_arr_norm.min(), ',', new_img_arr_norm.max(), ', and', new_img_arr_norm.mean().round(), 'respectively.')

### One-hot encoding

print()
print('train_labels before one hot encoding')
print(train_labels)

# one-hot encode labels
train_labels = keras.utils.to_categorical(train_labels, len(class_names))
val_labels = keras.utils.to_categorical(val_labels, len(class_names))

print()
print('train_labels after one hot encoding')
print(train_labels)


### Data Splitting
# split the training data into training and validation sets
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

########################################################
# Challenge Training and Validation Sets

#A. Training Set
print('The training set is of type', train_images.__class__)
print('The training set has', train_images.shape[0], 'samples.\n')

print('The number of labels in our training set and the number images in each class are:\n')
print(np.unique(train_labels, return_counts=True))

#B. Validation Set
print('The validation set is of type', val_images.__class__)
print('The validation set has', val_images.shape[0], 'samples.\n')

print('The number of labels in our validation set and the number images in each class are:\n')
print(np.unique(val_labels, return_counts=True))
########################################################



