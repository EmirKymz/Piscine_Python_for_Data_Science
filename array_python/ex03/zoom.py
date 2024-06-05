import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
from PIL import Image


def main():
    """
    The main function of the program.
    - Load an image from the disk.
    - Convert the image to grayscale.
    - Slice the image to a specific region.
    - Display the sliced image.
    - Print the new shape of the sliced image.
    """
    try:
        image_data = ft_load("../animal.jpeg")

        if image_data is None:
            return

        image = Image.fromarray(image_data)
        gray_image = image.convert('L')
        gray_image_data = np.array(gray_image)

        zoomed_image = gray_image_data[90:490, 450:850]

        print(f"New shape after slicing: {zoomed_image.shape}")

        print(zoomed_image.reshape(400, 400, 1))

        plt.imshow(zoomed_image, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
