from ping3 import ping
from scapy.all import *
import time
import sys
import struct

# python3 pingv4.py "larycxpajorj h bnpdarmjm nw anmnb"

EncryptedMessage = sys.argv[1]

i = 0
while i < len(EncryptedMessage):
    character = format(ord(EncryptedMessage[i]), '02X') # Se obtiene el caracter y luego se inserta en el Data. Modelo tipo linux:
    Data = bytes.fromhex( character + "608f0000000000101112131415161718191a1b1c1d1e1f202122232425262728292a2b2c2d2e2f3031323334353637")

    # Timestamp
    timestamp = int(time.time())					# Obtenemos el tiempo actual para asignarlo al timestamp
    timestampBytes = struct.pack('<Q', timestamp)	#Lo pasamos a Byte para poder enviarlo y lo ajustamos a <Q
	#
    icmp_packet = IP(dst="127.0.0.1") / ICMP(type=8, code=0, id= 4160, seq=1 + i)  # Creamos el paquete ICMP
	#
    icmp_packet = icmp_packet  / timestampBytes / Data	#Le anadimos el Timestamp y el valor del campo Data

    send(icmp_packet)	# Enviamos un paquete cada segundo
    time.sleep(1)		
    i += 1

