input.onButtonPressed(Button.A, function () {
	
})
input.onGesture(Gesture.ScreenUp, function () {
    basic.showLeds(`
        . # . # .
        . . . . .
        # . . . #
        . # # # .
        . . . . .
        `)
})
input.onGesture(Gesture.Shake, function () {
	
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showLeds(`
        . # . # .
        # . # . #
        . # . # .
        # . # . #
        . # . # .
        `)
    basic.showLeds(`
        . # # # .
        # . # . #
        # # . # #
        # . # . #
        . # # # .
        `)
    basic.showArrow(ArrowNames.West)
})
input.onButtonPressed(Button.AB, function () {
	
})
input.onButtonPressed(Button.B, function () {
    music.playTone(988, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . # . # .
        # . # . #
        # . # . #
        . # # # .
        . . # . .
        `)
    basic.showString("!")
    music.playTone(988, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . # . # .
        # . # . #
        # . # . #
        . # # # .
        . . # . .
        `)
    basic.showString("!")
    music.playTone(988, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . # . # .
        # . # . #
        # . # . #
        . # # # .
        . . # . .
        `)
    basic.showString("!")
    music.playTone(988, music.beat(BeatFraction.Whole))
    basic.showLeds(`
        . # . # .
        # . # . #
        # . # . #
        . # # # .
        . . # . .
        `)
    basic.showString("Oh no")
    basic.showString("SUS")
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        # . . . #
        `)
    music.playTone(988, music.beat(BeatFraction.Breve))
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    basic.showLeds(`
        . # . # .
        . . . . .
        . . . . .
        . # # # .
        # . . . #
        `)
})
basic.showString("Start")
basic.showLeds(`
    # . # . #
    . # . # .
    # . # . #
    . # . # .
    # . # . #
    `)
loops.everyInterval(1800000, function () {
    basic.showIcon(IconNames.Heart)
})
basic.forever(function () {
	
})
loops.everyInterval(3600000, function () {
    basic.showString("1 Hour!")
})
