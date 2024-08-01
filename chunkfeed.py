import numpy as np
from PIL import Image
import os
from binary import *

def save_image_chunks(image_path, rows_per_chunk):
    img = Image.open(image_path)
    img_data = np.array(img)
    img_mode = img.mode
    img_width = img.width
    img_height = img.height

    chunk_files = []
    for start_row in range(0, img_height, rows_per_chunk):
        end_row = min(start_row + rows_per_chunk, img_height)
        chunk_data = img_data[start_row:end_row, :, :]
        chunk_file_path = f"{os.path.splitext(image_path)[0]}_chunk_{start_row // rows_per_chunk}.png"
        chunk_files.append(chunk_file_path)
        chunk_img = Image.fromarray(chunk_data, mode=img_mode)
        chunk_img.save(chunk_file_path)
    
    return chunk_files

def reconstruct_image_from_chunks(chunk_files, output_image_path):
    chunks = [np.array(Image.open(chunk_file)) for chunk_file in chunk_files]
    img_data = np.vstack(chunks)
    img_mode = Image.open(chunk_files[0]).mode
    reconstructed_img = Image.fromarray(img_data.astype(np.uint8), mode=img_mode)
    reconstructed_img.save(output_image_path)


# Split the image into chunks by rows
rows_per_chunk = 1000  # Define the number of rows per chunk
chunk_files = save_image_chunks('output_image.png', rows_per_chunk)

# Reconstruct the image from the chunks
reconstruct_image_from_chunks(chunk_files, 'reconstructed_from_chunks.png')

# Convert the reconstructed image back to binary
reconstructed_binary_data = image_to_binary('reconstructed_from_chunks.png')
with open('recon.exe', 'wb') as f:
    f.write(reconstructed_binary_data)

