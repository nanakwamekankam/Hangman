import time
import turtle
import random


def draw_pole():
    p = turtle.Turtle()

    p.goto(-300, 0)
    p.forward(100)
    p.goto(-250, 0)
    p.left(90)
    p.forward(300)
    p.right(90)
    p.forward(75)
    p.right(90)
    p.forward(50)

    time.sleep(1)

    return p


def word_generator():
    words = ['Generator', 'business', 'Hangman', 'politician', "python", "jumble", 'forgiveness', "difficult",
             "answer", "xylophone", 'technical', 'engineering', 'artillery', 'weapon', 'arsenal', 'spectacular',
             'sensational', 'mediocrity', 'ghanaian', 'madness', 'patriotism', 'skepticism']
    word = random.choice(words)

    return word


def letters_of_word(word):
    letters = list(word)

    return letters


def step_1(p):
    p.up()
    p.goto(-175, 200)
    p.down()
    p.circle(25)
    p.up()
    p.right(90)
    p.goto(-175, 200)
    p.down()


def step_2(p):
    p.forward(15)
    p.left(45)
    p.forward(50)
    p.up()
    p.left(180)
    p.forward(50)
    p.left(90)
    p.down()


def step_3(p):
    p.forward(50)
    p.up()
    p.right(180)
    p.forward(50)
    p.right(135)
    p.down()


def step_4(p):
    p.forward(100)


def step_5(p):
    p.left(45)
    p.forward(50)
    p.up()
    p.left(180)
    p.forward(50)
    p.left(90)


def step_6(p):
    p.down()
    p.forward(50)
    time.sleep(2)


def steps_hangman(p, i):
    if i == 1:
        return step_6(p)
    elif i == 2:
        return step_5(p)
    elif i == 3:
        return step_4(p)
    elif i == 4:
        return step_3(p)
    elif i == 5:
        return step_2(p)
    elif i == 6:
        return step_1(p)
