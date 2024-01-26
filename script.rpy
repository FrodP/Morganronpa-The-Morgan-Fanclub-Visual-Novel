# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define bry = Character("Bryson", image="bry")
define ell = Character("Abyss", image="ell") 
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show bry
    # These display lines of dialogue.
    bry "this is a test"
    show ell
    ell "wow cool test bryson"
    show bry
    label choices:
        default eatsbabies = False
        ell "btw what do you think about babies?"
    menu:
        "I actually eat babies":
            jump choicebabyhate
        "I love babies":
            jump choicebabylove

    label choicebabyhate:
        ell "what is wrong with you bro"
        $ eatsbabies = True
        jump commonanswer

    label choicebabylove:
        ell "i actually dislike them but i wouldn't eat them or something"
        jump commonanswer

    label commonanswer:
        ell "uhhh"
    
    label flags:
        if eatsbabies:
            "we gon kill u nigga"
        else:
            ell "i wont kill you i guess"
    
    ell "ok test over still need to figure out how to switch sprites and stuff"
    # This ends the game.

    return
