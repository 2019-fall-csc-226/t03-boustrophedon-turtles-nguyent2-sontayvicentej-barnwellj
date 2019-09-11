#################################################################################
# Author: Thy H. Nguyen
#   Jhonny Sontay-Vicente
# Username: nguyent2
# sontayvincentej
# Assignment: T03
# Purpose: Making two functions doing the Boustrophedon
# Citation: https://docs.python.org/3.3/library/turtle.html?
#################################################################################
# Acknowledgements:
# Citation: https://docs.python.org/3.3/library/turtle.html?
#
#################################################################################

import turtle

def draw_square(thy):
    """
    This functions draw a square outside
    """
    pass
    thy.pendown()
    for i in range(4):
        thy.forward(500)
        thy.left(90)


def moving_forward(th):
    """
    This function draws the last line of the Boustrophedon
    :param th:
    :return:
    """
    th.forward(460)

def fill_in_the_last_line(thyy):
    thyy.left(90)
    thyy.forward(20)
    thyy.left(90)
    thyy.forward(460)

def boustrophedon(jhonny):
    """
    This functions fills the inside of the square with Boustrophedon
    """
    pass

    jhonny.pendown()
    for i in range(int(500/40-1)): #Since 1 loop is 2 lines, which is the pensize is 20*2=40
        jhonny.forward(460)
        jhonny.left(90)
        jhonny.forward(20)
        jhonny.left(90)
        jhonny.forward(460)
        jhonny.right(90)
        jhonny.forward(20)
        jhonny.right(90)
    moving_forward(jhonny)
    fill_in_the_last_line(jhonny)



def main():
    """
    Call function_1() and function_2()
    """
    # ...
    wn = turtle.Screen()
    thy = turtle.Turtle()
    thy.pensize(20)
    thy.color("blue")
    jhonny = turtle.Turtle()
    jhonny.pensize(20)
    jhonny.color("yellow")
    thy.penup()
    thy.setposition(-250, -250)
    jhonny.penup()
    jhonny.setposition(-230, -230)

    draw_square(thy)            # Function call to function_1
    boustrophedon(jhonny)            # Function call to function_2

    wn.exitonclick()

main()

