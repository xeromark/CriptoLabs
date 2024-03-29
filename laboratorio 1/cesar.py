import sys

# python3 cesar.py "criptografia y seguridad en redes" 9

message = sys.argv[1]	# Mensaje a cifrar
n = int(sys.argv[2])

EncryptedMessage = ""
# Recorre cada caracter y le aplica la traslacion
for c in message:	
	if ord(c) + n >= 97 and ord(c) + n <= 122:
		EncryptedMessage += chr(ord(c) + n)
	elif " " == c:
		EncryptedMessage += " "
	else:
		EncryptedMessage += chr(ord(c) + n - 26)

print(EncryptedMessage)	#Imprime el mensaje cifrado




