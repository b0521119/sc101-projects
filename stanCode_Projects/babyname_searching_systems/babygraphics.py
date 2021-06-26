"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    total_width = width - 2 * GRAPH_MARGIN_SIZE
    vertical_line_space = total_width / len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + vertical_line_space * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    for i in range(len(YEARS)):
        x_position = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x_position, 0, x_position, CANVAS_HEIGHT)
        canvas.create_text(x_position + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i]
                           , anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    width_line_space = ((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE) / len(YEARS))
    rank_space = ((CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / 1000)
    color_count = 0
    # find baby_name
    for i in lookup_names:
        year = name_data[str(i)]
        year_count = 0
        pre_x_position = GRAPH_MARGIN_SIZE
        pre_y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
        color = str(COLORS[color_count % len(COLORS)])  # repeat the color
        # find year and get rank value
        for j in YEARS:
            if str(j) not in year:
                beside_text = str(i) + ' *'
                y_position = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
            else:
                beside_text = str(i) + ' ' + str(name_data[str(i)][str(j)])
                rank = int(name_data[str(i)][str(j)])
                y_position = GRAPH_MARGIN_SIZE + (rank_space * rank)
            if year_count != 0:  # draw 11 lines
                canvas.create_line(pre_x_position, pre_y_position, GRAPH_MARGIN_SIZE + (year_count * width_line_space)
                                   , y_position, width=LINE_WIDTH, fill=color)
            pre_x_position = GRAPH_MARGIN_SIZE + (year_count * width_line_space)
            pre_y_position = y_position
            # put the text on
            canvas.create_text(pre_x_position + TEXT_DX,
                               y_position, text=beside_text, anchor=tkinter.SW, fill=color)
            year_count += 1
        color_count += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
