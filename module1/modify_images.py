#!/usr/bin/env python3
from PIL import Image
import glob
import os

size = 128, 128  # new size

# Iterate through each file in the current directory
for infile in glob.glob("ic_*"):
    # Get the file directory
    file, ext = os.path.splitext(infile)
    # Open the file
    img = Image.open(infile)
    # Rotate the image
    img.rotate(270)
    # Resize the image from 192x192 to 128x128
    img_resized = img.resize(size)
    # Change the image mode from P(palettised) to RGB
    # Have a look https://stackoverflow.com/questions/52307290/what-is-the-difference-between-images-in-p-and-l-mode-in-pil
    img_resized.convert('RGB').save("/opt/icons/" + file + ".jpeg", "JPEG")
