"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return: img, which become upside-down
    """
    img = SimpleImage(filename)
    reflect_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            reflect_pixel1 = reflect_img.get_pixel(x, y)
            reflect_pixel2 = reflect_img.get_pixel(x, reflect_img.height-1-y)

            reflect_pixel1.red = pixel.red
            reflect_pixel1.green = pixel.green
            reflect_pixel1.blue = pixel.blue

            reflect_pixel2.red = pixel.red
            reflect_pixel2.green = pixel.green
            reflect_pixel2.blue = pixel.blue

    return reflect_img


def main():
    """
    TODO: This program is to let the img become upside-down
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()



if __name__ == '__main__':
    main()
