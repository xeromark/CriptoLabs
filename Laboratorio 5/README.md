# Levantar los contenedores
  
    docker compose build
    docker compose up

# C1 - C4-S1

    docker exec -it c1 bash

# Terminal de C4-S1

    tshark -i eth0 -w capture.pcap

Para c4_s1 se observa por loopback:

    tshark -i lo -w capture.pcap

# Terminal C1

    ssh prueba@c4_s1

# Parte 3
  La idea es poner los menos pesados

    Ciphers 3des-cbc
    MACs hmac-sha1
    HostKeyAlgorithms ssh-ed25519
    KexAlgorithms diffie-hellman-group1-sha1    
