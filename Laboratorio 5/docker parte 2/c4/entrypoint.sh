#!/bin/bash

# Iniciar el servicio SSH
service ssh start

# Para que el contenedor siga en ejecuci�n
tail -f /dev/null
