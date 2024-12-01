# from main import *

class LetterKit:
    # TODO: Implement letters D, J, Q, V, X, Y, Z
    def __init__(self, scale:int=1):

        self.size = scale
        self.scale = self.size
        self._gcode = [f"; LetterKit Gcode with scale of {self.size} "]
        self._cnc = False
        self._pendown_z = 57.2
        self._penup_z = self._pendown_z +4  

        self._rel = True
        self._set_rel()

    def _command(self, cmd:str) -> None:
        self._gcode.append(cmd)
    
    def _gotoxy(self, x, y, comment:str="") -> str:
        self._command(f"G{int(not self._cnc)} X{x/10} Y{y/10}; GOTO {(x*self.scale)/10}|{(y*self.scale)/10} {comment}") 
    
    def _set_rel(self):
        self._command("G91; Set to relative positioning")
        self._rel = True

    def _set_abs(self):
        self._command("G90; Set to absolute positioning")
        self._rel = False

    def _penup(self):
        was_rel = self._rel
        if was_rel: 
            self._set_abs()
        self._command(f"G1 Z{self._penup_z}; PENUP")
        if was_rel: 
            self._set_rel()

    def _pendown(self):
        was_rel = self._rel
        if was_rel: 
            self._set_abs()
        self._command(f"G1 Z{self._pendown_z}; PENDOWN")
        if was_rel: 
            self._set_rel()  

    
    """doc
        Alle Bushctaben MÜSSEN erwarten, dass der stift am anfang oben ist, und MÜSSEN den Stift am ende nach oben fahren!
        Alle buchstaben sind selbst für den abstand verantwortlich!
    """
        
    def a(self):
        self._command("; Write Letter A")
        self._pendown()
        self._gotoxy(50, 100)
        self._gotoxy(50, -100)
        self._penup()
        self._gotoxy(-75, 50)
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(75, -50)
        self._command("; End of Letter A")

    def b(self):
        self._command("; Write Letter B")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(50,0)
        self._gotoxy(0, -50)
        self._gotoxy(-50, 0)
        self._gotoxy(60, 0)
        self._gotoxy(0, 50)
        self._gotoxy(-60, 0)
        self._penup()
        self._gotoxy(100, 0)
        self._command("; End of Letter B")
    
    def c(self):
        self._command("; Write Letter C")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(70, 0)
        self._penup()
        self._gotoxy(-70, -100)
        self._pendown()
        self._gotoxy(70, 0)
        self._penup()
        self._gotoxy(30, 0)
        self._command("; End of Letter C")
    
    def d(self, acknowledge: bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter D: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter D not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter D is not implemented yet")

    def e(self): 
        self._command("; Write letter E")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(60, 0)
        self._penup()
        self._gotoxy(-60, -50)
        self._pendown()
        self._gotoxy(60, 0)
        self._penup()
        self._gotoxy(-60, -50)
        self._pendown()
        self._gotoxy(60,0)
        self._penup()
        self._gotoxy(40, 0)
        self._command("; End of letter E")
    
    def f(self):
        self._command("; Write letter F")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(60, 0)
        self._penup()
        self._gotoxy(-60, -50)
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(40, 50)
        self._command("; End of letter F")
    
    def g(self): 
        self._command("; Write letter G")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(-20, -50)
        self._pendown()
        self._gotoxy(20, 0)
        self._gotoxy(0, -50)
        self._gotoxy(-50, 0)
        self._penup()
        self._gotoxy(100, 0)
        self._command("; End of letter G")
    
    def h(self):
        self._command("; Write letter H")
        self._pendown()
        self._gotoxy(0, 100)
        self._penup()
        self._gotoxy(0, -50)
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(0, 50)
        self._pendown()
        self._gotoxy(0, -100)
        self._penup()
        self._gotoxy(50, 0)
        self._command("; End of letter H")

    def i(self):
        self._command("Wite letter I")
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(-50, 100)
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(-25, 0)
        self._pendown()
        self._gotoxy(0, -100)
        self._penup()
        self._gotoxy(75, 0)
        self._command("; End of letter I")
    
    def j(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter J: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter J not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter J is not implemented yet")
    
    def k(self):
        self._command("; Write letter K")
        self._pendown()
        self._gotoxy(0, 100)
        self._penup()
        self._gotoxy(50, 0)
        self._pendown()
        self._gotoxy(-50,-50)
        self._gotoxy(50,-50)
        self._penup()
        self._gotoxy(50, 0)
        self._command("; End of letter K")
    
    def l(self):
        self._command("; Write letter L")
        self._penup()
        self._gotoxy(50, 0)
        self._pendown()
        self._gotoxy(-50, 0)
        self._gotoxy(0, 100)
        self._penup()
        self._gotoxy(100, -100)
        self._command("; End of letter L")
    
    def m(self):
        self._command("; Write letter M")
        self._pendown()
        self._gotoxy(25, 100)
        self._gotoxy(25, -100)
        self._gotoxy(25, 100)
        self._gotoxy(25, -100)
        self._penup()
        self._gotoxy(50, 0)
        self._command("; End of letter M")
    
    def n(self):
        self._command("; Write letter N")
        self._pendown()
        self._gotoxy(25, 100)
        self._gotoxy(25, -100)
        self._gotoxy(25, 100)
        self._penup()
        self._gotoxy(75, -100)
        self._command("; End of letter J")
    
    def o(self):
        self._command("; Write letter O")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(50, 0)
        self._gotoxy(0, -100)
        self._gotoxy(-50, 0)
        self._penup()
        self._gotoxy(100, 0)
        self._command("; End of letter O")
    
    def p(self):
        self._command("; Write letter P")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(50, 0)
        self._gotoxy(0, -50)
        self._gotoxy(-50, 0)

        self._penup()
        self._gotoxy(-100, -50)
        self._command("; End of letter P")
    
    def q(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter Q: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter Q not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter Q is not implemented yet")

    def r(self):
        self._command("; Write letter R")
        self._pendown()
        self._gotoxy(0, 100)
        self._gotoxy(50, 0)
        self._gotoxy(0, -50)
        self._gotoxy(-50, 0)
        self._gotoxy(-50, -50)
        self._penup()
        self._gotoxy(50, 0)
        self._command("; End of letter R")
    
    def s(self): # TODO: Besser machen
        self._command("; Write letter S")
        self._pendown()
        self._gotoxy(50,0)
        self._gotoxy(0,50)
        self._gotoxy(-50, 0)
        self._gotoxy(0,50)
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(50, -100)
        self._command("; End of letter S")
    
    def t(self):
        self._command("; Write letter T")
        self._gotoxy(0, 100)
        self._pendown()
        self._gotoxy(50, 0)
        self._penup()
        self._gotoxy(-25, 0)
        self._pendown()
        self._gotoxy(0, -100)
        self._penup()
        self._gotoxy(50, 0)
        self._command("; End of letter T")
    
    def u(self):
        self._command("; Write letter U")
        self._gotoxy(0, 100)
        self._pendown()
        self._gotoxy(0, -100)
        self._gotoxy(50, 0)
        self._gotoxy(0, 100)
        self._penup()
        self._gotoxy(50, -100)
        self._command("; End of letter U")

    def v(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter V: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter V not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter V is not implemented yet")
    
    def w(self):
        self._command("; Write letter W")
        self._gotoxy(0, 100)
        self._pendown()
        self._gotoxy(25, -100)
        self._gotoxy(25, 100)
        self._gotoxy(25, -100)
        self._gotoxy(25, 100)
        self._penup()
        self._gotoxy(50, -100)
        self._command("; End of letter W")

    def x(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter X: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter X not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter X is not implemented yet")

    def y(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter Y: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter Y not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter Y is not implemented yet")


    def z(self, acknowledge:bool=False) -> NotImplementedError:
        # TODO: Implement letter
        self._command("; Letter Z: Not implemented yet!")
        if not acknowledge:
            raise NotImplementedError("Letter Z not implemented yet! Aborting!\nYou may skip this by setting acknowledge to True!")
        else: 
            print("Please note that the letter Z is not implemented yet")
    
    def space(self):
        self._command("; Blank space 1cm")
        self._penup()
        self._gotoxy(100, 0)
        self._penup()
        self._command("; End of space")
    

if __name__ == "__main__":
    print("Executing main function of LetterKit")
    pendown_z = 57.2
    penup_z = pendown_z +4  

