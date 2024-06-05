from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Control the input values as follows:
    - The path must be a string.
    - The path must not be empty.
    - The file must be a .jpeg or .jpg file.

    The function:
    - Loads image from the given path.
    - Converts the image to RGB.
    - Prints the shape of the image.
    - Prints the image as a numpy array.
    - Returns the image as a numpy array.
    """
    try:
        assert isinstance(path, str), \
            "Error: The path must be a string."
        assert path.endswith(".jpeg") or path.endswith(".jpg"), \
            "Error: The file must be a .jpeg, .jpg file."
        assert path != "", \
            "Error: The path cannot be empty."
        image = Image.open(path)

        image = image.convert('RGB')
        image_data = np.array(image)

        print(f"The shape of image is: {image_data.shape}")

        print(image_data)

        return image_data

    except FileNotFoundError:
        print("Error: The file was not found.")
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
