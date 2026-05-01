import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))


if image is not None:
    cropped = image[100:400, 100:400]

    cv2.imshow('Original Image' , image)
    cv2.imshow('Cropped Image' , cropped)
    cv2.imwrite('cropped-minion.png' , cropped)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print('Image not found')