"""
Gaussian Blur is a widely used image processing technique that applies a Gaussian function to blur an image. It is commonly used for reducing noise and detail in an image, creating a smooth and soft effect. The Gaussian function is defined by its mean (center) and standard deviation (spread), which determine the amount of blurring applied to the image. The Gaussian Blur can be applied using the cv2.GaussianBlur() function in OpenCV, which takes the input image, kernel size, and standard deviation as parameters. The kernel size is typically an odd integer (e.g., 3, 5, 7) that defines the size of the Gaussian kernel used for blurring. The standard deviation controls the amount of blurring, with larger values resulting in more blurring. Gaussian Blur is effective in reducing noise while preserving edges, making it a popular choice for various applications such as image smoothing, background blurring, and pre-processing for edge detection.
"""
import cv2
from pathlib import Path

image_path = Path(__file__).parent / "apple.jpg"

image = cv2.imread(str(image_path))

blurred = cv2.GaussianBlur(image , (21, 21) , 5)

cv2.imshow('Original Image' , image)
cv2.imshow('Blurred Image' , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
