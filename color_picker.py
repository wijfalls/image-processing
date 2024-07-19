from PIL import Image

def get_pixel_color(image_path):
    try:
        # Open the image file
        image = Image.open(image_path)
        
        # Get the pixel color of the first pixel (top-left corner)
        pixel_color = image.getpixel((0, 0))
        
        # Return the RGB values of the pixel color
        return pixel_color
    except Exception as e:
        return None

# Provide the path to your image file here
image_path = 'img.jpg'

# Call the function and print the result
result = get_pixel_color(image_path)

if result is not None:
    print(f"Pixel color at (0, 0): {result}")
else:
    print("Failed to open the image or retrieve the pixel color.")
