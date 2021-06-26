"""
File: my_drawing
Name: Jennifer Chueh
----------------------
This file uses campy module to
draw on a GWindow object
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    This program is to draw the ceramic tile in my house.
    """
    window = GWindow(width=500, height=500, title='my_drawing')

    label = GLabel('【Under the Sea】', x=260, y=50)
    label.font = 'Times New Roman-25'
    label.color = 'navy'
    window.add(label)
    label1 = GLabel('Wish everyone be safe', x=292, y=80)
    label1.font = 'Times New Roman-15'
    window.add(label1)

    circle_mid = GOval(180, 180, x=230, y=120)  # mid fish
    circle_mid.filled = True
    circle_mid.fill_color = 'yellow green'
    circle_mid.color = 'yellow green'
    window.add(circle_mid)
    eye_outside_mid = GOval(40, 40, x=235, y=193)
    eye_outside_mid.filled = True
    eye_outside_mid.fill_color = 'white'
    eye_outside_mid.color = 'white'
    window.add(eye_outside_mid)
    eye_inside_mid = GOval(30, 30, x=238, y=198)
    eye_inside_mid.filled = True
    eye_inside_mid.fill_color = 'yellow green'
    eye_inside_mid.color = 'yellow green'
    window.add(eye_inside_mid)

    circle_big = GOval(230, 230, x=125, y=240)  # big fish
    circle_big.filled = True
    circle_big.fill_color = 'green'
    circle_big.color = 'green'
    window.add(circle_big)
    eye_outside_big = GOval(60, 60, x=130, y=330)
    eye_outside_big.filled = True
    eye_outside_big.fill_color = 'white'
    eye_outside_big.color = 'white'
    window.add(eye_outside_big)
    eye_inside_big = GOval(50, 50, x=133, y=335)
    eye_inside_big.filled = True
    eye_inside_big.fill_color = 'green'
    eye_inside_big.color = 'green'
    window.add(eye_inside_big)

    circle_small = GOval(50, 50, x=30, y=40)  # small fish
    circle_small.filled = True
    circle_small.fill_color = 'lime'
    circle_small.color = 'lime'
    window.add(circle_small)
    eye_outside_small = GOval(14, 14, x=35, y=58)
    eye_outside_small.filled = True
    eye_outside_small.fill_color = 'white'
    eye_outside_small.color = 'white'
    window.add(eye_outside_small)
    eye_inside_small = GOval(10, 10, x=36, y=60)
    eye_inside_small.filled = True
    eye_inside_small.fill_color = 'lime'
    eye_inside_small.color = 'lime'
    window.add(eye_inside_small)

    triangle_mid = GPolygon()  # mid fish tail
    triangle_mid.add_vertex((410, 220))
    triangle_mid.add_vertex((460, 170))
    triangle_mid.add_vertex((460, 270))
    triangle_mid.filled = True
    triangle_mid.fill_color = 'tan'
    triangle_mid.color = 'tan'
    window.add(triangle_mid)

    triangle_big = GPolygon()  # big fish tail
    triangle_big.add_vertex((355, 365))
    triangle_big.add_vertex((435, 285))
    triangle_big.add_vertex((435, 445))
    triangle_big.filled = True
    triangle_big.fill_color = 'darkslategrey'
    triangle_big.color = 'darkslategrey'
    window.add(triangle_big)

    triangle_small = GPolygon()  # small fish tail
    triangle_small.add_vertex((81, 66))
    triangle_small.add_vertex((101, 46))
    triangle_small.add_vertex((101, 86))
    triangle_small.filled = True
    triangle_small.fill_color = 'coral'
    triangle_small.color = 'coral'
    window.add(triangle_small)

    fin_big = GPolygon()  # big fish fin
    fin_big.add_vertex((240, 360))
    fin_big.add_vertex((290, 335))
    fin_big.add_vertex((290, 385))
    fin_big.filled = True
    fin_big.fill_color = 'darkslategrey'
    fin_big.color = 'black'
    window.add(fin_big)
    fin_line1_big = GLine(240, 360, 275, 350)
    window.add(fin_line1_big)
    fin_line2_big = GLine(240, 360, 280, 360)
    window.add(fin_line2_big)
    fin_line3_big = GLine(240, 360, 275, 370)
    window.add(fin_line3_big)

    fin_mid = GPolygon()  # mid fish fin
    fin_mid.add_vertex((320, 213))
    fin_mid.add_vertex((350, 198))
    fin_mid.add_vertex((350, 228))
    fin_mid.filled = True
    fin_mid.fill_color = 'tan'
    fin_mid.color = 'black'
    window.add(fin_mid)
    fin_line1_mid = GLine(320, 213, 343, 213)
    window.add(fin_line1_mid)
    fin_line2_mid = GLine(320, 213, 340, 208)
    window.add(fin_line2_mid)
    fin_line3_mid = GLine(320, 213, 340, 218)
    window.add(fin_line3_mid)

    fin_small = GPolygon()  # small fish fin
    fin_small.add_vertex((58, 65))
    fin_small.add_vertex((68, 60))
    fin_small.add_vertex((68, 70))
    fin_small.filled = True
    fin_small.fill_color = 'coral'
    fin_small.color = 'black'
    window.add(fin_small)
    fin_line1_small = GLine(58, 65, 66, 65)
    window.add(fin_line1_small)
    fin_line2_small = GLine(58, 65, 66, 63)
    window.add(fin_line2_small)
    fin_line3_small = GLine(58, 65, 66, 67)
    window.add(fin_line3_small)

    bub_big1 = GOval(20, 20, x=90, y=330)  # big fish bubbles
    bub_big1.filled = True
    bub_big1.fill_color = 'skyblue'
    bub_big1.color = 'skyblue'
    window.add(bub_big1)
    bub_big2 = GOval(35, 35, x=70, y=285)
    bub_big2.filled = True
    bub_big2.fill_color = 'skyblue'
    bub_big2.color = 'skyblue'
    window.add(bub_big2)

    bub_mid1 = GOval(15, 15, x=205, y=195)  # mid fish bubbles
    bub_mid1.filled = True
    bub_mid1.fill_color = 'skyblue'
    bub_mid1.color = 'skyblue'
    window.add(bub_mid1)
    bub_mid2 = GOval(25, 25, x=192, y=163)
    bub_mid2.filled = True
    bub_mid2.fill_color = 'skyblue'
    bub_mid2.color = 'skyblue'
    window.add(bub_mid2)

    bub_small1 = GOval(8, 8, x=18, y=53)  # small fish bubbles
    bub_small1.filled = True
    bub_small1.fill_color = 'skyblue'
    bub_small1.color = 'skyblue'
    window.add(bub_small1)
    bub_small2 = GOval(12, 12, x=11, y=37)
    bub_small2.filled = True
    bub_small2.fill_color = 'skyblue'
    bub_small2.color = 'skyblue'
    window.add(bub_small2)







if __name__ == '__main__':
    main()
