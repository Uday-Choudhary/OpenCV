import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))
print(image)
if image is None:
    print("Not loaded")
else:
    print("Image loaded successful")



