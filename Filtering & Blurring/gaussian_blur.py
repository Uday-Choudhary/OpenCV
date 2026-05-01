import cv2
from pathlib import Path

image_path = Path(__file__).parent / "apple.jpg"

image = cv2.imread(str(image_path))

blurred = cv2.GaussianBlur(image , (21, 21) , 5)

cv2.imshow('Original Image' , image)
cv2.imshow('Blurred Image' , blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
