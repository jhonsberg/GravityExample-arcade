"""
Title: Gravity Example
Name: Jonah Honsberger
Date: 11/24/2022 [MM-DD-YYYY]
"""

import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRAVITY = -0.1


class Ball:
   def __init__(self, position_x, position_y, change_x, change_y, radius, color):

       # Take the parameters of the init function above,
       # and create instance variables out of them.
       self.x = position_x
       self.y = position_y
       self.vx = change_x
       self.vy = change_y
       self.ax = 0
       self.ay = 0
       self.radius = radius
       self.color = color

   def draw(self):
       """ Draw the balls with the instance variables we have. """
       arcade.draw_circle_filled(self.x,
                                 self.y,
                                 self.radius, self.
                                 color)

   def update(self):
       # Add gravity to the vertical speed
       self.vy = self.vy + GRAVITY

       # Add acceralation to the speed
       self.vx = self.vx + self.ax
       self.vy = self.vy + self.ay

       # Move the ball
       self.y += self.vy
       self.x += self.vx

       # See if the ball hit the edge of the screen. If so, change direction
       if self.x < self.radius:
           self.x = self.radius

       if self.x > SCREEN_WIDTH - self.radius:
           self.x = SCREEN_WIDTH - self.radius
           self.vx = 0

       if self.y < self.radius:
           self.y = self.radius
           self.vy = 0

       if self.y > SCREEN_HEIGHT - self.radius:
           self.y = SCREEN_HEIGHT - self.radius
           self.vy = 0


class MyGame(arcade.Window):

   def __init__(self, width, height, title):

       # Call the parent class's init function
       super().__init__(width, height, title)

       # Make the mouse disappear when it is over the window.
       # So we just see our object, not the pointer.
       self.set_mouse_visible(False)

       arcade.set_background_color(arcade.color.ASH_GREY)

       # Create our ball
       self.ball = Ball(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, 0, 0, 15, arcade.color.AUBURN)

   def on_draw(self):
       # Called whenever we need to draw the window.
       arcade.start_render()
       self.ball.draw()

   def update(self, delta_time):
       self.ball.update()

   def on_key_press(self, key, modifiers):
       # Called whenever the user presses a key.
       if key == arcade.key.LEFT:
           self.ball.ax = -0.2
       elif key == arcade.key.RIGHT:
           self.ball.ax = 0.2
       elif key == arcade.key.UP:
           self.ball.ay = 0.2
       elif key == arcade.key.DOWN:
           self.ball.ay = -0.2

   def on_key_release(self, key, modifiers):
       # Called whenever a user releases a key. 
       if key == arcade.key.LEFT or key == arcade.key.RIGHT:
           self.ball.ax = 0
       elif key == arcade.key.UP or key == arcade.key.DOWN:
           self.ball.ay = 0


def main():
   window = MyGame(640, 480, "Gravity Example")
   arcade.run()


main()

