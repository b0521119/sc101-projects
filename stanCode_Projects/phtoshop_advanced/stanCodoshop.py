"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

Let the picture become a beautiful scenery without any people.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    dist_red = (red - pixel.red) ** 2
    dist_green = (green - pixel.green) ** 2
    dist_blue = (blue - pixel.blue) ** 2
    dist = (dist_red + dist_green + dist_blue) ** 0.5  # ** 0.5 present開根號
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixel_red = 0
    for pixel in pixels:
        pixel_red += pixel.red
    avg_red = pixel_red // len(pixels)

    pixel_green = 0
    for pixel in pixels:
        pixel_green += pixel.green
    avg_green = pixel_green // len(pixels)

    pixel_blue = 0
    for pixel in pixels:
        pixel_blue += pixel.blue
    avg_blue = pixel_blue // len(pixels)

    rgb = [avg_red, avg_green, avg_blue]  # create a list to put avg rgb
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    avg_rgb = get_average(pixels)  # Get a list [avg_red, avg_green, avg_blue]

    first_pixel_dist = get_pixel_dist(pixels[0], avg_rgb[0], avg_rgb[1], avg_rgb[2])
    small_dist = first_pixel_dist
    ans = pixels[0]

    for pixel in pixels[1:]:
        pixel_dist = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])
        if pixel_dist < small_dist:
            small_dist = pixel_dist
            ans = pixel
    return ans


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):  # (x, y) position from (0, 0) to (width-1, height-1)
        for y in range(height):
            result_pixel = result.get_pixel(x, y)
            pixel_list = []  # create a list to put the pixels which are in the same position in different pictures

            for img in images:  # find the same position in different pictures
                img_pixel = img.get_pixel(x, y)
                pixel_list.append(img_pixel)

            best = get_best_pixel(pixel_list)
            result_pixel.red = best.red
            result_pixel.green = best.green
            result_pixel.blue = best.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
