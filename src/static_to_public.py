import os
import shutil

def copy_directory_recursive(src, dst):
    """
    Recursively copies contents from src to dst after cleaning the destination.

    :param src: Source directory path
    :param dst: Destination directory path
    """
    # Check if source directory exists
    if not os.path.exists(src):
        print(f"[ERROR] Source directory '{src}' does not exist.")
        return

    # Clean the destination directory if it exists
    if os.path.exists(dst):
        print(f"[INFO] Deleting contents of destination directory '{dst}'.")
        shutil.rmtree(dst)
    os.mkdir(dst)  # Create a fresh destination directory

    # Iterate through the source directory's contents
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        # If it's a directory, copy recursively
        if os.path.isdir(src_path):
            print(f"[INFO] Copying directory: {src_path} -> {dst_path}")
            copy_directory_recursive(src_path, dst_path)
        else:
            # If it's a file, copy the file
            print(f"[INFO] Copying file: {src_path} -> {dst_path}")
            shutil.copy(src_path, dst_path)

