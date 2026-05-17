#https://docs.micropython.org/en/latest/esp32/quickref.html
#https://docs.micropython.org/en/latest/library/index.html

#conferir compatibilidade

#libraries
import machine
import time
import random

#modulos
buzzer = machine.PWM(machine.Pin(13))
sensor = machine.Pin(14, machine.Pin.IN)

#SONS
#apelidos frequencias
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
G2 = 98
#relações
def tone(pin, frequency, duration):
    pin.freq(frequency)
    pin.duty(200)#modo de operação, valor = volume [0, 1023]
    time.sleep_ms(duration)
    #milissegundos
    pin.duty(0) #terminar

#soooongs :p
def awn_sensor():
    tone(buzzer, D4, 200)
    time.sleep_ms(100)
    tone(buzzer, G4, 50)
def gaaah():
    tone(buzzer, G2, 3000)
def conected():
    tone(buzzer, F4, 600)
    time.sleep_ms(100)
    tone(buzzer, FS4, 200)
    tone(buzzer, D4, 100)
    tone(buzzer, DS4, 100)
    tone(buzzer, GS4, 200)
def understood_song():
    tone(buzzer, F4, 600)
    time.sleep_ms(100)
    tone(buzzer, FS4, 200)
    tone(buzzer, G4, 200)
    tone(buzzer, GS4, 200)
def offended_song():
    tone(buzzer, E4, 500)
    time.sleep_ms(100)
    tone(buzzer, DS4, 200)
    tone(buzzer, D4, 200)
    tone(buzzer, C4, 200)
def song_distracted1():
    pass
    #inventa?
def song_distracted2():
    pass#traduzir mais uma ai
def song_distracted3():
    pass

def rand_responses():
    x = random.randint(1, 12)
    if x <=1:
        gaaah()
    elif x <=2:
        offended_song()
    else:
        awn_sensor()

understood_song()
#loop sensor
no_sense = 0

while True:
    yes_sense = sensor.value()

    if yes_sense == 1 and no_sense == 0:
        rand_responses()

    no_sense = yes_sense
    time.sleep_ms(500) #espera 0,5 seg antes de checar dnv
    #se pah meo.....
    # y= sensor (ou 1 ou 0)
    # if y = 1 e n = 0
    # tocar som
    # uuuh
    # n = 0 = y
    # dorme caraio()
