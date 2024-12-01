import os,sys
from letterkit import LetterKit

global pendown_z, penup_z, is_rel, outpu_file

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

if __name__ == "__main__":
    penup()
    gotoxy(80,180)
    pendown()

    set_rel()

    letters = LetterKit()
    letters._pendown_z = pendown_z
    letters._penup_z = penup_z

    letters.h()
    letters.a()
    letters.l()
    letters.l()
    letters.o()
    letters.space()
    letters.w()
    letters.e()
    letters.l()
    letters.t()

    gcode.extend(letters._gcode)

    penup()


    writeout()