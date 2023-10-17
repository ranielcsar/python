from PIL import Image, ImageOps
import os

screen_sizes = {
    "small": (320, 320),
    "medium": (768, 768),
    "large": (1024, 1024),
    "extra_large": (1440, 1440),
}


def resize_images_to_screen_sizes(image_src: str, extension: str):
    # abre a imagem
    image = Image.open(image_src)

    # retorna um tuple ('nome do arquivo', 'extensão')
    filename = os.path.splitext(image.filename)[0]

    # modo de cores para conversão
    image = image.convert("RGB")

    # cria pasta no mesmo diretório com o nome do arquivo
    create_images_folder(f"./{filename}")

    # redimensiona usando os valores de 'screen_sizes' e salva na pasta criada
    for [key, value] in screen_sizes.items():
        ImageOps.cover(image, value).save(f"./{filename}/{key}.{extension}")

    print("\n### converted successfully ###")
    print(f"\n### see the folder with name: {filename}\n")


def create_images_folder(name: str):
    return os.mkdir(name)


img_src = input("Enter image source: ")
new_extension = input("Enter EXTENSION to convert to (webp, jpeg): ")
resize_images_to_screen_sizes(img_src, new_extension)
