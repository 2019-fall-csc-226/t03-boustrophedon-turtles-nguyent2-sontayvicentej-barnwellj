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
wn = turtle.Screen()
thy = turtle.Turtle()
thy.pensize(20)
thy.color("blue")
jhonny = turtle.Turtle()
jhonny.pensize(19)
jhonny.color("yellow")
thy.penup()
thy.setposition(-250,-250)
jhonny.penup()
jhonny.setposition(-224, -224)
def function_1():
    """
    This functions draw a square outside
    """
    pass
    thy.pendown()
    for i in range(4):
        thy.forward(501)
        thy.left(90)

def function_2():
    """
    This functions fills in the square with Boustrophedon
    """
    pass

    jhonny.pendown()
    jhonny.forward(480)
    jhonny.left(90)
    jhonny.forward
    jhonny.forward(480)
    jhonny.right(90)


def main():
    """
    Call function_1() and function_2()
    """
    # ...
    function_1()            # Function call to function_1
    function_2()            # Function call to function_2


main()
wn.exitonclick()
