# this code is a macro looter for tibia
from pynput.mouse import Controller, Button, Listener
from pynput.keyboard import Controller as KeyboardController, Listener, Key
import time
import threading

# the array contains the points of the mouse for the macro, are 9 points
points = [(873, 373), (954, 375), (955, 456), (953, 535), (871, 535), (792, 536), (791, 453), (791, 373), (872, 456)]

mouse = Controller()
keyboard = KeyboardController()


def on_press(key):
    # in this function we get the key that is pressed and start the macro
    if key == Key.f11:
        t = threading.Thread(target=click_sequence) # thread are created to improve the performance
        t.start()

def click_sequence():
    # in click_sequence we move the mouse and click for each point in the array.
    # the keys in game for looting is shift + right click
    (x, y) = mouse.position

    keyboard.press(Key.shift)

    for point in points:
        mouse.position = point
        mouse.click(Button.right, 1)
        time.sleep(0.01)

    keyboard.release(Key.shift)
    mouse.position = (x, y)

# the listener is created to wait for a key to be pressed
with Listener(on_press=on_press) as listener:
   listener.join()