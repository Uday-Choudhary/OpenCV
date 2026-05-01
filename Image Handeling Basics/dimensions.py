import cv2
from pathlib import Path

image_path = Path(__file__).parent / "minions.jpg"
image = cv2.imread(str(image_path))

if image is not None:
    h,w,c = image.shape
    print(f"Image Loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print('Image not loaded')
