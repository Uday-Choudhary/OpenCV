"""
Median Blurring is a non-linear filtering technique used to reduce noise in an image. It works by replacing each pixel's value with the median value of the neighboring pixels within a specified kernel size. This method is particularly effective at removing salt-and-pepper noise while preserving edges in the image. The kernel size is typically an odd integer (e.g., 3, 5, 7) that defines the size of the neighborhood considered for calculating the median. The cv2.medianBlur() function in OpenCV can be used to apply median blurring to an image, where the first argument is the input image and the second argument is the kernel size. Median blurring is commonly used in various applications such as image preprocessing, noise reduction, and edge preservation in images.
"""
import cv2
from pathlib import Path

image_path = Path(__file__).parent / "apple.jpg"

image = cv2.imread(str(image_path))

blurred = cv2.medianBlur(image, 15) 

cv2.imshow('Original Image' , image)
cv2.imshow('Blurred Image' , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows() 