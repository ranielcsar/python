from PIL import Image, ImageOps
import os

screen_sizes = {"small": (250, 250), "medium": (500, 500), "large": (750, 750)}


def resize_images_to_screen_sizes(image_src: Image):
    images = []
    image = Image.open(image_src)
    filename = os.path.splitext(image_src.filename)[0]
    image = image.convert("RGB")

    for [key, value] in screen_sizes.items():
        newImage = ImageOps.cover(image, value)
        images.append({key: newImage})

    return images
