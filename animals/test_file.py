#!/usr/bin/env python
# coding: utf-8

# In[1]:


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



# In[8]:


# dimensions of our images.  
img_width, img_height = 224, 224  
   
top_model_weights_path = 'bottleneck_fc_model.h5'  
train_data_dir = '../data/train'  
validation_data_dir = '../data/validation'  
test_data_dir = '../data/test'  
   
# number of epochs to train top model  
epochs = 100  
# batch size used by flow_from_directory and predict_generator  
batch_size = 50  

num_classes = 6


# build the VGG16 network
vgg = applications.VGG16(include_top=False, weights='imagenet')



# build top model
model = Sequential()
model.add(Flatten(input_shape=(7,7,512)))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='sigmoid'))

model.load_weights('bottleneck_fc_model.h5')





def animal_class(file):
    image_path = file

    orig = cv2.imread(image_path)

    #print("[INFO] loading and preprocessing image...")
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)

    # important! otherwise the predictions will be '0'
    image = image / 255

    image = np.expand_dims(image, axis=0)
    # print(image)


    # In[96]:

    animals = {
	    '[0]':'Borboleta',
	    '[1]':'Galinha',
	    '[2]':'Elefante',
	    '[3]':'Cavalo',
	    '[4]':'Aranha',
	    '[5]':'Esquilo'
    }
    
    # get the bottleneck prediction from the pre-trained VGG16 model

    bottleneck_prediction = vgg.predict(image)
    #print("PRED", bottleneck_prediction)
  
    # use the bottleneck prediction on the top model to get the final classification
    #class_predicted = model.predict_classes(bottleneck_prediction)
    
    pred = model.predict(bottleneck_prediction)
    
    #print(pred[0])
    #print(pred[0].max())
    #print(np.where(pred[0] == pred[0].max())[0])


    return pred#animals[str(class_predicted)]
