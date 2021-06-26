"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_advanced import BreakoutGraphicsAdvanced

FRAME_RATE = 1000 / 120 + 10  # 120 frames per second
NUM_LIVES = 3  # Number of attempts


def main():
    graphics = BreakoutGraphicsAdvanced(brick_cols=5, brick_rows=5)
    lives = NUM_LIVES
    count_brick = 0

    # Add animation loop here!
    vx = graphics.get_dx()
    vy = graphics.get_dy()

    while True:
        if graphics.is_game_start:
            # update
            graphics.ball.move(vx, vy)

        if graphics.ball.y >= graphics.window.height:
            lives -= 1
            if lives > 0:
                graphics.reset_ball()
            else:
                graphics.window.add(graphics.lose, x=(graphics.window.width - graphics.win.width) / 2,
                                    y=((graphics.window.height - graphics.win.width) / 2) + 70)
                break

        # check window width and height
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            vx *= -1
        if graphics.ball.y <= 0:
            vy *= -1

        # check ball hit
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2 * graphics.ball_radius)
        obj4 = graphics.window.get_object_at(graphics.ball.x + 2 * graphics.ball_radius,
                                             graphics.ball.y + 2 * graphics.ball_radius)
        if obj1 is not None:
            if obj1 is not graphics.paddle and obj1 is not graphics.score_board:
                graphics.ball_hit_brick(obj1)
                count_brick += 1
            elif obj1 == graphics.paddle:
                pass
            vy *= -1
        elif obj2 is not None:
            if obj2 is not graphics.paddle and obj2 is not graphics.score_board:
                graphics.ball_hit_brick(obj2)
                count_brick += 1
            elif obj2 == graphics.paddle:
                pass
            vy *= -1
        elif obj3 is not None:
            if obj3 is not graphics.paddle and obj3 is not graphics.score_board:
                graphics.ball_hit_brick(obj3)
                count_brick += 1
            elif obj3 == graphics.paddle:
                pass
            vy *= -1
        elif obj4 is not None:
            if obj4 is not graphics.paddle and obj4 is not graphics.score_board:
                graphics.ball_hit_brick(obj4)
                count_brick += 1
            elif obj4 == graphics.paddle:
                pass
            vy *= -1

        if count_brick == graphics.brick_rows * graphics.brick_cols:
            graphics.window.add(graphics.win, x=(graphics.window.width - graphics.win.width) / 2,
                                y=((graphics.window.height - graphics.win.width) / 2) + 70)
            break

        # pause (must in the while loop)
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
