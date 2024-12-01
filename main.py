import os,sys

global pendown_z, penup_z, is_rel, outpu_file

pendown_z = 57.2
penup_z = pendown_z +4

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
    gotoxy(150,150)
    pendown()

    set_rel()

    # H Buchstabe
    gotoxy(0, 10) # h strich hoch
    gotoxy(0, -5) # hälfte runter
    gotoxy(5,0) # zur seite
    gotoxy(0,5) # hoch
    gotoxy(0,-10) # runter

    # I buchstabe
    penup()
    gotoxy(5,0) # zur seite
    pendown() 
    gotoxy(0,10) # hoch

    penup()


    writeout()