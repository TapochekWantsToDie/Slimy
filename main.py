import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN_WIDTH, SCREEN_HEIGHT = arcade.window_commands.get_display_size()

SPRITE_SCALING_COIN = 1
SPRITE_SCALING_WALL = 2
SPRITE_SCALING_PLAYER = 1
COIN_COUNT = 5
MOVEMENT_SPEED = 3

class MyGame(arcade.Window):
    """ The main class of the app. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_list = None
        self.coin_list = None
        self.wall_list = None
        self.badGuy_list = None

        arcade.set_background_color(arcade.color.AMARANTH_PINK)

    def setup(self):
        """ Setup the game and initialize variables. """

        # Create lists of sprites
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.badGuy_list = arcade.SpriteList()

        # Score
        self.score = 0

        # set the player and
        # Their image
        self.player_sprite = arcade.Sprite("player.png",
                                           SPRITE_SCALING_PLAYER)
        self.player_health = 100

        self.player_sprite.center_x = 140  # Starting position
        self.player_sprite.center_y = 130
        self.player_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        """
        # Create walls
        for i in range(8):
            for j in range(8):

                if i % 2 != 0:
                    continue;
                # Create an instance of the walls
                # and their image
                wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

                # Set the position of the walls
                wall.center_x = 185 * i + 238
                wall.center_y = 91 * j + 41

                # Add a wall to the list
                self.wall_list.append(wall)

        # More walls
        for i in range(8):
            for j in range(7):

                if i % 2 == 0:
                    continue;
                # Create an instance of the walls
                # and their image
                wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

                # Set the position of the walls
                wall.center_x = 185 * i + 238
                wall.center_y = 91 * j + 220

                # Add a wall to the list
                self.wall_list.append(wall)

                # All four walls
                for i in range(11):
                    # Create an instance of the walls
                    # and their image
                    wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

                    # Set the position of the walls
                    wall.center_x = 50
                    wall.center_y = 90 * i + 45

                    # Add a wall to the list
                    self.wall_list.append(wall)

        for i in range(11):
            # Create an instance of the walls
            # and their image
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

            # Set the position of the walls
            wall.center_x = 1770
            wall.center_y = 90 * i + 45

            # Add a wall to the list
            self.wall_list.append(wall)

        for i in range(19):
            # Create an instance of the walls
            # and their image
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

            # Set the position of the walls
            wall.center_x = 93 * i + 145
            wall.center_y = 45

            # Add a wall to the list
            self.wall_list.append(wall)

        for i in range(19):
            # Create an instance of the walls
            # and their image
            wall = arcade.Sprite("wall.png", SPRITE_SCALING_WALL)

            # Set the position of the walls
            wall.center_x = 93 * i + 145
            wall.center_y = 945

            # Add a wall to the list
            self.wall_list.append(wall)
        """

        #create blades
        for i in range(10):
            badGuy = arcade.Sprite("blade.png")

            #randomly until we(you) fix the walls
            badGuy.center_x = random.randrange(SCREEN_WIDTH)
            badGuy.center_y = random.randrange(SCREEN_HEIGHT)

            #adding blade to other bad guys
            self.badGuy_list.append(badGuy)

        # Create coins
        for i in range(COIN_COUNT):
            # Create instance of the coins
            # and their image
            coin = arcade.Sprite("coin.png", SPRITE_SCALING_COIN)

            # Set the position of the coins
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add a coin to the list
            self.coin_list.append(coin)
    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.wall_list.draw()
        self.badGuy_list.draw()

        # Draw our score on the screen
        score_text = f"maney: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.csscolor.WHITE, 18)

        #health rectangle
        arcade.draw_xywh_rectangle_filled(100, 10, self.player_health, 20, arcade.csscolor.RED)
        #cute white border for health rectangle
        arcade.draw_xywh_rectangle_outline(100, 10, 100, 20, arcade.csscolor.WHITE, 2)

    def on_key_press(self, key, modifiers):
        """It's called when a key is pressed"""

        if key == arcade.key.W:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """It's called when a key is released"""

        if key == arcade.key.W or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Here is all game logic and logic of movement."""
        # Generate a list of all coins' sprites, that intersect with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                              self.coin_list)

        #I saw the thing over it and decided to do same to bad guys (blades)
        badGuys_doingBad_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                                     self.badGuy_list)


        self.physics_engine.update()

        #If we touch coin it leaves us and we get score if we touch blade we get hurt ouch
        for badGuy in badGuys_doingBad_list:
            self.player_health -= 5
            self.player_sprite.center_y -= MOVEMENT_SPEED
            """
            if self.player_sprite.center_y - MOVEMENT_SPEED*1.5 != badGuys_doingBad_list:
                self.player_sprite.center_y -= MOVEMENT_SPEED*1.5
            elif self.player_sprite.center_y + MOVEMENT_SPEED*1.5 != badGuys_doingBad_list:
                self.player_sprite.center_y += MOVEMENT_SPEED * 1.5
            if self.player_sprite.center_x - MOVEMENT_SPEED*1.5 != badGuys_doingBad_list:
                self.player_sprite.center_x -= MOVEMENT_SPEED * 1.5
            elif self.player_sprite.center_x + MOVEMENT_SPEED*1.5 != badGuys_doingBad_list:
                self.player_sprite.center_x -= MOVEMENT_SPEED * 1.5
            """

        # Go with loop through all intersected sprites, deleting them and increasing the score.
        for coin in coins_hit_list:
            coin.kill()
            self.score += 1


def main():
    #window = arcade.Window(fullscreen = True)
    game = MyGame(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 100, 'I don\'t know how to do it')
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

