import math
from pynput import keyboard

def openfile(file):
    ofile = 0
    with open('/home/smarttin/Documents/terminalclicker ja random huuhaata/peleja/txt/'+file+'.txt', 'r') as f:
        ofile = float(f.readlines()[0])
    f.close()
    return ofile

def writefile(file, wfile):
    with open('/home/smarttin/Documents/terminalclicker ja random huuhaata/peleja/txt/'+file+'.txt', 'w') as g:
        g.write(str(wfile))
    g.close()

def on_press(Key):
    
    if Key == keyboard.Key.ctrl:
        clicks = openfile('clicks')
        builds = openfile('builds')

        clicks = clicks + int(1.4 ** builds)
        writefile('clicks', clicks)
        print(int(clicks))

    elif Key == keyboard.Key.shift:
        clicks = openfile('clicks')
        builds = openfile('builds')
        price = openfile('price')
        priceceil = int(math.ceil(price))

        if clicks >= priceceil:
            clicks = clicks - priceceil
            builds = builds + 1
            #price = price ** (107.5/100)
            price = math.factorial(builds)/(builds**builds) + 15 #lol ei

            writefile('builds', builds)
            writefile('price', price)
            writefile('clicks', clicks)
            print("Rakennuksia: ", int(builds))

        else:
            print("Hinta: ", priceceil)

print("Tervetuloa! Paina Ctrl clikkaaksei ja Shift ostaaksesi uusia rakennuksia.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()