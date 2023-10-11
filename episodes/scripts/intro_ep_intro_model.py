# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 09:37:03 2023

@author: Jason Bell
"""

from tensorflow import keras
import matplotlib.pyplot as plt
from icwithcnn_functions import prepare_image_icwithcnn # custom function
import seaborn as sns
import pandas as pd
import time

start = time.time()

# load the cifar dataset included with the keras packages
(train_images, train_labels), (val_images, val_labels) = keras.datasets.cifar10.load_data()

print('Train: Images=%s, Labels=%s' % (train_images.shape, train_labels.shape))
print('Validate: Images=%s, Labels=%s' % (val_images.shape, val_labels.shape))


# normalize the RGB values to be between 0 and 1
train_images = train_images / 255.0
val_images = val_images / 255.0

# create a list of classnames
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

# plot a subset of the images
# create a figure object and specify width, height in inches
plt.figure(figsize=(10,10))

for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.axis('off')
    plt.title(class_names[train_labels[i,0]])
plt.show()


# define the inputs, layers, and outputs of a CNN model

# CNN Part 1
# Input layer of 32x32 images with three channels (RGB)
inputs_intro = keras.Input(shape=train_images.shape[1:])

# CNN Part 2
# Convolutional layer with 50 filters, 3x3 kernel size, and ReLU activation
x_intro = keras.layers.Conv2D(50, (3, 3), activation='relu')(inputs_intro)
# Second Convolutional layer
x_intro = keras.layers.Conv2D(50, (3, 3), activation='relu')(x_intro)
# Flatten layer to convert 2D feature maps into a 1D vector
x_intro = keras.layers.Flatten()(x_intro)

# CNN Part 3
# Output layer with 10 units (one for each class)
outputs_intro = keras.layers.Dense(10, activation='softmax')(x_intro)

# create the model
model_intro = keras.Model(inputs=inputs_intro, outputs=outputs_intro, name="cifar_model_intro")

# compile the model
model_intro.compile(optimizer = 'adam', 
                    loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True), 
                    metrics = ['accuracy'])

# fit the model
history_intro = model_intro.fit(train_images, train_labels, 
                                epochs = 10, 
                                validation_data = (val_images, val_labels))

# save the model
model_intro.save('fit_outputs/01_intro_model.h5')


# use model to make a prediction on unseen image

# specify a new image and prepare it to match cifar10 dataset
new_img_path = "../data/Jabiru_TGS.JPG" # path to image
new_img_prepped = prepare_image_icwithcnn(new_img_path) # custom function

# predict the classname
result_intro = model_intro.predict(new_img_prepped) # make prediction
print(' The predicted probability of each class is: ', result_intro.round(4))
print('The class with the highest predicted probability is: ', class_names[result_intro.argmax()])

####
####
#### continues in build episode 03
####
####

# monitor the training progress

# convert the intro model training history into a dataframe for plotting 
history_intro_df = pd.DataFrame.from_dict(history_intro.history)

# plot the loss and accuracy from the training process
fig, axes = plt.subplots(1, 2)
fig.suptitle('cifar_model_intro')
sns.lineplot(ax=axes[0], data=history_intro_df[['loss', 'val_loss']])
sns.lineplot(ax=axes[1], data=history_intro_df[['accuracy', 'val_accuracy']])

end = time.time()

print()
print()
print("Time taken to run program was:", end - start, "seconds")