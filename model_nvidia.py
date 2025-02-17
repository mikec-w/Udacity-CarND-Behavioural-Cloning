## Model for Autonomous Driving

# Import Library
import csv
import cv2 
import os
import numpy as np
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D, Conv2D, Dropout
from sklearn.model_selection import train_test_split

# Based on the NVidia Deep Learning Network
# https://devblogs.nvidia.com/deep-learning-self-driving-cars/

# Copy data from OneDrive if not on this machine....
# Use the download script... (download.sh)

# Load Data to start
samples = []

# Steer angle correction to apply to left and right hand images
steer_correction = 0.2

# Load the driving log data
with open('/opt/data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    # skip header
    next(reader)
    for line in reader:
        
        samples.append(line)
        # Left Camera - copy image from left camera and offset steering
        samples.append(line)
        samples[-1][0] = samples[-1][1]
        samples[-1][3] = str(float(samples[-1][3])+steer_correction)
        # Right Camera   - copy image from right camera and offset steering
        samples.append(line) 
        samples[-1][0] = samples[-1][2]
        samples[-1][3] = str(float(samples[-1][3])-steer_correction)
        
# Split Training and validation set
train_samples, validation_samples = train_test_split(samples, test_size=0.2)
        
# Use a generator to load the images as required rather than as a whole set
def generator(samples, batch_size=32):
    num_samples = len(samples)
    while 1: # loop forever so generator never terminates
        shuffle(samples)
        for offset in range(0, num_samples, batch_size):
            batch_samples = samples[offset:offset+batch_size]
            
            images = []          
            measurements = []
            for batch_sample in batch_samples:
                name = '/opt/data/IMG/' + batch_sample[0].split('/')[-1]
                image = cv2.imread(name)
                # Change colour to match
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                images.append(image)
                # Get steering wheel measurement (4th column)
                measurements.append(float(batch_sample[3]))
            
                # Add inverted images to the set 
                images.append(cv2.flip(image, 1))
                measurements.append(-float(batch_sample[3]))
    
    
            X_train = np.array(images)
            y_train = np.array(measurements)
            yield shuffle(X_train, y_train)

# Generator functions
batch_size=32
train_generator = generator(train_samples, batch_size=batch_size)
validation_generator = generator(validation_samples, batch_size=batch_size)

# NVidai model
model = Sequential()

# Preprocessing (normalize & crop image)
model.add(Cropping2D(cropping=((50,20),(0,0)), input_shape=(160,320,3)))
model.add(Lambda(lambda x: (x / 255.0) - 0.5))
          
# Model
# Conv2D 
model.add(Conv2D(24, kernel_size=(5,5), strides=(2,2),activation="relu"))
# Conv2D 5x5 kernel - 31x98x24        
model.add(Conv2D(36, kernel_size=(5,5), strides=(2,2),activation="relu"))
# Conv2D 5x5 kernal - 14, 47, 36
model.add(Conv2D(48, kernel_size=(5,5), strides=(2,2),activation="relu"))
# Conv2D 5x5 kernal - 5 22 48
model.add(Conv2D(64, kernel_size=(3,3),activation="relu"))
# Conv2D 3x3 kernel - 3 20 64
model.add(Conv2D(64, kernel_size=(3,3),activation="relu"))
# Conv2D 3x3 kkernal 1 18 64

# Flatten
model.add(Flatten())

# Fully Connected Layers
# Dropout added to reduce overfitting and increase robustness

# Fully connected 1164 - 100
model.add(Dense(100))
model.add(Dropout(0.25))
# Fully connected 100 - 50
model.add(Dense(50))
model.add(Dropout(0.25))
# Fully connected 50 - 10
model.add(Dense(10))
model.add(Dropout(0.25))
# Fully connect 10 -1 
model.add(Dense(1))


# Compilte the model - mean squared error as the losss function and adam as the optimiser

model.compile(loss='mse', optimizer='adam')

# Train the model using the generator functions to get the image data
model.fit_generator(train_generator, steps_per_epoch=np.ceil(len(train_samples)/batch_size), \
                    validation_data=validation_generator, validation_steps=np.ceil(len(validation_samples)/batch_size), epochs=10, verbose=1)
          
    
# Save the model
model.save('model.h5')
          
          