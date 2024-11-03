Proyecto de Validación de Cadenas con Máquina de Turing y Árbol de Derivación


Este proyecto implementa un sistema para la validación de cadenas mediante un autómata finito y una máquina de Turing, con generación de tablas de transición y representación de árboles de derivación.

Estructura del Proyecto
  main.py: Punto de entrada del proyecto. Permite cargar cadenas desde un archivo de texto y ejecuta el proceso de validación.
  Validaciones: Módulo que contiene las clases Grafo, NodoDerivacion y TuringMachine, encargadas de manejar la lógica de validación de cadenas, el árbol de derivación y la simulación de la máquina de Turing.
  
Funcionalidades
  Validación de Cadenas: Valida cada cadena proporcionada, generando un árbol de derivación para mostrar el proceso.
  Máquina de Turing: Simulación de una máquina de Turing con dos cintas para validar la cadena, registrar transiciones y detectar errores.
  Generación de Tablas de Transición: Muestra una tabla detallada de cada transición en el proceso de validación.
  Exploración de Caracteres: Detecta y cuenta los caracteres especiales y los caracteres válidos del lenguaje en la cadena.
  Interfaz de Selección de Archivos: Permite al usuario seleccionar un archivo .txt con las cadenas a validar.
  
Requisitos
Python 3.x
Tkinter: Usado para la interfaz de selección de archivos.

Como usar el proyecto. 
  Para instalar Tkinter:  
                pip install tk
  El programa se ejecuta desde el main.py
  Seleccionar el archivo de entrada: Cuando el programa se ejecute, aparecerá un diálogo para seleccionar un archivo .txt con las cadenas a validar. Cada línea debe contener una cadena.

Resultados: Para cada cadena, el programa:
  Muestra si la cadena es válida o no.
  Imprime la tabla de transiciones realizadas.
  Genera y muestra el árbol de derivación.
  Ejecuta la máquina de Turing y muestra su resultado, incluyendo las dos cintas y los movimientos realizados.
