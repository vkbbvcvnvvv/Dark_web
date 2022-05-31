import os
import time
os.system ("clear")
os.system ("figlet Z")

print ("\033[1;31m[1]/\033[1;34mInstall pkg termux\033[1;31m(termux)")
time.sleep (0.3)
#____________________________________
print ("\033[1;31m[2]/\033[1;34mInstall metasploit\033[1;31m(termux)")
time.sleep (0.3)
#______________________________________
print ("\033[1;31m[3]/\033[1;34mInstall languages ​​on the termux\033[1;31m(termux)")
time.sleep (0.3)
#________________________________________
print ("\033[1;31m[4]/\033[1;34mIinstall ngrok\033[1;031m(termux)")
time.sleep (0.3)

#_______________________________________

name = input ("Chose Nuber : ")
if name == "1" :
    os.system ("apt update && apt upgrade -y")
#_____________________________________
if name =="2" :
    os.system ("wget https://raw.githubusercontent.com/gushmazuko/metasploit_in_termux/master/metasploit.sh")
    os.system ("chmod +x metasploit.sh")
    os.system ("./metasploit.sh")
    os.system ("msfconsole")
#ـــــــــــــــــــــــــــــــــــــــ
if name =="3" :
    os.system ("pkg inastall python")
    os.system ("pkg install python2")
    os.system ("pkg install python3")
    os.system ("pkg inastall php")
    os.system ("pkg inastall java")
    os.system ("pkg inastall bash")
#ـــــــــــــــــــــــــــــــــــ
if name =="4" :
    os.system ("git clone https://github.com/Err0r-ICA/Ngrok.git")
    os.system ("cd Ngrok")
    os.system ("chmod +x termux-ngrok.sh")
    os.system ("sh termux-ngrok.sh")
    os.system ("ngrok http 8080")
