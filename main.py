"""

da die Variablen mit let deklariert werden, sind diese nur innerhalb ihres Blockes nutzbar

wird in javascrpt etwas mit var erzeugt, ist es nicht konvertierbar zu den Blöcken

"""
LED_Y = 0
LED_X = 0
level = 1
while not (input.button_is_pressed(Button.A)):
    if True:
        pass
basic.show_icon(IconNames.YES)
basic.pause(1000)

def on_forever():
    global LED_X, LED_Y
    basic.clear_screen()
    LED_X = pins.map(input.acceleration(Dimension.X) * level, -1023, 1023, 0, 5)
    LED_Y = pins.map(input.acceleration(Dimension.Y) * level, -1023, 1023, 0, 5)
    led.plot(LED_X, LED_Y)
    if LED_X < 0 or LED_X > 5 or (LED_Y > 5 or LED_Y < 0):
        basic.set_led_color(0xff0000)
        basic.show_icon(IconNames.NO)
        music.start_melody(music.built_in_melody(Melodies.FUNERAL), MelodyOptions.ONCE)
        basic.pause(2000)
        basic.turn_rgb_led_off()
basic.forever(on_forever)
