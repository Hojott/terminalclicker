import math
from pynput import keyboard

def openfile(file):
    ofile = 0
    with open('./txt/'+file+'.txt', 'r') as f:
        ofile = int(f.readlines()[0])
    f.close()
    return ofile

def writefile(file, wfile):
    with open('./txt/'+file+'.txt', 'w') as g:
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

        if clicks >= price:
            clicks = clicks - price
            builds = builds + 1
            #price = int(math.ceil(price ** (107.5/100)))
            price = int(math.ceil(math.factorial(builds)/(builds**builds)) + 15) #lol ei

            writefile('builds', builds)
            writefile('price', price)
            writefile('clicks', clicks)
            print("Rakennuksia: ", int(builds))

        else:
            print("Hinta: ", price)

print("Tervetuloa! Paina Ctrl clikkaaksei ja Shift ostaaksesi uusia rakennuksia.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
