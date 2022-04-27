# Bibliotecas
#
from libs import android
from libs import windows
from libs import linux
from libs import connect
from os import system
#
#

# Função do menu
def menu():
	system('clear')
	print("""
         _nnnn_                      
        dGGGGMMb     ,-----------------------
       @p~qp~~qMb    | AUTO CREATOR BACKDOOR |
       M|@||@) M|   _;-----------------------
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--' 

[01] - Android 📱️
[02] - Windows 💻️
[03] - linux 🐧️
[04] - Connect Backdoor 👨‍💻️
	""")
	cmd = str(input('➡️  '))
	
	if cmd == '1':
		android.fun_android_menu()
	elif cmd == '2':
		windows.fun_windows_menu()
	elif cmd == '3':
		linux.fun_linux_menu()
	elif  cmd == '4':		
		connect.fun_connect_menu()
menu()