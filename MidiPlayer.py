import mido
from mido import MidiFile
from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)


mid = MidiFile('solitudeineminor.mid')

def reader():
    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if msg.is_meta:
                pass
            else:
                if msg.type == 'note_on':
                    m = msg.bytes()
                    for bytes in m:
                        print (bytes)       # Printing just to confirm message is being read
                        handleNotes(bytes, bytes, bytes)
                print(msg)      # Again printing to check its reading correctly




def handleNotes(channel, note, velocity):
  if note == 65: # Change the note range to 1 value
    GPIO_PIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 69:
    GPIO_PIN = 27
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 72:
    GPIO_PIN = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 76:
    GPIO_PIN = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 79:
    GPIO_PIN = 24
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 83:
    GPIO_PIN = 26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)
  if note == 86:
    GPIO_PIN = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    GPIO.output(GPIO_PIN, GPIO.HIGH)
    sleep(.25)
    GPIO.output(GPIO_PIN, GPIO.LOW)



reader()