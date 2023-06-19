import math
from pynput import keyboard

def openfile(file):
    with open('./txt/'+file+'.txt', 'r') as f:
        ofile = int(f.readlines()[0])
    return ofile

def writefile(file, wfile):
    with open('./txt/'+file+'.txt', 'w') as f:
        f.write(str(wfile))

def on_press(key):
    if key == keyboard.Key.ctrl:
        clicks = openfile('clicks')
        builds = openfile('builds')

        clicks = clicks + int(1.4 ** builds)
        writefile('clicks', clicks)
        print(int(clicks))

    elif key == keyboard.Key.shift:
        clicks = openfile('clicks')
        builds = openfile('builds')
        price = openfile('price')

        if clicks >= price:
            clicks = clicks - price
            builds = builds + 1
            price = int(math.ceil(price * math.exp(1/4)))

            writefile('builds', builds)
            writefile('price', price)
            writefile('clicks', clicks)
            print(f"Rakennuksia: {builds}\n- Seuraava hinta: {price}")

        else:
            print("Hinta: ", price)

    elif key == keyboard.Key.esc:
        exit()

print("Tervetuloa! Paina Ctrl clikkaaksei ja Shift ostaaksesi uusia rakennuksia.")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
