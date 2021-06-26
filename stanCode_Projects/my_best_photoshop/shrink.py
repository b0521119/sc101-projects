"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: img, which become half-sized
    """
    img = SimpleImage(filename)
    half_img = SimpleImage.blank(img.width // 2, img.height // 2)

    for x in range(0, img.width, 2):       # 0, 2, 4, 6...
        for y in range(0, img.height, 2):  # 0, 2, 4, 6...
            pixel = img.get_pixel(x, y)
            half_pixel = half_img.get_pixel(x//2, y//2)  # 0, 1, 2, 3...

            half_pixel.red = pixel.red
            half_pixel.green = pixel.green
            half_pixel.blue = pixel.blue

    return half_img


def main():
    """
    This program is to let the image be half width and half height from the origin.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
