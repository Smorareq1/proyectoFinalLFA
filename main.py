import grafo
import tkinter as tk
from tkinter import filedialog


def validacion_cadena(cadena):

    print(f"Validando la cadena: {cadena}")
    cintaIzquierda = []
    cintaDerecha = []
    par = True
    for char in cadena:
        if par:
            cintaIzquierda.append(char)
        else:
            cintaDerecha.append(char)
        # Alterna el valor de `par` en cada iteración
        par = not par

    # Crear el grafo
    g = grafo.Grafo()
    # Validar la cadena
    validacion = g.validar_cadena(cadena)
    print(f"La cadena {cadena} es {'aceptada' if validacion else 'rechazada'}.")
    print (f"Caracteres especiales encontrados: {g.CaracteresEspecialesEncontrados}")
    print(f"Cinta izquierda: {cintaIzquierda}")
    print(f"Cinta derecha: {cintaDerecha}")

def cadenaToArreglo(cadena):
    return list(cadena)

def cadenasAValidar(cadena):
    print("----------------------------------------------------")
    arregloCadena = cadenaToArreglo(cadena)
    validacion_cadena(arregloCadena)
    print("----------------------------------------------------")
    print("\n")

def abrir_archivo():
    # Configura el explorador de archivos
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal de Tkinter
    archivo = filedialog.askopenfilename(title="Selecciona el archivo de cadenas",
                                         filetypes=[("Archivos de texto", "*.txt")])

    if archivo:
        # Abrir y leer el archivo seleccionado
        with open(archivo, "r") as f:
            for linea in f:
                cadena = linea.strip()  # Quitar saltos de línea y espacios extra
                if cadena:  # Validar solo si la línea no está vacía
                    cadenasAValidar(cadena)


#Importar txt con las cadenas a validar
abrir_archivo()




