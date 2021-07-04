# House in the summer rain

import turtle
import random
t = turtle.Turtle()
t.ht()
t.speed(0)
height, width = t.screen.window_height(), t.screen.window_width()

def rect(length, width, pencolor, fillcolor):
    """Draws a rectangle a the clockwise direction starting from the
       top-left."""
    before = t.color()
    t.color(pencolor, fillcolor)
    t.setheading(0)
    t.begin_fill()
    for i in range(2):
        t.fd(length)
        t.rt(90)
        t.fd(width)
        t.rt(90)
    t.end_fill()
    t.color(*before)

def penup_goto(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    
def rectangle(p1, p2, p3, p4):
    penup_goto(*p1)
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)
    t.goto(p1)

def windows(x1, y1, width, height):
    bottom_left = (x1, y1)
    bottom_right = (x1 + width, y1)
    top_left = (x1, y1 + height)
    top_right = (x1 + width, y1 + height)
    
    # Draw windows
    t.color('black', 'light blue')
    t.begin_fill()
    rectangle(bottom_left, bottom_right, top_right, top_left)
    t.end_fill()
    
    #Draw window grills
    t.color('black')
    penup_goto(x1 + width / 2, y1)
    t.goto(x1 + width / 2, y1 + height)
    penup_goto(x1, y1 + height / 2)
    t.goto(x1 + width, y1 + height / 2)
    
def house(x1, y1, x2, y2, width, height):
    # Tip of house is at (x, y)
    # Bottom left-hand corner of the house is at (x2, y2)
    tip = (x1, y1)
    bottom_left = (x2, y2)
    bottom_right = (x2 + width, y2)
    top_left = (x2, y2 + height)
    top_right = (x2 + width, y2 + height)

    #Draw chimney
    chimney_height = 50
    chimney_top_left = ((top_right[0] + x1) / 2, top_right[1] + chimney_height)
    penup_goto(*chimney_top_left)
    rect(20, chimney_height, 'black', 'gray')
    
    #Draw the roof triangle
    t.color('black', 'brown')
    t.begin_fill()
    penup_goto(*tip)
    t.goto(top_left)
    t.goto(top_right)
    t.goto(tip)
    t.end_fill()

    #Draw the house body
    t.color('black', 'pink')
    penup_goto(*top_left)
    t.begin_fill()
    rectangle(top_right, bottom_right, bottom_left, top_left)
    t.end_fill()

    # Draw side windows
    margin = 20
    width, height = 20, 20
    windows(bottom_left[0] + margin, bottom_left[1] + margin, width, height)
    windows(bottom_right[0] - margin - width, bottom_right[1] + margin, width, height)
    windows(top_left[0] + margin, top_left[1] - height - margin, width, height)
    windows(top_right[0] - width - margin, top_right[1] - height - margin, width, height)

    #Draw middle circle window
    margin = 10
    rad = 18
    penup_goto(tip[0], top_left[1] - margin - rad * 2)
    t.setheading(0)
    t.color("black", "light blue")
    
    # Draw the window
    t.begin_fill()
    t.circle(rad)
    t.end_fill()

    # Draw the window grills
    t.setheading(90)
    t.fd(rad * 2) # Go to top
    t.rt(180)
    t.fd(rad) # Go to center
    t.rt(90)
    t.fd(rad) # Go left
    t.rt(180)
    t.fd(rad * 2) # Go right

    # Draw door
    door_mid = (tip[0], bottom_left[1])
    width = 25
    height = 34
    top_left = (door_mid[0] - width / 2, door_mid[1] + height)
    penup_goto(*top_left)
    rect(width, height, 'black', 'peru')
    
    # Draw door knob.
    door_knob_location = (tip[0] + width / 4, bottom_left[1] + height / 2)
    penup_goto(*door_knob_location)
    t.color('orange', 'orange')
    t.dot()

    # Done!
    
def draw_flower(num_flowers, rad, fillcolor):
    t.color(fillcolor, fillcolor)
    t.begin_fill()
    angle_to_turn = 360 / num_flowers
    for i in range(num_flowers):
        t.circle(rad)
        t.rt(angle_to_turn)
    t.end_fill()
    
def draw_sky_and_ground():
    top_left = (-width / 2, height / 2)
    penup_goto(*top_left)
    rect(width, height / 2, 'white', 'sky blue')
    penup_goto(-width / 2, 0)
    rect(width, height / 2, 'white', 'green')
    
def draw_sun():
    start = (-width / 2, 240)
    penup_goto(*start)
    rad = height / 2 - 240
    t.color('yellow', 'yellow')
    t.begin_fill()
    t.circle(rad)
    t.end_fill()
    rays = 9
    ray_length = 20
    for ray_idx in range(1, rays + 1):
        t.pu()
        t.circle(rad, 10)
        t.rt(90)
        t.fd(15)
        t.pd()
        t.fd(ray_length)
        t.pu()
        t.bk(ray_length+15)
        t.lt(90)

def draw_clouds():
    for i in range(random.randint(8,10)):
        random_loc = random.randrange(-200, 200), random.randrange(50, height / 2)
        penup_goto(*random_loc)
        draw_flower(random.randint(6, 10), random.randint(10, 25), 'white')

def draw_rain():
    norm = t.pensize()
    t.pensize(2)
    t.color('light gray')
    for x in range(-width // 2, width // 2 + 100, 50):
        penup_goto(x, height / 2)
        rain_length = 30
        distance_between_each_rain_line = random.randint(20, 30)
        t.setheading(265)
        for i in range(int(height / (rain_length + distance_between_each_rain_line)) + 1):
            t.fd(rain_length)
            t.pu()
            t.fd(distance_between_each_rain_line)
            t.pd()
    t.pensize(norm)
    t.setheading(0)

def draw_pathway(x1, y1, len_tip):
    penup_goto(x1, y1)
    t.color('black', '#918E7D')
    t.begin_fill()
    t.setheading(270)
    t.rt(10)
    while t.position()[1] - 10 > -height / 2: # Force turtle to move out
        t.fd(10)
    bottom_left = t.position()
    penup_goto(x1, y1)
    t.setheading(0)
    t.fd(len_tip)
    t.rt(90-10)
    while t.position()[1] - 10 > -height / 2: # Force turtle to move out
        t.fd(10)
    t.goto(bottom_left)
    t.end_fill()

def draw_bushes(x1, y1):
    penup_goto(x1, y1)
    t.setheading(0)
    draw_flower(random.randint(8, 10), 20, 'dark green')

def draw_single_fence(x1, y1, width, height_tip, height_body):
    # (x1, y1) -> tip of triangle
    top_left = (x1 - width / 2, y1 - height_tip)
    top_right = (x1 + width / 2, y1 - height_tip)
    bottom_left = (top_left[0], top_left[1] - height_body)
    bottom_right = (top_right[0], top_right[1] - height_body)
    t.color("black", "saddle brown")
    t.begin_fill()
    penup_goto(x1, y1)
    t.goto(top_left)
    t.goto(bottom_left)
    t.goto(bottom_right)
    t.goto(top_right)
    t.goto(x1, y1)
    t.end_fill()

def draw_postbox(x, y):
    #(x, y) -> bottom corner
    postbox_height = 70
    iron_width = 20
    height_mailbox = 20
    length_mailbox = 40
    penup_goto(x, y)
    rect(iron_width, -postbox_height, 'black', 'gray')
    penup_goto(x + iron_width, y + postbox_height - height_mailbox)
    rect(length_mailbox, -height_mailbox, 'black', 'blue')
    penup_goto(x + iron_width + length_mailbox, y + postbox_height - height_mailbox)
    t.color('black', 'blue')
    t.begin_fill()
    t.circle(height_mailbox / 2, 180)
    t.end_fill()
    penup_goto(x + iron_width + 10, y + postbox_height - height_mailbox)
    t.write("Postbox")
    
def draw_fences(fence_x, fence_y, fence_width, fence_height_tip, fence_height, draw_knob=False):
    while fence_x < width / 2 + fence_width:
        draw_single_fence(fence_x, fence_y, fence_width, fence_height_tip, fence_height)
        if -10 <= fence_x <= 10 and draw_knob:
            # Draw fence knob
            t.pu()
            t.setheading(270)
            t.fd(50/2+10)
            t.rt(90)
            t.fd(2)
            t.pd()
            t.color("gray", "gray")
            t.dot(5)
        fence_x += fence_width

def draw_tree(x, y, width, height):
    # (x, y) -> top left hand corner of the bark
    penup_goto(x, y)
    rect(width, height, 'black', '#654321')
    penup_goto(x + width / 2, y + 30)
    draw_flower(random.randint(8, 10), random.randint(20, 25), 'green')

def draw_grass(x, y):
    num_grass = random.randint(3, 5)
    width_grass = random.randint(10, 20)
    height_grass = 20
    penup_goto(x, y)
    for i in range(num_grass):
        t.goto(x + width_grass / 2, y + height_grass)
        t.goto(x + width_grass, y)
        x += width_grass

def draw_grass_patch(): 
    for i in range(10):
        x, y = random.randint(-width // 2, width // 2 - 50), random.randint(-height // 2, -50)
        draw_grass(x, y)
        
draw_sky_and_ground()
draw_grass_patch()
draw_sun()
draw_clouds()
house_tip = (0, 100)
house_left_bottom = (-100, -50)
house_width, house_height = 200, 100
# Draw fences at the back of the house
draw_fences(-width / 2, 0, 10, 5, 30)
house(*house_tip, *house_left_bottom, house_width, house_height)
# Draw bushes in front of the house
delta_x, delta_y = 15, 0
for i in range(3):
    draw_bushes(house_left_bottom[0] - delta_x, house_left_bottom[1] - delta_y)
    draw_bushes(house_left_bottom[0] + house_width + delta_x, house_left_bottom[1] - delta_y)
    delta_x += 10
    delta_y += 40
# Fence must be somewhere below the bushes
# Set starting point of fences
fence_width = 20
fence_y = t.position()[1] - 40
fence_x = -width / 2
# Draw pathway first
draw_pathway(house_tip[0] - 20, house_left_bottom[1], 40)
# Draw postbox next
draw_postbox(-100, -200)
#Draw fences at the front
draw_fences(fence_x, fence_y, fence_width, 10, 50, True)
draw_tree(250, -50, 30, 100)
draw_tree(-250, -50, 30, 100)
draw_rain()
