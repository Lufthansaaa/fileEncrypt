import os

def calculate_chunk_size_by_percentage(file_path, percentage):
    file_size = os.path.getsize(file_path)
    chunk_size = int(file_size * percentage)
    return chunk_size

# Example usage:
file_path = 'exe.exe'
percentage = 0.1  # 10% of the file size
chunk_size = calculate_chunk_size_by_percentage(file_path, percentage)
print(f"Calculated chunk size for {percentage * 100}% of file size: {chunk_size} bytes")
