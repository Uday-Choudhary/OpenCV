import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))



if image is not None:
    print("Image loaded")
    cv2.imshow('Window Title', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Not loaded")
