import os
from moviepy.editor import ImageSequenceClip
from PIL import Image
import numpy as np

# Function to create a GIF from a list of images
def create_gif(images, gif_path, fps=10):
    # Load the first image to get its size
    first_image = Image.open(images[0])
    width, height = first_image.size

    # Resize all images to the same size
    images_resized = [Image.open(image).resize((width, height)) for image in images]

    # Convert images to NumPy arrays
    images_np = [np.array(image) for image in images_resized]

    # Create GIF
    clip = ImageSequenceClip(images_np, fps=fps)
    clip.write_gif(gif_path, fps=fps)
    print(f"GIF created at {gif_path}")

# Function to get a list of image files in a directory
def get_image_files(directory):
    image_files = [file for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return sorted(image_files)

# Main function to generate GIF
def main():
    # Set the path to the directory containing images
    image_directory = r"A:\images"

    # Set the output GIF path
    output_gif_path = "output.gif"

    # Get a list of image files in the directory
    image_files = get_image_files(image_directory)

    # Check if there are any image files
    if not image_files:
        print("No image files found in the specified directory.")
        return

    # Create GIF from images
    create_gif([os.path.join(image_directory, image) for image in image_files], output_gif_path)

if __name__ == "__main__":
    main()
