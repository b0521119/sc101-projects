"""
File: blur.py
Name: Jennifer Chueh
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the smiling picture
    :return: blurred image
    """
    blurred = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            red = 0
            green = 0
            blue = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            image_pixel = img.get_pixel(pixel_x, pixel_y)
                            red = red + image_pixel.red
                            green = green + image_pixel.green
                            blue = blue + image_pixel.blue
                            count += 1
            new_pixel = blurred.get_pixel(x, y)
            new_pixel.red = red / count
            new_pixel.green = green / count
            new_pixel.blue = blue / count
    return blurred


def main():
    """
    This program is to let the picture become blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
