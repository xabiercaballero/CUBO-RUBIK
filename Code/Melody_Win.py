import rp2
from machine import Pin
from rp2 import PIO
import time

@rp2.asm_pio(out_init=[PIO.OUT_LOW])
def echo():
    wrap_target()
    mov(pins, isr)     
    mov(isr, invert(isr))
    pull(noblock)      
    mov(x, osr)
    mov(y, x)
    label("loop")
    jmp(y_dec, "loop")  
    wrap()

sm = rp2.StateMachine(0, echo, freq=1_000_000, out_base=Pin(7))
sm.active(1)

def play(note, duration):
    if note:
        sm.put(1_000_000 // note)
        time.sleep(duration/30)
        sm.put(0)
        time.sleep(0.001)

# Melodia (Happy Bithday)
win_melody = [
    notes['C4'], notes['C4'], 
    notes['D4'], notes['C4'], notes['F4'],
    notes['E4'], notes['C4'], notes['C4'], 
    notes['D4'], notes['C4'], notes['G4'],
    notes['F4'], notes['C4'], notes['C4'],
  
    notes['C5'], notes['A4'], notes['F4'], 
    notes['E4'], notes['D4'], notes['AS4'], notes['AS4'],
    notes['A4'], notes['F4'], notes['G4'],
    notes['F4']
]

win_durations = [
    2, 4, 
    2, 2, 2,
    2, 2, 4, 
    2, 2, 2,
    1, 2, 4,
  
    2, 2, 2, 
    2, 2, 2, 4,
    2, 2, 2,
    1
]

# Reproducir melodia
for note, duration in zip(win_melody, win_durations):
    play(note, duration)
