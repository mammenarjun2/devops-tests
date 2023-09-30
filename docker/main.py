
# modules used to work with files and process to run commands against them

import os
import subprocess

image_path = '/app/images/' # docker file path for images

def calculate_hash(image_path):

# using subprocess function to run perl script and capture output

    process = subprocess.Popen(['perl', 'phash.pl', image_path], stdout=subprocess.PIPE)
    output, _ = process.communicate() # filtering hashes
    hash_value = output.strip().decode() # decoded value
    return hash_value
    
# Intially couldn't iterate over multiple images with phash.pl
# So i created loop below to iterate over images folder and list all hashes. 
def process_images(image_path):
    duplicate_image_hashes = {}  

    print(f"---Printing & checking duplicate hashes from images---")

    for root, _, files in os.walk(image_path):
        for file in files:
            file_path = os.path.join(root, file)
            image_hash = calculate_hash(file_path) # helper subprocess function used to iterate hashes & images
            print(f"Image: {file_path}, Hash: {image_hash}")

            
            if image_hash in duplicate_image_hashes:
                print(f"Duplicate found: {file_path}, Hash: {image_hash}")
                os.remove(file_path)
            else:
                duplicate_image_hashes[image_hash] = file_path

    print(f"---Duplicate hashes removed from images folder---")        
process_images(image_path)                   

