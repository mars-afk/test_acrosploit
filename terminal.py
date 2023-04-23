from colorama import Fore

green = Fore.GREEN
blue = Fore.BLUE
white = Fore.WHITE
red = Fore.RED
start_text = rf'''


                                         .__         .__  __    
_____    ___________  ____  ____________ |  |   ____ |__|/  |_  
\__  \ _/ ___\_  __ \/  _ \/  ___/\____ \|  |  /  _ \|  \   __\ 
 / __ \\  \___|  | \(  <_> )___ \ |  |_> >  |_(  <_> )  ||  |   
(____  /\___  >__|   \____/____  >|   __/|____/\____/|__||__|   
     \/     \/                 \/ |__|                          


'''


class Acroconsole:
    colors = []
    
    def __init__(self):

        self.colors = {
            "red":Fore.RED,
            "black":Fore.BLACK,
            "grey":Fore.LIGHTBLACK_EX,
            "blue":Fore.BLUE,
            "green":Fore.GREEN,
            "cyan":Fore.CYAN,
            "white":Fore.WHITE,
            "yellow":Fore.YELLOW,
            "heavenly":Fore.LIGHTYELLOW_EX

        }

    def clr(self,c,str):
        if self.colors[c] is not None:


            return f"{self.colors[c]}{str}"
            
        

       




        pass
    def start_up(self):
        print(self.clr("grey",start_text))


    def printsuccess(self,str):
        print(f"{blue}[{white}✔️{blue}] {white}{str}")

    def printerror(self,str):
        print(f"{red}[{white}❌{red}] {white}{str}")
    def printimportant(self,str):
        print(f"{blue}[{white}*{blue}] {white}{str}")
        


