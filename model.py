## Model for Autonomous Driving

# Import Library
import csv
import cv2 
import os
import numpy as np
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, Cropping2D
from sklearn.model_selection import train_test_split

# Based on the NVidia Deep Learning Network

# Copy data from OneDrive if not on this machine....
# Use the download script...

# Load Data to start
samples = []
with open('/opt/data/driving_log.csv') as csvfile:
    reader = csv.reader(csvfile)
    # skip header
    next(reader)
    for line in reader:
        samples.append(line)
        
       
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
                images.append(image)
                # Get steering wheel measurement (4th column)
                measurements.append(float(batch_sample[3]))
    
    
            X_train = np.array(images)
            y_train = np.array(measurements)
            yield shuffle(X_train, y_train)

# Generator functions
batch_size=32
train_generator = generator(train_samples, batch_size=batch_size)
validation_generator = generator(validation_samples, batch_size=batch_size)

# Start with Basic Model to get it all running (regression network)
model = Sequential()

# Preprocessing (normalize & crop image)
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160, 320,3)))
model.add(Cropping2D(cropping=((50,20),(0,0))))
# Model

model.add(Flatten())
model.add(Dense(1))
           
model.compile(loss='mse', optimizer='adam')
#model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=7)
model.fit_generator(train_generator, steps_per_epoch=np.ceil(len(train_samples)/batch_size), \
                    validation_data=validation_generator, validation_steps=np.ceil(len(validation_samples)/batch_size), \
                    epochs=5, verbose=1)
          
model.save('model.h5')
          
          