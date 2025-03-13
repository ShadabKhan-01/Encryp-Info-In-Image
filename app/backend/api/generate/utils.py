import numpy as np

def manipulate_pixels(rgb_pixels, binary_text):
    """
    Manipulates the RGB values of an image based on a binary string.

    - If the binary value is 1, modify the RGB value:
        - If the value is 255, decrease by 1.
        - Otherwise, increase by 1.
    - If the binary value is 0, keep the pixel unchanged.
    - At the end, mark the end of manipulation with [254, 254, 254].

    Parameters:
        rgb_pixels (list): A 3D list representing the RGB values of an image.
        binary_text (str): A binary string to use for manipulation.

    Returns:
        list: The manipulated RGB pixel array.
    """

    binary_length = len(binary_text)  # Total binary bits
    pixels_needed = binary_length // 3  # Number of pixels needed

    # Flatten the 3D list into a 1D list of RGB values for easy manipulation
    flat_pixels = np.array(rgb_pixels).reshape(-1, 3)

    # Modify pixel values based on binary text
    binary_index = 0  # Track binary text position
    for i in range(pixels_needed):
        for j in range(3):  # Iterate over R, G, B values
            if binary_index < binary_length and binary_text[binary_index] == '1':
                if flat_pixels[i, j] == 255:
                    flat_pixels[i, j] -= 1
                else:
                    flat_pixels[i, j] += 1
            # Move to the next binary value
            binary_index += 1

    # Mark the end of manipulation with a special flag (R=254, G=254, B=254)
    if pixels_needed < len(flat_pixels):  # Ensure we don't go out of bounds
        flat_pixels[pixels_needed] = [254, 254, 254]

    # Reshape back to original image dimensions
    manipulated_pixels = flat_pixels.reshape(np.array(rgb_pixels).shape)
    
    return manipulated_pixels
