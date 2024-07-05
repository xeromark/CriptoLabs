#!/bin/bash

# Iniciar el servicio SSH
service ssh start

# Para que el contenedor siga en ejecución
tail -f /dev/null
