"""
Canny Edge Detection is a popular edge detection algorithm used in computer vision and image processing. It was developed by John F. Canny in 1986 and is widely used for its ability to detect edges in images while minimizing noise. The Canny Edge Detection algorithm consists of several steps:
1. Noise Reduction: The image is first smoothed using a Gaussian filter to reduce noise.
2. Gradient Calculation: The gradient magnitude and direction are calculated using the Sobel operator.
3. Non-maximum Suppression: The algorithm suppresses pixels that are not part of an edge.
4. Hysteresis Thresholding: Two threshold values are used to identify strong and weak edges. Strong edges are those with gradient magnitudes above the high threshold, while weak edges are those with gradient magnitudes between the low and high thresholds. The algorithm then connects weak edges to strong edges if they are adjacent.
The Canny Edge Detection algorithm is effective in detecting edges while minimizing false positives and is widely used in various applications such as object detection, image segmentation, and feature extraction.
"""
import cv2
from pathlib import Path

image_path = Path(__file__).parent / "flower.jpeg"

image = cv2.imread(str(image_path) , cv2.IMREAD_GRAYSCALE)


edges = cv2.Canny(image , 50 , 150 , )

cv2.imshow('Original Image' , image)
cv2.imshow('Canny Edges' , edges)   
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
90-0 black
130-255 white
180-255 white
50-0 black
"""