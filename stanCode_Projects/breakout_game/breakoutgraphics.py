"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle (bottom of the window)
        self.window_width = window_width
        self.window_height = window_height
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self.paddle = GRect(self.paddle_width, self.paddle_height,
                            x=(self.window_width - self.paddle_width) / 2, y=self.window_height - self.paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(2 * ball_radius, 2 * ball_radius)
        self.ball.filled = True
        self.window.add(self.ball,
                        x=(self.window_width - 2 * ball_radius) / 2, y=(self.window_height - 2 * ball_radius) / 2)

        # Default initial velocity for the ball
        self._dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = self._dx * -1
        self._dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.is_game_start = False
        onmouseclicked(self.m_click)
        onmousemoved(self.m_paddle)

        # Draw bricks
        position_x = 0  # initial brick x-position
        position_y = brick_offset  # initial brick y-position
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        for i in range(brick_rows):  # BRICK_ROWS = 10
            for j in range(brick_cols):  # BRICK_COLS = 10
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick,
                                x=position_x + brick_width * j + brick_spacing * j,
                                y=position_y + brick_height * i + brick_spacing * i)
                if i < 2:  # define bricks color
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif i < 10:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                else:
                    self.brick.fill_color = 'purple'
                    self.brick.color = 'purple'

    def m_paddle(self, m_paddle):
        """
        :param m_paddle: mouse position
        paddle moves with mouse, but paddle stay in the same x-position
        """
        self.paddle.x = m_paddle.x - self.paddle.width / 2
        self.paddle.y = self.window_height - self.paddle_offset
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x >= self.window_width - self.paddle.width:
            self.paddle.x = self.window_width - self.paddle.width

    def m_click(self, mouse):
        """
        :param mouse: mouse click
        let the game start
        """
        if self.ball.x == (self.window_width - 2 * self.ball_radius) / 2 and \
                self.ball.y == (self.window_height - 2 * self.ball_radius) / 2:
            self.is_game_start = True
        else:
            pass

    def check_ball_hit(self, obj):
        """
        :param obj: the object that ball detect
        check the obj is brick or paddle
        """
        if obj is not self.paddle:
            self.window.remove(obj)
        elif obj == self.paddle:
            pass

    def reset_ball(self):
        self.window.add(self.ball, x=(self.window_width - 2 * self.ball_radius) / 2,
                        y=(self.window_height - 2 * self.ball_radius) / 2)
        self.is_game_start = False

    # def brick_not_in_window(self):
    #     brick_is_not_in_window = self.brick is None
    #     return brick_is_not_in_window

    # Getter
    def get_dx(self):
        return self._dx

    def get_dy(self):
        return self._dy
