import os

def split_file(file_path, chunk_size=500*1024*1024):
    file_size = os.path.getsize(file_path)
    with open(file_path, 'rb') as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_file_name = f"{file_path}.part{part_num}"
            with open(part_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            part_num += 1
    os.remove(file_path)

def split_all_files_in_directory(directory, chunk_size=500*1024*1024):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith('.txt'):
            split_file(file_path, chunk_size)

directory_path = "I:/15_6_2567/2"
split_all_files_in_directory(directory_path)
