# -*- coding: utf-8 -*-
"""
Image Classification with Convolutional Neural Networks

Episode 01 Introduction to Deep Learning

"""

#%%

# load the required packages

from tensorflow import keras # data and neural network
from sklearn.model_selection import train_test_split # data splitting
import matplotlib.pyplot as plt # plotting

#%%

# create a function to prepare the dataset

def prepare_dataset(train_images, train_labels):
    
    # normalize the RGB values to be between 0 and 1
    train_images = train_images / 255
    test_images = train_labels / 255
    
    # one hot encode the training labels
    train_labels = keras.utils.to_categorical(train_labels, len(class_names))
    
    # split the training data into training and validation set
    train_images, val_images, train_labels, val_labels = train_test_split(
    train_images, train_labels, test_size = 0.2, random_state=42)

    return train_images, val_images, train_labels, val_labels

#%%

# load the data
(train_images, train_labels), (test_images, test_labels) = keras.datasets.cifar10.load_data()

# create a list of class names associated with each CIFAR-10 label
class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

### Step 3. Prepare data

# prepare the dataset for training
train_images, val_images, train_labels, val_labels = prepare_dataset(train_images, train_labels)

#%%

# CHALLENGE EXAMINE THE CIFAR-10 DATASET

print('Train: Images=%s, Labels=%s' % (train_images.shape, train_labels.shape))
print('Validate: Images=%s, Labels=%s' % (val_images.shape, val_labels.shape))
print('Test: Images=%s, Labels=%s' % (test_images.shape, test_labels.shape))

#%%

#### Visualise a subset of the CIFAR-10 dataset

plt.figure(figsize=(10,10)) # create a plot

# add images to plot
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.imshow(train_images[i])
    plt.axis('off')
    plt.title(class_names[train_labels[i,].argmax()])
    
plt.show() # view plot

#%%

### Step 4. Build a new architecture from scratch

# create a function that defines a convolutional neural network

def create_model_intro():
    
    # CNN Part 1
    # Input layer of 32x32 images with three channels (RGB)
    inputs_intro = keras.Input(shape=train_images.shape[1:])
    
    # CNN Part 2
    # Convolutional layer with 16 filters, 3x3 kernel size, and ReLU activation
    x_intro = keras.layers.Conv2D(16, (3, 3), activation='relu')(inputs_intro)
    # Pooling layer with input window sized 2,2
    x_intro = keras.layers.MaxPooling2D((2, 2))(x_intro)
    # Second Convolutional layer with 32 filters, 3x3 kernel size, and ReLU activation
    x_intro = keras.layers.Conv2D(32, (3, 3), activation='relu')(x_intro)
    # Second Pooling layer with input window sized 2,2
    x_intro = keras.layers.MaxPooling2D((2, 2))(x_intro)
    # Flatten layer to convert 2D feature maps into a 1D vector
    x_intro = keras.layers.Flatten()(x_intro)
    # Dense layer with 64 neurons and ReLU activation
    x_intro = keras.layers.Dense(64, activation='relu')(x_intro)
    
    # CNN Part 3
    # Output layer with 10 units (one for each class) and softmax activation
    outputs_intro = keras.layers.Dense(10, activation='softmax')(x_intro)
    
    # create the model
    model_intro = keras.Model(inputs = inputs_intro, 
                              outputs = outputs_intro, 
                              name = "cifar_model_intro")
    
    return model_intro


#%%

# create the introduction model
model_intro = create_model_intro()

# view model summary
model_intro.summary()

#%%

### Step 5. Choose a loss function and optimizer and compile model

# compile model
model_intro.compile(optimizer = 'adam',
                    loss = keras.losses.CategoricalCrossentropy(),
                    metrics = ['accuracy'])

#%%

### Step 6. Train the model

# fit model
model_intro.fit(train_images, train_labels, epochs = 10,
                validation_data = (val_images, val_labels),
                batch_size=32)

#%%

### Step 7. Perform a Prediction/Classification

# make prediction for the first test image
result_intro = model_intro.predict(test_images[0].reshape(1,32,32,3))

# extract class for prediction with highest probability
class_names[result_intro.argmax()]

#%%

# plot the first test image with its true label

plt.figure() # create a plot

# display image
plt.imshow(test_images[0])
plt.title('True class:' + class_names[result_intro.argmax()])

plt.show() # view plot

#%%

### Step 10. Share Model

# save model
model_intro.save('fit_outputs/model_intro.keras')








