init -2:
    image ctc_blink:
        "ctc.png"
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat

    image ctc_anchored:
        "ctc2.png"
        yalign 0.96 xalign 0.95
        linear 0.75 alpha 1.0
        linear 0.75 alpha 0.0
        repeat

define e = Character("Eileen", color="#FFFFFF", ctc="ctc_blink", ctc_position="nestled")
define narrator = Character(None, what_color="#FF0000", ctc="ctc_anchored", ctc_position="fixed")

label start:
    "Testing the narrator"

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
