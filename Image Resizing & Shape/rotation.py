import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print('Image not found')
else:
    print('Image Loaded')
    (h,w) = image.shape[:2]

    center = (w//2 , h//2)
    # Rotate the image by 45 degrees
    M = cv2.getRotationMatrix2D(center , 45 , 1.0)
    # Perform the rotation
    rotated = cv2.warpAffine(image , M , (w,h))

    cv2.imshow('Original Image' , image)
    cv2.imshow('Rotated Image' , rotated)
    cv2.imwrite('rotated-minion.png' , rotated)
    cv2.waitKey()
    cv2.destroyAllWindows()
