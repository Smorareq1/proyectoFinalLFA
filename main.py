import grafo

def validacion_cadena(cadena):

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
    g.mostrar_tabla_transicion()

def cadenaToArreglo(cadena):
    return list(cadena)

# Crear el grafo y validar una cadena
cadenaString = "aba*##b"
validacion_cadena(cadenaToArreglo(cadenaString))




