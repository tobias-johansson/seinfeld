import os
import random
import time
import RPi.GPIO as io
import pygame.mixer as m

sounds = ["sound/" + f for f in os.listdir("sound")]
print sounds

m.init()
# m.music.load("Seinfeld.ogg")

io.setmode(io.BCM)

door_sensor = 2
# io.setup(door_sensor, io.IN, pull_up_down=io.PUD_UP)
io.setup(door_sensor, io.IN)

print m.music.get_volume()

doorOpen = False
while True:
  closed = not io.input(door_sensor)
  if doorOpen and closed:
    doorOpen = False
    print "Closed"
    print "Stop!"
    m.music.fadeout(2000)
  elif not doorOpen and not closed:
    doorOpen = True
    print "Opened"
    print "Play!"
    m.music.load(random.choice(sounds))
    m.music.play(start=0.0)
  time.sleep(0.1)

