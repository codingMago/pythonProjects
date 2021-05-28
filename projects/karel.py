# Educating with karel
# Helping teach functions

from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    """
    Karel draws the text, "HELLO WORLD". Works in Extension world 20*20.
    pre: Karel is facing east at (01, 01), prior to writing "HELLO WORLD".
    post: Karel is facing east at (20, 10), after writing "HELLO WORLD".
    """
    go_top()
    draw_h()
    draw_e()
    draw_l()
    draw_l()
    draw_o()
    move_down()
    draw_w()
    draw_o()
    move()
    draw_r()
    draw_l()
    draw_d()

def draw_line4():
    for i in range(4):
        move()
        paint_corner(CYAN)


def draw_line3():
    for i in range(3):
        move()
        paint_corner(CYAN)

def draw_line2():
    for i in range(2):
        move()
        paint_corner(CYAN)


def draw_h():
    turn_south()
    paint_corner(CYAN)
    draw_line5()
    turn_north()
    for i in range(2):
        move()
    turn_east()
    draw_line2()
    turn_north()
    draw_line2()
    turn_south()
    draw_line5()
    turn_left()
    for i in range(2):
        move()

def move_down(): # Ready for next word
    turn_south()
    for i in range(6):
        move()

def go_top():
    turnNorth()
    while front_is_clear():
        move()
# Karel turns right
def turn_right():
    for i in range(3):
        turn_left()

# Karel turns around
def turn_around():
    for i in range(2):
        turn_left()

def turn_north():
    while not_facing_north():
        turn_left()

def turn_east():
    while not_facing_east():
        turn_left()

def turn_south():
    while not_facing_south():
        turn_left()

def turn_west():
    while not_facing_west():
        turn_left()









# pre: Facing East post: East of E by two
def draw_e():
    turn_left()
    draw_line()
    turn_right()
    draw_prong()
    for i in range(2):
        move()
    turn_left()
    draw_prong()
    for i in range(2):
        move()
    turn_left()
    draw_prong()
    turn_left()
    for i in range(4):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, two spaces past the completed letter L.
"""
def draw_l():
    turn_left()
    draw_line()
    turn_around()
    for i in range(4):
        move()
    turn_left()
    draw_prong()
    turn_left()
    for i in range(4):
        move()

""" 
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter O. 
"""
def draw_o():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_around()
    for i in range(3):
        move()

"""
pre: Karel is facing west.
post: Karel is facing east, two spaces past the completed letter W. 
"""
def draw_w():
    turn_right()
    draw_line()
    turn_around()
    for i in range(3):
        move()
    turn_left()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    turn_around()
    draw_line()
    turn_around()
    for i in range(4):
        move()
    turn_left()
    for i in range(2):
        move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, two spaces past the completed letter R.
"""
def draw_r():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_left()
    move()
    turn_left()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    paint_corner(CYAN)
    turn_left()
    for i in range(2):
        move()

"""
pre: Karel is facing east, two spaces past the previous letter.
post: Karel is facing east, one space past the completed letter D.
"""
def draw_d():
    turn_left()
    draw_line()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_right()
    move()
    for i in range(3):
        paint_corner(CYAN)
        move()
    turn_right()
    move()
    paint_corner(CYAN)
    move()
    turn_around()
    for i in range(3):
        move()







# Karel draws a line 5 spaces long.


# Karel draws a line 2 spaces long.
def draw_prong():
    move()
    paint_corner(CYAN)
    move()
    paint_corner(CYAN)
    turn_around()
    for i in range(2):
        move()
    turn_left()





if __name__ == "__main__":
    run_karel_program()