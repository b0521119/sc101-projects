"""
File: draw_line.py
Name: Jennifer Chueh (1.5hr)
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20

window = GWindow()
cir = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    """
    onmouseclicked(circle)


def circle(m1):
    """
    first step: show circle at first click
    """
    window.add(cir)
    cir.x = m1.x - SIZE / 2
    cir.y = m1.y - SIZE / 2
    onmouseclicked(draw_line)


def draw_line(m2):
    """
    second step: draw a line and remove the circle
    :param m2:
    """
    line = GLine(cir.x + SIZE / 2, cir.y + SIZE / 2, m2.x, m2.y)  # start point
    window.add(line)
    window.remove(cir)
    onmouseclicked(circle)



if __name__ == "__main__":
    main()
