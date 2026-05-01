import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is None:
    print('Image not found')
else:
    print("Image loaded")

    cv2.putText(image , "Hello mini  World" , (200,830) , cv2.FONT_HERSHEY_DUPLEX , 1.2 , (0,255,255) , 2)

    cv2.imshow('Adding text over image' , image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()