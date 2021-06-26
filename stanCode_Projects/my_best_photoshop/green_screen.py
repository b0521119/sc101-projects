"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, the green screen pixels are replaced by pixels of background image
    """

    for x in range(background_img.width):
        for y in range(background_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)

            if figure_pixel.green > bigger * 2:
                back_pixel = background_img.get_pixel(x, y)
                figure_pixel.red = back_pixel.red
                figure_pixel.green = back_pixel.green
                figure_pixel.blue = back_pixel.blue

    return figure_img


def main():
    """
    This function conducts green screen replacement
    which is able to photoshop a person onto any background
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
