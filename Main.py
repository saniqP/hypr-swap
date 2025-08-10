import time
import os
import subprocess, json
from Files.check import is_package_installed
from Files.install import install

def get_hyprland_monitors():
    result = subprocess.run(["hyprctl", "monitors", "-j"], capture_output=True, text=True)
    monitors = json.loads(result.stdout)
    return monitors

image_path = "~/BG.png"
path = os.path.expanduser("~/.config/hypr/hyprpaper.conf")
monitors = get_hyprland_monitors()

print("=================HYPR-SWAP=================")
print('------------Cheking   Hyprpaper------------')
print("[*]start cheking")
time.sleep(2)
print("[#]end cheking")
if not is_package_installed("hyprpaper"):
    print("[*]start installed hyprpaper")
    install()
    
    
print('------------Deleting old config------------')
os.system(f"rm -r {path}")
print('[#]config deleted')
time.sleep(2)
print('------------Creating new config------------')
os.system(f"touch {path}")
print("[#]config created")
time.sleep(2)
image_path = input("[*] Enter path: ")
print(f"[#] {path}")
time.sleep(3)
print('------------Set  up  wallpapers------------')
os.system(f"echo 'preload = {image_path}' >> {path}")
print('[#]image loaded')
time.sleep(2)
for monitor in monitors:
    os.system(f"echo 'wallpaper = {monitor['name']}, {image_path}' >> {path}")
print('[#]image connected')
time.sleep(2)
os.system(f"echo 'exec-once = hyprpaper' >> {"~/.config/hypr/hyprland.conf"}")
print('[#]hyprpaper added to hyprland')
time.sleep(3)
print("=================HYPR-SWAP=================")              
print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⡿⠛⠉⠉⠉⠛⢿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⠋⡀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀
⠀⠀⣀⣰⣶⣿⣿⣿⣿⣿⣿⣀⣀⣀⣀⣀⣀⣰⣰⣶⣿⣿⣿⣿⣿⣿⣷⣦⣤⣀
⠉⠉⠉⠉⠈⠉⠛⠛⠛⠛⣿⣿⡽⣏⠉⠉⠉⠉⠉⣽⣿⠛⠉⠉⠉⠉⠉⠉⠉⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣦⣄⣀⣠⣴⣾⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""")  
print("thanks for using my utilite")     



