#!/usr/bin/env python3

import sys
import signal
import os
from termcolor import colored as c

# funcion para forzar salida del programa
def ctr_c(signum, frame):
    print(c('\n\nSaliendo del programa...', 'red'))
    sys.exit(1)
    
signal.signal(signal.SIGINT, ctr_c)

# funcion para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')
    
# funcion para terminar el programa
def terminar_programa():
    limpiar_pantalla()
    print(c('\n\nSaliendo del programa...', 'red'))
    sys.exit(0)

# Funcion para validar el dato introducido
def validar_dato(dato):
    while True:
        try:
            cadena = input(dato).strip()
            
            # Validamos que tenga contenido
            if not cadena:
                raise ValueError(c(f"\n[!] No se permiten cadenas vacias\n", "red"))
                continue
            
            # Validamos que no ingresen numeros
            for character in cadena:
                if not character.isalpha():
                    raise ValueError(c("\n[!] No se perminten valores numericos\n", "red"))
                
            return cadena
            
        except ValueError as e:
            print(c("\n[-] Error: Ingresa una cadena valida\n", "red"))
        

class InvierteCadenas:
    def __init__(self, cadena: str) -> str:
        self.cadena = cadena

    @property
    def invertir_cadena(self) -> str:
        return c(f"\n[+] La cadena invertida es: ( {self.cadena[::-1]} )", "cyan")

def main():
    print(c('\n\nBienvenido al programa de invierte de cadenas', 'green'))
    
    while True:
        opcion = input(c('\n\nIntroduce una opcion: (1) Invertir cadena - (2)Limpiar pantalla - (3) Salir   ', 'green'))
        
        if opcion == '1':
            cadena = validar_dato(c('\nIntroduce la cadena a invertir: ', 'cyan'))
            
            # Objeto principal
            invierte_cadenas = InvierteCadenas(cadena)
            print(invierte_cadenas.invertir_cadena)
            
        elif opcion == '2':
            limpiar_pantalla()
            
        elif opcion == '3':
            terminar_programa()
        
        else:
            print(c('\nOpcion no valida.', 'red'))

# flujo principal del programa
if __name__ == '__main__':
    main()