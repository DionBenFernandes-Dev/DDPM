import os
import shutil
from math import ceil

def split_images_into_subfolders(source_folder, num_subfolders=11):
    # Get all image files from the source folder
    image_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Calculate the number of images per subfolder
    num_images = len(image_files)
    images_per_subfolder = ceil(num_images / num_subfolders)
    
    # Create subfolders and distribute images
    for i in range(num_subfolders):
        subfolder_path = os.path.join(source_folder, str(i))
        os.makedirs(subfolder_path, exist_ok=True)
        
        # Get the slice of images for this subfolder
        start_index = i * images_per_subfolder
        end_index = min(start_index + images_per_subfolder, num_images)
        for image in image_files[start_index:end_index]:
            src_path = os.path.join(source_folder, image)
            dst_path = os.path.join(subfolder_path, image)
            shutil.move(src_path, dst_path)

    print(f"Images have been split into {num_subfolders} subfolders equally.")

# Example usage
source_folder = 'data/cifar10/train/train'
split_images_into_subfolders(source_folder)
