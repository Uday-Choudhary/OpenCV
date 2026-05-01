import cv2
import numpy as np
from pathlib import Path

"""
Sharpening an image is a technique used to enhance the edges and details in an image. It can be achieved using various methods, such as convolution with a sharpening kernel. The sharpening kernel emphasizes the differences between neighboring pixel values, which results in a sharper appearance. One common sharpening kernel is the Laplacian kernel, which can be defined as follows:
[ 0, -1, 0]
[-1, 5, -1]
[ 0, -1, 0]
This kernel works by subtracting the average of the neighboring pixels from the center pixel, which enhances the edges and details in the image. The cv2.filter2D() function in OpenCV can be used to apply the sharpening kernel to an image, where the first argument is the input image, the second argument is the desired depth of the output image (use -1 to keep the same depth), and the third argument is the sharpening kernel. Sharpening can be useful in various applications, such as improving the visibility of features in an image, enhancing textures, and making details more prominent."""

image_path = Path(__file__).parent / "camel.jpg"

image = cv2.imread(str(image_path))

sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5 , -1],
                              [0, -1, 0]])
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

cv2.imshow('Original Image' , image)
cv2.imshow('Sharpened Image' , sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()