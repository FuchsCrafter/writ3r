
; DEFAULT CODE
G28; Home all axis
M106 S0; set fan 0 per cent
G21; mm units
G92 E0; Set the current extruder position to 0
G0 F2000; Set speed to 400 mm/min
G90; Initially set to absolute pos
G0 Z61.2; Initially go to penup
; END DEFAULT CODE


G1 Z61.2; PENUP

G1 X150 Y150; GOTOXY 150|150

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0 Y10; GOTOXY 0|10

G1 X0 Y-5; GOTOXY 0|-5

G1 X5 Y0; GOTOXY 5|0

G1 X0 Y5; GOTOXY 0|5

G1 X0 Y-10; GOTOXY 0|-10

G90; Set to absolute positioning

G1 Z61.2; PENUP

G91; Set to relative positioning

G1 X5 Y0; GOTOXY 5|0

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0 Y10; GOTOXY 0|10

G90; Set to absolute positioning

G1 Z61.2; PENUP

G91; Set to relative positioning

G90; Set to absolute positioning

G1 Z61.2; PENUP

G91; Set to relative positioning

