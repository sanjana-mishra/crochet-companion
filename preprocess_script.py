from PIL import Image
import os

def process_images(input_folder):
    # List all files in the input folder
    files = os.listdir(input_folder)
    
    # Counter for naming
    count = 1
    
    # Iterate through the files
    for file_name in files:
        if file_name.endswith('.png'):
            # Open the image
            img_path = os.path.join(input_folder, file_name)
            img = Image.open(img_path)
            
            # Convert the image to RGBA mode if it's not already in RGBA
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Get the alpha channel of the image
            alpha = img.split()[-1]
            
            # Create a new image with a white background
            new_img = Image.new("RGB", img.size, "white")
            new_img.paste(img, (0, 0), alpha)
            
            # Determine the maximum dimension (width or height)
            max_dimension = max(new_img.size)
            
            # Create a square canvas of the maximum dimension
            square_img = Image.new("RGB", (max_dimension, max_dimension), "white")
            paste_position = ((max_dimension - new_img.width) // 2, (max_dimension - new_img.height) // 2)
            square_img.paste(new_img, paste_position)
            
            # Resize the image to 512x512 pixels
            resized_img = square_img.resize((512, 512))
            
            # Generate the new file name
            new_file_name = f'val_{count + 0}.png'
            
            # Save the resized image with the new file name
            resized_img.save(os.path.join(input_folder, new_file_name))
            print(f"Processed {file_name} and saved as {new_file_name}")
            
            # Increment the counter
            count += 1

# Specify input folder
input_folder = '/Users/sanjanamishra/Desktop/757_project/dataset copy/val_gray'

# Process images in the input folder
process_images(input_folder)
