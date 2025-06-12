#!/usr/bin/env python3

import sys
import os
import signal
from termcolor import colored as c 

# funcion para controlar la salida del progrmaa
def ctrl_c(signal, frame):
    print(c('\n\nSaliendo...', 'red'))
    sys.exit(0)

signal.signal(signal.SIGINT, ctrl_c)

# funcion para limpiar la pantalla
def clean_screen():
    os.system('clear' if os.name == 'nt' else 'clear')

# funcion para salir del programa correctamente
def finish_program():
    print(c('\n\nFin del programa', 'green'))
    sys.exit(0)

# Clase principal
class FigurasGeometricas:
    
    def triangulo(self, base: float, alto: float) -> float:
        area = (base * alto) / 2
        return c(f'\nEl area del triangulo es {area:.2f}', 'green')
    
    def cuadrado(self, lado: float) -> float:
        area = lado * lado
        return c(f'\nEl area del cuadrado es {area:.2f}', 'green')
    
    def rectangulo(self, base: float, alto: float) -> float:
        area = base * alto
        return c(f'\nEl area del rectangulo es {area:.2f}', 'green')
    
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
 

# Objeto principal
figura = FigurasGeometricas()

def main():
    print(c(f"\n[+] bienvenido al programa de area de figuras geomtricas", 'green'))
    
    while True:
        print(c('\n[+] Escriba la opcion deseada:  (1) Triangulo - (2) Cuadrado - (3) Rectangulo - (4) Limpiar pantalla - (5) Salir', 'green'))
        opcion_menu = input(c('\nOpcion: ', 'cyan'))
        
        if opcion_menu == '1':
            base = validar_dato(c('\nBase: ', 'cyan'))
            alto = validar_dato(c('\nAlto: ', 'cyan'))
            
            print(figura.triangulo(base, alto))
            
        elif opcion_menu == '2':
            lado = validar_dato(c('\nLado: ', 'cyan'))
            
            print(figura.cuadrado(lado))
            
        elif opcion_menu == '3':
            base = validar_dato(c('\nLargo: ', 'cyan'))
            alto = validar_dato(c('\nAlto: ', 'cyan'))
            
            print(figura.rectangulo(base, alto))
            
        elif opcion_menu == '4':
            clean_screen()
        
        elif opcion_menu == '5':
            finish_program()
        
        else:
            print(c('\nOpcion no valida', 'red'))

if __name__ == '__main__':
    main()