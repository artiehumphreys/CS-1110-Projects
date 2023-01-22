#Artie Humphreys, bsg6vr
import uvage,random
width = 800
height = 800
camera = uvage.Camera(width, height) #setting up camera

character = uvage.from_color(width/2,12.5,"blue",25,25) #the rectangle (the playable character)

block_width1 = random.randint(100,700) #initializing the configurations of the first five blocks.
block_width2 = random.randint(100,700)
block_width3 = random.randint(100,700)
block_width4 = random.randint(100,700)
block_width5 = random.randint(100,700)
block_height = 50
distance = 75 #distance between the two blocks
marca = 0 #a score counter (marca is score in spanish)

walls = [uvage.from_color(block_width1/2,170,"black",block_width1, 50),
         uvage.from_color(width-(width-block_width1-100)/2,170,"black",(width-block_width1-distance), 50),
         uvage.from_color(block_width2/2,340,"black",block_width2, 50),
         uvage.from_color(width-(width-block_width2-100)/2,340,"black",(width-block_width2-distance), 50),
         uvage.from_color(block_width3/2,510,"black",block_width3, 50),
         uvage.from_color(width-(width-block_width3-100)/2,510,"black",(width-block_width3-distance), 50),
         uvage.from_color(block_width4/2,680,"black",block_width4, 50),
         uvage.from_color(width-(width-block_width4-100)/2,680,"black",(width-block_width4-distance), 50),
         uvage.from_color(block_width5/2,849,"black",block_width5, 50),
         uvage.from_color(width-(width-block_width5-100)/2,849,"black",(width-block_width5-distance), 50),
         ] #would've been nice to use a class, but this will do. Here, I use the random widths generated earlier to construct the inital five blocks.



# make a parameter-less method that will be called every frame.
def tick():
    """

    :return: A game?
    """
    global block_height
    global width
    global distance
    global marca
    game_on = True #to make it so that we can replay the game after dying
    score_once = False #to make sure the score counter doesn't count more than once per completed block-pair
    yvel = 0.5 #the y velocity of the character
    changex = 0.5 #how much the x of the character changes with each arrow press
    camera.clear("white")
    camera.draw(character)

    if character.y <= -12.5: #if the block is off the screen in the y direction
        game_on = False #stop the game
        camera.draw(uvage.from_text(400,400,"Game Over! Your score was: " + str(marca), 50, "blue"))
        camera.draw(uvage.from_text(400,500, "Press Space to play again", 50, "blue"))
        if uvage.is_pressing("space"):
            game_on = True
            character.x = 400 #resetting the character
            character.y = 25
            marca = 0 #resetting the score



    if game_on:
        for wall in walls: #for each wall in the list of walls
            camera.draw(wall)
            wall.y -= 2.5 #this is how fast the walls "move"
            character.y += yvel #a constant gravitational pull towards the bottom for the character. If not on top of a block, it will fall faster than the blocks
            #dealing with top collision
            if wall.touches(character) and walls.index(wall) % 2 == 0 and character.x <= wall.width: #if a wall has an even index (%2 = 0), it is on the left side of the screen, therefore the x position of the character must be within the width of the block
                character.move_to_stop_overlapping(wall)
            elif wall.touches(character) and walls.index(wall) %2 == 1 and character.x >= 800-wall.width: #same as above, but since this is a wall on the right, it needs to have different parameters for the x position
                character.move_to_stop_overlapping(wall)
            #dealing with side collision
            if wall.touches(character) and walls.index(wall) % 2 == 0 and character.x >= wall.width and character.y-12.5 < wall.y+block_height/2: #the side collision is a little more nuanced. You need to consider not only it's x position, but its y as well (if the character is at the same y level)
                character.move_to_stop_overlapping(wall)
            elif wall.touches(character) and walls.index(wall) % 2 == 1 and character.x <= 800-wall.width and character.y-12.5 < wall.y+block_height/2:
                character.move_to_stop_overlapping(wall)

            if wall.y - 3.5 <= character.y <= wall.y + 3.5 and score_once == False: #this line took me a while. Score once makes sure that the score is only counted once. the 3.5 is a buffer for the character because there were times when the score didn't count.
                marca +=1
                score_once = True
            else:
                score_once = False

            if wall.y < -block_height/2: #generating new walls once they're off the screen
                wall.y = 800+block_height/2
                if (walls.index(wall))%2 == 0:
                    new_width = random.randint(100,700)
                    walls[walls.index(wall)].x = (new_width)/2
                    walls[walls.index(wall)].size = (new_width, 50)

                if (walls.index(wall))%2 == 1:
                    walls[walls.index(wall)].x = width-((width-new_width-distance)/2)
                    walls[walls.index(wall)].size = ((width - new_width - distance),50)



            if uvage.is_pressing("right arrow") and (not character.x > 800): #movement
                character.x += changex
            else:
                pass
            if uvage.is_pressing("left arrow") and (not character.x < 0):
                character.x -= changex
            else:
                pass


            if character.y >= 785: #if player goes too fast and character goes off screen
                character.y = 785


    camera.draw(uvage.from_text(750, 750, str(marca), 50, "blue"))  # the score gamebox, positioned in the bottom right corner of the screen

    camera.display() # you almost always want to end this method with this line
uvage.timer_loop(30, tick)
# tell uvage to call the tick method 30 times per second uvage.timer_loop(30, tick)
# this line of code will not be reached until after the window is closed