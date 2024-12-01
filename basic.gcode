
G28; Home all axis

M106 S0; set fan 0 per cent

G21; mm units

G92 E0; Set the current extruder position to 0

G0 F2000; Set speed to 400 mm/min

; TODO: Might change
G90; Set Absolute positioning mode

G0 Z57.2; Move Z up to 57 mm / PENDOWN

; CODE HERE

; Make a vertical line that is 2 cm long
G0 Z70; PENUP
G0 X130 Y130; GOTOXY 120|130
G0 Z57.2; PENDOWN
G0 X130 Y150; GOTOXY 120|150
G0 Z70; PENUP

; Make a circle at 100|100
G0 X110 Y110;
G0 Z57.2; PENDOWN
G2 X110 Y110 I-7 J0; Clockwise arc to complete the circle
G0 Z70; PENUP

; CODE END

G4 P5000; wait 5 secs

; End of G-code
