from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from the disk.
    :param path: The path of the image to load.
    :return: The image data.

    Errorhandling:
    - FileNotFoundError: The file was not found.
    - assert: The file must be a valid JPG or JPEG file.
    - Exception: An unexpected error occurred.
    """
    try:
        assert path.endswith(".jpg") or path.endswith(".jpeg"), \
            "The file must be a valid JPG or JPEG file."
        image = Image.open(path)

        image = image.convert('RGB')
        image_data = np.array(image)

        print(f"The shape of image is: {image_data.shape}")

        print(image_data)

        return image_data
    except AssertionError as e:
        print(f"Error: {e}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
