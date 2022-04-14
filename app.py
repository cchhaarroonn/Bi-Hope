import pymem
import pymem.process
import keyboard
import time
from colorama import Fore

dwLocalPlayer = 0xDB65DC
dwForceJump = 0x527C38C
m_fFlags = 0x104
RESET = Fore.RESET
BLUE = Fore.BLUE

print(f"""{BLUE}

$$$$$$$\  $$\         $$\   $$\                               
$$  __$$\ \__|        $$ |  $$ |                              
$$ |  $$ |$$\         $$ |  $$ | $$$$$$\   $$$$$$\   $$$$$$\  
$$$$$$$\ |$$ |$$$$$$\ $$$$$$$$ |$$  __$$\ $$  __$$\ $$  __$$\ 
$$  __$$\ $$ |\______|$$  __$$ |$$ /  $$ |$$ /  $$ |$$$$$$$$ |
$$ |  $$ |$$ |        $$ |  $$ |$$ |  $$ |$$ |  $$ |$$   ____|
$$$$$$$  |$$ |        $$ |  $$ |\$$$$$$  |$$$$$$$  |\$$$$$$$\ 
\_______/ \__|        \__|  \__| \______/ $$  ____/  \_______|
                                          $$ |                
                                          $$ |                
                                          \__|                          
{RESET}
""")

hotkey = str(input("Hotkey: "))


pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

while True:
    if keyboard.is_pressed("escape"):
        exit()

    if keyboard.is_pressed(hotkey):
        force_jump = client+dwForceJump
        player = pm.read_int(client+dwLocalPlayer)
        onGround = pm.read_int(player+m_fFlags)
        if player and onGround and onGround == 257:
            pm.write_int(force_jump, 6)
            time.sleep(0.08)
            pm.write_int(force_jump, 6)
