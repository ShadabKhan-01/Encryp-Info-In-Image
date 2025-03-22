import numpy as np

def extract_binary_from_pixels(original_pixels, modified_pixels):
    """
    Extracts binary data from the differences between original and modified images.

    - Only checks the blue (B) value of each pixel.
    - If the modified blue value is:
        - Increased by 1 → Binary '1'
        - Decreased by 1 → Binary '1'
        - Same as original → Binary '0'
    - Stops when encountering the end marker [254, 254, 254].

    Parameters:
        original_pixels (list): Original 3D list representing the RGB values.
        modified_pixels (list): Modified 3D list with manipulated blue values.

    Returns:
        str: The extracted binary string.
    """

    # Flatten the 3D pixel arrays to 1D for easy comparison
    original_flat = np.array(original_pixels).reshape(-1, 3)
    modified_flat = np.array(modified_pixels).reshape(-1, 3)

    binary_text = ""

    for i in range(len(original_flat)):
        # Check for the end marker
        if list(modified_flat[i]) == [254, 254, 254]:
            break

        # Compare only the blue value (index 2)
        original_blue = original_flat[i, 2]
        modified_blue = modified_flat[i, 2]

        # If blue value is modified, add '1', otherwise add '0'
        if modified_blue != original_blue:
            binary_text += "1"
        else:
            binary_text += "0"

    return binary_text

def binary_to_text(binary_string):
    """
    Converts a binary string to its original text.

    - Groups the binary string into 8-bit chunks.
    - Converts each 8-bit chunk to a character using ASCII.

    Parameters:
        binary_string (str): The binary string to convert.

    Returns:
        str: The decoded text.
    """

    # Split the binary string into 8-bit chunks
    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]

    # Convert each 8-bit chunk to a character and join to form the original text
    decoded_text = ''.join([chr(int(char, 2)) for char in chars if len(char) == 8])

    return decoded_text
