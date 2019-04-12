import pygame
import pygame.midi
from time import sleep

# Initialize the Pygame and pygame.midi modules
pygame.init()
pygame.midi.init()
startSong = pygame.midi.midis2events("pianomidi.mid", -1)


def reader(startSong):
  while startSong.hasNext:
    if startSong.byte1 == 0x9:
        handleNotes(
        startSong.byte1,
        startSong.byte2,
        startSong.byte3
        );
        print(handleNotes())
        break
    break


def handleNotes(channel, pitch, velocity):
  port = 0;
  latency = 1;
  instrument = 0
  velocity = 127
  midiOutput = pygame.midi.Output(port, latency)
  midiOutput.set_instrument(instrument)
  if pitch == 24:
    midiOutput = pygame.midi.Output(2, 1)
  if pitch == 25:
    midiOutput = pygame.midi.Output(3, 1)
  if pitch == 26:
    midiOutput = pygame.midi.Output(7, 1)
  if pitch == 27:
    midiOutput = pygame.midi.Output(8, 1)
  if pitch == 28:
    midiOutput = pygame.midi.Output(10, 1)
  if pitch == 29:
    midiOutput = pygame.midi.Output(11, 1)
  if pitch == 30:
    midiOutput = pygame.midi.Output(12, 1)

  for note in range(24, 30):
    midiOutput.note_on(note, velocity)
    sleep(.25)
    midiOutput.note_off(note, velocity)


print(reader(startSong))
pygame.midi.quit()
