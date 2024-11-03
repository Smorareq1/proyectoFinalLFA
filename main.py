# main.py

import Validaciones
import tkinter as tk
from tkinter import filedialog


def validacion_cadena(cadena):
    print(f"Validando la cadena: {cadena}")

    g = Validaciones.Grafo()
    raiz, transiciones, validacion = g.validar_cadena(cadena)

    if(validacion):
        print("Cadena válida")
    else:
        print("Cadena inválida")

    print("\n")
    print("Tabla de transiciones:")
    g.mostrar_tabla_transicion(transiciones)
    print("\n")
    g.mostrar_arbol(raiz)
    print("\n")
    g.mostrar_caracteres_especiales()
    print("\n")
    g.mostrar_caracteres_del_lenguaje()

    print("\n")

    # Mostrar la maquina de Turing
    print("Máquina de Turing:")
    tm = Validaciones.TuringMachine(cadena)
    tm.validar_cadena()
    tm.mostrar_cintas()
    tm.mostrar_resultado()

    # Mostrar la estructura de la máquina de Turing
    tm.mostrar_maquina_turing()


def cadenaToArreglo(cadena):
    return list(cadena)


def cadenasAValidar(cadena):
    print("-" * 100)
    arregloCadena = cadenaToArreglo(cadena)
    validacion_cadena(arregloCadena)
    print("-" * 100)
    print("\n")


def abrir_archivo():
    # Configura el explorador de archivos
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(title="Selecciona el archivo de cadenas",
                                         filetypes=[("Archivos de texto", "*.txt")])

    if archivo:
        # Abrir y leer el archivo seleccionado
        with open(archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()  # Quitar saltos de línea y espacios extra
                if cadena:  # Validar solo si la línea no está vacía
                    cadenasAValidar(cadena)


# Importar txt con las cadenas a validar
abrir_archivo()
