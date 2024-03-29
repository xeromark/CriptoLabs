from scapy.all import *
import sys

# python3 readv2.py cesar.pcapng

def Decoder(message, n):	# Decifra el mensaje
	EncryptedMessage = ""	# Segun n traslacion
	for c in message:
		if ord(c) - n >= 97 and ord(c) - n <= 122:
			EncryptedMessage += chr(ord(c) - n)
		elif " " == c:
			EncryptedMessage += " "
		else:
			EncryptedMessage += chr(ord(c) - n + 26)

	return EncryptedMessage

# Ruta al archivo pcapng
archivo_pcapng = "./" + sys.argv[1]

# Lee el archivo pcapng
paquetes = rdpcap(archivo_pcapng)

EncryptedMessage = ""

for paquete in paquetes:
	if ICMP in paquete: # Verifica si es un paquete ICMP
		data = paquete[ICMP].payload.load
		data = data[8:]  # Omitir los primeros 8 bytes
		EncryptedMessage += chr(data[0])


i = 0
while i < 26:	# Imprime todas las posibles traslaciones
	print(str(i) + " " + Decoder(EncryptedMessage,i))
	i+=1
