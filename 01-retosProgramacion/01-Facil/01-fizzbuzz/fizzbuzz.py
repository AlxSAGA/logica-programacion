#!/usr/bin/env python3
from termcolor import colored as c 
import sys
import signal
import os

def ctrl_c(sig, frame):
    print(c(f"\n[-] Programa finalizado..\n", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def finish_program():
    print(c(f"\n[+] Programa finalizado correctamente...\n", "green"))
    sys.exit(0)

class FizzBuzz:
    def __init__(self, valor_final:int) -> int:
        self.valor_inicial = 1
        self.valor_final = valor_final

    def fizz_buzz(self) -> int:
        for numero_fuzz in range(self.valor_inicial, self.valor_final+1):
            if numero_fuzz % 3 == 0 and numero_fuzz % 5 == 0:
                print(c(f"{numero_fuzz} FIZZBUZZ", "red"))

            elif numero_fuzz % 3 == 0:
                print(c(f"{numero_fuzz} FIZZ", "blue"))

            elif numero_fuzz % 5 == 0:
                print(c(f"{numero_fuzz} BUZZ", "cyan"))

            else:
                print(numero_fuzz)

# Funcion para validar que el tipo de dato sea correcto
def validar_dato(datos):
    while True:
        try:
            valor = input(datos).strip() # Eliminamos espacios al inicio y al final de la cadena

            # Validamos entradas vacias
            if not valor:
                raise ValueError(c("\n[-] Error: No se permiten cadenas vacias..", "red"))
                continue

            # Validamos que las entradas no sean de tipo str
            if not valor.isdigit():
                raise ValueError(c("\n[-] Error: Solo se permiten numeros", "red"))
                continue

            dato = int(valor)

            if dato <= 0:
                raise ValueError(c("\n[!] Error: Los numeros deven ser positivos..", "red"))

            return dato

        except ValueError as e:
            print(c(f"\n[!] Error: Ingresa un numero valido...", "red"))

    
def main():
    print(c(f"\n[*] Welcome to FizzBuzz\n", "cyan"))
    print(c(f"Programa que muestra los numeros determinados: Múltiplos de 3 por la palabra 'fizz' - Múltiplos de 5 por la palabra 'buzz' - Múltiplos de 3 y de 5 a la vez por la palabra 'fizzbuzz'", "cyan"))

    while True:

        opcion_fuzz = input(c(f"\n[+] Selecciona una opcion: (1)Iniciar Programa - (2)Limpiar pantalla - (3)Salir\n\n-->   ", "blue"))

        if opcion_fuzz == "1":
            valor_final = validar_dato(c("\n[+] Ingresa el rango:  ", "blue"))

            fizz_buzz_mourdev = FizzBuzz(valor_final)
            fizz_buzz_mourdev.fizz_buzz()

        elif opcion_fuzz == "2":
            clean_screen()

        elif opcion_fuzz == "3":
            finish_program()

        else:
            print(c(f"\n[-] Error valor incorrecto...\n", "red"))


# Flujo principal del programa
if __name__ == '__main__':
    main()
