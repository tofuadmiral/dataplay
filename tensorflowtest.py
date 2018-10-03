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

plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(label_names[train_labels[i]])

plt.show()



## now we'll configure the layers and then build the model

# basic block is the layer
# layers extract representations
# chain tgt simple layers

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)), 
    keras.layers.Dense(128, activation = tf.nn.relu), 
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
# first layer just flattens into one d array of 784 pixels
# then two dense layers, fully connected neural layers
# first has 128 nodes, second has 10 node softmax
# the second has 10 probability scores that sum to 1
# each node has a score that indiciates whether belongs to one of ten classes

# now we need to add some settings
# loss function to measure how accurate the model is during training, minimize this
# optimizer to update the model based on data and loss func
# metrics: monitor training, i.e. accuracy is the number that are correct

model.compile(optimizer=tf.train.AdamOptimizer(), 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              

# now we train
# involves feed the training data in, train_images and train_labels
# then model learns
# we ask the model to make predictions on test_images
# we verify that it's right via test_labels

print(model.fit(train_images, train_labels, epochs=5))

# CLOSE THE WINDOWS bc we know what image it's going to be 
plt.close(all)

# now we want to see how it performs on the test dataset
test_loss, test_acc, = model.evaluate(test_images, test_labels)
print('Test Accuracy: ', test_acc, '\ntest loss: ', test_loss)

# actually performs worse on this stuff, which is an example of overfitting
# overfitting is when the model performs worse on test data then the training data

# now, let's make some predictions 
predictions = model.predict(test_images)
print(predictions[0])
whichcategory=np.argmax(predictions[0])
print('the max category is: ', whichcategory, 'which corresponds to: ', label_names[whichcategory])




