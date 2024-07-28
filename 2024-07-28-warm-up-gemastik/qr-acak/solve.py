import numpy as np
from PIL import Image

# Load the image
image_path = './gemastik_5.png'
img = Image.open(image_path)

# Convert the image to a numpy array
img_array = np.array(img)

# Get the dimensions of the image
height, width = img_array.shape[:2]

# Create a new array for the shifted image
shifted_img = np.zeros_like(img_array)

# Shift odd rows to the left and even rows to the right
for i in range(height):
    if i % 2 == 0:  # Even row
        shifted_img[i] = np.roll(img_array[i], 5)
    else:  # Odd row
        shifted_img[i] = np.roll(img_array[i], -5)

# Convert the numpy array back to an image
shifted_image = Image.fromarray(shifted_img)

# Save the shifted image
shifted_image.save('shifted_qrcode.png')
