import numpy as np
from PIL import Image
import os
import math

def file_to_binary(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def binary_to_image(binary_data, output_image_path):
    byte_arr = np.frombuffer(binary_data, dtype=np.uint8)
    length = len(byte_arr)

    # Calculate width and height
    width = math.ceil(math.sqrt(length / 3))
    height = math.ceil(length / (3 * width))
    
    padding_size = (width * height * 3 - length) % (width * height * 3)
    if padding_size > 0:
        byte_arr = np.pad(byte_arr, (0, padding_size), constant_values=0)
    
    byte_arr = byte_arr.reshape((height, width, 3))
    img = Image.fromarray(byte_arr, 'RGB')
    img.save(output_image_path)

def image_to_binary(image_path):
    img = Image.open(image_path)
    byte_arr = np.array(img).flatten()
    return byte_arr.tobytes()