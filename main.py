import os
import hashlib
from collections import defaultdict
import argparse
import time


def get_file_hash(file_path):
    """Generate the MD5 hash of a file's content."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()


def find_duplicate_files(directory_path):
    duplicate_files = defaultdict(list)

    for path_from_root, _, files in os.walk(directory_path):
        for filename in files:
            file_path = os.path.join(path_from_root, filename)
            if os.path.isfile(file_path):
                file_hash = get_file_hash(file_path)
                duplicate_files[file_hash].append(file_path)

    for hash_val, file_paths in duplicate_files.items():
        if len(file_paths) > 1:
            print("Duplicate files:", ", ".join(file_paths))


if __name__ == '__main__':
    startTime = time.time()
    parser = argparse.ArgumentParser(description="Find duplicate files in a directory.")
    parser.add_argument('--directory_path', type=str, help='Path to the directory to scan for duplicates')
    args = parser.parse_args()
    find_duplicate_files(args.directory_path)
    executionTime = (time.time() - startTime)
    print('Execution time in seconds: ' + str(executionTime))
