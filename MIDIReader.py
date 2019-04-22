import mido
from mido import MidiFile
import pygame
import pygame.midi
from time import sleep

# Initialize the Pygame and pygame.midi modules
pygame.init()
pygame.midi.init()




mid = MidiFile('pianomidi.mid')

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
  port = 0
  instrument = 0
  midiOutput = pygame.midi.Output(port, velocity)
  midiOutput.set_instrument(instrument)
  if note >= 0 & note < 39: # Change the note range to 1 value
    port = 2
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 39 & note < 54:
    port = 3
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 54 & note < 69:
    port = 7
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 69 & note < 84:
    port = 8
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 84 & note < 99:
    port = 10
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 99 & note < 114:
    port = 11
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)
  if note >= 114:
    port = 12
    midiOutput.note_on(port, velocity)
    sleep(.25)
    midiOutput.note_off(port, velocity)



reader()
