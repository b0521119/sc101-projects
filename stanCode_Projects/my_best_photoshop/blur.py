"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: str, the file path of the original image
    :return: img, which become blurred
    """
    # img = SimpleImage(img)
    blur_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            img_pixel = img.get_pixel(x, y)
            blur_pixel = blur_img.get_pixel(x, y)

            if x == 0 and y == 0:
                pixel1 = img.get_pixel(x + 1, y)
                pixel2 = img.get_pixel(x, y + 1)
                pixel3 = img.get_pixel(x + 1, y + 1)

                new_red0 = (pixel1.red + pixel2.red + pixel3.red) // 3
                new_green0 = (pixel1.green + pixel2.green + pixel3.green) // 3
                new_blue0 = (pixel1.blue + pixel2.blue + pixel3.blue) // 3

                blur_pixel.red = new_red0
                blur_pixel.green = new_green0
                blur_pixel.blue = new_blue0
            elif x == img.width and y == 0:
                pixel4 = img.get_pixel(x - 1, y)
                pixel5 = img.get_pixel(x - 1, y + 1)
                pixel6 = img.get_pixel(x, y + 1)

                new_red1 = (pixel4.red + pixel5.red + pixel6.red) // 3
                new_green1 = (pixel4.green + pixel5.green + pixel6.green) // 3
                new_blue1 = (pixel4.blue + pixel5.blue + pixel6.blue) // 3

                blur_pixel.red = new_red1
                blur_pixel.green = new_green1
                blur_pixel.blue = new_blue1
            elif x == 0 and y == img.height:
                pixel7 = img.get_pixel(x + 1, y)
                pixel8 = img.get_pixel(x, y - 1)
                pixel9 = img.get_pixel(x + 1, y - 1)

                new_red2 = (pixel7.red + pixel8.red + pixel9.red) // 3
                new_green2 = (pixel7.green + pixel8.green + pixel9.green) // 3
                new_blue2 = (pixel7.blue + pixel8.blue + pixel9.blue) // 3

                blur_pixel.red = new_red2
                blur_pixel.green = new_green2
                blur_pixel.blue = new_blue2
            elif x == img.width and y == img.height:
                pixel10 = img.get_pixel(x - 1, y)
                pixel11 = img.get_pixel(x - 1, y - 1)
                pixel12 = img.get_pixel(x, y - 1)

                new_red3 = (pixel10.red + pixel11.red + pixel12.red) // 3
                new_green3 = (pixel10.green + pixel11.green + pixel12.green) // 3
                new_blue3 = (pixel10.blue + pixel11.blue + pixel12.blue) // 3

                blur_pixel.red = new_red3
                blur_pixel.green = new_green3
                blur_pixel.blue = new_blue3
            elif 0 < x < img.width-1 and y == 0:
                pixel13 = img.get_pixel(x - 1, y)
                pixel14 = img.get_pixel(x + 1, y)
                pixel15 = img.get_pixel(x - 1, y + 1)
                pixel16 = img.get_pixel(x, y + 1)
                pixel17 = img.get_pixel(x + 1, y + 1)

                new_red4 = (pixel13.red + pixel14.red + pixel15.red + pixel16.red + pixel17.red) // 5
                new_green4 = (pixel13.green + pixel14.green + pixel15.green + pixel16.green + pixel17.green) // 5
                new_blue4 = (pixel13.blue + pixel14.blue + pixel15.blue + pixel16.blue + pixel17.blue) // 5

                blur_pixel.red = new_red4
                blur_pixel.green = new_green4
                blur_pixel.blue = new_blue4
            elif x == 0 and 0 < y < img.height-1:
                pixela = img.get_pixel(x + 1, y)
                pixelb = img.get_pixel(x, y - 1)
                pixelc = img.get_pixel(x + 1, y - 1)
                pixeld = img.get_pixel(x, y + 1)
                pixele = img.get_pixel(x + 1, y + 1)

                new_red5 = (pixela.red + pixelb.red + pixelc.red + pixeld.red + pixele.red) // 5
                new_green5 = (pixela.green + pixelb.green + pixelc.green + pixeld.green + pixele.green) // 5
                new_blue5 = (pixela.blue + pixelb.blue + pixelc.blue + pixeld.blue + pixele.blue) // 5

                blur_pixel.red = new_red5
                blur_pixel.green = new_green5
                blur_pixel.blue = new_blue5
            elif x == img.width and 0 < y < img.height-1:
                pixelf = img.get_pixel(x - 1, y)
                pixelg = img.get_pixel(x - 1, y - 1)
                pixelh = img.get_pixel(x, y - 1)
                pixeli = img.get_pixel(x - 1, y + 1)
                pixelj = img.get_pixel(x, y + 1)

                new_red6 = (pixelf.red + pixelg.red + pixelh.red + pixeli.red + pixelj.red) // 5
                new_green6 = (pixelf.green + pixelg.green + pixelh.green + pixeli.green + pixelj.green) // 5
                new_blue6 = (pixelf.blue + pixelg.blue + pixelh.blue + pixeli.blue + pixelj.blue) // 5

                blur_pixel.red = new_red6
                blur_pixel.green = new_green6
                blur_pixel.blue = new_blue6
            elif 0 < x < img.width-1 and y == img.height:
                pixelk = img.get_pixel(x - 1, y)
                pixell = img.get_pixel(x + 1, y)
                pixelm = img.get_pixel(x - 1, y - 1)
                pixeln = img.get_pixel(x, y - 1)
                pixelo = img.get_pixel(x + 1, y - 1)

                new_red7 = (pixelk.red + pixell.red + pixelm.red + pixeln.red + pixelo.red) // 5
                new_green7 = (pixelk.green + pixell.green + pixelm.green + pixeln.green + pixelo.green) // 5
                new_blue7 = (pixelk.blue + pixell.blue + pixelm.blue + pixeln.blue + pixelo.blue) // 5

                blur_pixel.red = new_red7
                blur_pixel.green = new_green7
                blur_pixel.blue = new_blue7
            elif 0 < x < img.width-1 and 0 < y < img.height-1:
                pixel11 = img.get_pixel(x, y)
                pixel22 = img.get_pixel(x - 1, y)
                pixel33 = img.get_pixel(x + 1, y)
                pixel44 = img.get_pixel(x - 1, y - 1)
                pixel55 = img.get_pixel(x, y - 1)
                pixel66 = img.get_pixel(x + 1, y - 1)
                pixel77 = img.get_pixel(x - 1, y + 1)
                pixel88 = img.get_pixel(x, y + 1)
                pixel99 = img.get_pixel(x + 1, y + 1)

                new_red8 = (pixel11.red + pixel22.red + pixel33.red +
                            pixel44.red + pixel55.red + pixel66.red +
                            pixel77.red + pixel88.red + pixel99.red) // 9
                new_green8 = (pixel11.green + pixel22.green + pixel33.green +
                              pixel44.green + pixel55.green + pixel66.green +
                              pixel77.green + pixel88.green + pixel99.green) // 9
                new_blue8 = (pixel11.blue + pixel22.blue + pixel33.blue +
                             pixel44.blue + pixel55.blue + pixel66.blue +
                             pixel77.blue + pixel88.blue + pixel99.blue) // 9

                blur_pixel.red = new_red8
                blur_pixel.green = new_green8
                blur_pixel.blue = new_blue8

    return blur_img


def main():
    """
    This program is to let the image become blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
