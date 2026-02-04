import time

class NavegadorWeb:
    def __init__(self):
        self.pila_atras = []       # Guarda las paginas a las que se puede devolver
        self.pila_adelante = []    # Guarda las páginas a las que se puede avanzar
        self.pagina_actual = None

    def cargar_pagina(self, url):
        print("\nCargando página...")
        time.sleep(1)

        if self.pagina_actual is not None: #Verifica si  ya hay una pagina abierta
            self.pila_atras.append(self.pagina_actual) #Si habia una pagina abierta la guarda en la pila de atras para poder regresar después

        self.pagina_actual = url  #Se actualiza el valor de la variable
        self.pila_adelante.clear()#Se borra la pila de adelante

        print(f"Página cargada: {self.pagina_actual}")
        time.sleep(1)

    def ir_atras(self):
        print("\nIntentando retroceder...")
        time.sleep(1)

        if not self.pila_atras:  #Revisa si la pila esta vacia
            print("No hay páginas anteriores.")
            time.sleep(1)
            return

        self.pila_adelante.append(self.pagina_actual) #Se guarda en la pila de adelante , para poder regresar si el usuario avanza
        self.pagina_actual = self.pila_atras.pop() #Se saca la última página guardada en la pila de atrás.

        print(f"Has vuelto a: {self.pagina_actual}")
        time.sleep(1)

    def ir_adelante(self):
        print("\nIntentando avanzar...")
        time.sleep(1)

        if not self.pila_adelante: #Verifica si hay paginas para avanzar
            print("No hay páginas siguientes.")
            time.sleep(1)
            return

        self.pila_atras.append(self.pagina_actual) #la pagina actual se guarda en pila de atras 
        self.pagina_actual = self.pila_adelante.pop()# Se toma la última página de la pila de adelante y se convierte en la actual

        print(f"Has avanzado a: {self.pagina_actual}")
        time.sleep(1)

    def mostrar_pagina_actual(self):
        print("\nMostrando página actual...")
        time.sleep(1)
        print(f"Página actual: {self.pagina_actual}")
        time.sleep(1)

navegador = NavegadorWeb()

navegador.cargar_pagina("google.com")
navegador.cargar_pagina("youtube.com")
navegador.cargar_pagina("github.com")

for _ in range(3):
    navegador.ir_atras()
for _ in range(3):
    navegador.ir_adelante()

navegador.mostrar_pagina_actual()
