## tensorflow test

import tensorflow as tf 
from tensorflow import keras

# helper libraries 
import numpy as np 
import matplotlib.pyplot as plt 
print(tf.__version__)


## we will use fashion mnist as a tester for our program, library of a lot of clothes 

# keras already has this built in so import it 
fashionpics = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashionpics.load_data()
# train images/labels are what we use to train,
# test images/lables is what we use to evaluate the model
# images are 28*28 arrays of 255 values, and labels are 0-9 where
# each number corresponds to a diff cateogry i.e. dress, etc. 


## store the labels bc we don't have them
label_names = ['T-shirt/top', 'trouser', 'pullover', 'dress', 'coat', 'sandal', 'shirt', 'sneaker', 'bag', 'ankle boot']

print(train_images.shape)
print(len(train_labels))
print(len(test_images)) # 6-1 split for train vs test

print(train_labels)

plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)


# now we want to scale the values to a range of 0-1
# before we feed it into the nn model
# cast integer to float and divide by 255

train_images = train_images / 255.0
test_images = test_images / 255.0

# display first 25 images from training set and display class name
# after this, we'll be ready to build and train





