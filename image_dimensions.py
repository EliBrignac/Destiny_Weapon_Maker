import os
from PIL import Image
img_path = r"images\2a2a95b819312fc6fef728911cfd6fa2.jpg"
img = Image.open(img_path)
img_shape = img.size
print(f"Image:  - Shape: {img_shape}")