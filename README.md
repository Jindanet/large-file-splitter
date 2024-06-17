# Large File Splitter

Large File Splitter is a Python utility to split large text files into smaller parts. It is particularly useful for managing large text files that need to be split into smaller chunks for easier handling and processing.

## Features

- Split large text files into smaller parts of specified size.
- Automatically delete the original large file after splitting.
- Handles files ranging from 1GB to 4GB efficiently.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/jindanet/large-file-splitter.git
    cd large-file-splitter
    ```

2. Install any required dependencies (if applicable).

## Usage

1. Place your large text files in the target directory (e.g., `I:/15_6_2567/2`).
2. Modify the `directory_path` variable in the script to point to your target directory.
3. Run the script:

    ```bash
    python split_files.py
    ```

## Example

```python
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
