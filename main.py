import colorama  , art , tabulate
import time
from tqdm import tqdm
import os
import threading
import requests
from terminal import Acroconsole
#import simple_term_menu

console = Acroconsole()
colorama.init()
cur_dir = os.getcwd()

console.start_up()



#HOST_PATTERN = "\ *host\ *=\ *[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}"
#PORT_PATTERN = "\ *port\ *=\ *[0-9]{1,65000}"

'''

      ngrok_start = threading.Thread(target=start_ngrok,args=("a",))
                       
                       dashboard = threading.Thread(target=start_dashboard,args=("a",))
                       dashboard.start()
                       
                       ngrok_start.start()

'''

console.printimportant("Acrosploit has started with some limitations.")





def start_ngrok():
     os.system(f"ngrok http 3001")



def start_dashboard():
    os.system(f"node {cur_dir}\\Acroweb\\index.js")



def mainf():
     pass
   
     

                    

                                 
                    

                    

                  
                



    

mainf()



#1 USE HTTP WEB AS SERVER (HOST)
#2 USE PROGRAM AS CLIENT (use payload generator for client python file and send it to your target)