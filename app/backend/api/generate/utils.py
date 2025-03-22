from PIL import Image
import numpy as np
from io import BytesIO
import base64

def manipulate_pixels(rgb_pixels, binary_text):
    """
    Manipulates only the blue (B) value of each pixel based on a binary string.

    - If the binary value is 1, modify the blue value:
        - If the blue value is 255, decrease by 1.
        - Otherwise, increase by 1.
    - If the binary value is 0, keep the blue value unchanged.
    - At the end, mark the end of manipulation with [254, 254, 254].

    Parameters:
        rgb_pixels (list): A 3D list representing the RGB values of an image.
        binary_text (str): A binary string to use for manipulation.

    Returns:
        list: The manipulated RGB pixel array.
    """

    binary_length = len(binary_text)  # Total binary bits
    pixels_needed = binary_length  # 1 bit modifies 1 blue value

    # Flatten the 3D list into a 1D list of RGB values for easy manipulation
    flat_pixels = np.array(rgb_pixels).reshape(-1, 3)

    # Modify only the blue value of each pixel based on binary text
    for i in range(min(pixels_needed, len(flat_pixels))):  # Limit to available pixels
        if binary_text[i] == '1':
            if flat_pixels[i, 2] == 255:  # Blue value at index 2
                flat_pixels[i, 2] -= 1
            else:
                flat_pixels[i, 2] += 1
        # Move to the next bit and next pixel

    # Mark the end of manipulation with a special flag (R=254, G=254, B=254)
    if pixels_needed < len(flat_pixels):  # Check bounds
        flat_pixels[pixels_needed] = [254, 254, 254]

    # Reshape back to original image dimensions
    manipulated_pixels = flat_pixels.reshape(np.array(rgb_pixels).shape)
    
    return manipulated_pixels



def save_image(modified_pixels):
    """
    Converts modified pixel array back to image and returns it as a base64 string.
    
    Parameters:
        modified_pixels (list): 3D list of modified RGB pixel values.

    Returns:
        str: Base64 encoded image data.
    """
    modified_array = np.array(modified_pixels, dtype=np.uint8)
    img = Image.fromarray(modified_array)
    
    # Save image to a BytesIO object
    img_buffer = BytesIO()
    img.save(img_buffer, format="PNG")
    
    # Encode image as base64 string for easy transfer
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    
    return img_base64