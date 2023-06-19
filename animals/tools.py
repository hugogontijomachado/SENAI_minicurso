#Loading up all libraries
import numpy as np  
from keras.preprocessing.image import ImageDataGenerator#, img_to_array, load_img  
from keras.utils.image_utils import img_to_array, load_img
from keras.models import Sequential  
from keras.layers import Dropout, Flatten, Dense  
from keras import applications  
from keras.utils.np_utils import to_categorical  
import matplotlib.pyplot as plt  
import math  
import cv2  
import datetime


# build the VGG16 network
vgg = applications.VGG16(include_top=False, weights='imagenet')

num_classes = 6


# build top model
model = Sequential()
model.add(Flatten(input_shape=(7,7,512)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='sigmoid'))

model.load_weights(r'models/bottleneck_fc_model.h5')

def predict(filename):

    image = load_img(filename, target_size=(224, 224))
    image = img_to_array(image) / 255
    image = np.expand_dims(image, axis=0)

    bottleneck_prediction = vgg.predict(image)    
    pred = model.predict(bottleneck_prediction)
    return [x for x in pred[0]]
