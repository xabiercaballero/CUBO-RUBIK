import rp2
from machine import Pin
from rp2 import PIO
import time

def Turn_On_Buzzer():
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

    # Definir las notas musicales
    notes = {
        'B0': 31, 'C1': 33, 'CS1': 35, 'D1': 37, 'DS1': 39, 'E1': 41, 'F1': 44, 'FS1': 46, 'G1': 49, 'GS1': 52, 'A1': 55, 'AS1': 58, 'B1': 62,
        'C2': 65, 'CS2': 69, 'D2': 73, 'DS2': 78, 'E2': 82, 'F2': 87, 'FS2': 93, 'G2': 98, 'GS2': 104, 'A2': 110, 'AS2': 117, 'B2': 123,
        'C3': 131, 'CS3': 139, 'D3': 147, 'DS3': 156, 'E3': 165, 'F3': 175, 'FS3': 185, 'G3': 196, 'GS3': 208, 'A3': 220, 'AS3': 233, 'B3': 247,
        'C4': 262, 'CS4': 277, 'D4': 294, 'DS4': 311, 'E4': 330, 'F4': 349, 'FS4': 370, 'G4': 392, 'GS4': 415, 'A4': 440, 'AS4': 466, 'B4': 494,
        'C5': 523, 'CS5': 554, 'D5': 587, 'DS5': 622, 'E5': 659, 'F5': 698, 'FS5': 740, 'G5': 784, 'GS5': 831, 'A5': 880, 'AS5': 932, 'B5': 988,
        'C6': 1047, 'CS6': 1109, 'D6': 1175, 'DS6': 1245, 'E6': 1319, 'F6': 1397, 'FS6': 1480, 'G6': 1568, 'GS6': 1661, 'A6': 1760, 'AS6': 1865, 'B6': 1976,
        'C7': 2093, 'CS7': 2217, 'D7': 2349, 'DS7': 2489, 'E7': 2637, 'F7': 2794, 'FS7': 2960, 'G7': 3136, 'GS7': 3322, 'A7': 3520, 'AS7': 3729, 'B7': 3951,
        'C8': 4186, 'CS8': 4435, 'D8': 4699, 'DS8': 4978
    }

    # Definir la melodia y sus duraciones

   

    
    # Melodia (Mario Bross)
    melody = [
        notes['E5'], notes['E5'], None, notes['E5'], None, notes['C5'], notes['E5'],
        notes['G5'], None, notes['G4'], None, 
        notes['C5'], notes['G4'], None, notes['E4'],
        notes['A4'], notes['B4'], notes['AS4'], notes['A4'],
        notes['G4'], notes['E5'], notes['G5'], notes['A5'], notes['F5'], notes['G5'],
        None, notes['E5'], notes['C5'], notes['D5'], notes['B4'],
        notes['C5'], notes['G4'], None, notes['E4'],
        notes['A4'], notes['B4'], notes['AS4'], notes['A4'],
        notes['G4'], notes['E5'], notes['G5'], notes['A5'], notes['F5'], notes['G5'],
        None, notes['E5'], notes['C5'], notes['D5'], notes['B4'],
        
        None, notes['G5'], notes['FS5'], notes['F5'], notes['DS5'], notes['E5'],
        None, notes['GS4'], notes['A4'], notes['C4'], None, notes['A4'], notes['C5'], notes['D5'],
        None, notes['DS5'], None, notes['D5'],
        notes['C5'], None,
        
        None, notes['G5'], notes['FS5'], notes['F5'], notes['DS5'], notes['E5'],
        None, notes['GS4'], notes['A4'], notes['C4'], None, notes['A4'], notes['C5'], notes['D5'],
        None, notes['DS5'], None, notes['D5'],
        notes['C5'], None,
        
        notes['C5'], notes['C5'], notes['C5'], None, notes['C5'], notes['D5'],
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        
        notes['C5'], notes['C5'], notes['C5'], None, notes['C5'], notes['D5'], notes['E5'],
        None, 
        notes['C5'], notes['C5'], notes['C5'], None, notes['C5'], notes['D5'],
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        notes['E5'], notes['E5'], None, notes['E5'], None, notes['C5'], notes['E5'],
        notes['G5'], None, notes['G4'], None, 
        notes['C5'], notes['G4'], None, notes['E4'],
        
        notes['A4'], notes['B4'], notes['AS4'], notes['A4'],
        notes['G4'], notes['E5'], notes['G5'], notes['A5'], notes['F5'], notes['G5'],
        None, notes['E5'], notes['C5'], notes['D5'], notes['B4'],
        
        notes['C5'], notes['G4'], None, notes['E4'],
        notes['A4'], notes['B4'], notes['AS4'], notes['A4'],
        notes['G4'], notes['E5'], notes['G5'], notes['A5'], notes['F5'], notes['G5'],
        None, notes['E5'], notes['C5'], notes['D5'], notes['B4'],
        
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['D5'], notes['A5'], notes['A5'], notes['A5'], notes['G5'], notes['F5'],
        
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['B4'], notes['F5'], notes['F5'], notes['F5'], notes['E5'], notes['D5'],
        notes['C5'], notes['E4'], notes['E4'], notes['C4'],
        
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['D5'], notes['A5'], notes['A5'], notes['A5'], notes['G5'], notes['F5'],
        
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['B4'], notes['F5'], notes['F5'], notes['F5'], notes['E5'], notes['D5'],
        notes['C5'], notes['E4'], notes['E4'], notes['C4'],
        notes['C5'], notes['C5'], notes['C5'], None, notes['C5'], notes['D5'], notes['E5'],
        None,
        
        notes['C5'], notes['C5'], notes['C5'], None, notes['C5'], notes['D5'],
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        notes['E5'], notes['E5'], None, notes['E5'], None, notes['C5'], notes['E5'],
        notes['G5'], None, notes['G4'], None, 
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['D5'], notes['A5'], notes['A5'], notes['A5'], notes['G5'], notes['F5'],
        
        notes['E5'], notes['C5'], notes['A4'], notes['G4'],
        notes['E5'], notes['C5'], notes['G4'], None, notes['GS4'],
        notes['A4'], notes['F5'], notes['F5'], notes['A4'],
        notes['B4'], notes['F5'], notes['F5'], notes['F5'], notes['E5'], notes['D5'],
        notes['C5'], notes['E4'], notes['E4'], notes['C4'],
        
        # Sonido de Game Over
        notes['C5'], notes['G4'], notes['E4'],
        notes['A4'], notes['B4'], notes['A4'], notes['GS4'], notes['AS4'], notes['GS4'],
        notes['G4'], notes['D4'], notes['E4']
    ]

    durations = [
        8, 8, 8, 8, 8, 8, 8,
        4, 4, 8, 4, 
        4, 8, 4, 4,
        4, 4, 8, 4,
        8, 8, 8, 4, 8, 8,
        8, 4, 8, 8, 4,
        4, 8, 4, 4,
        4, 4, 8, 4,
        8, 8, 8, 4, 8, 8,
        8, 4, 8, 8, 4,
        
        4, 8, 8, 8, 4, 8,
        8, 8, 8, 8, 8, 8, 8, 8,
        4, 4, 8, 4,
        2, 2,
        
        4, 8, 8, 8, 4, 8,
        8, 8, 8, 8, 8, 8, 8, 8,
        4, 4, 8, 4,
        2, 2,
        
        8, 4, 8, 8, 8, 4,
        8, 4, 8, 2,
        
        8, 4, 8, 8, 8, 8, 8,
        1, 
        8, 4, 8, 8, 8, 4,
        8, 4, 8, 2,
        8, 8, 8, 8, 8, 8, 4,
        4, 4, 4, 4, 
        4, 8, 4, 4,
        
        4, 4, 8, 4,
        8, 8, 8, 4, 8, 8,
        8, 4, 8, 8, 4,
        
        4, 8, 4, 4,
        4, 4, 8, 4,
        8, 8, 8, 4, 8, 8,
        8, 4, 8, 8, 4,
        
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 8, 8, 8, 8, 8,
        
        8, 4, 8, 2,
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 4, 8, 8, 8, 8,
        8, 4, 8, 2,
        
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 8, 8, 8, 8, 8,
        
        8, 4, 8, 2,
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 4, 8, 8, 8, 8,
        8, 4, 8, 2,
        8, 4, 8, 8, 8, 8, 8,
        1,
        
        8, 4, 8, 8, 8, 4,
        8, 4, 8, 2,
        8, 8, 8, 8, 8, 8, 4,
        4, 4, 4, 4, 
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 8, 8, 8, 8, 8,
        
        8, 4, 8, 2,
        8, 4, 8, 4, 4,
        8, 4, 8, 2,
        8, 4, 8, 8, 8, 8,
        8, 4, 8, 2,
        
        # Sonido de Game Over
        4, 4, 4,
        8, 8, 8, 8, 8, 8,
        8, 8, 2
    ]



    ## Reproducción sin duraciones
    # def play(note, duration):
    #   if note:
    #     sm.put(1_000_000//note)
    #   else:
    #     sm.put(0)
    cont=0
    def play(note, duration):
        if note:
            sm.put(1_000_000 // note)
            time.sleep(duration/30)
            sm.put(0)
            time.sleep(0.001)

    # # Reproducir melodia
    # for i, note, duration in enumerate(melody):
    #     play(int(melody[i]), float(durations[i]))

    # Reproducir melodia
    for note, duration in zip(melody, durations):
        play(note, duration)
