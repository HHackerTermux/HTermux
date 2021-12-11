from colorama import *
import subprocess
import time 
import os 

def mainMenu():
  subprocess.call(["clear"])
  print(Fore.RED + "I Am Not Responsible In Any Damage! ")
  print(Fore.RED + """|██╗  ██╗████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗│
│██║  ██║╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝│
│███████║   ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ │
│██╔══██║   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ │
│██║  ██║   ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗│
│╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝""")
  print(Fore.YELLOW + "1.Tool-X")
  print(Fore.YELLOW + "2.Zphisher")
  print(Fore.YELLOW + "3.Social Box")
  print(Fore.YELLOW + "4.Infect")
  print(Fore.YELLOW + "5.LockPhish")
  print(Fore.YELLOW + "6.LazyBee")
  print(Fore.YELLOW + "7.Mbomb")
  print(Fore.YELLOW + "8.AllHackingTools")
  print(Fore.RED + "9.Exit The Program")
  selection=int(input("""┌─[HTermux]─
└──╼ ❯❯❯"""))
  if selection==1: 
    ToolX()
  elif selection==2: 
    Zphish()
  elif selection==3:
    Box()
  elif selection==4:
    infect()
  elif selection==5:
    lock()
  elif selection==6: 
    lazy()
  elif selection==7:
    bomb()
  elif selection==8:
    htool()
  elif selection==9:
    subprocess.call(["clear"])
    print(Fore.BLUE + "☺️Bye Bye")
    time.sleep(1)
    exit()
  else:
    subprocess.call(["clear"])
    print(Fore.WHITE + "Invalid Input")
    anykey=input("Enter To continue") 
    mainMenu()
def ToolX():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + Back.BLACK + "This Command Install Tool-X")
  print("1.Install")
  print("2.Back")
  selection1=int(input("""┌─[HTermux]─
  └──╼ ❯❯❯"""))
  if selection1==1:
    subprocess.call(["clear"])
    ToolXInstall()
  elif selection1==2:
    subprocess.call(["clear"])
    mainMenu()
  else:
    subprocess.call(["clear"])
    print(Fore.GREEN + "Invalid Input")
    anykey=input("Enter Anything To Continue")
    ToolX()
def ToolXInstall(): 
  subprocess.call(["clear"])
  print("Please Wait")
  time.sleep(0.5) 
  subprocess.call(["git", "clone", "https://github.com/rajkumardusad/Tool-X.git"]) 
  time.sleep(0.5)
  os.chdir("Tool-X")
  time.sleep(0.2)
  subprocess.call(["chmod", "+x", "install"])
  time.sleep(0.1)
  subprocess.call(["sh", "install"])
  
def Zphish():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install Zphisher All In One Phishing tool")
  print("1.Install")
  print("2.Back")
  selection2=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection2==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/htr-tech/zphisher"]) 
    time.sleep(0.5)
    os.chdir("zphisher")
    time.sleep(0.2)
    time.sleep(0.1)
    subprocess.call(["bash", "zphisher.sh"])
  elif selection2==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()
        
def Box():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install Social Box All In One BruteForce  tool")
  print("1.Install")
  print("2.Back")
  selection3=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection3==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/samsesh/SocialBox-Termux"]) 
    time.sleep(0.5)
    os.chdir("SocialBox-Termux")
    time.sleep(0.2)
    subprocess.call(["chmod", "+x", "install-sb.sh"])
    time.sleep(0.1)
    subprocess.call(["bash", "install-sb.sh"])
  elif selection3==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()

def infect():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install Infect You Can Infect Other Phone With This")
  print("1.Install")
  print("2.Back")
  selection2=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection2==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/noob-hackers/infect"]) 
    time.sleep(0.5)
    os.chdir("infect")
    time.sleep(0.2)
    time.sleep(0.1)
    subprocess.call(["bash", "infect.sh"])
  elif selection2==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()
 
def lock():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install lockphish  An Lock Phishing tool")
  print("1.Install")
  print("2.Back")
  selection5=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection5==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/noob-hackers/hacklock"]) 
    time.sleep(0.5)
    os.chdir("hacklock")
    time.sleep(0.2)
    time.sleep(0.1)
    subprocess.call(["bash", "hacklock.sh"])
  elif selection5==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()

def lazy():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install LazyBee An Wordlist Generator")
  print("1.Install")
  print("2.Back")
  selection6=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection6==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/noob-hackers/lazybee"]) 
    time.sleep(0.5)
    os.chdir("lazybee")
    time.sleep(0.2)
    time.sleep(0.1)
    subprocess.call(["python2", "lazybee.py"])
  elif selection6==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()

def bomb():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install Mbomb An Gmail To Gmail Bomber tool")
  print("1.Install")
  print("2.Back")
  selection2=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection2==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/palahsu/MBomb"]) 
    time.sleep(0.5)
    os.chdir("MBomb")
    time.sleep(0.2)
    subprocess.call(["pip", "install", "tqdm"])
    time.sleep(0.1)
    subprocess.call(["python", "MBomb.py"])
  elif selection2==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()

def htool():
  subprocess.call(["clear"])
  print(Fore.GREEN + "Info")
  print(Fore.RED + "This Command Will Install AllHackingTools All In One Hacking tool")
  print("1.Install")
  print("2.Back")
  selection7=int(input("""┌─[HTermux]─
      └──╼ ❯❯❯"""))
  if selection7==1: 
    subprocess.call(["clear"])
    print(Fore.RED + "Please Wait")
    time.sleep(0.5)
    subprocess.call(["git", "clone", "https://github.com/mishakorzik/AllHackingTools"]) 
    time.sleep(0.5)
    os.chdir("AllHackingTools")
    time.sleep(0.2)
    time.sleep(0.1)
    subprocess.call(["bash", "Install.sh"])
  elif selection7==2: 
    mainMenu()
  else: 
    print("Invalid Choice ")
    anykey=input("Enter Anything To Continue")
    mainMenu()

mainMenu()