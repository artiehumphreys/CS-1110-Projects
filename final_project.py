#Names


    #Artie Humphreys - bsg6vr
    #Graham Lenert - dxf3ty

#Description of Game
    #Our game will be similar to the game Breakout.
    #There will be a platform on the bottom of the screen that the user controls horizontally
    #A ball will be bouncing on the screen, and the player will try to have the ball bounce off the platform.
    #On the top of the screen, there will be a bunch of boxes. When the ball touches the boxes, the box will
    #be destroyed, and the ball will bounce downwards towards the player's platform. If the player does not
    #bounce the ball, the game will be over. The goal is for the player to remove all the boxes

#3 Basic Features
    #1: User Input
        #The player will use the arrows keys to move the bottom platform left or right
        #If the player is standing still, the ball will bounce based on where it hit on the player
        #However, if the player is moving, the ball will get a boost in the direction that it was going
    #2: Game Over
        #If the ball goes beneath the platform (meaning the player missed the ball), the game over
        #screen will appear to indicate that the player has lost. This screen will include the score
        #If the ball goes above the boxes (meaning the player has won), the game over screen will appear
        #to indicate that the player has won, the game over screen will appear
    #3: Graphics/Images
        #The boxes will be made of different images, and background will be an image
#4 Additional Features
    #1: Collectibles
        #Occasionally, a coin will appear on the screen. If the player manages to touch the coins with the ball,
        #the player's score will be increased
    #2: Enemies
        #Occasionally, enemies move around the screen and follow the player. If the ball touches an enemy,
        #the score will be decreased
    #3: Score/Timer
        #On the player, a score will be displayed to the user to indicate their current score.
        #Breaking blocks will increase this score, hitting coins will increase this score, and hitting
        #enemies will decrease this score. When the game is over, this score will be displayed on the
        #game over screen
    #4: Restart from Game OVer
        #On the end screen, there will be an option to restart the game. If the user follows the instructions to restart the game
        #(Button and/or key press), the game will be reset to the beginning.


#imports
import uvage
import random

game_status = True
start_new_game = True
win_or_loss = False
enemy_bool = False
score_bool = False
frame_count = 0

#camera width and height
cam_width = 1200
cam_height = 600



#List of URLs used for images
background_url = "https://techcrunch.com/wp-content/uploads/2021/10/GettyImages-1176555906.jpg"
enemy_url = "https://freepngimg.com/thumb/emoji/102385-devil-emoji-download-hd.png"
token_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Star_coin.png/604px-Star_coin.png"
ball_url = "https://freepngimg.com/thumb/categories/1873.png"

#player width; player is a square, so it is also the height of the player
player_width = 100
player_height = 20



#create camera
camera = uvage.Camera(cam_width, cam_height)

#initialize player and ball variables
player = 0
ball = 0
ball_x_speed = 0
current_score = 0


#create enemy
enemy = uvage.from_image(cam_width/2 ,400, enemy_url)
enemy.scale_by(.1)

token_scalar = .075
token = uvage.from_image(random.randint(50,1150), random.randint(300,500),token_url)
token.scale_by(token_scalar)

#initialze box list
box_list = []

def create_all_boxes():
    """
    :return: returns nothing; when called, sets the game back to its starting position
    """
    global box_list
    global player
    global ball
    global ball_x_speed
    global current_score

    #create player
    player = uvage.from_color(cam_width / 2, cam_height - player_height / 2, "grey", player_width, player_height)

    current_score = 0


    #create ball
    ball = uvage.from_image(cam_width / 2 + random.randint(-300, 300), cam_height / 2, ball_url)
    ball.scale_by(.25)
    ball.speedy = -7
    ball_x_speed = 7
    ball.speedx = ball_x_speed


    box_height = 25
    #Generate random widths for all the boxes
    row1_box1_width = random.randint(150, 250)
    row1_box2_width = random.randint(50, 200)
    row1_box3_width = random.randint(150, 250)
    row1_box4_width = random.randint(50, 200)
    row1_box5_width = random.randint(150, 250)
    row1_box6_width = random.randint(50, 200)
    row1_box7_width = random.randint(150, 250)

    row2_box1_width = random.randint(200, 300)
    row2_box2_width = random.randint(100, 200)
    row2_box3_width = random.randint(50, 100)
    row2_box4_width = random.randint(200, 250)
    row2_box5_width = random.randint(50, 100)
    row2_box6_width = random.randint(50, 100)
    row2_box7_width = random.randint(50, 150)

    row3_box1_width = random.randint(100,200)
    row3_box2_width = random.randint(200,300)
    row3_box3_width = random.randint(100,200)
    row3_box4_width = random.randint(200,300)

    #create top row of boxes
    row1_center = row1_box1_width / 2
    row1_box1 = uvage.from_color(row1_center, box_height / 2, "red", row1_box1_width, box_height)
    row1_center += row1_box1_width / 2 + row1_box2_width / 2
    row1_box2 = uvage.from_color(row1_center, box_height / 2, "dark red", row1_box2_width, box_height)
    row1_center += row1_box2_width / 2 + row1_box3_width / 2
    row1_box3 = uvage.from_color(row1_center, box_height / 2, "red", row1_box3_width, box_height)
    row1_center += row1_box3_width / 2 + row1_box4_width / 2
    row1_box4 = uvage.from_color(row1_center, box_height / 2, "dark red", row1_box4_width, box_height)
    row1_center += row1_box4_width / 2 + row1_box5_width / 2
    row1_box5 = uvage.from_color(row1_center, box_height / 2, "red", row1_box5_width, box_height)
    row1_center += row1_box5_width / 2 + row1_box6_width / 2
    row1_box6 = uvage.from_color(row1_center, box_height / 2, "dark red", row1_box6_width, box_height)
    row1_center += row1_box6_width / 2 + row1_box7_width / 2
    row1_box7 = uvage.from_color(row1_center, box_height / 2, "red", row1_box7_width, box_height)
    row1_center += row1_box7_width / 2
    row1_finalBox = uvage.from_color((cam_width - (cam_width - row1_center)) + (cam_width - row1_center) / 2,
                                     box_height / 2, "dark red", cam_width - row1_center, box_height)

    #create middle row of boxes
    row_offset = box_height
    row2_center = row2_box1_width / 2
    row2_box1 = uvage.from_color(row2_center, box_height / 2 + row_offset, "blue", row2_box1_width, box_height)
    row2_center += row2_box1_width / 2 + row2_box2_width / 2
    row2_box2 = uvage.from_color(row2_center, box_height / 2 + row_offset, "light blue", row2_box2_width, box_height)
    row2_center += row2_box2_width / 2 + row2_box3_width / 2
    row2_box3 = uvage.from_color(row2_center, box_height / 2 + row_offset, "blue", row2_box3_width, box_height)
    row2_center += row2_box3_width / 2 + row2_box4_width / 2
    row2_box4 = uvage.from_color(row2_center, box_height / 2 + row_offset, "light blue", row2_box4_width, box_height)
    row2_center += row2_box4_width / 2 + row2_box5_width / 2
    row2_box5 = uvage.from_color(row2_center, box_height / 2 + row_offset, "blue", row2_box5_width, box_height)
    row2_center += row2_box5_width / 2 + row2_box6_width / 2
    row2_box6 = uvage.from_color(row2_center, box_height / 2 + row_offset, "light blue", row2_box6_width, box_height)
    row2_center += row2_box6_width / 2 + row2_box7_width / 2
    row2_box7 = uvage.from_color(row2_center, box_height / 2 + row_offset, "blue", row2_box7_width, box_height)
    row2_center += row2_box7_width / 2
    row2_finalBox = uvage.from_color((cam_width - (cam_width - row2_center)) + (cam_width - row2_center) / 2,
                                     box_height / 2 + row_offset, "light blue", cam_width - row2_center, box_height)

    #create bottom row of boxes
    row_offset += box_height
    row3_center = row3_box1_width / 2
    row3_box1 = uvage.from_color(row3_center, box_height / 2 + row_offset, "light green", row3_box1_width, box_height)
    row3_center += row3_box1_width / 2 + row3_box2_width / 2
    row3_box2 = uvage.from_color(row3_center, box_height / 2 + row_offset, "green", row3_box2_width, box_height)
    row3_center += row3_box2_width/2 + row3_box3_width /2
    row3_box3 = uvage.from_color(row3_center,box_height/2 + row_offset, "light green",row3_box3_width,box_height)
    row3_center += row3_box3_width/2 + row3_box4_width/2
    row3_box4 = uvage.from_color(row3_center,box_height/2 + row_offset,"green",row3_box4_width,box_height)
    row3_center += row3_box4_width /2
    row3_finalBox = uvage.from_color((cam_width - (cam_width - row3_center)) + (cam_width - row3_center) / 2,
                                     box_height / 2 + row_offset, "light green", cam_width - row3_center, box_height)

    box_list = [row1_box1, row1_box2, row1_box3, row1_box4, row1_box5, row1_box6, row1_box7, row1_finalBox,
                row2_box1, row2_box2, row2_box3, row2_box4, row2_box5, row2_box6, row2_box7, row2_finalBox,
                row3_box1, row3_box2, row3_box3, row3_box4, row3_finalBox]

def handle_user_input():
    """
    :return: return nothing, but controls player's horizontal movement; doesn't let them go off the sides too
    """
    if uvage.is_pressing("left arrow") and player.x > (0 + player_width / 2):
        player.speedx = -15
    elif uvage.is_pressing("right arrow") and player.x < (cam_width - player_width / 2):
        player.speedx = 15
    else:
        player.speedx = 0
    player.move_speed()




def game_over():
    """
    :return: returns nothing; but shows the game over screen when called
    """
    global game_status
    global start_new_game
    global current_score
    global win_or_loss

    camera.clear("black")


    if win_or_loss == True:
        final_score = uvage.from_text(cam_width / 2, cam_height / 2, "You Won! Score of " + str(current_score), 48, "Green")
    elif win_or_loss == False:
        final_score = uvage.from_text(cam_width / 2, cam_height / 2, "You Lost! Your score was: " + str(current_score), 48, "Red")
    else:
        final_score = uvage.from_text(cam_width / 2, cam_height / 2, "You Lost! Your score was: " + str(current_score), 48, "Red")

    play_again = uvage.from_text(cam_width/2, 200, "Press Space to Play Again", 60, "Light Blue")
    if uvage.is_pressing("space") and game_status == False:
        game_status = True
        start_new_game = True


    camera.draw(play_again)
    camera.draw(final_score)
    camera.display()



def handle_ball_movement():
    """
    :return: returns nothing; but handles movement of the ball and the enemy
    """
    global game_status
    global current_score
    global win_or_loss
    global frame_count
    global enemy_bool
    global score_bool
    for i in box_list:
        if ball.touches(i):
            ball.speedy *= -1.15
            ball.move_speed()
            i.move(0,-2500)
            current_score += 1
    if current_score >= 2:
        enemy_bool = True #enemy activates after 2 points are scored

    middle = 5 #middle of the character
    #included side boosting
    if ball.touches(player) and uvage.is_pressing("left arrow"):
        ball.speedy *= -1
        ball.speedx = -ball_x_speed * 1.75
    elif ball.touches(player) and uvage.is_pressing("right arrow"):
        ball.speedy *= -1
        ball.speedx = ball_x_speed * 1.75
    #this may look weird, but this is a system of inequalities to determine where on the player the ball lands.
    #we use its relative position to determine the balls trajectory
    elif ball.touches((player)) and (player.x-player.width) <= ball.x <= player.x - middle:
        ball.speedy *= -1
        ball.speedx = ((ball.x-player.x)/(player_width*.25))*ball_x_speed
    elif ball.touches((player)) and (player.x + middle) <= ball.x <= player.x + player.width:
        ball.speedy *= -1
        ball.speedx = ((ball.x-player.x)/(player_width*.25))*ball_x_speed
    elif ball.touches((player)) and (player.x - middle) < ball.x < player.x + middle:
        ball.speedy *= -1
        ball.speedx = ((ball.x-player.x)/(player_width*.25))*ball_x_speed




    #enemy movement
    enemy_speed_value = 200
    if enemy_bool == True:
        chasex = 0
        chasey = 0
        if frame_count%120 == 0: #every 4 seconds, the enemy moves to the coordinate of the ball at that frame (can be changed to make it harder or easier)
            chasex = ball.x
            chasey = ball.y
        if enemy.x >= ball.x: #handling positive and negative movement
            enemy.x -= (enemy.x-chasex) / enemy_speed_value
        if enemy.x < ball.x:
            enemy.x += (enemy.x - chasex) / enemy_speed_value

        if enemy.y >= ball.y:
            enemy.y -= (enemy.y - chasey) / enemy_speed_value
        if enemy.y < ball.y:
            enemy.y += (enemy.y - chasey) / enemy_speed_value
        if enemy.touches(ball) and score_bool == False: #the enemy will reduce the score by 5
            current_score -= 5
            score_bool = True #to make sure the score only counts once
        if not enemy.touches(ball):
            score_bool = False




    if ball.x <= 0 or ball.x >= cam_width:
        ball.speedx *= -1

    if ball.y >= cam_height:
        game_status = False
        win_or_loss = False

    if current_score < 0:
        game_status = False
        win_or_loss = False

    if ball.y < -25/2:
        game_status = False
        win_or_loss = True




def tick():
    """
    :return: returns nothing, but this is the main function that runs 30 times a second and calls all the other helper functions
    """
    global current_score
    global activeToken
    global token
    global frame_count
    global enemy_bool
    global start_new_game
    camera.clear("black")
    frame_count += 1


    if game_status == True:



        if start_new_game == True:
            create_all_boxes()
            start_new_game = False
            enemy_bool = False


        score = uvage.from_text(player.x, player.y, str(current_score), 28, "dark blue")


        handle_user_input()
        handle_ball_movement()


        if ball.touches(token):
            token=uvage.from_image(random.randint(50, 1150), random.randint(300, 500),token_url)
            token.scale_by(token_scalar)

            current_score += 10


        ball.move_speed()


        background = uvage.from_image(cam_width/2, cam_height/2, background_url)
        background.scale_by(.75)
        camera.draw(background)


        camera.draw(token)

        camera.draw(player)
        camera.draw(ball)
        if enemy_bool == True:
            camera.draw(enemy)


        for box in box_list:
            camera.draw(box)
        camera.draw(score)



        camera.display()
    elif game_status == False:
        game_over()


#loop the code in the tick loop
uvage.timer_loop(30, tick)
