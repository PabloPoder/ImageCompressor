import os
from PIL import Image # pip install Pyllow 
from tqdm import tqdm # progress bar / pip install tqdm


# The images will be save in the same directory
# Example 'C:/Images/Football/'
imagesFolder = 'C:/Images/'
# Name of the compressed image
ATTACHED_NAME = "compressed_"

FILE_TYPES = [".jpg", ".jpeg", ".png"]


def convert_to_jpeg():
    for input_file in os.listdir(imagesFolder):
        output_file = os.path.splitext(input_file)[0] + ".jpg"
        if input_file != output_file:
            try:
                with Image.open(imagesFolder + input_file) as im:
                    # Create background to fill the .png (can change the color)
                    new_image = Image.new("RGB", (im.width, im.height), color=(255, 255, 255))
                    new_image.paste(im)
                    new_image.save(imagesFolder + output_file)
            except OSError:
                print("❌ Cannot convert: ", input_file)
        
    
def compress_overwrite_file():
    for input_file in tqdm(os.listdir(imagesFolder)):
        name, extension = os.path.splitext(imagesFolder + input_file)
        if extension in FILE_TYPES:
            try:
                with Image.open(imagesFolder + input_file) as im:
                    im.save(imagesFolder + input_file, optimized = True, quality = 60)
            except OSError:
                print("❌ Cannot compress: ", input_file)
    print("Compression complete! ✅")


def compress_renaming_file():
    for input_file in tqdm(os.listdir(imagesFolder)):
        name, extension = os.path.splitext(imagesFolder + input_file)
        if extension in FILE_TYPES:
            try:
                with Image.open(imagesFolder + input_file) as im:
                    im.save(imagesFolder + ATTACHED_NAME + input_file, optimized = True, quality = 60)
            except OSError:
                print("❌ Cannot compress: ", input_file)
    print("Compression complete! ✅")


# convert_to_jpeg()
# compress_overwrite_file()
# compress_renaming_file()