'''
Get Bitcoin Value
http://api.coindesk.com/v1/bpi/currentprice.json
'''

from os import system
import urllib.request, json, time
import pygame



  
  
  
  
global btc
global btc2



def obter_valor():
	try:
		url = "http://api.coindesk.com/v1/bpi/currentprice.json"
		with urllib.request.urlopen(url) as url:
			response = url.read()
			data = json.loads(response.decode('utf-8'))
			valor = float(data['bpi']['USD']['rate'].replace(",", ""))
			return valor
	except urllib.error.HTTPError:
		print('URL inexistente!')

def exibir_valores(tempo=1):
	
	valor = obter_valor()
	nova_cotacao = True
	
	print('1 Bitcoin vale %f dólares!' % valor)
	system('pause')
	btc=input("Digite o valor em queda ex-> 38000.000000 ")
	btc2=input("Digite o valor em alta ex-> 38000.000000 ")
	while True:
		valor_atual = obter_valor()
		if valor_atual < valor:
			print('--->  caindo:  Bitcoin  vale %f dólares!' % valor_atual)
			nova_cotacao = True
		elif valor_atual > valor:
			print('+++++++++> subindo:  Bitcoin vale %f dólares!' % valor_atual)
			nova_cotacao = True
		else:
			if nova_cotacao == True:
				print('Aguardando uma nova cotação...')
				nova_cotacao = False
		valor = valor_atual
		time.sleep(tempo)
		if valor <= float(btc) or valor >= float(btc2):
     			sonar()
		
	         
def sonar():
	pygame.init()
	pygame.mixer.music.load('a.mp3')
	pygame.mixer.music.play()
	pygame.event.wait()
	#sonar = pygame.event.wait()
 

  
exibir_valores()
