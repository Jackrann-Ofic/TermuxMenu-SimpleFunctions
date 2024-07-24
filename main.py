import time
import subprocess
import threading
import json
from loc import *
from rich.console import Console
from rich.panel import Panel

console = Console()
rodando = False

def bateria_power():
	bt = subprocess.run(['termux-battery-status'], capture_output=True, text=True, check=True)
	return bt.stdout
	
def receber_local():
	loc = subprocess.run(['termux-location'], capture_output = True)
	return loc.stdout

def monitorar_bateria():
	while True:
		bateria = bateria_power()
		bt_json = json.loads(bateria)
		bt_porcentagem = bt_json.get("percentage")
		if bt_porcentagem <= 5:
			local = receber_local()
			local_json = json.loads(local)
			local_latitude = local_json.get("latitude")
			local_longitude = local_json.get("longitude")
			if maior_valor_de_latitude >= local_latitude >= menor_valor_de_latitude and maior_valor_de_longitude >= local_longitude >= menor_valor_de_longitude:
				subprocess.run(['termux-volume', 'music', '8'])
				subprocess.run(['termux-tts-speak', 'Você deveria colocar o telefone para carregar'])
		time.sleep(3000)

battery_thread = threading.Thread(target = monitorar_bateria)
battery_thread.daemon = True

while True:
	passou_na_alfandega = subprocess.run(['termux-fingerprint'], capture_output = True)
	pna_json = json.loads(passou_na_alfandega.stdout)
	auth_result = pna_json.get("auth_result")

	if auth_result == "AUTH_RESULT_SUCCESS":
		console.clear()
		print("\n Autenticação completa")
		print("\n Abrindo menu em 5 segundos...")
		time.sleep(5)
		console.clear()
		rodando = True
		break
	elif auth_result == "AUTH_RESULT_FAILURE":
		console.clear()
		print("lamento... você não passou...")
		time.sleep(3)
		console.clear()
	else:
		console.clear()
		print("Tu conseguiu fazer algo que nem eu sei oque foi...")
		print("Depois compartilha oque você fez comigo pq eu realmente não tenho ideia de que macumba foi essa")
		time.sleep(10)
		console.clear()

battery_thread.start()

while rodando == True:
	options = [
        "[1] Pisca-pisca",
        "[2] Sair"
	]
	options_text = "\n".join(options)
	menu_panel = Panel.fit(options_text, title="Main Menu", border_style="cyan")
	console.print(menu_panel)
	
	escolha = input("Comando a ser realizado: \n")
	
	if escolha == '1':
		agnum = True
		while agnum == True:
			subprocess.run('clear')
			strx = input('Quantas vezes a luz vai piscar: \n')
			stry = input('Quanto tempo a luz deve permanecer ligada (em segundos) \n')
			strz = input('Qual o intervalo de tempo (em segundos) entre o piscar da luz \n')
			try:
				x = int(strx)
				y = float(stry)
				z = float(strz)
				agnum = False
			except:
				print("Responda usando números válidos")
				time.sleep(3)
		i = 0
		for i in range(i, x):
			subprocess.run(['termux-torch', 'on'])
			time.sleep(y)
			subprocess.run(['termux-torch', 'off'])
			time.sleep(z)
			i += 1
	elif escolha == '2':
		rodando = False
	else:
		print("\n Responda apenas com a numeração de cada ação")
		time.sleep(2)
	console.clear()
		
print("\n Desligando aplicação")
time.sleep(2)
console.clear()
