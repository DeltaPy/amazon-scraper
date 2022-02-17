import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time
from os import system

print(" █████╗ ███╗   ███╗ █████╗ ███████╗ ██████╗ ███╗   ██╗      ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ ")
print("██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██╔═══██╗████╗  ██║      ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
print("███████║██╔████╔██║███████║  ███╔╝ ██║   ██║██╔██╗ ██║█████╗███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝")
print("██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║   ██║██║╚██╗██║╚════╝╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗")
print("██║  ██║██║ ╚═╝ ██║██║  ██║███████╗╚██████╔╝██║ ╚████║      ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║")
print("╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝      ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝")
print("By BassDrop07")
                                            
                                                                                                                                                    
url = input("Insert the product URL for which you want to do the tracking: ")
updateRate = int(input("Refresh every how many seconds: "))
print("Connecting to: " + url)
time.sleep(1)
system("cls")
print("Running!\tPress CTRL + C to STOP")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
while True:
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("[" +current_time+ "] [", end ='')

    result = str(soup.find(id="availability"))

    if 'Disponibilità immediata.' in result:
        print("Available" + "]", end ='')
        # requests.post("", data ={"content":"@everyone " + url + " E disponibileeeee!!!!!"}) //Discord webHook call
    else: 
        print("Not Avaialble!" + "]", end ='')
    if r.status_code == 200:
        print("["+"Request code: " + str(r.status_code) +"]")
    else: print("[" + "Request code: " + str(r.status_code) +"]")
    time.sleep(updateRate)
    

exit()