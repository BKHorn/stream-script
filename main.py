def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_up():
    basic.show_leds("""
        . # . # .
                . . . . .
                # . . . #
                . # # # .
                . . . . .
    """)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_up():
    basic.show_leds("""
        . # . # .
                # . # . #
                . # . # .
                # . # . #
                . # . # .
    """)
    basic.show_leds("""
        . # # # .
                # . # . #
                # # . # #
                # . # . #
                . # # # .
    """)
    basic.show_arrow(ArrowNames.WEST)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    pass
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . # . # .
                # . # . #
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.show_string(".")
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . # . # .
                # . # . #
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.show_string(".")
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . # . # .
                # . # . #
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.show_string(".")
    music.play_tone(988, music.beat(BeatFraction.WHOLE))
    basic.show_leds("""
        . # . # .
                # . # . #
                # . # . #
                . # # # .
                . . # . .
    """)
    basic.show_string("Oh no")
    basic.show_string("SUS")
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                . # # # .
                # . . . #
    """)
    music.play_tone(988, music.beat(BeatFraction.BREVE))
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    basic.show_leds("""
        . # . # .
                . . . . .
                . . . . .
                . # # # .
                # . . . #
    """)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

basic.show_string("Start")
basic.show_leds("""
    # . # . #
        . # . # .
        # . # . #
        . # . # .
        # . # . #
""")

def on_every_interval():
    basic.show_icon(IconNames.HEART)
loops.every_interval(1800000, on_every_interval)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval2():
    basic.show_string("1 Hour!")
loops.every_interval(3600000, on_every_interval2)
