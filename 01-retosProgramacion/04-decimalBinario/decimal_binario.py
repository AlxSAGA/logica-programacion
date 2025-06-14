#!/usr/bin/env python3

import sys
import signal
import os
from termcolor import colored as c

# Funciones personalizadas

# funcion para forzar la salida del programa
def ctrl_c(signal, frame):
    print(c("\n\nSaliendo...\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

# funcion para limpiar la pantalla
def limpiarPantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# funcion para terminar el programa
def terminar_programa():
    limpiarPantalla()
    print(c("\n\nPrograma terminado correctamente...\n", "red"))
    sys.exit(0)

# funcion para validar el tipo de dato ingresado por el usuario.
def validar_numero(numero_decimal):
    while True:
        try:
            numero_a_converit = input(numero_decimal).strip()
            
            # Validamos que el dato no sea vacio
            if not numero_a_converit:
                raise ValueError(c("\n[!] Error: NO se permiten cadenas vacias...", "red"))
                continue
            
            # Validamos que el dato no sea de tipo string
            if numero_a_converit[0] == '-' and numero_a_converit[1:].isdigit():
                return int(numero_a_converit)
            
            if numero_a_converit.isdigit():
                return int(numero_a_converit)
            
            raise ValueError()
        
        except ValueError as e:
            print(c("\n[!] Error: Ingresa un numero valido...\n", "red"))

# clase principal
class ConversionarDecimalBinario:    
            
    def convertir_a_binario(self, numero_decimal):
        if numero_decimal == 0:
            return "0"
        
        # Aqui almacenamos el numero final en binario
        binario = ""
        num = abs(numero_decimal)
        
        # Iteramos sobre el dato introducio
        while num > 0:
            binario = str(num % 2) + binario
            num = num // 2
        
        return binario if numero_decimal > 0 else "-" + binario
                
    
# objeto principal
obj = ConversionarDecimalBinario()

# funcion principal
def main():
    print(c("\nBienvenidos al programa de conversion de decimal a binario...\n", "green"))
    
    while True:
        print(c("\n(1) Inicar Programa - (2) Limpiar Pantalla - (3) Terminar programa: ", "blue"))
        
        opcion = input(c("\nSeleccione una opcion:  ", "yellow"))
        
        if opcion == "1":
            numero_decimal = validar_numero(c("\n[+] Ingresa el numero?  ", "cyan"))
            print(c(f"\n[+] El numero en binario es: {obj.convertir_a_binario(numero_decimal)}", "green")) # llamada a la funcion
            
        elif opcion == "2":
            limpiarPantalla()
            
        elif opcion == "3":
            terminar_programa() 
            
        else:
            print(c("\n\n[!] Opcion invalida, intente nuevamente...\n", "red"))
            
    
# flujo principal del programa
if __name__ == '__main__':
    main()