
#!/usr/bin/env python3
from PIL import Image
import glob
import os

size = 600, 400

for image in os.listdir('./supplier-data/images/'):
    if image.endswith('.tiff'):
        # Open the file
        img = Image.open(os.path.join(
            './supplier-data/images/', image))
        # Get the file directory
        file, ext = os.path.splitext(image)
        # Resize the image from 3000x2000 to 600x400
        img_resized = img.resize(size)
        # Change the image mode from P(palettised) to RGB
        img_resized.convert('RGB').save(
            './supplier-data/images/' + file + ".jpeg", "JPEG")
