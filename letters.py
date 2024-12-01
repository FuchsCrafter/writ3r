# from main import *

pendown_z = 57.2
penup_z = pendown_z +4

class LetterKit:
    def __init__(self, scale:int=1):
        self.size = scale
        self.scale = self.size
        self._gcode = [f"; LetterKit Gcode with scale of {self.size} "]
        self._rel = False
        self._cnc = False

    def _command(self, cmd:str) -> None:
        self._gcode.append(cmd)
    
    def _gotoxy(self, x, y) -> str:
        self._command(f"G{int(not self._cnc)} X{x} Y{y}; GOTO {x*self.scale}|{y*self.scale}") 
    
    def _set_rel(self):
        self._command("G91; Set to relative positioning")
        self._rel = True

    def _set_abs(self):
        self._command("G90; Set to absolute positioning")
        self._rel = False

    def _penup(self):
        global penup_z

        _ = self._rel
        if (_): self._set_abs()
        self._command(f"G1 Z{penup_z}; PENUP")
        if (_): self._set_rel()

    def _pendown(self):
        global pendown_z

        _ = self._rel
        if(_): self._set_abs()
        self._command(f"G1 Z{pendown_z}; PENDOWN")
        if (_): self._set_rel()      
        

