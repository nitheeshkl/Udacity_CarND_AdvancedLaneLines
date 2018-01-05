# Udacity_CarND_AdvancedLaneLines
Term1-Project4: Advanced lane lines detection

## Goals

* Compute the camera calibration matrix and distortion co-efficients give a set of chessboard images
* Apply a distortion correction to raw images
* Use color transforms, gradients,etc to create a theresholded binary images
* Apply a perspective transfor to rectify binary image
* Detect lane pixels and fit to find the lane boundary
* Determine the curvature of the lane and vehicel position wieth rescpect to center.
* Warp the detected lane boundaries back onto the original images
* Output visual display of the lane boundaries and numerical estimation of the lane curvature and vehicle position.

## [Rubric](https://review.udacity.com/#!/rubrics/571/view) Points

### Here I will consider the rubric points individually and describe how I addressed each point in my implementation.  

---

### Writeup / README

#### 1. Provide a Writeup / README that includes all the rubric points and how you addressed each one.  You can submit your writeup as markdown or pdf.  [Here](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) is a template writeup for this project you can use as a guide and a starting point.  

You're reading it!

### Camera Calibration

#### 1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The _calibrate_camera()_ method implemented in the second cell of the python notebook performs the camera calibration. It uses the OpenCV methods _findChessboardCorners()_ and _calibrateCamera()_ to find the clibration matrix and distortion coefficients. The _findChessboardCorners()_ method takes in a distorted and grayed checkerboard image along with number of internal corners and returns image points. This is done for all the image in the set of checkerboard images and these image points along with their corresponding object points are provided to _calibrateCamera()_ method which returns the calibration matrix and distortion coefficients.

The _undistort()_ warapper method takes in an image along with the calibration matrix and distortion coefficients and returns a rectified image using the OpenCV's _undistort()_ method.

A sample distorted calibration checkboard image and its distortion corrected image is as shown below

| Distored image | Rectified image |
|----------------|-----------------|
|![distorted image](https://raw.githubusercontent.com/nitheeshkl/Udacity_CarND_AdvancedLaneLines/master/camera_cal/calibration1.jpg) | ![rectified image](https://raw.githubusercontent.com/nitheeshkl/Udacity_CarND_AdvancedLaneLines/master/camera_cal/calibration1_undistorted.jpg) |

The python notebook shows these corrections for all the checkboard images used.

### Pipeline

#### 1. Provide an example of a distortion-corrected image.

The same camera that we calibrated above is used for capturing the images from the car. Therefore, use the _undistort()_ method with calibration matrix and distrotion coefficients to rectify all the images from the video. The sample demo of a image from the project video and its rectified image is as shown below

| Original image | Rectified image |
|----------------|-----------------|
|![distorted image](https://raw.githubusercontent.com/nitheeshkl/Udacity_CarND_AdvancedLaneLines/master/test_images/straight_lines1.jpg) | ![rectified image](https://raw.githubusercontent.com/nitheeshkl/Udacity_CarND_AdvancedLaneLines/master/test_images/straight_lines1.jpg) |

#### 2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.
