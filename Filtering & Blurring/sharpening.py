import cv2
import numpy as np
from pathlib import Path

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