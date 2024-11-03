class NodoDerivacion:
    def __init__(self, estado, transicion, hermanos=None):
        self.estado = estado
        self.transicion = transicion
        self.hermanos = hermanos or []
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def mostrar_arbol(self, prefijo="", es_ultimo=True):
        print(prefijo + ("└── " if es_ultimo else "├── ") +
              f"Estado: {self.estado}, Transición: {self.transicion}, Hermanos: {[f'{h[0]}:{h[1]}' for h in self.hermanos]}")
        prefijo_hijo = prefijo + ("    " if es_ultimo else "│   ")
        for i, hijo in enumerate(self.hijos):
            es_ultimo_hijo = i == len(self.hijos) - 1
            hijo.mostrar_arbol(prefijo_hijo, es_ultimo_hijo)


class Grafo:
    def __init__(self):
        self.caracteresEspeciales = {'*', '#'}
        self.CaracteresEspecialesEncontrados = {}

        self.caracteresDelLenguaje = {'a', 'b'}
        self.caracteresDelLenguajeEncontrados = {}

        self.grafo = {
            'q0': [('q1', 'a')],
            'q1': [('q2', 'b')],
            'q2': [('q3', 'a')],
            'q3': [('q1', 'b'), ('q3', 'a'), ('q4', '*')],
            'q4': [('q4', '#'), ('q3', 'a'), ('q1', 'b')]
        }
        self.estado_inicial = 'q0'
        self.error_transicion = None

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        raiz = NodoDerivacion(estado_actual, 'Inicio')
        nodo_actual = raiz
        transiciones = []

        for char in cadena:
            transicion_valida = False
            opciones = []
            eleccion = None

            for estado_siguiente, peso in self.grafo[estado_actual]:
                opciones.append((estado_siguiente, peso))
                if peso == char and not transicion_valida:
                    estado_actual = estado_siguiente
                    transicion_valida = True
                    eleccion = (estado_siguiente, peso)

                    if peso in self.caracteresEspeciales:
                        self.CaracteresEspecialesEncontrados[peso] = self.CaracteresEspecialesEncontrados.get(peso,
                                                                                                              0) + 1

                    if peso in self.caracteresDelLenguaje:
                        self.caracteresDelLenguajeEncontrados[peso] = self.caracteresDelLenguajeEncontrados.get(peso,
                                                                                                                0) + 1

                    transiciones.append((nodo_actual.estado, estado_actual, char))
                    break

            if transicion_valida:
                hijo = NodoDerivacion(estado_actual, eleccion, [opt for opt in opciones if opt != eleccion])
                nodo_actual.agregar_hijo(hijo)
                nodo_actual = hijo
            else:
                # Crear un nodo para indicar la transición inválida
                hijo_invalido = NodoDerivacion(estado_actual, f'Error: no hay transición con {char}')
                nodo_actual.agregar_hijo(hijo_invalido)
                self.error_transicion = f"Error: Transición inválida desde {estado_actual} con {char}."
                return raiz, transiciones, False  # Retornar inválido si hay error de transición

        return raiz, transiciones, True  # Retornamos la cadena como válida siempre que no haya transición inválida

    def mostrar_tabla_transicion(self, transiciones):
        print(f"{'Estado Actual':^15}{'Estado Siguiente':^20}{'Transición (Carácter)':^20}")
        print("=" * 55)
        for estado_actual, estado_siguiente, caracter in transiciones:
            print(f"{estado_actual:^15}{estado_siguiente:^20}{caracter:^20}")
        if self.error_transicion:
            print("=" * 55)
            print(f"{self.error_transicion:^55}")

    def mostrar_arbol(self, raiz):
        print("Árbol de derivación:")
        raiz.mostrar_arbol()

    def mostrar_caracteres_especiales(self):
        if(len(self.CaracteresEspecialesEncontrados) > 0):
            print("Caracteres especiales encontrados:")
            for caracter, cantidad in self.CaracteresEspecialesEncontrados.items():
                print(f"{caracter}: {cantidad}")
        else:
            print("Caracteres especiales encontrados: ")
            print("\t" + "No se encontraron caracteres especiales.")

    def mostrar_caracteres_del_lenguaje(self):
        if(len(self.caracteresDelLenguajeEncontrados) > 0):
            print("Caracteres del lenguaje encontrados:")
            for caracter, cantidad in self.caracteresDelLenguajeEncontrados.items():
                print(f"{caracter}: {cantidad}")
        else:
            print("Caracteres del lenguaje encontrados: ")
            print("\t" + "No se encontraron caracteres del lenguaje.")

    def obtener_transicion(self, estado_actual, caracter):
        for estado_siguiente, simbolo in self.grafo.get(estado_actual, []):
            if simbolo == caracter:
                return estado_siguiente
        return None


class TuringMachine:
    def __init__(self, cadena):
        self.cadena = cadena
        self.cinta1 = ['␣'] * len(cadena)
        self.cinta2 = ['␣'] * len(cadena)
        self.pos1 = 0
        self.pos2 = 0
        self.estado = 'q0'
        self.grafo = Grafo()
        self.cinta_alternante = True  # True para cinta1, False para cinta2
        self.transiciones = []  # Lista para almacenar las transiciones

    def mover_derecha(self):
        if self.cinta_alternante:
            self.pos1 += 1
        else:
            self.pos2 += 1
        self.cinta_alternante = not self.cinta_alternante

    def mover_izquierda(self):
        if self.cinta_alternante:
            self.pos1 -= 1
        else:
            self.pos2 -= 1
        self.cinta_alternante = not self.cinta_alternante

    def validar_cadena(self):
        for caracter in self.cadena:
            estado_siguiente = self.grafo.obtener_transicion(self.estado, caracter)
            if estado_siguiente:
                # Movimiento a la derecha en ambas cintas
                if self.cinta_alternante:
                    self.cinta1[self.pos1] = caracter
                    movimiento = 'D'  # Mueve hacia la derecha
                else:
                    self.cinta2[self.pos2] = caracter
                    movimiento = 'D'  # Mueve hacia la derecha

                # Registrar la transición
                self.transiciones.append((self.estado, estado_siguiente, caracter, movimiento))
                self.estado = estado_siguiente
                self.mover_derecha()
            else:
                # Registro de transición inválida y termina
                self.transiciones.append((self.estado, None, caracter, 'P'))
                self.grafo.error_transicion = f"Error: Transición inválida desde {self.estado} con '{caracter}'."
                return False  # Termina con error en la transición

        return True  # La cadena es válida si no hubo transición inválida

    def mostrar_cintas(self):
        print("Cinta 1:", ''.join(self.cinta1))
        print("Cinta 2:", ''.join(self.cinta2))

    def mostrar_resultado(self):
        if self.grafo.error_transicion:
            print(self.grafo.error_transicion)
        else:
            print("Cadena aceptada")

        # Mostrar la tabla de transiciones
        self.mostrar_tabla_transicion()

    def mostrar_tabla_transicion(self):
        print(f"{'Estado Actual':^15}{'Estado Siguiente':^20}{'Transición (Carácter)':^20}{'Movimiento':^15}")
        print("=" * 75)
        for estado_actual, estado_siguiente, caracter, movimiento in self.transiciones:
            print(
                f"{estado_actual:^15}{estado_siguiente if estado_siguiente else 'Error':^20}{caracter:^20}{movimiento:^15}")
        print("=" * 75)

    def mostrar_maquina_turing(self):
        print("Estructura de la máquina de Turing M_t:")
        print("Alfabeto de símbolos: {'a', 'b', '*', '#'}")
        print("Alfabeto de entrada: {'a', 'b', '*', '#'}")
        print("Espacio en blanco: '␣'")
        print("Conjunto de estados: {'q0', 'q1', 'q2', 'q3', 'q4'}")
        print("Estado inicial: 'q0'")
        print("Conjunto de estados de aceptación: {'q4'}")









