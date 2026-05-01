import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))


if image is None:
    print('Image not found')
else:
    print("Image loaded")

    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)  

    cv2.imshow('Original Image', image)
    cv2.imshow('Flipped Horizontal', flipped_horizontal)
    cv2.imshow('Flipped Vertical', flipped_vertical)
    cv2.imshow('Flipped Both', flipped_both)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
