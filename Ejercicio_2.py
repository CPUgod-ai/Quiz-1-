class NodoTrie:
    def __init__(self):
        self.hijos = {}          # Guarda las letras hijas del nodo
        self.es_fin = False     # Indica si aquí termina una palabra


class Trie:
    def __init__(self):
        self.raiz = NodoTrie()  # Se crea la raíz del árbol (no tiene letra)

    def insertar(self, palabra):
        actual = self.raiz     # Apunta al nodo inicial (raíz)
        for letra in palabra.lower():  # Recorre la palabra letra por letra
            if letra not in actual.hijos:  # Si la letra no existe en el nodo actual
                actual.hijos[letra] = NodoTrie()  # Se crea un nuevo nodo para esa letra
            actual = actual.hijos[letra]  # Avanza al siguiente nodo
            
        actual.es_fin = True   # Marca el final de la palabra

    def _buscar_palabras(self, nodo, prefijo, resultados):
        if nodo.es_fin:        # Si el nodo representa el final de una palabra
            resultados.append(prefijo)  # Se agrega la palabra a los resultados

        for letra, hijo in nodo.hijos.items():  # Recorre los hijos del nodo
            self._buscar_palabras(hijo, prefijo + letra, resultados)  # Llamada recursiva

    def autocompletar(self, prefijo):
        actual = self.raiz     # Comienza desde la raíz
        prefijo = prefijo.lower()  # Convierte el prefijo a minúscula

        for letra in prefijo:  # Recorre el prefijo letra por letra
            if letra not in actual.hijos:  # Si el prefijo no existe
                return []      # No hay coincidencias
            actual = actual.hijos[letra]  # Avanza en el Trie

        resultados = []        # Lista para guardar las palabras encontradas
        self._buscar_palabras(actual, prefijo, resultados)  # Busca las coincidencias
        return resultados      # Devuelve el autocompletado


trie = Trie()  # Se crea el Trie

palabras = [
    "universidad", "universitario", "uniforme", "unidad", "unión",
    "arboleda", "arbóreo", "arborización",
    "Sergio", "servicio", "servidor", "seriedad", "semestre",
    "profesor", "profesora", "profesional", "programación", "proyecto"
]

for palabra in palabras:
    trie.insertar(palabra)    # Inserta cada palabra en el Trie

print(trie.autocompletar("uni"))   
print(trie.autocompletar("arbol")) 
print(trie.autocompletar("ser"))   
print(trie.autocompletar("prof"))  
