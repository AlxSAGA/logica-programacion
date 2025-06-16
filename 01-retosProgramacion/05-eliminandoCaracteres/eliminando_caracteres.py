#!/usr/bin/env python3

import sys
import os
import signal
from termcolor import colored as c

# funcion para forzar el cierrrrro de la terminal
def ctrl_c(signal, frame):
    print(c("\n\n\n[-] Saliendo...", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

# funcion para terminar el programa
def terminar_programa():
    print(c("\n\n[-] Programa finalizado...", 'red'))
    sys.exit(0)

# funcion para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# funcion para validar el dato
def validar_dato(cadena: str) -> str:
    while True:
        cadena_validada = input(cadena).strip()
            
        if cadena_validada:
            return cadena_validada

        print(c("\n[!] Error: No se permiten cadenas vacías", "red"))

# clase principal del programa
class EliminarCaracteres:
    def __init__(self, string_uno: str, string_dos: str) -> str:
        self.string_uno = string_uno
        self.string_dos = string_dos
        self.unicos1, self.unicos2 = self.calcular_diferencias()
    
    def calcular_diferencias(self):
        return (
            [c for c in self.string_uno if c not in self.string_dos],
            [c for c in self.string_dos if c not in self.string_uno]
        )

    @property   
    def resultado_cadena_uno(self) -> str:
        return c(f"\n[+] Caracteres solo presentes en cadena1: {', '.join(self.unicos1)}", "cyan")

    @property
    def resultado_cadena_dos(self) -> str:
        return c(c(f"\n[+] Caracteres solo presentes en cadena2: {', '.join(self.unicos2)}", "cyan"))

# Menu de bienvenida:
def mostrar_bienvenida():
    print(c("\n[+] Bienvenidos, Este programa recibe dos cadenas como parametros e imprime lo siguiente:\n", "green"))
    print(c("- cadena1 contendrá todos los caracteres presentes en la cadena1 pero NO estén presentes en cadena2.", "green"))
    print(c("- cadena2 contendrá todos los caracteres presentes en la cadena2 pero NO estén presentes en cadena1.", "green"))
    print(c("- Presiona Ctrl+C para salir en cualquier momento\n", "green"))

# funcion principal del programa
def main():
    mostrar_bienvenida()
    
    while True:
        opcion = input(c(f"\n[+] Menu: (1)Iniciar - (2)Limpiar pantalla  ", "blue"))
        
        if opcion == "1":
            cadena_uno = validar_dato(c("\n[+] Ingresa la primera frase:  ", "blue"))
            cadena_dos = validar_dato(c("[+] Ingresa la segunda frase  ", "blue"))
            
            comparador = EliminarCaracteres(cadena_uno, cadena_dos) # Objeto principal
            print(comparador.resultado_cadena_uno)
            print(comparador.resultado_cadena_dos)
            
        elif opcion == "2":
            limpiar_pantalla()
            mostrar_bienvenida()
            
        else:
            print(c("\n[!] Error: Opcion invalida...", "red"))

# Flujo principal del programa
if __name__ == '__main__':
    main()