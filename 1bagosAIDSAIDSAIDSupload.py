#https://docs.micropython.org/en/latest/esp32/quickref.html
#https://docs.micropython.org/en/latest/library/index.html

#olá pequeno B4G0, bem vindo ao meu quarto.

#libraries
import machine
import time
import random
import math

import network
import socket

#modulos
buzzer = machine.PWM(machine.Pin(13))
sensor = machine.Pin(14, machine.Pin.IN)
#adaptar motor e definiçoes de conjuntos de moves
#inserir sistema de senha....

#SONS : Definiçoes q tow usando veyr
#A4 = 440Hz como referência

NOTES = {
    "C": -9,
    "CS": -8,
    "D": -7,
    "DS": -6,
    "E": -5,
    "F": -4,
    "FS": -3,
    "G": -2,
    "GS": -1,
    "A": 0,
    "AS": 1,
    "B": 2
}


def freq(note, octave):
    #A4 = 440Hz como referência:
    n = NOTES[note] + (octave - 4) * 12
    #n = quantidade de semitons distante do A4
    return round(440 * (2 ** (n / 12)))
    #arredonfar f=440(2⁽n/12⁾)
    #f=frequencia respondida

#relações
volume = 740
def tone(pin, frequency, duration):
    pin.freq(frequency)
    pin.duty(volume)#modo de operação, valor = volume [0, 1023]
    time.sleep_ms(duration)
    #milissegundos
    pin.duty(0) #terminar

#atalho
def play(note, octave, duration):
    tone(buzzer, freq(note, octave), duration)

#soooongs :p
def awn_sensor():
    play("D", 4, 300)
    time.sleep_ms(100)
    play("G", 4, 100)
def gaaah():
    play("G", 2, 3000)
def understood_song():
    play("F", 4, 600)
    time.sleep_ms(100)
    play("FS", 4, 200)
    play("G", 4, 200)
    play("GS", 4, 200)
def offended_song():
    play("E", 4, 500)
    time.sleep_ms(100)
    play("DS", 4, 200)
    play("D", 4, 200)
    play("C", 4, 200)

def working():
    play("A", 5, 200)
def nworking():
    play("C", 4, 200)

def alert():
    for _ in range (3):
        play("B", 4, 200)
        play("E", 5, 200)
def hello():
    play("G", 4, 200)
    play("E", 4, 500)

def rand_responses():
    x = random.randint(1, 12)
    if x <=1:
        gaaah()
    elif x <=2:
        offended_song()
    else:
        awn_sensor()

#LAN MODE
wifi_connected = False
s = None
no_sense = 0

#conecta wifi
ssid = "NetTri-Jair"
key = "beterrabaazul"
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig((
    "#ip pessoal", #ip pessoal, 67= ip esp
    "255.255.255.0", #formato/mascara
    "#ip do roteador", #roteador
    "#ip do roteador"
))

if not wlan.isconnected():
    wlan.connect(ssid, key)

for _ in range(50):
    if wlan.isconnected():
        wifi_connected = True
        break
    time.sleep_ms(100)
    

if wifi_connected:
    print("wifi working")
    working()

    # só inicializa o socket se a rede estiver funcionando
    try:
        s = socket.socket()
        s.bind(("0.0.0.0", 6767))
        s.listen(1)
        s.settimeout(0.01) 
        print("servidor 6767 pronto")
        working()
    except Exception as e:
        print("erro socket:", e)
        nworking()
else:
    print("nao foi possivel conectar")
    nworking()
#loop
while True:

    y = sensor.value()

    if y == 1 and no_sense == 0:
        rand_responses()

    no_sense = y
    # y= sensor (ou 1 ou 0)
    # if y = 1 e n = 0
    # trocar volume e tocar som


    if wifi_connected and s is not None:
        user = None
        try:
            user, addr = s.accept()
            req = user.recv(1024)
            response = "aguardando comandos"

            if req:
                req = req.decode()

                if "/ALERT" in req:
                    alert()
                    response = "comando recebido"
                elif "/MIDDLEF" in req:
                    offended_song()
                    response = "comando recebido"
                elif "/HELLO" in req:
                    hello()
                    response = "comando recebido"
                elif "/VOLUME" in req:
                    if volume == 500:
                        volume = 100
                    else:
                        volume = 500
                    rand_responses()
                    response = "comando recebido"
                elif "/SILENCE" in req:
                    volume = 0
                    response = "comando recebido"
  
                #responde em HTTP padrão para o pc
                user.send(
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: text/plain\r\n"
                    "Connection: close\r\n"
                    "\r\n"
                    + response)

            user.close() 

        except OSError:
            #cai aqui se n tiver comando
            pass
        except Exception as e:
            print(e)
            pass

    time.sleep_ms(10)