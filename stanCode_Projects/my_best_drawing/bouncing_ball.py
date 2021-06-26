"""
File: bouncing_ball
Name: Jennifer Chueh (4hr)
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5          # x-position velocity
DELAY = 35      # pause time
GRAVITY = 1     # simulate g
SIZE = 20       # ball's diameter
REDUCE = 0.9    # next bouncing height
START_X = 30    # initial x-position
START_Y = 40    # initial x-position

window = GWindow(800, 500, title='bouncing_ball.py')

ball = GOval(SIZE, SIZE)
count_run = 0  # how many runs


def main():
    """
    This program simulates a bouncing ball.
    """
    ball.filled = True
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bouncing_ball)


def bouncing_ball(m):
    global count_run
    vy = 1
    while True:
        ball.move(VX, vy)
        vy = vy + GRAVITY
        if onmouseclicked(click):
            pass
        if ball.y + ball.height >= window.height:
            vy = vy * REDUCE
            vy = vy * -1
        if ball.x - ball.width >= window.width:
            count_run += 1
            break
        # pause (must in the while loop)
        pause(DELAY)
    if count_run == 3:  # third time and stop bouncing
        window.add(ball, x=START_X, y=START_Y)
    else:
        window.add(ball, x=START_X, y=START_Y)
        onmouseclicked(bouncing_ball)


def click(mouse):
    pass














if __name__ == "__main__":
    main()
