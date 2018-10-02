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


