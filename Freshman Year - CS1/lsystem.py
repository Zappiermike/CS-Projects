## This is a combination of Listings 9.6, 9.7 (with a bug fix), and
## 9.8 (with minor improvements) from Python Programming in Context by
## Miller and Ranum to serve as a starting point for an MCS-177
## project.


##Michael Scheie
##Jackson Keeley
##ANSWERS ARE AT THE BOTTOM##

from cTurtle import Turtle
from random import choice

## Listing 9.6
# applyProduction: string dict-of-char:string integer -> string
def applyProduction(axiom,rules,n):
    for i in range(n):
        newString = ""
        for ch in axiom:
            if ch in rules:
                newString = newString + choice(rules.get(ch,ch))
            else: newString = newString + rules.get(ch,ch)
        axiom = newString
    return axiom

## Listing 9.7
# drawLS: Turtle string number number -> void
def drawLS(aTurtle,instructions,angle,distance):
    stateSaver = []
    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == '[':
            pos = aTurtle.position()
            head = aTurtle.heading()
            stateSaver.append((pos,head))
        elif cmd == "G":
            aTurtle.up()
            aTurtle.forward(distance)
            aTurtle.down()
        elif cmd == ']':
            pos,head = stateSaver.pop()
            aTurtle.up()   # this line was not in Listing 9.7 (a bug)
            aTurtle.setposition(pos)
            aTurtle.setheading(head)
            aTurtle.down() # this line was not in Listing 9.7 (a bug)

## Listing 9.8
# lsystem: string dict-of-char:string integer (integer, integer) number number number -> void
def lsystem(axiom,rules,depth,initialPosition,heading,angle,length):
    aTurtle = Turtle()
    aTurtle.speed(10)       # this line improves on Listing 9.8
    aTurtle.shape('blank') # this line improves on Listing 9.8
    aTurtle.up()
    aTurtle.setposition(initialPosition)
    aTurtle.down()
    aTurtle.setheading(heading)
    ## The variable "instructions" was called "newRules" in Listing 9.8,
    ## which was misleading regarding what kind of thing it names.
    instructions = applyProduction(axiom,rules,depth)
    drawLS(aTurtle,instructions,angle,length)
    aTurtle.exitOnClick()

#Number 1: >>> lsystem("F", {"F":["F-F++F-F"]}, 4, (-250,0), 0, 60, 6)
#Number 2: N/a (done)
#For number 3 on the project, once done correctly, the ending will show triangles within other triangles. This type of design is called the sierpinski triangle.
#Number 3: >>> lsystem("F-F-F", {"F":"F-F-F-GG", "G":"GG"}, 3, (-200,0), 0, 120, 30)
#Number 4: >>> lsystem("F", {"F":"F[-F]F[+F]F", "G":"GG"}, 3, (0,-200), 90, 60, 10)
#Number 5: >>> lsystem("F", {"F":["F[-F]F[+F]F","F[-F]F","F[+F]F"], "G":"GG"}, 3, (-300,0), 0, 25, 25)
#Number 6: Dragon Curve: >>> lsystem("FX", {"X":["X+YF+"],"Y":["-FX-Y"]}, 10, (-100,0), 0, 90, 10)
#           Fractal Plant: >>> lsystem("X", {"X":["F-[[X]+X]+F[+FX]-X"],"F":["FF"]}, 6, (-300,-100), 0, 25, 6)


