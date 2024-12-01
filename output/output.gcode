
; DEFAULT CODE
G28; Home all axis
M106 S0; set fan 0 per cent
G21; mm units
G92 E0; Set the current extruder position to 0
G0 F2000; Set speed to 400 mm/min
G90; Initially set to absolute pos
G0 Z59.2; Initially go to penup
; END DEFAULT CODE


G1 Z59.2; PENUP

G1 X80 Y180; GOTOXY 80|180

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G90; Set to absolute positioning

G1 X80 Y150; GOTOXY 80|150

G91; Set to relative positioning

G90; Set to absolute positioning

G1 X80 Y120; GOTOXY 80|120

G91; Set to relative positioning

; LetterKit Gcode with scale of 1 

G91; Set to relative positioning

; Write Letter A

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y10.0; GOTO 5.0|10.0 

G1 X5.0 Y-10.0; GOTO 5.0|-10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-7.5 Y5.0; GOTO -7.5|5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X7.5 Y-5.0; GOTO 7.5|-5.0 

; End of Letter A

; Write Letter B

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y-5.0; GOTO 0.0|-5.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G1 X6.0 Y0.0; GOTO 6.0|0.0 

G1 X0.0 Y5.0; GOTO 0.0|5.0 

G1 X-6.0 Y0.0; GOTO -6.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X10.0 Y0.0; GOTO 10.0|0.0 

; End of Letter B

; Write Letter C

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X7.0 Y0.0; GOTO 7.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-7.0 Y-10.0; GOTO -7.0|-10.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X7.0 Y0.0; GOTO 7.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X3.0 Y0.0; GOTO 3.0|0.0 

; End of Letter C

; Letter D: Not implemented yet!

; Write letter E

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X6.0 Y0.0; GOTO 6.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-6.0 Y-5.0; GOTO -6.0|-5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X6.0 Y0.0; GOTO 6.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-6.0 Y-5.0; GOTO -6.0|-5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X6.0 Y0.0; GOTO 6.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X4.0 Y0.0; GOTO 4.0|0.0 

; End of letter E

; Write letter F

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X6.0 Y0.0; GOTO 6.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-6.0 Y-5.0; GOTO -6.0|-5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X4.0 Y5.0; GOTO 4.0|5.0 

; End of letter F

; Write letter G

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-2.0 Y-5.0; GOTO -2.0|-5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X2.0 Y0.0; GOTO 2.0|0.0 

G1 X0.0 Y-5.0; GOTO 0.0|-5.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X10.0 Y0.0; GOTO 10.0|0.0 

; End of letter G

; Write letter H

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X0.0 Y-5.0; GOTO 0.0|-5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X0.0 Y5.0; GOTO 0.0|5.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y-10.0; GOTO 0.0|-10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

; End of letter H

Wite letter I

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-5.0 Y10.0; GOTO -5.0|10.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-2.5 Y0.0; GOTO -2.5|0.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y-10.0; GOTO 0.0|-10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X7.5 Y0.0; GOTO 7.5|0.0 

; End of letter I

; Letter J: Not implemented yet!

; Write letter K

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X-5.0 Y-5.0; GOTO -5.0|-5.0 

G1 X5.0 Y-5.0; GOTO 5.0|-5.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

; End of letter K

; Write letter L

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X10.0 Y-10.0; GOTO 10.0|-10.0 

; End of letter L

; Write letter M

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G1 X2.5 Y-10.0; GOTO 2.5|-10.0 

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G1 X2.5 Y-10.0; GOTO 2.5|-10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

; End of letter M

; Write letter N

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G1 X2.5 Y-10.0; GOTO 2.5|-10.0 

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X7.5 Y-10.0; GOTO 7.5|-10.0 

; End of letter J

; Write letter O

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y-10.0; GOTO 0.0|-10.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X10.0 Y0.0; GOTO 10.0|0.0 

; End of letter O

; Write letter P

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y-5.0; GOTO 0.0|-5.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-10.0 Y-5.0; GOTO -10.0|-5.0 

; End of letter P

; Letter Q: Not implemented yet!

; Write letter R

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y-5.0; GOTO 0.0|-5.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G1 X-5.0 Y-5.0; GOTO -5.0|-5.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

; End of letter R

; Write letter S

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y5.0; GOTO 0.0|5.0 

G1 X-5.0 Y0.0; GOTO -5.0|0.0 

G1 X0.0 Y5.0; GOTO 0.0|5.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y-10.0; GOTO 5.0|-10.0 

; End of letter S

; Write letter T

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X-2.5 Y0.0; GOTO -2.5|0.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y-10.0; GOTO 0.0|-10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y0.0; GOTO 5.0|0.0 

; End of letter T

; Write letter U

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X0.0 Y-10.0; GOTO 0.0|-10.0 

G1 X5.0 Y0.0; GOTO 5.0|0.0 

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y-10.0; GOTO 5.0|-10.0 

; End of letter U

; Letter V: Not implemented yet!

; Write letter W

G1 X0.0 Y10.0; GOTO 0.0|10.0 

G90; Set to absolute positioning

G1 Z57.2; PENDOWN

G91; Set to relative positioning

G1 X2.5 Y-10.0; GOTO 2.5|-10.0 

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G1 X2.5 Y-10.0; GOTO 2.5|-10.0 

G1 X2.5 Y10.0; GOTO 2.5|10.0 

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G1 X5.0 Y-10.0; GOTO 5.0|-10.0 

; End of letter W

; Letter X: Not implemented yet!

; Letter Y: Not implemented yet!

; Letter Z: Not implemented yet!

G90; Set to absolute positioning

G1 Z59.2; PENUP

G91; Set to relative positioning

G90; Set to absolute positioning

G1 Z79.2

G1 Z59.2; PENUP

