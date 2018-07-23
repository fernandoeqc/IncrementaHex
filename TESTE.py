# hexa = "0001,00FF,00FF,00FF,00FF,00FF,00FF,00FF,0018"

def le_codigo(obj_arq,num_lin=0):
	a=0
	for i in obj_arq:										#le o arquivo
		a+=1												#incrementa contador
		if a > num_lin:										#quando chegar na linha desejada...
			break											#para o loop
	return(i)
		

def separa_nomes(obj_arq,linha_inicial=0,linha_final=100):
	string=[]
	saida=[]
	for linha in obj_arq:
		if not isinstance(obj_arq,list):					#se objeto de entrada não for uma lista...
			#linha = linha.strip()							#retira \n dos nomes do arquivo(suportado por arquivos)
			linha = linha.split(',')						#separa nomes separados por virgula (suportado por arquivos)
		string.append(linha)								#adiciona linha atual em string
	string = string[linha_inicial:linha_final]				#retira apenas as linhas solicitadas
	for i in range(len(string)):							#verifica cada sub-lista da lista principal gerada
		for j in range(len(string[i])):						#verifica cada nome nas sub-listas da lista principal
			if not string[i][j] == "":						#se string for diferente de vazio...
				saida.append(string[i][j])					#guarda nome na lista saída	
	return(saida)	


def separa_hex(lista):
	hx=[]
	inte=[]
	hx = lista.split(",")
	for i in hx:
		inte.append(i.replace("00","0x"))
	return(inte)
	

def incrementa(lista):
	byte0 = int(lista[0],16)
	byte1 = int(lista[1],16)
	if byte0 == 255:
		byte0 = 1
		if byte1 == 255:
			byte1 = 1
		else:
			byte1 += 1
	else:
		byte0 += 1
	lista[0] = '%#04x'%byte0
	lista[1] = '%#04x'%byte1
	return(lista)
	
	
def calcula_crc(lista):
	somador=0
	for i in range(len(lista)-1):
		somador+=int(lista[i],16)
	somador = 2040-somador+24
	while(somador>255):
		somador=somador-256	
	return('%#04x'%somador)
	

def concatena(lista,crc):
	conc=""
	lista[len(lista)-1] = crc
	for i in lista:
		i = i.replace("0x","00")
		i = i.upper()
		conc = conc + i
	conc = conc + '\n'
	return(conc)
	
	
def salvar_edit(lista):	
	string=""
	for i in range(15):
		if lista[i] == ",":
			continue
		else:
			lista.insert(i+1,",")
	for i in lista:
		string = string + i
	return(string)

	

inicio = open("inicio.txt",'r')					#=====================================================================================
a = separa_nomes(inicio,0,300)					#ABRE ARQ DE DADOS DO CODIGO
inicio.close()									#COPIA PARA LISTA 'a'
inicio = open("app.hex",'w')					#
for i in a:										#COLA NO ARQ HEXADECIMAL
    inicio.write(i)								#FECHA ARQ DE DADOS DO CODIGO
inicio.close()									#=====================================================================================

codigo = open("codigo.txt",'r')					#=====================================================================================
cod = le_codigo(codigo)							#COPIA CODIGO ANTIGO E GUARDA EM VARIAVEL 'COD'
codigo.close()									#=====================================================================================


hx = separa_hex(cod)
# print(hx)
inc = incrementa(hx)
# print(inc)
crc = calcula_crc(inc)
# print(crc)
result = concatena(inc,crc)
# print(result)

padrao = open("app.hex",'a')					#=====================================================================================
padrao.write(result)							#ADICIONA CODIGO INCREMENTADO AO ARQ HEX 
padrao.close()									#=====================================================================================

padrao = open("codigo.txt",'w')					#=====================================================================================
edit = salvar_edit(inc)							#
padrao.write(edit)								#SALVA CODIGO INCREMENTADO NO ARQ 'CODIGO' 
print(edit)										#
padrao.close()									#=====================================================================================

fim = open("fim.txt",'r')						#=====================================================================================
b = separa_nomes(fim,0,300)						#ABRE ARQ DE DADOS DO CODIGO
fim.close()										#COPIA PARA LISTA 'a'
fim = open("app.hex",'a')						#
for i in b:										#COLA NO ARQ HEXADECIMAL
    fim.write(i)								#FECHA ARQ DE DADOS DO CODIGO
fim.close()										#=====================================================================================

import time

time.sleep(10)




















