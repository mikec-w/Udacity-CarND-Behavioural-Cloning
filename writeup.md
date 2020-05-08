# **Behavioral Cloning** 

## Writeup Template

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./report/cnn-architecture-624x890.png "Model Visualization"
[image2]: ./report/centre_line.jpg "Centre Driving"
[image3]: ./report/recover1.jpg "Recovery Image"
[image4]: ./report/recover2.jpg "Recovery Image"
[image5]: ./report/recover3.jpg "Recovery Image"
[image6]: ./report/original.jpg "Normal Image"
[image7]: ./report/flipped.jpg "Flipped Image"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model_nivida.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup.md summarizing the results
* video.mp4 video showing the unaided lap 

Using the Udacity provided simulator and the drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

The model_nvidia.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

The model employed was based on prior NVidia research (https://devblogs.nvidia.com/deep-learning-self-driving-cars/).

In order to reduce overfitting, dropouts were added to the final 3 fully connected layers. In addition the training set was enhanced with the horizontally flipped images and the addition of the left and right camera images with steering corrections. 



### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was to attempt to replicated the work previously performed by NVIDIA. As their work attempted to solve exactly the same problem, starting with it as the base solution was sensible as most of the lower level design decisions would have already been proven out. 

Using KERAS the model detailed in the reference paper (above) was built and initially trained on provided sample data. This allowed any issues to be resolved before moving on to larger training sets.

A modification was made to the model to add suitable dropouts are each of the fully connected layers at the end of the model. These were set to have a 25% probability of dropping a node during training in order to prevent overfitting and generate a more robust model.

Having trained the model using the training set collected using the philosophy detailed above, the final validation was to run the car in autonomous mode. This was reasonably successful and the car managed to complete one entire lap wihout venturing onto the kerbs. However, it is clear that a more substantial training set is probably necessary to result in a smoother drive for the occupants and to better maintain the centre-of-the-lane position.


#### 2. Final Model Architecture

The final model architecture (model_nvidia.py) consisted of a convolution neural network with the following layers and layer sizes ...

* 1 cropping layer
* 1 normalization layer
* 5 convolution layers
* 4 fully connected layers with dropouts

Here is a visualization of the architecture (note: visualizing the architecture is optional according to the project rubric)

![alt text][image1]

The first layer crops superfluous data from the image by removing the top and bottom (the sky and the car). The convolution layers perform feature extraction with the first three strided (2x2 and 5x5 kernel) before the final two using a 3x3 non-strided layer. 

#### 3. Creation of the Training Set & Training Process

Having verified the model structure, the most significant challenge was generating a suitable test data set that was comprehensive enough to control the vehicle. Initial attempts using the keyboard controls proved disappointing as the steering angles generated were somewhat binary in nature. To resolve this, the simulator was run on a local PC and a bluetooth XBOX controller was connected. This allowed analogue steer control and made it significantly easier to produce steady continuous angles around bends.

With a few laps of centre lane driving (remembering the model inverted the images for training so it was not necessary to reverse the driving direction), it was necessary to augment the training set with some lane recovery manoeuvres. These are necessary to help recover the car when the initial training set proved inadequate for some of the more unusual situations. The recovery manoeuvres can be clearly seen in the resulting video where the car looks to be drifting off the road before a rather dramatic steering correction is applied. In a real world scenario this would not be particularly desirable for occupants of the car and, while still necessary to cover all scenarios, would hopefully become less necessary with further enhanced training data.

Using these recovery manoeuvres the car manages to complete an entire lap of the course without venturing onto the kerb surfaces.

Below is an example of centre line driving:

![alt text][image2]

These images show an example of an attempted recovery:

![alt text][image3]
![alt text][image4]
![alt text][image5]

Note how the three examples demonstrate the different types of kerb used on the test track.

Here is an example of an original and a flipped image used to augment the dataset. Note the steering measurement is also flipped.

![alt text][image6]
![alt text][image7]

After the collection process, I had 20127 image data points. I then preprocessed this data by converting the image to RGB (from BGR) and normalizing the colour values. 

I finally randomly shuffled the data set and put 20% of the data into a validation set. 

The training data was split into training and validation sets and the mean squared error monitoring through the training process. In most cases, both sets had very similar mse values suggesting that the model was neither over or underfitting. It was noted, however, that a set of sample data that resulted in a lower mse value did not necessarily result in a better performance on track. This was attributed to the training set being inadequate to cover all eventualities that may occur.

The model used an adam optimizer, so the learning rate was not tuned manually. The number of EPOCHs did seem to have an effect but we generally stabilised by about the 10th iteration. Dropout rate was adjusted slightly but did not seem to have any clearly noticable effect, accordingly a 25% dropout rate was chosen.

