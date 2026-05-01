"""
1- cv2.bitwise_and() - Performs a bitwise AND operation between two images. It takes two images as input and produces an output image where each pixel is the result of a logical AND operation between the corresponding pixels of the input images.
2- cv2.bitwise_or() - Performs a bitwise OR operation between two images. It takes two images as input and produces an output image where each pixel is the result of a logical OR operation between the corresponding pixels of the input images.
3- cv2.bitwise_xor() - Performs a bitwise XOR operation between two images. It takes two images as input and produces an output image where each pixel is the result of a logical XOR operation between the corresponding pixels of the input images.
4- cv2.bitwise_not() - Performs a bitwise NOT operation on an image. It takes a single image as input and produces an output image where each pixel is the result of a logical NOT operation on the corresponding pixel of the input image.
"""

'''
img1 img2 height width same hote hain
use only black and white images'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

cv2.circle(img1, (150, 150), 80, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)

bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not = cv2.bitwise_not(img1)

titles = ["Circle", "Rectangle", "AND", "OR", "XOR", "NOT"]
images = [img1, img2, bitwise_and, bitwise_or, bitwise_xor, bitwise_not]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], cmap='gray')
    plt.title(titles[i])
    plt.axis("off")

plt.show()
