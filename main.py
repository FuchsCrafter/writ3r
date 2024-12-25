import os,sys
from letterkit import LetterKit
from tkinter import *
from tkinter.ttk import *

global pendown_z, penup_z, is_rel, outpu_file, gcode

pendown_z = 57.2
penup_z = pendown_z +2

is_rel = False

outpu_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output", "output.gcode")

gcode = [
f"""
; DEFAULT CODE
G28; Home all axis
M106 S0; set fan 0 per cent
G21; mm units
G92 E0; Set the current extruder position to 0
G0 F2000; Set speed to 400 mm/min
G90; Initially set to absolute pos
G0 Z{penup_z}; Initially go to penup
; END DEFAULT CODE
"""
]

def command(command:str="; TBD"):
    global gcode
    gcode.append(command)


def gotoxy(x,y):
    command(f"G1 X{x} Y{y}; GOTOXY {x}|{y}")

def set_rel():
    global is_rel
    command("G91; Set to relative positioning")
    is_rel = True

def set_abs():
    global is_rel
    command("G90; Set to absolute positioning")
    is_rel = False


def penup():
    global penup_z
    _ = is_rel
    if (_): set_abs()
    command(f"G1 Z{penup_z}; PENUP")
    if (_): set_rel()

def pendown():
    global pendown_z
    _ = is_rel
    if(_): set_abs()
    command(f"G1 Z{pendown_z}; PENDOWN")
    if (_): set_rel()

def writeout():
    global gcode
    global outpu_file
    penup()
    f = open(outpu_file, "w")
    for el in gcode:
        f.write(el + "\n\n")
    f.close()

def transform_to_2d_list(original_list, n):
    return [original_list[i:i + n] for i in range(0, len(original_list), n)]


def main():
    global txtinp
    global gcode
    global current_y
    penup()

    letters = LetterKit()
    letters._pendown_z = pendown_z
    letters._penup_z = penup_z


    # Hier wird der Input gelesen und dann bereinigt, dass man am ende ein 2d-array hat, bei welchem jede "unterliste" 15 elemente hat (= 15 zeichen lang ist)
    allowlist = list("abcdefghijklmnopqrstuvwxyz ") # Liste mit zeichen die erlaubt sind (auch das leerzeichen)
    text = list(txtinp.get('1.0','end').lower()) # input einlesen und kleiner machen
    text = [el for el in text if el in allowlist] # filtern mithilfe der allowlist
    text = ["space" if el == " " else el for el in text] # alle leerzeichen mit "space" ersetzen wegen funktionsname
    text = transform_to_2d_list(text, 15) # EINE ZEILE => 15 ZEICHEN
    print(text)

    current_y = 270 # HÖCHSTER Y-WERT
    start_x = 15 # ABSTAND ZUM RAND BEIM START

    letters._set_abs()
    letters._gotoxy(start_x*10, current_y*10, "New line")
    letters._set_rel()



    for zeile in text:

        current_y = current_y -  12 # ZEILENHÖHE

        for el in zeile:
            getattr(letters, el)()
        

        letters._set_abs()
        letters._gotoxy(start_x*10, current_y*10, "New line")
        letters._set_rel()
    
    gcode.extend(letters.outputGcode())

        

    # for letter in 'abcdefg':
    #     getattr(letters, letter)()
    # 
    # gcode.extend(letters.outputGcode())

    
    # set_abs()
    # gotoxy(10, 185)
    # set_rel()


    penup()
    set_abs()
    command(f"G1 Z{penup_z+20}")


    writeout()



if __name__ == "__main__":

    root = Tk()
    root.geometry("300x450")
    root.title("writ3r")

    txtinp = Text(root)
    txtinp.pack(pady=5)

    writebtn = Button(root, text="Writeout", command=main)
    writebtn.pack(pady=5)



    root.mainloop()