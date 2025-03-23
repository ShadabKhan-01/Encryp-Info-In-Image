import numpy as np

def extract_binary_from_pixels(original_pixels, modified_pixels):
    """
    Extracts binary data from the differences between original and modified images.
    """
    original_flat = np.array(original_pixels).reshape(-1, 3)
    modified_flat = np.array(modified_pixels).reshape(-1, 3)

    binary_text = ""

    for i in range(len(original_flat)):
        if (list(modified_flat[i]) == [254, 254, 254] and list(modified_flat[i+1]) == [1, 1, 1]) or (list(original_flat[i]) == [254, 254, 254] and list(original_flat[i+1]) == [1, 1, 1]) :
            break

        original_blue = original_flat[i, 2]
        modified_blue = modified_flat[i, 2]

        # Only mark 1 for ±1 changes in blue channel
        if (modified_blue != original_blue):
            binary_text += "1"
        else:
            binary_text += "0"

    return binary_text


def binary_to_text(binary_string):
    """
    Converts a binary string to its original text.
    """

    # Pad the binary if it's not a multiple of 8
    if len(binary_string) % 8 != 0:
        padding_length = 8 - (len(binary_string) % 8)
        binary_string += "0" * padding_length

    chars = [binary_string[i:i+8] for i in range(0, len(binary_string), 8)]
    
    # Convert binary to characters and ignore bad chunks
    decoded_text = ''.join([chr(int(char, 2)) for char in chars if len(char) == 8])

    return decoded_text
