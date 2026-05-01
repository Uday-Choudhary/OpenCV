# OpenCV Learning Progress Report

## Overview

I started learning OpenCV with a practical, hands-on approach. Instead of only reading concepts, I created small programs for each core topic and organized them into separate folders. This helped me understand how images and video frames are loaded, processed, transformed, drawn on, filtered, analyzed, and used for real-time detection.

The current work covers the foundation of computer vision using Python and OpenCV, including image handling, drawing functions, resizing and transformations, filtering, edge detection, contour and shape detection, video capture, video saving, and real-time face, eye, and smile detection using Haar cascades.

## Repository Structure

```text
OpenCV/
├── Image Handeling Basics/
├── Image Resizing & Shape/
├── Image Drawing Functions/
├── Filtering & Blurring/
├── Edge Detection in Open CV/
├── Contor & Shape Detection/
├── Video Functions/
├── Face Detection in OpenCV/
├── README.md
├── main.py
├── pyproject.toml
└── generated output images/videos
```

The project is divided topic-wise so each OpenCV concept can be studied independently. I also saved output files such as grayscale images, resized images, rotated images, cropped images, drawn images, contour-detected images, and a recorded video to verify that the programs are producing visible results.

## Environment And Dependencies

The project uses Python with OpenCV and supporting libraries.

Main dependencies:

- `opencv-python` for image processing, video processing, drawing, detection, and display windows.
- `numpy` for creating image matrices and custom kernels.
- `matplotlib` for visual comparison of bitwise operations.
- `pathlib` for reliable file path handling.

The project configuration is maintained in `pyproject.toml`, which currently includes:

```text
opencv-python
matplotlib
```

## 1. Image Handling Basics

Folder: `Image Handeling Basics/`

This section helped me understand how OpenCV represents and works with images.

### What I learned

- Loading an image using `cv2.imread()`.
- Checking whether an image was loaded successfully.
- Displaying images using `cv2.imshow()`.
- Holding display windows using `cv2.waitKey()`.
- Closing windows properly using `cv2.destroyAllWindows()`.
- Reading image dimensions using `image.shape`.
- Converting a color image into grayscale using `cv2.cvtColor()`.
- Saving processed images using `cv2.imwrite()`.
- Using `Path(__file__).parent` to make image paths work relative to the script location.

### Files implemented

- `loading.py`: Loads an image and checks if it exists.
- `displaying.py`: Displays an image in an OpenCV window.
- `dimensions.py`: Prints image height, width, and channel information.
- `grayscale.py`: Converts the image from BGR to grayscale.
- `saving.py`: Saves an image output.
- `assignment1.py`: Takes user input to either show or save a grayscale version of the image.

### Key understanding

OpenCV loads images as NumPy arrays. A color image usually has three channels in BGR format, not RGB. This is important because color order affects how images appear and how color-based processing should be handled.

## 2. Image Resizing And Shape Transformations

Folder: `Image Resizing & Shape/`

This section focused on changing the structure and orientation of images.

### What I learned

- Resizing an image using `cv2.resize()`.
- Cropping an image using NumPy array slicing.
- Flipping an image horizontally, vertically, or both using `cv2.flip()`.
- Rotating an image using a rotation matrix.
- Creating a rotation matrix with `cv2.getRotationMatrix2D()`.
- Applying affine transformation using `cv2.warpAffine()`.

### Files implemented

- `resize.py`: Resizes an image and saves the resized output.
- `crop.py`: Crops a selected area from an image.
- `flipped.py`: Flips an image.
- `rotation.py`: Rotates an image by 45 degrees and saves the result.

### Outputs generated

- `resize-minion.png`
- `cropped-minion.png`
- `rotated-minion.png`

### Key understanding

Image transformation is mostly about changing pixel positions. Cropping is a direct array operation, while rotation needs a transformation matrix because the image coordinates have to be recalculated.

## 3. Drawing Functions

Folder: `Image Drawing Functions/`

This section helped me learn how to annotate or modify images by drawing on them.

### What I learned

- Drawing a line using `cv2.line()`.
- Drawing a rectangle using `cv2.rectangle()`.
- Drawing a circle using `cv2.circle()`.
- Writing text on an image using `cv2.putText()`.
- Controlling color, thickness, position, radius, and font scale.
- Accepting user input to perform drawing operations dynamically.

### Files implemented

- `d_line.py`: Draws a line on an image.
- `d_rect.py`: Draws a rectangle on an image.
- `d_circle.py`: Draws a circle on an image.
- `d_text.py`: Writes text on an image.
- `Assignment2.py`: Interactive script where the user chooses whether to draw a line, rectangle, circle, or text.

### Outputs generated

- `line-minion.png`
- `rectangle-minion.png`
- `circle-minion.png`

### Key understanding

Drawing functions are very useful in computer vision because detection results are usually shown using bounding boxes, labels, points, or highlighted regions. This learning later helped in face, eye, smile, and contour detection.

## 4. Filtering, Blurring, And Sharpening

Folder: `Filtering & Blurring/`

This section focused on improving or changing image quality using filters.

### What I learned

- Applying Gaussian blur using `cv2.GaussianBlur()`.
- Applying median blur using `cv2.medianBlur()`.
- Understanding kernel size and its effect on the result.
- Using custom kernels with `cv2.filter2D()`.
- Sharpening an image with a manually defined NumPy kernel.

### Files implemented

- `gaussian_blur.py`: Applies Gaussian blur to smooth an image.
- `median_b.py`: Applies median blur, useful for reducing noise.
- `sharpening.py`: Uses a sharpening kernel to enhance image details.

### Key understanding

Filtering changes pixel values based on nearby pixels. Blurring reduces noise and detail, while sharpening increases edge contrast and makes details more visible. These operations are important preprocessing steps before tasks like edge detection or object detection.

## 5. Edge Detection And Bitwise Operations

Folder: `Edge Detection in Open CV/`

This section introduced feature extraction and binary image operations.

### What I learned

- Using Canny edge detection with `cv2.Canny()`.
- Understanding the role of lower and upper thresholds in edge detection.
- Loading images directly in grayscale for edge processing.
- Creating black images using NumPy arrays.
- Drawing white shapes on black backgrounds.
- Applying bitwise operations:
  - `cv2.bitwise_and()`
  - `cv2.bitwise_or()`
  - `cv2.bitwise_xor()`
  - `cv2.bitwise_not()`
- Comparing multiple image results using `matplotlib`.

### Files implemented

- `canny_func.py`: Detects edges in an image using the Canny algorithm.
- `bitwise_op.py`: Demonstrates AND, OR, XOR, and NOT operations on binary shapes.

### Key understanding

Edge detection helps find important boundaries in an image. Bitwise operations are useful when working with masks, object isolation, segmentation, and combining image regions.

## 6. Contour And Shape Detection

Folder: `Contor & Shape Detection/`

This section moved from basic image processing into image analysis.

### What I learned

- Converting an image to grayscale before contour detection.
- Applying thresholding using `cv2.threshold()`.
- Finding contours using `cv2.findContours()`.
- Drawing contours using `cv2.drawContours()`.
- Approximating shape boundaries using `cv2.approxPolyDP()`.
- Calculating contour perimeter using `cv2.arcLength()`.
- Classifying shapes based on the number of detected corners.
- Labeling shapes using `cv2.putText()`.

### File implemented

- `contour_fun.py`: Detects contours, approximates shape corners, identifies basic shapes, labels them, and saves the output.

### Output generated

- `contours_detected.png`

### Key understanding

Contours are useful for detecting object boundaries. After finding contours, we can approximate them and classify shapes such as triangles, quadrilaterals, pentagons, and circles based on the number of corners.

## 7. Video Capture And Video Saving

Folder: `Video Functions/`

This section helped me understand that video in OpenCV is processed frame by frame.

### What I learned

- Opening the webcam using `cv2.VideoCapture(0)`.
- Reading frames inside a loop using `cap.read()`.
- Displaying live video using `cv2.imshow()`.
- Exiting a video loop using keyboard input with `cv2.waitKey()`.
- Releasing camera resources using `cap.release()`.
- Getting frame width and height from camera properties.
- Creating a video writer using `cv2.VideoWriter()`.
- Choosing a codec using `cv2.VideoWriter_fourcc()`.
- Saving webcam output as a video file.

### Files implemented

- `using_cap.py`: Opens the webcam and displays live camera feed.
- `saving_video.py`: Records webcam video and saves it as `my_video.avi`.

### Output generated

- `my_video.avi`

### Key understanding

OpenCV treats video as a continuous stream of images. Every frame can be processed the same way as a normal image, which is why image processing concepts directly apply to real-time video applications.

## 8. Face, Eye, And Smile Detection

Folder: `Face Detection in OpenCV/`

This is the most advanced section in the current learning progress. It uses Haar cascade classifiers for real-time detection through the webcam.

### What I learned

- Loading Haar cascade classifiers using `cv2.CascadeClassifier()`.
- Using OpenCV's built-in Haar cascade path through `cv2.data.haarcascades`.
- Capturing live webcam frames.
- Converting each frame to grayscale before detection.
- Detecting faces using `detectMultiScale()`.
- Understanding important detection parameters:
  - `scaleFactor`: controls how much the image size is reduced at each scale.
  - `minNeighbors`: controls detection strictness and reduces false positives.
- Drawing face bounding boxes.
- Creating a region of interest, or ROI, inside the detected face.
- Running eye and smile detection only inside the face ROI.
- Showing labels such as `Eyes Detected` and `Smile Detected`.

### Files implemented

- `app.py`: Detects faces in real time using the webcam.
- `face_eye_smile.py`: Detects faces, eyes, and smiles in real time.

### Haar cascade files included

- `haarcascade_frontalface_default.xml`
- `haarcascade_eye.xml`
- `haarcascade_smile.xml`

### Key understanding

Face detection works better when the image is converted to grayscale. After detecting a face, detecting eyes and smiles inside the face area is more efficient and more accurate than scanning the full frame. This also introduced me to the concept of region-based processing.

## Important OpenCV Concepts Learned

### Image as an array

An image is stored as a matrix of pixel values. In OpenCV, this matrix is represented using NumPy arrays.

### BGR color format

OpenCV reads color images in BGR format by default. This is different from the RGB format commonly used in other libraries.

### Grayscale conversion

Many computer vision algorithms work better or faster on grayscale images because they only need intensity information, not full color data.

### Kernel-based operations

Blur and sharpening operations use kernels. A kernel moves across the image and recalculates pixel values based on neighboring pixels.

### Thresholding

Thresholding converts an image into a binary form, which is useful for contour detection and segmentation.

### Contours

Contours represent boundaries of objects. They are useful for detecting shapes, object outlines, and segmented regions.

### Real-time processing

Video processing works by continuously reading frames, processing each frame, displaying the result, and exiting cleanly when required.

### Haar cascade detection

Haar cascades are pre-trained classifiers that can detect objects like faces, eyes, and smiles. They are useful for understanding classical computer vision before moving into deep learning-based detection.

## Practical Outcomes

By completing this learning work, I can now:

- Load, display, inspect, and save images.
- Convert images to grayscale.
- Resize, crop, flip, and rotate images.
- Draw lines, rectangles, circles, and text on images.
- Apply blur and sharpening filters.
- Detect edges using the Canny algorithm.
- Use bitwise operations for mask-like image processing.
- Detect and label contours and simple shapes.
- Capture live webcam video.
- Save webcam recordings.
- Perform real-time face detection.
- Extend face detection to eye and smile detection using ROI-based processing.

## Current Strengths

- The learning is hands-on and file-based, with each concept implemented separately.
- Most scripts include basic image-load validation.
- The folder structure makes topics easy to revise.
- Outputs are saved for visual proof of learning.
- The project has moved from basic image operations to real-time computer vision.

## Areas To Improve Next

The next improvements I plan to make are:

- Rename folders with correct spellings for a cleaner professional structure.
- Add a more detailed `README.md` with setup and run instructions.
- Add comments consistently in all scripts.
- Handle webcam read failures in every real-time script.
- Add command-line arguments instead of hardcoded file paths.
- Build one combined mini project, such as a real-time face detection dashboard.
- Learn color masking using HSV color space.
- Learn object tracking.
- Explore background subtraction and motion detection.
- Compare Haar cascade detection with modern deep learning-based face detection.

## Summary

This project shows my first complete practical pass through OpenCV fundamentals. I covered the full flow from basic image loading to real-time detection. The most important learning was understanding that computer vision is built step by step: first by reading images as arrays, then transforming them, extracting features, identifying regions, and finally applying detection logic on live video frames.

The current codebase demonstrates that I have learned the core OpenCV building blocks and can now start combining them into more useful real-world computer vision applications.
