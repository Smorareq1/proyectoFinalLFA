class NodoDerivacion:
    def __init__(self, estado, transicion, hermanos=None):
        self.estado = estado  # Estado actual en el nodo
        self.transicion = transicion  # Transición elegida
        self.hermanos = hermanos or []  # Transiciones alternativas (hermanos)
        self.hijos = []  # Hijos del nodo

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def mostrar_arbol(self, prefijo="", es_ultimo=True):
        # Mostrar el nodo actual con el prefijo de líneas para representar el árbol
        print(prefijo + ("└── " if es_ultimo else "├── ") +
              f"Estado: {self.estado}, Transición: {self.transicion}, Hermanos: {[f'{h[0]}:{h[1]}' for h in self.hermanos]}")

        # Preparar el prefijo para los hijos
        prefijo_hijo = prefijo + ("    " if es_ultimo else "│   ")
        for i, hijo in enumerate(self.hijos):
            es_ultimo_hijo = i == len(self.hijos) - 1
            hijo.mostrar_arbol(prefijo_hijo, es_ultimo_hijo)


class Grafo:
    def __init__(self):
        self.caracteresEspeciales = {'*', '#'}
        self.CaracteresEspecialesEncontrados = {}

        self.grafo = {
            'q0': {'q1': 'a'},
            'q1': {'q2': 'b'},
            'q2': {'q3': 'a'},
            'q3': {'q1': 'b', 'q3': 'a', 'q4': '*'},
            'q4': {'q4': '#', 'q3': 'a', 'q1': 'b'}
        }
        self.estado_inicial = 'q0'

    def mostrar_tabla_transicion(self):
        print("Tabla de Transiciones:")
        print(f"{'Estado Actual':<15}{'Estado Siguiente':<20}{'Transición (Carácter)'}")
        print("-" * 50)

        for estado, transiciones in self.grafo.items():
            for estado_siguiente, caracter in transiciones.items():
                print(f"{estado:<15}{estado_siguiente:<20}{caracter}")

    def validar_cadena(self, cadena):
        estado_actual = self.estado_inicial
        raiz = NodoDerivacion(estado_actual, 'Inicio')  # Nodo raíz del árbol de derivación
        nodo_actual = raiz

        for char in cadena:
            transicion_valida = False
            opciones = []
            eleccion = None

            # Recorremos todas las transiciones desde el estado actual
            for estado_siguiente, peso in self.grafo[estado_actual].items():
                opciones.append((estado_siguiente, peso))
                if peso == char and not transicion_valida:
                    estado_actual = estado_siguiente
                    transicion_valida = True
                    eleccion = (estado_siguiente, peso)

                    # Registrar el carácter especial encontrado
                    if peso in self.caracteresEspeciales:
                        self.CaracteresEspecialesEncontrados[peso] = self.CaracteresEspecialesEncontrados.get(peso, 0) + 1
                    break

            # Si la transición fue válida, creamos el nodo hijo en el árbol de derivación
            if transicion_valida:
                hijo = NodoDerivacion(estado_actual, eleccion, [opt for opt in opciones if opt != eleccion])
                nodo_actual.agregar_hijo(hijo)
                nodo_actual = hijo  # Moverse al siguiente nodo
            else:
                print(f"Transición inválida desde {estado_actual} con {char}.")
                return False

        # Imprimir el árbol de derivación completo
        print("Árbol de derivación:")
        raiz.mostrar_arbol()
        return True
